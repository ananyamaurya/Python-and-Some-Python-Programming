
"""
author : ananya_maurya
"""
from time import sleep

from selenium import  webdriver

def test_single_input_text():
    chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    chrome_browser.maximize_window()
    ad_close_button = chrome_browser.find_element_by_class_name('at-cm-no-button')
    ad_close_button.click()
    input_field = chrome_browser.find_element_by_id('user-message')
    input_field.send_keys('Hip Hip Hurray')
    assert 'Show Message' in chrome_browser.page_source
    button_button = chrome_browser.find_elements_by_xpath("//form[@id='get-input']/button[1]")
    button_button[0].click()
    output_message = chrome_browser.find_element_by_id('display')
    assert 'Allah Maaf Kare' in output_message.text
    sleep(10)
    chrome_browser.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chrome_browser = webdriver.Chrome('./chromedriver')
    test_single_input_text()
