from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")

browser.get('https://apps.paybooks.in/')
assert 'Paybooks Login | Paybooks App | Paybooks Admin Login' in browser.title

elem = browser.find_element(By.NAME, 'p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()