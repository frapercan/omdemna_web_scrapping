import urllib.request
from multiprocessing.pool import ThreadPool
from tqdm import tqdm
import pickle
import os
import pandas as pd


class Scrapper:
    def __init__(self, threads=5, driver_path='/usr/lib/chromium-browser/chromedriver'):
        self.country_code = None
        self.ISO = None
        self.state_code = None
        self.state_ISO = None
        self.state_name = None
        self.columns = ['ISO', 'COUNTRY_CODE', 'STATE_CODE', 'STATE_ISO', 'TITLE', 'RESUME', 'PUBLICATION_DATE', 'URL',
                     'DOC_TYPE']
        self.resources = pd.DataFrame(
            columns=self.columns)
        self.path = None
        self.threads = threads
        self.driver_path = driver_path

    def load_resources(self):
        self.resources = pickle.load(open("resources.p", "rb"))

    def save_resources(self):
        pickle.dump(self.resources, open("resources.p", "wb"))

    def extract_information(self):
        pass

    def download_documents(self):
        results = ThreadPool(self.threads).imap(self.download_url, self.resources.values())
        for i in results:
            pass

    def download_url(self, url):
        document_name = url.split('/')[-1]
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "codes/" + self.country_code + "/" + document_name)
        if not os.path.isfile(filename):
            try:
                with DownloadProgressBar(unit='B', unit_scale=True,
                                         miniters=1, desc=url.split('/')[-1]) as t:
                    urllib.request.urlretrieve(url, filename=filename, reporthook=t.update_to)
            except Exception as e:
                print(e)

    def resume(self):
        print("Country code:{}".format(self.country_code))
        print("Country name:{}".format(self.ISO))
        print("State code:{}".format(self.state_code))
        print("State name:{}".format(self.state_name))
        print("References loaded: {}".format(len(self.resources.keys())))
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, "codes/" + self.country_code + "")
        print("Avaliable documents: {}".format(len(os.listdir(filename))))


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)
