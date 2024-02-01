import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
def random_time() -> float:
    return random.uniform(0.5, 1)
def oil_crawler(driver, searchTerm) -> list:
    # user setting
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    driver.implicitly_wait(10)
    
    driver.get("https://www.financialjuice.com/home") #사이트 접속
    
    
    # click sign in button
    li = driver.find_element(By.ID, 'liSignIn')
    li.find_element(By.TAG_NAME, "a").click() 

    # input userID & PWD
    inputEmail = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_inputEmail")
    time.sleep(random_time())

    inputPWD = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_inputPassword")
    time.sleep(random_time())

    inputEmail.send_keys("jhnamugeona@gmail.com")
    inputPWD.send_keys("sangmoon123")
    time.sleep(random_time())

    # finish login
    loginButton = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_btnLogin") # find by id
    loginButton.click()
    time.sleep(random_time())
    
    # move to Commodities tab
    # no class at commodities button -> use xpath
    temp = driver.find_element(By.XPATH, 
        "//*[@id=\"aspnetForm\"]/div[3]/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div/div/div[1]/ul/li[4]/a"
        )
    temp.click()
    
    # get Tag & title
    headline = driver.find_elements(By.CLASS_NAME, "headline-item") # webElement object(include tag, title...) in list
    # ===================  
    # <class name guide>
    # tag & time => drag-up
    # title => headline-title
    # ===================
    result = []
    for x in headline:
        tag = x.find_element(By.CLASS_NAME, "drag-up").text
        if searchTerm in tag:
            result.append(x.find_element(By.CLASS_NAME, "headline-title").text)
    return result
    