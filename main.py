from codes.mexico import Mexico

if __name__ == '__main__':
    scrapper = Mexico()
    scrapper.extract_urls()
    #scrapper.load_urls()
    scrapper.download_documents()
