from HTMLParser import HTMLParser, HTMLParseError
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "title":
        	print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
    	if tag == "title":
        	print "Encountered an end tag :", tag

    def handle_data(self, data):
    	if self.get_starttag_text() == "<title>":
        	print "Encountered some data  :", data

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:17.0) Gecko/20100101 Firefox/17.0')]
response = opener.open('http://www.cnn.com/2013/06/04/health/sunscreen-aging/index.html?hpt=hp_t1')
html = response.read()

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

try:
	parser.feed(html)
except HTMLParseError, e:
	# raise e
	print ""
