from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

def post_image(image_path, description, account="summalimetta", pw="pwhere"):

        service = Service("./chromedriver/chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument('headless');
        options.add_argument('window-size=1920x1060')
        driver = webdriver.Chrome(service=service, options=options)

        # open instagram
        driver.get("https://www.instagram.com")
        time.sleep(random.uniform(5, 10))

        # click away cookie screen
        cookie = driver.find_element(by=By.XPATH, value="//button[text()='Nur erforderliche Cookies erlauben']").click()
        time.sleep(random.uniform(5, 10))

        # login
        username = driver.find_element(by=By.CSS_SELECTOR, value="input[name='username']")
        username.clear()
        username.send_keys("summalimetta")
        time.sleep(random.uniform(3, 5))
        password = driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
        password.clear()
        password.send_keys("insertpwhere")
        time.sleep(random.uniform(3, 5))
        login = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']").click()
        time.sleep(random.uniform(5, 10))

        # click away notification window
        notnow = driver.find_element(by=By.XPATH, value="//button[text()='Jetzt nicht']").click()
        time.sleep(random.uniform(5, 10))

        # click new post button
        newpost = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
        time.sleep(random.uniform(5, 10))

        # chose from pc --- note needed, we can just inser the file directly
        # frompc = driver.find_element(by=By.XPATH, value="//button[text()='Vom Computer auswählen']").click()

        # enter file path
        # filedialog = driver.find_element(by=By.XPATH, value="//input[@type='file']")
        filedialog = driver.find_element(by=By.XPATH, value="/html/body/div[6]/div[2]/div/div/div/div[2]/div[1]/form/input")
        filedialog.send_keys(image_path)
        time.sleep(random.uniform(10, 20))

        # continue -- twice
        cont = driver.find_element(by=By.XPATH, value="//button[text()='Weiter']").click()
        time.sleep(random.uniform(5, 10))
        cont = driver.find_element(by=By.XPATH, value="//button[text()='Weiter']").click()
        time.sleep(random.uniform(5, 10))

        # fill description
        descr_box = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
        descr_box.send_keys(description)
        time.sleep(random.uniform(10, 20))

        # click share
        share = driver.find_element(by=By.XPATH, value="//button[text()='Teilen']").click()
        time.sleep(random.uniform(10, 20))