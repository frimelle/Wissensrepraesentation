# -*- coding: utf-8 -*-
__author__ = 'simon'
from RDFParser.Parser import Parser
import urllib, urllib2, os

def clearGraph():
    params = {'graph': 'der_erwaehlte' }

    data = urllib.urlencode(params)
    request = urllib2.Request('http://localhost:8080/data/', data)
    request.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(request)
    print(response.read())

path = os.path.join(os.getcwd() + "/data/family_initial_data")
parser = Parser(path)

try:
    clearGraph()
    params = {'graph': 'der_erwaehlte',
               'data': parser.getGraph(),
               'mime-type' : 'application/x-turtle' }

    data = urllib.urlencode(params)
    request = urllib2.Request('http://localhost:8080/data/', data)
    request.get_method = lambda: 'POST'
    response = urllib2.urlopen(request)
    print(response.read())

    # opener = urllib2.build_opener(urllib2.HTTPHandler)
    # request.get_method = 'PUT'
    # url = opener.open(request)
    # url.read()

except Exception, e:
    raise e

