# This Python file uses the following encoding: utf-8
#!/usr/bin/python
import urllib, urllib2, os

def clearGraph():
    params = { 'graph': 'der_erwaehlte' }
    data = urllib.urlencode( params )
    print data
    request = urllib2.Request( 'http://localhost:8000/data/', data )
    request.get_method = lambda: 'DELETE'
    response = urllib2.urlopen( request )
    print( response.read() )

def get_graph():
    graph = ""
    # Die selbstgeschriebenen Daten
    #path = os.path.join( os.getcwd() + "/data/turtle-family-data.ttl" )
    # Die durchs Python Skript erzeugten Daten
    path = os.path.join( os.getcwd() + "/data/family_data_script.ttl" )
    with open ( path, "r") as myfile:
        graph = myfile.read().replace('\n', '')
    return graph



try:
    clearGraph()
    params = { 'graph': 'der_erwaehlte',
    'data': get_graph(),
    'mime-type' : 'application/x-turtle' }
    data = urllib.urlencode( params )
    request = urllib2.Request( 'http://localhost:8000/data/', data )
    request.get_method = lambda: 'POST'
    response = urllib2.urlopen( request )
    print( response.read() )

except Exception, e:
    raise e
