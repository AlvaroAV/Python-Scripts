
from selenium import webdriver

driver = webdriver.Chrome()  # Initialize webdriver
driver.get('http://www.example.com')  # .get is used to load URL

# Open new 3 tabs (only tested on chrome)
driver.execute_script("window.open('','_blank');")
driver.execute_script("window.open('','_blank');")
driver.execute_script("window.open('','_blank');")

# Get a list of the current window handles
window_handles = driver.window_handles
# window_handles contains something like:
# [u'CDwindow-f01a68c5-9132-469c-adb9-c6c48e2b6264', u'CDwindow-0afe0c13-075d-4a12-a02a-4664b4229386', u'CDwindow-3267c872-e31b-4584-80d6-2f98058a2c41', u'CDwindow-8d43f4b6-7c53-431f-98a9-0b0f709194c0']


# Get current tab ID
current_tab_id = driver.current_window_handle

# Get last opened tab ID
last_tab_id = driver.window_handles[-1]

# Switch to last_tab_id
driver.switch_to_window(window_handles[-1])
