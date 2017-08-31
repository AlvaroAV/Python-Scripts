import base64

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
    Method to download an image directly from the browser.
    With this method you avoid accessing the image more than one time.
    
    E.g.: If you have an image that's get reloaded every time you access the link, 
          with this method you avoid accessing the image twice
'''

driver = webdriver.Chrome()  # Initialize webdriver
driver.get('https://instagram.com')  # .get is used to load URL

# Get images from the browser
img = driver.find_elements_by_css_selector('img')
img = img[0]

# Get the image as a base64 string
img_base64 = driver.execute_async_script("""
    var e = arguments[0], callback = arguments[1];
    e.addEventListener('load', function fn(){
        e.removeEventListener('load', fn, false);
        var cnv = document.createElement('canvas');     
        cnv.width = this.naturalWidth; cnv.height = this.naturalHeight;
        cnv.getContext('2d').drawImage(this, 0, 0);
        callback(cnv.toDataURL('image/jpg').substring(22));
    }, false);
    e.dispatchEvent(new Event('load'));
""", img)

# Save the image to a file
with open(r"image.png", 'wb') as f:
    f.write(base64.b64decode(img_base64))
