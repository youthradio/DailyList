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


response = urllib2.urlopen('http://thecnnfreedomproject.blogs.cnn.com/2013/02/12/bras-offers-lifeline-to-rescued-slaves/?hpt=hp_c2')
html = response.read()

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()

try:
	parser.feed(html)
except HTMLParseError, e:
	# raise e
	print ""
