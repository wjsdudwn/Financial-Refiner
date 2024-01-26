import selenium
import os


#print(os.getcwd())
#print("hello world")
class crawler():
    def __init__(self) -> None:
        # driver setting
        # set directory of chromedriver
        locate = os.getcwd() + "chromedriver.exe"
        driver = selenium.driver()
