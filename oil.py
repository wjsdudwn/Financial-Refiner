import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
def random_time():
    return random.uniform(0.5, 1.5)
def oil_crawler():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    options = Options()
    options.add_experimental_option("detatch", True)
    options.add_argument("--disable-blink-features=AutomationControlled") #강제로 자동화 브라우저가 아님을 말함
    driver = webdriver.Chrome() #executable_path = ''
    driver.implicitly_wait(10)
    driver.get("https://www.financialjuice.com/home") #사이트 접속
    signin_li = driver.find_element(By.ID, 'liSignIn') # Sign in 버튼을 포함하는 li 태그 찾기
    signin_a = signin_li.find_element(By.TAG_NAME, "a") # li 태그 안에 있는 a 태그 선택
    signin_a.click() # 클릭해서 로그인 창으로 이동
    input_email = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_inputEmail")
    time.sleep(random_time())
    input_password = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_inputPassword")
    time.sleep(random_time())
    input_email.send_keys("jhnamugeona@gmail.com")
    time.sleep(random_time())
    input_password.send_keys("sangmoon123")
    time.sleep(random_time())
    login_button = driver.find_element(By.ID, "ctl00_SignInSignUp_loginForm1_btnLogin") #버튼인데 input 태그로 되어 있음
    time.sleep(random_time())
    login_button.click()
    time.sleep(60)
    headline_list = driver.find_elements(By.CLASS_NAME, 'headline-title')
    title = driver.title



    return title

oil_crawler()