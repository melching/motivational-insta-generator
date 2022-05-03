from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

def post_image(image_path, description, account="summalimetta", pw="pwhere"):
        print("Start Selenium.")

        service = Service("./chromedriver/chromedriver")
        options = webdriver.ChromeOptions()
        # options.add_experimental_option('prefs', {'intl.accept_languages': 'de,de_DE'})
        options.add_argument('--headless')
        options.add_argument('--window-size=1920x1060')
        options.add_argument('--lang=de_DE')
        driver = webdriver.Chrome(service=service, options=options)
        try:
                print("Open Instagram.")
                # open instagram
                driver.get("https://www.instagram.com")
                time.sleep(random.uniform(5, 10))

                print("Removing Cookie Popup")
                # click away cookie screen
                cookie = driver.find_element(by=By.XPATH, value="//button[text()='Nur erforderliche Cookies erlauben' or text()='Only allow essential cookies']").click()
                time.sleep(random.uniform(5, 10))

                # login
                print("Logging In.")
                username = driver.find_element(by=By.CSS_SELECTOR, value="input[name='username']")
                username.clear()
                username.send_keys(account)
                time.sleep(random.uniform(3, 5))
                password = driver.find_element(by=By.CSS_SELECTOR, value="input[name='password']")
                password.clear()
                password.send_keys(pw)
                time.sleep(random.uniform(3, 5))
                login = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']").click()
                time.sleep(random.uniform(5, 10))

                print("Remove Notification Popup.") # not needed in headless mode
                # # click away notification window
                # notnow = driver.find_element(by=By.XPATH, value="//button[text()='Jetzt nicht']").click()
                # time.sleep(random.uniform(5, 10))

                # click new post button
                print("Start Posting Image.")
                newpost = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
                time.sleep(random.uniform(5, 10))

                # enter file path
                # filedialog = driver.find_element(by=By.XPATH, value="//input[@type='file']")
                filedialog = driver.find_element(by=By.XPATH, value="/html/body/div[8]/div[2]/div/div/div/div[2]/div[1]/form/input")

                filedialog.send_keys(image_path)
                time.sleep(random.uniform(10, 20))

                # continue -- twice
                cont = driver.find_element(by=By.XPATH, value="//button[text()='Weiter' or text()='Next']").click()
                time.sleep(random.uniform(5, 10))
                cont = driver.find_element(by=By.XPATH, value="//button[text()='Weiter' or text()='Next']").click()
                time.sleep(random.uniform(5, 10))

                # fill description
                # descr_box = driver.find_element(by=By.XPATH, value="/html/body/div[4]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea")
                descr_box = driver.find_element(by=By.CSS_SELECTOR, value='textarea[placeholder="Bildunterschrift verfassen …"],textarea[placeholder="Write a caption..."]')
                descr_box.send_keys(description)
                time.sleep(random.uniform(10, 20))

                # click share
                share = driver.find_element(by=By.XPATH, value="//button[text()='Teilen' or text()='Share']").click()
                print("Done.")
                time.sleep(random.uniform(10, 20))
        except Exception as e:
                driver.save_screenshot("screenshot.png")
                raise
