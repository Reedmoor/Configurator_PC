import sys
import os
import json
import scrapy
import time

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from time import sleep as pause
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from tqdm import tqdm
from reviewParser import parse_reviews

TEST_URL = "https://www.dns-shop.ru/product/a67afeaff7bbd9cb/robot-pylesos-dreame-x40-ultra-complete-belyj/"

def save_to_json(data, filename="items.json"):
    """Save data to JSON file."""
    try:
        # Создаем копию данных для сериализации
        serializable_data = []
        for item in data:
            serializable_item = {}
            for key, value in item.items():
                # Пропускаем несериализуемые объекты
                if not callable(value) and value is not None:
                    # Для списков проверяем вложенные элементы
                    if isinstance(value, list):
                        serializable_list = []
                        for subitem in value:
                            if not callable(subitem) and subitem is not None:
                                serializable_list.append(subitem)
                        serializable_item[key] = serializable_list
                    else:
                        serializable_item[key] = value
            serializable_data.append(serializable_item)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(serializable_data, f, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to JSON: {e}")
        # Для отладки можно вывести более подробную информацию
        import traceback
        traceback.print_exc()

def clean_price(price_str):

    if not price_str:
        return None

# Remove non-digit characters
    cleaned_price = ''.join(char for char in price_str if char.isdigit())

    try:
        return int(cleaned_price)
    except ValueError:
        return None

def parse_breadcrumbs(driver):
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # Find the breadcrumb list
    breadcrumb_list = soup.find('ol', class_='breadcrumb-list')

    # If no breadcrumb list found, return empty list
    if not breadcrumb_list:
        return []

    # Parse categories
    categories = []
    for item in breadcrumb_list.find_all('li', class_='breadcrumb-list__item'):
        # Skip the last item (current page)
        if 'breadcrumb_last' in item.get('class', []):
            continue

        # Find the link
        link = item.find('a', class_='ui-link')
        if link:
            categories.append({
                'url': f"https://www.dns-shop.ru{link.get('href', '')}",
                'name': link.find('span').text.strip()
            })

    if len(categories) > 2:
        categories = categories[1:-1]

    return categories


def parse_characteristics(driver):

    try:
        characteristics_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-card__characteristics'))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", characteristics_element)
    except Exception as e:
        print(f"Не удалось найти или прокрутить до 'product-characteristics-content': {e}")
        return {}

    soup = BeautifulSoup(driver.page_source, 'lxml')
    characteristics = {}

    # Находим основной контейнер с характеристиками
    content = soup.find('div', class_='product-characteristics-content')
    if not content:
        return characteristics

    # Проходим по всем группам характеристик
    groups = content.find_all('div', class_='product-characteristics__group')
    for group in groups:
        group_name = group.find('div', class_='product-characteristics__group-title').text.strip()
        characteristics[group_name] = []

        # Проходим по всем характеристикам в группе
        items = group.find_all('li', class_='product-characteristics__spec')
        for item in items:
            title_element = item.find('span', class_='product-characteristics__spec-title-content')
            value_element = item.find('div', class_='product-characteristics__spec-value')

            if title_element and value_element:
                title = title_element.text.strip()
                value = value_element.text.strip()

                # Удаляем лишние пробелы и переносы строк
                title = ' '.join(title.split())
                value = ' '.join(value.split())

                characteristics[group_name].append({
                    "title": title,
                    "value": value
                })

    return characteristics


def extract_images(driver, max_images=5):
    """Extract images using Selenium"""
    images = []

    # Сначала найдем и кликнем на миниатюру
    try:
        thumbnail = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product-images-slider__img.tns-complete'))
        )
        thumbnail.click()

        # Ждем появления просмотрщика изображений
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'media-viewer-image__main'))
        )
    except Exception as e:
        print(f"Error clicking thumbnail: {e}")
        return []

    while len(images) < max_images:  # Ограничиваем количество фотографий
        # Get current page source and parse it
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Проверяем наличие контейнера с классом media-viewer-image__main_with-desc
        if soup.find('div', class_='media-viewer-image__main.media-viewer-image__main_with-desc'):
            print("Found container with description, stopping parsing")
            break

        # Find the main media viewer container
        media_viewer = soup.find('div', class_='media-viewer-image__main')

        if not media_viewer:
            break

        # Find the main image
        main_img = media_viewer.find('img', class_='media-viewer-image__main-img')

        if main_img and 'src' in main_img.attrs:
            images.append(main_img['src'])
            print(f"Found image {len(images)}/{max_images}")

        if len(images) >= max_images:
            break

        try:
            right_control = driver.find_element(By.CSS_SELECTOR,
                                                'div.media-viewer-image__main > div.media-viewer-image__control_right')
            right_control.click()
            time.sleep(0.5)

        except Exception as e:
            print(f"Error clicking or finding next button: {e}")
            break

    return list(dict.fromkeys(images))


