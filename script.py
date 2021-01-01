from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from PIL import Image

import os
os.mkdir("result")

prn = []
seat_num = []

# MAKE CHANGE HERE
for i in range(19020475001, 19020475026):
    prn.append(i)

# MAKE CHANGE HERE
for i in range(100501, 100530):
    seat_num.append(i)


chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome(options=chrome_options)


for username in prn:

    browser.get("https://www.examination.siu.edu.in/examination/result.html")
    browser.switch_to.frame(0)


    for password in seat_num:

        browser.find_element_by_id("login").send_keys(username)

        browser.find_element_by_name("Submit").click()

        browser.find_element_by_id("login").send_keys(password)

        browser.find_element_by_name("Submit").click()

        try:
            WebDriverWait(browser, 2).until(EC.alert_is_present())
            alert = browser.switch_to.alert
            alert.accept()

        except TimeoutException:
            break

    ele = browser.find_element("xpath", '/html')
    total_height = ele.size["height"] + 1000

    browser.set_window_size(1920, total_height)
    browser.save_screenshot(f"./result/{username}.png")

    element = browser.find_element_by_xpath("/html/body/div[3]/div/div/div/div/table/tbody/tr/td/table/tbody")

    location = element.location
    size = element.size

    x = location['x']
    y = location['y']
    width = location['x']+size['width']
    height = location['y']+size['height']

    im = Image.open(f'./result/{username}.png')
    im = im.crop((int(x), int(y), int(width), int(height)))
    im.save(f'./result/{username}.png')

    seat_num.remove(password)


browser.quit()

# END OF SCRIPT