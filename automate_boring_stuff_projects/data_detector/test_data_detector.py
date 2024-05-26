"""
test_data_detector.py - Unit test for data_detect functions.
It uses pytest for testing and parametrize to test multiple input-output scenarios.
This script contains tests:
- date_detect
- url_detect

Written by Sergey Torshin @torshin5ergey
"""

import pytest
from data_detector import url_detect, date_detect

# Decorator for parametrizing a test function with multiple sets of input-expected
@pytest.mark.parametrize("text, expected", [
    ("https-sub-domain-tld https://www.example.org", "https://www.example.org"),
    ("http-sub-domain-tld/ http://www.example.org/", "http://www.example.org"),
    ("domain-tld exampleWebSite.org", "exampleWebSite.org"),
    ("domain-tld-tld google.co.uk", "google.co.uk"),
    ("domain-tld facebook.net", "facebook.net"),
    ("domain-tld-tld google.com.ng", "google.com.ng"),
    ("domain-tld-tld google.com.in", "google.com.in"),
    ("https-sub-domain-tld-path https://www.example.org/news", "https://www.example.org/news"),
    ("https-sub-domain-tld-path https://www.example.org/chinese/", "https://www.example.org/chinese"),
    ("https-sub-sub-domain-tld https://www.chinese.example.org", "https://www.chinese.example.org"),
    ("sub-domain-tld zh.wikipedia.org", "zh.wikipedia.org"),
    ("http-sub-domain-tld https://chinese.example.org", "https://chinese.example.org"),
    ("https-domain-path https://example.com/path/to/page", "https://example.com/path/to/page"),
    ("https-domain-tld-params https://example.com?param1=value1&param2=value2", "https://example.com?param1=value1&param2=value2"),
    ("https-domain-tld-section https://example.com#section", "https://example.com#section"),
    ("https-domain-tld-port https://example.com:8080", "https://example.com:8080"),
    ("No URLs in this text", None),
    ("""Сайт компании: https://www.example.com
Подробнее о продукте: http://example.com/product-details
Ссылка на блог: www.blog.example.org
Последняя статья: https://blog.example.org/latest-article
Контактная форма: https://www.example.com/contact-us
Ссылка на ресурс: https://resources.example.com/resource1
Поиск по сайту: https://www.example.com/search?query=python
Фрагмент обновлений: https://www.example.com#updates
Социальный профиль: https://twitter.com/example
Пост в блоге: https://blog.example.org/post/12345
Справка и поддержка: https://help.example.com
Раздел FAQ: https://www.example.com/faq
Страница с картой сайта: https://www.example.com/sitemap""", """https://www.example.com
http://example.com/product-details
www.blog.example.org
https://blog.example.org/latest-article
https://www.example.com/contact-us
https://resources.example.com/resource1
https://www.example.com/search?query=python
https://www.example.com#updates
https://twitter.com/example
https://blog.example.org/post/12345
https://help.example.com
https://www.example.com/faq
https://www.example.com/sitemap""")
])
@pytest.mark.skip
def test_url_detector(text, expected):
    assert url_detect(text) == expected

# Decorator for parametrizing a test function with multiple sets of input-expected
@pytest.mark.parametrize("text, expected", [
    ("Today is 2024-05-10 and tomorrow is 11/05/2024", "2024-05-10\n11/05/2024"),
    ("No dates in this text.", None),
    ("2022-01-01 is a date", "2022-01-01"),
    ("This is a date: 01-01-2022", "01-01-2022"),
    ("Another date: 2022/01/01", "2022/01/01"),
    ("Clean up dates in different date formats (such as 3/14/2019, 03-14-2019, and 2015/3/19) by replacing them with dates in a single, standard format.", "3/14/2019\n03-14-2019\n2015/3/19")
    ])
def test_data_detector(text, expected):
    assert date_detect(text) == expected

