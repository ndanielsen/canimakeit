from bs4 import BeautifulSoup
import requests


def assert_good_response(response):
    '''Raise exception if http response code isn't 200'''
    url = response.url
    status = response.status_code
    msg = 'unsuccessful request to {0}, got status {1}'.format(url, status)
    assert status is 200, msg.format(url, status)


def html_to_links(html_str):
    '''Grab all urls from links in the document'''
    soup = BeautifulSoup(html_str, 'html.parser')
    a_elements = soup.find_all('a')
    links = [el.attrs['href'] for el in a_elements]
    return links


def links_from_url(url):
    '''Grab all urls from all links on the page'''
    response = requests.get(url)
    assert_good_response(response)
    links = html_to_links(response.text)
    return links


def download_data_file(url, name):
    '''store a remote file on disk with name'''
    response = requests.get(url)
    assert_good_response(response)
    with open(name, 'wb') as f:
        for chunk in response.iter_content():
            f.write(chunk)
    return True
