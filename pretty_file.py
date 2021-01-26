#!/usr/bin/python

import json
import pprint
import sys

theFile = sys.argv[1]

# Opening JSON file 
theFile = open(theFile)
  
# returns JSON object as  
# a dictionary 
theJson = json.load(theFile) 
  
pp = pprint.PrettyPrinter()
pp.pprint(theJson)

