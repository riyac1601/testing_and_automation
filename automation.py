from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')
chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name("btn-default")
# print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys('I am EXTRA COOL!!')
show_message_button.click()

output_message = chrome_browser.find_element_by_id("display")
assert 'I am EXTRA COOL!!' in output_message.text

# chrome_browser.close()
chrome_browser.quit()
