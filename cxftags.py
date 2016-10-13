#!/usr/bin/python

"""
This module provides TAG numbers.
Actually it parses ./include/cxftags.h for TAG definitions.
"""

import re
import sys

INCLUDE_PATH = "./include/cxftags.h"

# Example: #define TAG_UP                    0
RE_TAG_V1 = re.compile("#define\s+(?P<name>TAG_[A-Z0-9_]+)\s+(?P<value>[0-9]+)")

# Example: const ULONG TAG_OVERPRINTLINEON                      = 3500;
RE_TAG_V2 = re.compile("const\s+ULONG\s+(?P<name>TAG_[A-Z0-9_]+)\s*=\s*(?P<value>[0-9]+);")

tagIndex = {}

def registerTag(name, value):
  # print "%s = %s" % (name, value)
  numval = int(value)
  globals()[name] = numval
  tagIndex[numval] = name

def getTag(value):
  return tagIndex.get(value)

def parseTags(path=INCLUDE_PATH, callback=registerTag):
  with open(path,"rt") as f:
    for line in f:
      line = line.strip()
      m = RE_TAG_V1.match(line)
      if m:
        callback(m.group("name"), m.group("value"))
      m = RE_TAG_V2.match(line)
      if m:
        callback(m.group("name"), m.group("value"))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    parseTags(path=sys.argv[1])
  else:
    parseTags()
