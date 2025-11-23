import requests
from bs4 import BeautifulSoup
import csv
import time
import argparse
import os

CACHE_DIR = "cache"

def fetch_page(country):
    """Загружает страницу страны с англоязычной Википедии, с кэшированием и User-Agent."""
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

    cache_file = os.path.join(CACHE_DIR, f"{country}.html")

    if os.path.exists(cache_file):
        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()

    url = f"https://en.wikipedia.org/wiki/{country.replace(' ', '_')}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html = response.text
        with open(cache_file, "w", encoding="utf-8") as f:
            f.write(html)
        time.sleep(1)  # пауза между запросами
        return html
    except Exception as e:
        print(f"Ошибка при загрузке {country}: {e}")
        return None


def parse_country_data(country, html):
    """Извлекает столицу, площадь и население из HTML."""
    soup = BeautifulSoup(html, "html.parser")
    info_box = soup.find("table", {"class": "infobox"})

    capital, area, population = None, None, None

    if info_box:
        rows = info_box.find_all("tr")
        for row in rows:
            header = row.find("th")
            data = row.find("td")
            if not header or not data:
                continue

            text = header.get_text().strip().lower()
            if "capital" in text and not capital:
                capital = data.get_text().split("\n")[0].strip()
            elif "area" in text and not area:
                area = data.get_text().split("\n")[0].strip()
                area = area.replace(",", "").split()[0]
            elif "population" in text and not population:
                population = data.get_text().split("\n")[0].strip()
                population = population.replace(",", "").split()[0]

    return {
        "country": country,
        "city": capital if capital else "N/A",
        "area": area if area else "N/A",
        "population": population if population else "N/A"
    }


def main(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        countries = [line.strip() for line in f if line.strip()]

    results = []
    for country in countries:
        html = fetch_page(country)
        if html:
            data = parse_country_data(country, html)
            results.append(data)

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["country", "city", "area", "population"])
        writer.writeheader()
        writer.writerows(results)

    print(f" Данные сохранены в {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wikipedia country parser")
    parser.add_argument("input", help="Файл со списком стран (например, countries.txt)")
    parser.add_argument("output", help="CSV-файл для сохранения (например, countries_data.csv)")
    args = parser.parse_args()

    main(args.input, args.output)

