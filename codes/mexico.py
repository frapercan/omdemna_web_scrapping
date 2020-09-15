from requests import get
from bs4 import BeautifulSoup
import pickle
import os
from scrapper import Scrapper


class Mexico(Scrapper):
    def __init__(self):
        super().__init__()
        self.country_code = '145'
        self.country_name = 'Mexico'
        self.URLs = ["http://www.diputados.gob.mx/LeyesBiblio/actual/{}.htm".format(year) for year in range(2020, 2008, -1)]
        self.REF_URL = "http://www.diputados.gob.mx/LeyesBiblio/"
        self.path = os.path.dirname(__file__)
        self.law_refs = {}
        self.resources = {}


    def extract_urls(self):
        for url in self.URLs:
            print("Extracting references from: {}".format(url))

            publications_page = get(url).content

            soup = BeautifulSoup(publications_page, features="html.parser")
            table = soup.find("table", {"id": "table2"})
            try:
                publications = table.find_all('a', href=True)
                for publication in publications:
                    self.law_refs[publication['href']] = self.REF_URL + publication['href'][3:]  # clean "../"
            except:
                print('{} not scrappable'.format(url))
        for law_ref in self.law_refs.keys():
            law_page = get(self.law_refs[law_ref]).content
            soup = BeautifulSoup(law_page, features="html.parser")

            anchors = soup.find_all('a')
            for anchor in anchors:

                try:
                    if ".pdf" in anchor['href'] and "_ima" not in anchor['href']:
                        # print(law_ref)
                        # print(anchor['href'])
                        self.resources[anchor['href'].split('/')[-1]] = self.REF_URL + "ref/" + anchor['href']
                except:
                    print("{} not scrappable".format(law_ref))

        print(self.resources)
        pickle.dump(self.resources,open( "resources.p", "wb"))




