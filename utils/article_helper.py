import os
from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NewsArticleSearchHelper(object):

    def __init__(self):
        chromedriver = "/home/v2john/Tools/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.timeout_seconds = 10
        self.search_url = "https://news.google.com/news/advanced_news_search"

    def get_news(self, search_term, start_time, end_time, pages_to_explore):
        self.driver.get(self.search_url)

        keyword_box = WebDriverWait(self.driver, self.timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, "all-keyword-input"))
        )
        keyword_box.send_keys(search_term)
        sleep(randint(1, 2))

        occurrence_selector = WebDriverWait(self.driver, self.timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, "position-filter-select"))
        )
        occurrence_selector.click()
        sleep(randint(1, 2))

        headline_selector = WebDriverWait(self.driver, self.timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, ":3"))
        )
        headline_selector.click()
        sleep(randint(1, 2))

        date_range_selector = WebDriverWait(self.driver, self.timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, "date-filter-select"))
        )
        date_range_selector.click()
        sleep(randint(1, 2))

        custom_range_selector = WebDriverWait(self.driver, self.timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, ":e"))
        )
        custom_range_selector.click()
        sleep(randint(1, 2))

        startDateBox = WebDriverWait(self.driver, self.timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, "ansp_start-date"))
        )
        startDateBox.send_keys(start_time)
        sleep(randint(1, 2))

        endDateBox = WebDriverWait(self.driver, self.timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, "ansp_end-date"))
        )
        endDateBox.send_keys(end_time)
        sleep(randint(1, 2))

        searchButton = WebDriverWait(self.driver, self.timeout_seconds).until(
            expected_conditions.presence_of_element_located((By.ID, "ansp_search-button"))
        )
        searchButton.click()

        # self.driver.quit()
