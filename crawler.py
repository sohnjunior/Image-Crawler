import os
import json
import urllib.request
from selenium import webdriver

from tqdm import tqdm

import re
import base64
from io import BytesIO
from PIL import Image


def get_image_from_base64(codec):
    """ convert base64 to image """
    base64_data = re.sub('^data:image/.+;base64,', '', codec)
    img = Image.open(BytesIO(base64.b64decode(base64_data)))
    if img.mode != 'RGB':
        img = img.convert('RGB')
    return img


class Crawler:
    """
    Google Web Image Crawler
    """
    def __init__(self):
        self.keyword = str(input('keyword... : '))  # image keyword for searching
        self.dirPath = ""                           # image stored directory

    def create_new_directory(self):
        """
        Create directory for download if it is not exist
        :return: None
        """
        self.cwd = os.getcwd()
        self.dirPath = os.path.join(self.cwd, self.keyword)

        if not os.path.exists(self.dirPath):
            os.mkdir(self.dirPath)

    def create_url(self):
        """
        Create the url path
        :return: url for searching
        """
        url = 'https://www.google.com/search?q=' + self.keyword + '&source=lnms&tbm=isch'
        return url

    def search_url(self, url):
        """
        Search from chrome browser
        :param url: search url
        :return: webdriver
        """
        # ========== headless driver options ========== #
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("lang=ko_KR")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        # ... etc
        # ============================================= #

        # if you don't want headless driver, remove chrome_option argument
        browser = webdriver.Chrome(os.path.join(self.cwd,'chromedriver'), chrome_options=chrome_options)
        browser.get(url)
        print(url)
        # scroll twice by 10000px
        for _ in range(1):
            browser.execute_script('window.scrollBy(0, 10000)')

        return browser

    def download_image(self, browser):
        """
        Download the image
        :param browser: google webdriver
        :return: None
        """
        elements = browser.find_elements_by_xpath('//img[contains(@class,"rg_i")]')
        element_size = len(elements)  # used for progress status

        for idx in tqdm(range(element_size), bar_format='{l_bar}{bar:20}{r_bar}{bar:-10b}'):
            save_path = self.dirPath + '/' + str(idx) + '.jpg'
            img_src = elements[idx].get_attribute('src')
            if img_src is None:
                img_src = elements[idx].get_attribute('data-src')

            if str(img_src).startswith('data:image'):
                img = get_image_from_base64(img_src)
                img.save(save_path, 'JPEG')
            else:
                try:
                    urllib.request.urlretrieve(img_src, save_path)
                except Exception as e:
                    print('exception: ', idx, e)

        browser.close()  # close the browser

    def run(self):
        """
        main routines
        :return:
        """
        self.create_new_directory()           # 1. create the directory
        url = self.create_url()              # 2. create the path
        browser = self.search_url(url)       # 3. search image
        self.download_image(browser)         # 4. download image


if __name__ == '__main__':
    newCrawler = Crawler()  # create new crawler
    newCrawler.run()
