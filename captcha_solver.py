import pytesseract
import re
import requests
from PIL import Image
from StringIO import StringIO

# Two easy examples using PyTesseract to solve captchas

def solve_captcha_file(f):
    ''' Solve a captcha from image file '''
    
    img = Image.open(f)
    result = pytesseract.image_to_string(img).replace('\n', '')
    result = re.sub('\W+', '', result)  # Clean string

    return result


def solve_captcha_url(url):
    ''' Solve a captcha from image url '''
    
    response = requests.get(url)
    img = Image.open(StringIO(response.content))
    result = pytesseract.image_to_string(img).replace('\n', '')
    result = re.sub('\W+', '', result)  # Clean string

    return result
