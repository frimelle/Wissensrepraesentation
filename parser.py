# This Python file uses the following encoding: utf-8
#!/usr/bin/python
import os

def parseLine(line):

    # Vor der ersten Klammer ist das Prädikat
    parametersStartIndex = line.index( "(" )

    # Zwischen den Klammern sind Subjekt und Objekt (die Parameter)
    parametersEndIndex = line.index( ")" )

    praedikat = line[:parametersStartIndex]
    parameter = line[parametersStartIndex + 1:parametersEndIndex].split(",")
    praedikat = praedikat.strip()
    parameter = [ x.strip() for x in parameter ]

    #Wenn es keinen zweiten Parameter gibt, wird "a" (turtle: rdf:type) als Prädikat verwendet
    if ( len( parameter ) == 1):
        parameter = [ praedikat ] + parameter
        praedikat = "a"

    relation = [ praedikat ] + parameter
    return relation

def turtleStr(prefix, praedikat, objekt, subjekt):
    tstring = prefix + subjekt
    tstring += " "
    # für das a als rdf:typ  wird kein Prefix benötigt
    if praedikat is "a":
        tstring += praedikat
    else:
        tstring += prefixr + praedikat + "Von"
    tstring += " "
    tstring += prefix + objekt
    tstring += " . \n"
    return tstring

def writeFile( filepath, graph ):
    f = open( filepath, 'w+' )
    f.write( graph )
    f.close

# den Prefix setzten um für das turtle Dokument
wrPrefix = "@prefix wrp: <http://github.com/frimelle/Wissensrepraesentation/person/> ."
wrrPrefix = "@prefix wrr: <http://github.com/frimelle/Wissensrepraesentation/relation/> ."
prefix = "wrp:"
prefixr = "wrr:"

path = os.path.join( os.getcwd() + "/data/family_initial_data" )
writepath = os.path.join( os.getcwd() + "/data/family_data_script.ttl" )

graph = wrPrefix + "\n" + wrrPrefix + "\n"

file = open(path, 'r')
for line in file:
    relation = parseLine(line.strip("\n"))
    graph += turtleStr(prefix, relation[0], relation[1], relation[2])

writeFile( writepath, graph )
