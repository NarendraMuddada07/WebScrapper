import requests
from bs4 import BeautifulSoup
from config import URL, POST_SELECTOR

def fetch_static():
    results = []
    page = 1

    while True:
        res = requests.get(f"{URL}/page/{page}/")
        soup = BeautifulSoup(res.text, 'lxml')
        posts = soup.select(POST_SELECTOR)

        if not posts:
            break  # No more pages

        for p in posts:
            quote_tag = p.find('span', class_='text')
            author_tag = p.find('small', class_='author')
            if quote_tag and author_tag:
                results.append((quote_tag.text.strip(), author_tag.text.strip()))

        page += 1

    return results
