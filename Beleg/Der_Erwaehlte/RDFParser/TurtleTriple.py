# -*- coding: utf-8 -*-
from samba.dcerpc.smb_acl import t

__author__ = 'simon'
class TurtleTriple:

    def __init__(self, prefix, predicate, object, subject):
        self.prefix = prefix
        self.subject = subject
        self.object = object
        self.predicate = predicate

    def __str__(self):
        turtleString = self.prefix + self.subject
        turtleString += " "
        turtleString += self.prefix + self.predicate
        turtleString += " "
        turtleString += self.prefix + self.object
        turtleString += " .\n"
        return turtleString