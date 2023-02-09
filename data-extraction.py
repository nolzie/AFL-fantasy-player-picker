import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulStoneSoup
from typing import static 


class WebScraper:
    def __init__(self) -> None:
        pass

    def download_page(self, url):
        """Naively extracts all the html for a given url

        Parameters
        ----------
        url : string
            This is the url for the website of interest

        Returns
        -------
        string
            the html for the provided url
        """
        self.response = requests.get(url)
        self.response.raise_for_status()
        return self.response.text


url = 'https://dtlive.com.au/afl/dataview.php'


scraper = WebScraper()
page_content = WebScraper.download_page(url)

soup = BeautifulSoup(content, 'html.parser')