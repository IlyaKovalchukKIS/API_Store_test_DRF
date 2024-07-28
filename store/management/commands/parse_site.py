from django.core.management import BaseCommand
from config.settings import BASE_DIR
from store.services import find_all_element, get_html, save_data, load_data_to_db


class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://www.farpost.ru/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/"
        try:
            response = get_html(url)
            data = find_all_element(response, "tr", "bull-list-item-js -exact")
            if not data and len(data) < 10:
                raise Exception("Data not found")
            save_data(BASE_DIR / "static/data.json", data)
        finally:
            load_data_to_db()
