import json
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from config.settings import BASE_DIR
from store.models import Advertisement

url = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
selenium_url = "http://selenium-chrome:4444/wd/hub"
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Remote(command_executor=selenium_url, options=chrome_options)


def get_html(url):
    driver.get(url)
    sleep(4)
    html = driver.page_source
    return html


def find_all_element(html, name, class_name):
    result = {}
    index = 0

    soup = BeautifulSoup(html, "html.parser")
    data = soup.find_all(name, class_=class_name)[:10]
    try:
        for i in data:
            index += 1
            res = BeautifulSoup(str(i), "html.parser")
            id = res.find("tr", class_="bull-list-item-js -exact").get("data-doc-id")
            title = res.find(
                "a", class_="bulletinLink bull-item__self-link auto-shy"
            ).text
            count_view = res.find("span", class_="views nano-eye-text").text
            position = index
            advertisement_url = res.find(
                "a", class_="bulletinLink bull-item__self-link auto-shy"
            ).get("href")
            get_ht = get_html("https://www.farpost.ru" + advertisement_url)
            author_get = BeautifulSoup(get_ht, "html.parser")
            author = author_get.find("span", class_="userNick auto-shy").text.strip(
                "\n"
            )
            result[index] = {
                "id_advertisement": int(id),
                "title": title,
                "author": author,
                "count_view": int(count_view),
                "position": position,
            }
    except Exception as e:
        print(e)
    finally:
        return result


def save_data(file_name, data):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data_to_db():
    Advertisement.objects.all().delete()
    with open(BASE_DIR / "static/data.json", "r") as file:
        for k, v in json.load(file).items():
            Advertisement.objects.create(**v)
