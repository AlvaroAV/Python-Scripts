import urllib2

# This is an example to get HTML code from desired URL
url = 'http://www.google.com'

urllib_object = urllib2.urlopen(url)  # Open url of the IP web camera
html_source = urllib_object.read()  # Read from the urllib object to get the source code
