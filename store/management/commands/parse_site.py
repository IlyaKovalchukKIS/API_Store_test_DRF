from django.core.management import BaseCommand

from config.settings import BASE_DIR
from store.services import find_all_element, get_html, save_data, load_data_to_db


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
        try:
            print("parse_site: Start")
            response = get_html(url)
            data = find_all_element(response, "tr", "bull-list-item-js -exact")
            if data and len(data.keys()) >= 10:
                save_data(BASE_DIR / "static/data.json", data)
        finally:
            load_data_to_db()
        print("parse_site: Done")
