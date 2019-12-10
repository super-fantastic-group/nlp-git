from requests import get
from bs4 import BeautifulSoup

def scrape_links_one_page():
    headers = {'User-Agent': 'Codeup Data Science'} 
    url = "https://github.com/search?q=stars%3A%3E0&s=stars&type=Repositories"
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text)
    extension = soup.find_all("a", {"class":"v-align-middle"}, {"data-hydro-click":"url"})
    extensions = []
    for count in range(len(extension)):
        extensions.append("github.com/" + extension[count].get_text())
    return extensions


def get_readme_text(url):
    response = get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    textboxes = soup.findAll("div", {"class": "Box-body"})
    readme_text = textboxes[0].text
    return readme_text