def parse_product_data(driver):
    """Extract rating and review_count"""
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # Находим JSON-LD скрипт
    script = soup.find('script', type='application/ld+json')
    if script:
        try:
            data = json.loads(script.string)

            rating = data.get('aggregateRating', {}).get('ratingValue')
            review_count = data.get('aggregateRating', {}).get('reviewCount')

            return {
                "rating": float(rating) if rating else None,
                "number_of_reviews": int(review_count) if review_count else None
            }
        except json.JSONDecodeError:
            print("Ошибка при парсинге JSON-LD")

    return {
        "rating": None,
        "number_of_reviews": None
    }

def parse_characteristics_page(driver, url):
    """Parse product page details."""
    driver.get(url)
    pause(randint(10, 13))

    soup = BeautifulSoup(driver.page_source, 'lxml')
    selector = scrapy.Selector(text=driver.page_source)

    def logo():
        json_ld_scripts = selector.xpath(
            "//script[@type='application/ld+json' and contains(text(), 'Product')]/text()").getall()
        brand_name = None
        for script_text in json_ld_scripts:
            try:
                json_data = json.loads(script_text)
                if 'brand' in json_data and isinstance(json_data['brand'], dict):
                    brand_name = json_data['brand'].get('name')
                    break
            except json.JSONDecodeError:
                continue
        return brand_name

    def safe_text(soup, tag, class_=None, attribute=None):
        element = soup.find(tag, class_=class_)
        return element.get(attribute).strip() if element and attribute else element.text.strip() if element else None

    def safe_list(soup, tag, class_=None, attribute=None):
        elements = soup.find_all(tag, class_=class_)
        return [element.get(attribute).strip() if attribute else element.text.strip() for element in elements if element]

    # Extract functions
    categories = parse_breadcrumbs(driver)
    images = extract_images(driver)
    characteristics = parse_characteristics(driver)
    product_data = parse_product_data(driver)

    # Extract product details
    item = {
        "id": selector.xpath("//div[@class='product-card-top__code']/text()").get(),
        "url": url,
        "categories": categories,
        "images": images,
        "name": safe_text(soup, 'div', class_="product-card-top__name"),
        "price_discounted": clean_price(selector.xpath("//div[contains(@class, 'product-buy__price_active')]/text()").get()) or 0,
        "price_original": clean_price(selector.xpath("//span[@class='product-buy__prev']/text()").get()) or
                          clean_price(selector.xpath("//div[@class='product-buy__price']/text()").get()),
        "rating": product_data['rating'],
        "number_of_reviews": product_data['number_of_reviews'],
        "brand_name": logo(),
        "description": safe_text(soup, 'div', class_="product-card-description-text"),
        "characteristics": characteristics,
        "drivers": safe_list(soup, 'a', class_="product-card-description-drivers__item-link", attribute='href'),
    }

    return item

def main():
    driver = uc.Chrome(version_main=133)
    # Read URLs from file
    with open('DNS_parsing/urls.txt', 'r') as file:
        urls = list(map(lambda line: line.strip(), file.readlines()))

    parsed_data = []
    for url in tqdm(urls, ncols=70, unit='товар', colour='blue', file=sys.stdout):
        try:
            parsed_data.append(parse_characteristics_page(driver, url))
            save_to_json(parsed_data)


            try:
                driver.get(url)
                pause(randint(1, 2))  # Random pause to simulate human behavior

                # Find and extract the reviews page URL
                rating_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//a[contains(@class, "product-card-top__rating_exists")]'))
                )
                reviews_url = rating_link.get_attribute("href")
                print(f"Reviews URL: {reviews_url}")

                # Navigate directly to reviews page
                driver.get(reviews_url)
                pause(randint(1, 2))  # Wait for the reviews page to load

                all_reviews = parse_reviews(driver)

                # Click "Load More" button to get additional reviews
                while True:
                    try:

                        load_more_button = WebDriverWait(driver, 5).until(
                            EC.element_to_be_clickable((By.XPATH,
                                                        '//button[contains(@class, "button-ui_lg") and contains(@class, "paginator-widget__more")]'))
                        )
                        load_more_button.click()
                        pause(randint(2, 4))  # Wait for new reviews to load

                        parse_reviews(driver)

                    except TimeoutException:
                        # No more "Load More" button, exit the loop
                        break

                # Save reviews to JSON
                save_to_json(all_reviews)
                print(f'Total reviews parsed: {len(all_reviews)}')

            except Exception as e:
                print(f"An error occurred: {e}")
                import traceback
                traceback.print_exc()
            finally:
                # Ensure driver is closed properly
                if driver:
                    try:
                        driver.quit()
                    except Exception as quit_error:
                        print(f"Error closing driver: {quit_error}")


        except Exception as e:
                print(f"Error parsing #url: {e}")

    # Save parsed data
    driver.quit()
    print('Product parsing complete!')

if __name__ == '__main__':
    main()