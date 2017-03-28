import os
from random import randint
from time import sleep
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils import log_helper

log = log_helper.get_logger(__name__)


class NewsArticleSearchHelper(object):

    def __init__(self):
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = \
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36"
        self.driver = webdriver.PhantomJS(desired_capabilities=dcap, executable_path="/usr/bin/phantomjs")
        self.timeout_seconds = 10
        self.search_url = "https://news.google.com/news/advanced_news_search"

    def destroy(self):
        self.driver.quit()

    def get_news(self, search_term, start_time, end_time, pages_to_explore):

        headline_elements = list()
        url_list = list()
        sleep(randint(60, 120))

        try:
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
            log.debug("Fired search")

            while pages_to_explore > 0:

                sleep(randint(2, 4))

                log.debug("Getting large elements")
                try:
                    large_headline_elements = WebDriverWait(self.driver, self.timeout_seconds).until(
                        expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, ".l._HId"))
                    )
                    headline_elements.extend(large_headline_elements)
                except Exception:
                    log.debug("No large elements found on page")

                log.debug("Getting small elements")
                try:
                    small_headline_elements = WebDriverWait(self.driver, self.timeout_seconds).until(
                        expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, "._sQb"))
                    )
                    headline_elements.extend(small_headline_elements)
                except Exception:
                    log.debug("No small elements found on page")

                log.debug("Moving to the next page")
                try:
                    next_page_button = WebDriverWait(self.driver, self.timeout_seconds).until(
                        expected_conditions.presence_of_element_located((By.ID, "pnnext"))
                    )
                    next_page_button.click()
                except Exception:
                    log.debug("No next button found on page")
                    break

                pages_to_explore -= 1

            url_list = list(map(lambda x: x.get_attribute("href"), headline_elements))

        except Exception as e:
            log.error("Error while searching for news, skipping " + search_term + " " + start_time)
            log.error(e)

        return url_list
