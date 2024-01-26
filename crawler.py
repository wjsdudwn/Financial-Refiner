import selenium
import os
from oil import oil_crawler

#print(os.getcwd())
#print("hello world")
class Crawler():
    '''
    def __init__(self) -> None:
        # driver setting
        # set directory of chromedriver
        locate = os.getcwd() + "chromedriver.exe"
        driver = selenium.driver()
    '''
    def oil(self):
        return oil_crawler()
    

result = Crawler().oil()
print(result)