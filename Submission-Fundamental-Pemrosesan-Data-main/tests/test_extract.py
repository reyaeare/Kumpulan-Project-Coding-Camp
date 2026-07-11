from utils.extract import scrape_page, scrape_main
from unittest.mock import patch

@patch("utils.extract.fetching_content")
def test_scrape_page_success(mock_fetching_content):
    mock_fetching_content.return_value = b"""
    <html>
        <body>
            <div class="collection-card">
                <h3 class="product-title">T-shirt 2</h3>
                <span class="price">$102.15</span>
                <p>Rating: 3.9 / 5</p>
                <p>3 Colors</p>
                <p>Size: M</p>
                <p>Gender: Women</p>
            </div>
        </body>
    </html>
    """

    result = scrape_page("https://example.com")

    assert len(result) == 1
    assert result[0]["Title"] == "T-shirt 2"


@patch("utils.extract.fetching_content")
def test_scrape_page_failed_content(mock_fetching_content):
    mock_fetching_content.return_value = None

    result = scrape_page("https://example.com")

    assert result == []


@patch("utils.extract.scrape_page")
def test_scrape_main_success(mock_scrape_page):
    mock_scrape_page.return_value = [
        {
            "Title": "T-shirt 2",
            "Price": "$102.15",
            "Rating": "3.9 / 5",
            "Colors": "3 Colors",
            "Size": "M",
            "Gender": "Women",
            "timestamp": "2025-01-01T00:00:00"
        }
    ]

    result = scrape_main(start_page=1, end_page=2)

    assert len(result) == 2