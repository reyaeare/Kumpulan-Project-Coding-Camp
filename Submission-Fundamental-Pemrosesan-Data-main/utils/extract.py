import requests
from bs4 import BeautifulSoup
from datetime import datetime


BASE_URL = "https://fashion-studio.dicoding.dev"


def fetching_content(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.content
    except Exception as error:
        print(f"Error fetching content: {error}")
        return None


def extract_product_data(card):
    try:
        title = card.find("h3", class_="product-title").get_text(strip=True)

        price_tag = card.find("span", class_="price")
        if price_tag is None:
            price_tag = card.find("p", class_="price")
        price = price_tag.get_text(strip=True) if price_tag else None

        details = card.find_all("p")

        rating = None
        colors = None
        size = None
        gender = None

        for detail in details:
            text = detail.get_text(strip=True)

            if "Rating:" in text:
                rating = text.replace("Rating:", "").strip()
            elif "Colors" in text:
                colors = text.strip()
            elif "Size:" in text:
                size = text.replace("Size:", "").strip()
            elif "Gender:" in text:
                gender = text.replace("Gender:", "").strip()

        return {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "timestamp": datetime.now().isoformat()
        }

    except Exception as error:
        print(f"Error extracting product data: {error}")
        return None


def scrape_page(url):
    try:
        content = fetching_content(url)
        if content is None:
            return []

        soup = BeautifulSoup(content, "html.parser")
        cards = soup.find_all("div", class_="collection-card")

        products = []
        for card in cards:
            product = extract_product_data(card)
            if product:
                products.append(product)

        return products

    except Exception as error:
        print(f"Error scraping page: {error}")
        return []


def scrape_main(start_page=1, end_page=50):
    try:
        all_products = []

        for page in range(start_page, end_page + 1):
            if page == 1:
                url = BASE_URL
            else:
                url = f"{BASE_URL}/page{page}"

            products = scrape_page(url)
            all_products.extend(products)

        return all_products

    except Exception as error:
        print(f"Error in scrape_main: {error}")
        return []