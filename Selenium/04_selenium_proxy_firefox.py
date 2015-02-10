from selenium import webdriver
from selenium.webdriver.common.proxy import *

profile = webdriver.FirefoxProfile()  # Generate Firefox profile


IP_PORT = "185.72.156.19:8089"
proxy = Proxy({  # Generate proxy settings for firefox
    'proxyType': ProxyType.MANUAL,
    'httpProxy': IP_PORT,
    'ftpProxy': IP_PORT,
    'sslProxy': IP_PORT,
    'noProxy': IP_PORT
    })

firefox = webdriver.Firefox(proxy=proxy)  # Load Firefox webdriver
firefox.get('http://www.myip.es')  # Get this URL, this page should return the IP of your proxy
