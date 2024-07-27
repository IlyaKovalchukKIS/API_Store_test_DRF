import json
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"


def get_html(url):
    with webdriver.Chrome() as driver:
        driver.get(url)
        sleep(2)
        html = driver.page_source
        return html


def find_all_element(html, name, class_name):
    result = {}
    index = 0

    soup = BeautifulSoup(html, "html.parser")
    data = soup.find_all(name, class_=class_name)[:10]

    for i in data:
        index += 1
        res = BeautifulSoup(str(i), "html.parser")
        id = res.find("tr", class_="bull-list-item-js -exact").get("data-doc-id")
        title = res.find("a", class_="bulletinLink bull-item__self-link auto-shy").text
        count_view = res.find("span", class_="views nano-eye-text").text
        position = index
        advertisement_url = res.find(
            "a", class_="bulletinLink bull-item__self-link auto-shy"
        ).get("href")
        get_ht = get_html("https://www.farpost.ru" + advertisement_url)
        author_get = BeautifulSoup(get_ht, "html.parser")
        author = author_get.find("span", class_="userNick auto-shy").text.strip("\n")
        result[index] = {
            "id": id,
            "title": title,
            "author": author,
            "count_view": count_view,
            "position": position,
        }
    return result


response = get_html(url)
data = find_all_element(response, "tr", "bull-list-item-js -exact")

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)
