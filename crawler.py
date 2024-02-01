import selenium
from selenium import webdriver
from oil import oil_crawler
from selenium.webdriver.chrome.options import Options

class Crawler():
    def __init__(self) -> None:
        option = Options()
        option.add_argument("--headless=new")
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome() 
    def oil(self) -> list:
        
        return oil_crawler(self.driver, "Energy")
        
print(Crawler().oil())