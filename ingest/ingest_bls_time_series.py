'''
Ingests BLS time series data

'''


# Python 3.5 -- can port to 2.7 by request
import os
import urlparse
import ingest_utils
# import re

BASE_URL = ur'http://download.bls.gov/pub/time.series/cu/'
OUTPUT_DIR = ur'../data/raw/bls'


def name_from_url(url, output_dir):
    '''make a file name from the url'''
    name = url.split('/')[-1]
    name = name.replace('.', '')
    name = name + '.tsv'
    name = os.path.join(output_dir, name)
    return name


def ingest(base_url, output_dir):
    links = ingest_utils.links_from_url(base_url)

    # Ignore the first link, it just goes to the parent directory
    links = links[1:]

    for url in links:
        abs_url = urlparse.urljoin(base_url, url)
        name = name_from_url(url, output_dir)
        ingest_utils.download_data_file(abs_url, name)

if __name__ == '__main__':
    ingest(BASE_URL, OUTPUT_DIR)
