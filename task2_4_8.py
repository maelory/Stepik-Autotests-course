from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    priceLabel = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    bookButton = browser.find_element_by_id('book')
    bookButton.click()

    '''
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    '''

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    print("X: ", x)
    y = calc(x)

    answerTextBox = browser.find_element_by_css_selector('#answer')
    answerTextBox.send_keys(y)

    submitButton = browser.find_element_by_css_selector('[type="Submit"]')
    submitButton.click()

finally:
    time.sleep(10)
    browser.quit()
