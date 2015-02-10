import urllib2

opener = urllib2.build_opener()  # Generate an opener to add our headers
opener.addheaders = [('User-agent', 'Mozilla/8.2')]  # Add User-agent Mozilla

site = opener.open('http://fmbip.com/')  # Open the url with this opener and its headers
html_code = site.read()

index = html_code.index("browser-id")  # Find the part in the HTML about the browser
print html_code[index:index+225]  # Print the HTML part for the site, it detects browser as Firefox
