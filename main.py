from modules.mexico.mexico import Mexico
from modules.mexico.mexico import Mexico
from modules.elsalvador.elsalvador import ElSalvadorAsambleaLegislativa

threads = 5
driver_path = '/usr/lib/chromium-browser/chromedriver'

if __name__ == '__main__':
    #scrapper = Mexico(threads=threads)
    #scrapper.extract_urls()
    # scrapper.load_urls()
    #scrapper.download_documents()

    scrapper = ElSalvadorAsambleaLegislativa()
    scrapper.extract_information()
    print(scrapper.resources)

