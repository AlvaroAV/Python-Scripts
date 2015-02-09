from selenium import webdriver

chrome_options = webdriver.ChromeOptions()  # Initialize your Chrome optioms

IP_PORT = '185.72.156.19:8089'  # Change this IP:PORT for your desired proxy
chrome_options.add_argument('--proxy-server=http://%s' % IP_PORT)

chrome = webdriver.Chrome(chrome_options=chrome_options)  # Initialize webdriver

chrome.get('http://www.myip.es')  # Get this URL, this page should return the IP of your proxy
