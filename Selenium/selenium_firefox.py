from selenium import webdriver

firefox = webdriver.Firefox()  # Initialize webdriver
firefox.get('http://www.google.com')  # .get is used to load an URL
