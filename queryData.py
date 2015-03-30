# This Python file uses the following encoding: utf-8
#!/usr/bin/python
from SPARQLWrapper import SPARQLWrapper, JSON

tante_query = """
    PREFIX wrr: <http://github.com/frimelle/Wissensrepraesentation/relation/>
    SELECT *
    WHERE { { ?kind wrr:sohnVon ?eltern . } UNION { ?kind wrr:tochterVon ?eltern . }
            {?tante wrr:schwesterVon ?eltern . } }
"""

cousine_query = """
    PREFIX wrr: <http://github.com/frimelle/Wissensrepraesentation/relation/>
    SELECT *
    WHERE { { ?kind wrr:sohnVon ?eltern . } UNION { ?kind wrr:tochterVon ?eltern . }
            {?tanteOnkel wrr:schwesterVon ?eltern . } UNION {?tanteOnkel wrr:bruderVon ?eltern . }
            {?cousine wrr:tochterVon ?tanteOnkel . }}
"""

cousin_query = """
    PREFIX wrr: <http://github.com/frimelle/Wissensrepraesentation/relation/>
    SELECT *
    WHERE { { ?kind wrr:sohnVon ?eltern . } UNION { ?kind wrr:tochterVon ?eltern . }
            {?tanteOnkel wrr:schwesterVon ?eltern . } UNION {?tanteOnkel wrr:bruderVon ?eltern . }
            {?cousin wrr:sohnVon ?tanteOnkel . }}
"""

nichte_query = """
        PREFIX wrr: <http://github.com/frimelle/Wissensrepraesentation/relation/>
        SELECT *
        WHERE { { ?kind wrr:bruderVon ?geschwister . } UNION { ?kind wrr:schwesterVon ?geschwister . }
                {?nichte wrr:tochterVon ?geschwister . }}
"""

def queryData( sparql_query ):
    try:
        sparql = SPARQLWrapper("http://localhost:8000/sparql/")
        sparql.setQuery( sparql_query )
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        return results
    except Exception, e:
        raise e

### Query nach Tante
results_tante = queryData( tante_query )
for result in results_tante["results"]["bindings"]:
    print result["tante"]['value'] + " tante von " + result["kind"]['value']

### Query nach Cousine
results_cousine = queryData( cousine_query )
for result in results_cousine["results"]["bindings"]:
    print result["cousine"]['value'] + " cousine von " + result["kind"]['value']

### Query nach Cousin
results_cousin = queryData( cousin_query )
for result in results_cousin["results"]["bindings"]:
    print result["cousin"]['value'] + " cousin von " + result["kind"]['value']

### Query nach Nichte
results_nichte = queryData( nichte_query )
for result in results_nichte["results"]["bindings"]:
    print result["nichte"]['value'] + " nichte von " + result["kind"]['value']
