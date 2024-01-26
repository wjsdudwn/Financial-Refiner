import selenium
from selenium import webdriver
from oil import oil_crawler


class Crawler():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
    
    def oil(self) -> list:
        return oil_crawler(self.driver)
    

result = Crawler().oil()
for x in result:
    print(x)