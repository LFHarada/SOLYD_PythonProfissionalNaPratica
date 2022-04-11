import json
import sys

import requests

URL_ALL = "https://restcountries.com/v2/all"
URL_NAME = "https://restcountries.com/v2/name"


def request(url):
    try:
        answer = requests.get(url)
        if answer.status_code == 200:
            return answer.text
    except:
        print("Error while requesting from: ", url)


def parsing(answer_text):
    try:
        return json.loads(answer_text)
    except:
        print("Error while parsing.")


def country_counting():
    answer = request(URL_ALL)
    if answer:
        list_of_countries = parsing(answer)
        if list_countries():
            return len(list_of_countries)


def list_countries(list_of_countries):
    for country in list_of_countries:
        print(country['name'])


def country_population(country_name):
    answer = request("{}/{}".format(URL_NAME, country_name))
    if answer:
        list_of_countries = parsing(answer)
        if list_of_countries:
            for country in list_of_countries:
                print("{} - {} hab.".format(country['name'], country['population']))
    else:
        print("Country not found!")


def country_currency(country_name):
    answer = request("{}/{}".format(URL_NAME, country_name))
    if answer:
        list_of_countries = parsing(answer)
        if list_of_countries:
            for country in list_of_countries:
                print("Currencies of", country['name'])
                currencies = country['currencies']
                for currency in currencies:
                    print("{} - {}".format(currency['name'], currency['code']))
    else:
        print("Country not found!")


def read_country_name():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print("Country name is necessary")


def print_help():
    print()
    print("## Bem vindo ao sistema de países ##")
    print()
    print("How to use:")
    print("Write in terminal the following command line:")
    print("python countries.py <action> <country name>")
    print()
    print("Actions: country_counting, currency, population")
    print()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_help()

    else:
        argument1 = sys.argv[1]

        if argument1 == "country_counting":
            number_of_countries = country_counting()
            print("There are {} countries in the world.".format(number_of_countries))
        elif argument1 == "currency":
            country = read_country_name()
            if country:
                country_currency(country)
        elif argument1 == "population":
            country = read_country_name()
            if country:
                argument2 = sys.argv[2]
        else:
            print("Invalid argument!")