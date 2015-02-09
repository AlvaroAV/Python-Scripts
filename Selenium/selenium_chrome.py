from selenium import webdriver

chrome = webdriver.Chrome()  # Initialize webdriver

chrome.get('http://www.google.com')  # .get is used to load URL
