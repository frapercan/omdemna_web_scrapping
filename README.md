# omdemna_web_scrapping
## Description
Information extraction from different official states of latinoamerica.

Structured using Country codes and States codes.
## Includes:
Including: Leyes Federales de México (145 - 0)

## Deployment:
*  Install python dependances

        pip install pickle
        pip install BeautifulSoup
        pip install tqdm
        
*  run main.py in root folder.

It's configured in order to start exploring the web looking for all references, storing them as **resources.p** on **codes/country** directory. 

Next it will download all documents using multiple threads as **filename.pdfs** in **codes/country/documents** directory. .
    