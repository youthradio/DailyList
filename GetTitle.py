from HTMLParser import HTMLParser, HTMLParseError
import urllib2

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.title = ''

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        if tag == "title":
            print "Encountered an end tag :", tag

    def handle_data(self, data):
<<<<<<< HEAD
        if self.get_starttag_text() == "<title>":
=======
    	if self.get_starttag_text() == "<title>":
>>>>>>> cbd84d65a57d717bd9ae6989aa9fe69675928907
            print "Encountered some data  :", data
            self.title = self.title + data


def getPageTitle(url):

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:17.0) Gecko/20100101 Firefox/17.0')]
    response = opener.open(url)
    html = response.read()

    # instantiate the parser and fed it some HTML
    parser = MyHTMLParser()

    try:
<<<<<<< HEAD
        parser.feed(html)
        return parser.title

    except HTMLParseError, e:
        # raise e
        print ""
=======
    	parser.feed(html)
        return parser.title

    except HTMLParseError, e:
    	# raise e
    	print ""
>>>>>>> cbd84d65a57d717bd9ae6989aa9fe69675928907
