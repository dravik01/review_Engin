import time
import pyautogui
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--lang=en-us")
options.add_argument("--disable-web-security")
options.add_argument("--allow-running-insecure-content")   
options.add_argument("--start-maximized") 
options.add_argument("--no-sandbox") #bypass OS security model
options.add_argument("--disable-dev-shm-usage") 
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# open browser
driver = webdriver.Chrome(executable_path="chromedriver", options=options)
url = "https://www.imdb.com"
driver.get(url)
driver.implicitly_wait(5)

with open("email.txt") as f:
    name = f.read()
    data = list(map(str, name.split('\n')))
    # print(words[0])


for i in data:
    email, pwd = i.split(' ')
    # Login 
    driver.find_element_by_xpath('//*[@id="imdbHeader"]/div[2]/div[5]/a').click()
    driver.implicitly_wait(5)

    driver.find_element_by_xpath('//*[@id="signin-options"]/div/div[1]/a[1]').click()
    driver.implicitly_wait(5)

    username = driver.find_element_by_xpath('//*[@id="ap_email"]')
    username.send_keys(email)
    driver.implicitly_wait(2)

    username = driver.find_element_by_xpath('//*[@id="ap_password"]')
    username.send_keys(pwd)
    driver.implicitly_wait(2)

    driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()

    with open("name.txt") as f:
        name = f.read()
        words = (list(map(str, name.split('\n'))))
                                            
    # Search Movie
    for i in words:
        name = i
        search = driver.find_element_by_xpath('//*[@id="suggestion-search"]')
        search.send_keys(name)
        driver.implicitly_wait(2)

        driver.find_element_by_xpath('//*[@id="suggestion-search-button"]').click()
        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
        driver.implicitly_wait(5)
        time.sleep(5)

        # Click on review button
        driver.find_element_by_xpath("//a[@class='ipc-button ipc-button--single-padding ipc-button--center-align-content ipc-button--default-height ipc-button--core-base ipc-button--theme-base ipc-button--on-accent2 ipc-text-button AddReviewActionButton__AddReviewButton-sc-11e8do2-0 ktUycW']").click()
        driver.implicitly_wait(5)
        time.sleep(5)


        # Give Review
        tabs = random.randint(9,10)
        # print(tabs)
        pyautogui.press('tab', tabs)
        pyautogui.press('enter')

        next_ele = 12 - tabs
        pyautogui.press('tab', next_ele)

        # write review
        with open("words.txt", "r") as f:
            allText = f.read()
            words = list(map(str, allText.split()))

        review = '' 
        for i in range(10):
            review += (random.choice(words)) + " "

        # print(review)
        pyautogui.write(random.choice(words))
        pyautogui.press('tab')
        pyautogui.write(review+"\U0001F44D"+"\U0001F44C"+".")

        # check NO and Press enter Manually 
        pyautogui.click(1306,615)

        # submit review
        pyautogui.press('tab')
        pyautogui.press('enter')
        # time.sleep(5)
        # print("exit")

        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(2)
        # # Exit browser

    driver.find_element_by_xpath("//div[@class='_3x17Igk9XRXcaKrcG3_MXQ navbar__user UserMenu-sc-1poz515-0 lkfvZn']").click()
    driver.implicitly_wait(5)
    time.sleep(2)

    pyautogui.press('tab', 6)
    pyautogui.press('enter')

    # driver.quit()