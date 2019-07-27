import os
import json
import urllib.request
from selenium import webdriver


class Crawler:

    # constructor
    def __init__(self):
        self.keyword = str(input('keyword... : '))  # image keyword for searching
        self.dirPath = ""                           # image stored directory

    # create directory for download if it is not exist
    def createNewDirectory(self):
        cwd = os.getcwd()
        self.dirPath = os.path.join(cwd, self.keyword)

        if not os.path.exists(self.dirPath):
            os.mkdir(self.dirPath)

    # create the url path
    def createURL(self):
        url = 'https://www.google.com/search?q=' + self.keyword + '&source=lnms&tbm=isch'
        return url

    # search from chrome browser
    def searchURL(self, url):
        # ========== headless driver options ========== #
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("lang=ko_KR")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        # ... etc
        # ============================================= #

        # if you don't want headless driver, remove chrome_option argument
        browser = webdriver.Chrome('chromedriver.exe', chrome_options=chrome_options)
        browser.get(url)

        # scroll twice by 10000px
        for _ in range(1):
            browser.execute_script('window.scrollBy(0, 10000)')

        return browser

    # download the image
    def downloadImage(self, browser):
        elements = browser.find_elements_by_xpath('//div[contains(@class,"rg_meta")]')
        element_size = len(elements)  # used for progress status
        for idx, element in enumerate(elements):

            img = json.loads(element.get_attribute('innerHTML'))["ou"]
            img_type = json.loads(element.get_attribute('innerHTML'))["ity"]

            try:
                raw_img = urllib.request.urlopen(img).read()
                filePath = self.dirPath + '/' + str(idx) + '.' + img_type

                with open(filePath, mode="wb") as file:
                    file.write(raw_img)
            except:
                pass  # ignore exception

            # display progress status every 10 items
            if idx % 10 == 0:
                print('{}%  completed...'.format(idx * 100 / element_size))

        browser.close()  # close the browser

    # main routines
    def run(self):
        self.createNewDirectory()           # 1. create the directory
        url = self.createURL()              # 2. create the path
        browser = self.searchURL(url)       # 3. search image
        self.downloadImage(browser)         # 4. download image


