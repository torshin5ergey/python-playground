#! python3

# searchpypi.py - Opens several search results for PyPi


import sys
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def setup_webdriver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    return webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=options
    )

def search_pypi(driver, query):
    search_url = "https://pypi.org/search?q="
    driver.get(search_url + query)
    try:
        wait = WebDriverWait(driver, 5)
        elements = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".package-snippet"))
        )
        return elements
    except TimeoutException:
        return []

def open_search_results(links, max_results=5):
    num_to_open = min(max_results, len(links))
    for link in links[:num_to_open]:
        url = link.get_attribute("href")
        print("Opening", url)
        webbrowser.open(url)


def main():
    print("Searching...")
    driver = setup_webdriver()
    try:
        search_query = " ".join(sys.argv[1:])
        links = search_pypi(driver, search_query)
        open_search_results(links)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
