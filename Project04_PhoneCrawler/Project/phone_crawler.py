import re
import threading

import requests
from bs4 import BeautifulSoup

URL_DOMAIN = "https://django-anuncios.solyd.com.br"
URL_VEHICLES = "https://django-anuncios.solyd.com.br/automoveis/"

URLS = []
PHONE_NUMBERS = []


def url_request(url):

    try:
        answer = requests.get(url)

        if answer.status_code == 200:
            return answer.text
        else:
            print("Error: Request...")

    except Exception as error:
        print("Error: Request...")
        print(error)


def parsing(html_answer):

    try:
        soup = BeautifulSoup(html_answer, 'html.parser')
        return soup

    except Exception as error:
        print("Error: HTML Parsing...")
        print(error)


def find_links(soup):

    try:
        main_cards = soup.find("div", class_="ui three doubling link cards")
        cards = main_cards.findAll("a")

    except Exception as error:
        print("Error: Finding links...")
        print(error)
        return None

    links = []

    for card in cards:
        try:
            link = card['href']
            links.append(link)

        except Exception as error:
            print("Erro...")
            print(error)
            pass

    return links


def find_phone_number(soup):

    try:
        description = (
            soup.find_all("div", class_="sixteen wide column")[2].p.get_text().strip()
        )

    except Exception as error:
        print("Erro ao encontrar description...")
        print(error)
        return None

    regex = re.findall(
        r"\(?0?([1-9]{2})[ \-\.\)]{0,2}(9[ \-\.]?\d{4})[ \-\.]?(\d{4})", description
    )

    if regex:
        return regex


def discover_phone_numbers():

    while True:
        try:
            ad_link = URLS.pop(0)

        except Exception as error:
            print("Erro...")
            print(error)
            return None

        ad_answer = url_request(URL_DOMAIN + ad_link)

        if ad_answer:
            ad_soup = parsing(ad_answer)

            if ad_soup:
                phone_numbers = find_phone_number(ad_soup)

                if phone_numbers:

                    for phone_number in phone_numbers:
                        print("Phone number found:", phone_number)
                        PHONE_NUMBERS.append(phone_number)
                        save_phone_number(phone_number)


def save_phone_number(telefone):

    string_telefone = f"{telefone[0]}{telefone[1]}{telefone[2]}\n"

    try:
        with open("phone_numbers.csv", "a") as archive:
            archive.write(string_telefone)

    except Exception as error:
        print("Error: Saving archive...")
        print(error)


if __name__ == "__main__":

    search_answer = url_request(URL_VEHICLES)

    if search_answer:
        search_soup = parsing(search_answer)

        if search_soup:
            URLS = find_links(search_soup)

            THREADS = []

            for i in range(15):
                t = threading.Thread(target=discover_phone_numbers)
                THREADS.append(t)

            for t in THREADS:
                t.start()

            for t in THREADS:
                t.join()