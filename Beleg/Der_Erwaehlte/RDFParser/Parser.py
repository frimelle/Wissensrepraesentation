# -*- coding: utf-8 -*-
__author__ = 'simon'

import os, sys
from TurtleTriple import TurtleTriple

class Parser:
    """" this class takes raw (prolog style) family relation data and converts it to turtle syntax """

    wtPrefix = "@prefix wt: <http://github.com/frimelle/Wissensrepraesentation/> ."

    def __init__(self, initial_data_file):
        if not os.path.isfile(initial_data_file):
            raise "Error parsing initial data: File " + initial_data_file + " not found"

        self.relations = self.readInitialData(initial_data_file)
        self.triples = [ TurtleTriple("wt:", relation[0], relation[1], relation[2]) for relation in self.relations ]

    def readInitialData(self, initialDataFile):
        fileHandle = open(initialDataFile, 'r')
        # Read lines from the raw data and store them in the relation list which is formatted as follows:
        # [ [ relation, parameter1, parameter2 ... ] [ relation, parameter1, parameter2... ] ]
        relations = []
        for line in fileHandle:
            try:
                relations.append(self.splitLine(line.strip("\n")))
            except ValueError:
                print("Malformatted raw line: " + line)
                continue
        fileHandle.close()
        return relations

    def splitLine(self, line):
        """
        :param line:
        :return: A list where the first index is always the relation and the second (and optional third)
            indices are the subject and object
            Order: predicate, object, subject
        """
        # Extract until first brace as this is the relation
        parametersStartIndex = line.index( "(" )
        # Between the braces are the parameters
        parametersEndIndex = line.index( ")" )

        predicate = line[:parametersStartIndex]
        parameters = line[parametersStartIndex + 1:parametersEndIndex].split(",")

        predicate = predicate.strip()
        parameters = [ x.strip() for x in parameters ]

        # If there is no second parameters the predicate becomes the object
        # and the predicate is a simple "is"
        if (len( parameters ) == 1):
            parameters = [ predicate ] + parameters
            predicate = "is"

        relation = [ predicate ] + parameters
        return relation

    def getGraph(self):
        graph = self.wtPrefix + "\n"
        for triple in self.triples:
            graph += str(triple)
        return graph

parser = Parser("../data/family_initial_data")
graphFile = open("../der_erwaehlte.ttl", "w")
graphFile.write(parser.getGraph())
graphFile.close()
