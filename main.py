#!/usr/bin/python

"""
Main file -- starter for convertor.
"""

import optparse
import os
import sys

import cxftags as tags
import records as recs
from unzip import UnzipStream

# Command line options: optparse.OptionParser()
options = None
args = None

def parseOptions():
  global options, args
  parser = optparse.OptionParser()
  parser.add_option("-p", '--preview-extract', dest="preview", type="string", default=None, help="Extract preview to given file")
  parser.add_option("-v", '--verbose', action="store_true", dest="verbose", default=False)
  (options,args) = parser.parse_args()

recordIndent = ""

def printRecord(rec):
  "Debug print of parsed record"
  global recordIndent
  # print recordIndent + tags.getTag(rec.tag)
  print recordIndent + tags.getTag(rec.tag) + " " + str(rec)
  if rec.tag == tags.TAG_DOWN:
    recordIndent += "  "
  elif rec.tag == tags.TAG_UP:
    recordIndent = recordIndent[:-2]

def handleRecord(rec):
  if options.verbose:
    printRecord(rec)
  if rec.tag == tags.TAG_PREVIEWBITMAP_GIF:
    savePreview(rec, ".gif")
  elif rec.tag == tags.TAG_PREVIEWBITMAP_PNG:
    savePreview(rec, ".png")
  elif rec.tag == tags.TAG_PREVIEWBITMAP_JPEG:
    savePreview(rec, ".jpg")

def savePreview(rec, extens):
  if options.preview:
    path = options.preview+extens
    print "Saving preview to '%s'" % path
    with open(path, "wb") as out:
      out.write(rec.data)

def parseRecordStream(fs, handler=printRecord):
  stream = fs
  if recs.parseID(stream):
    print "ID valid"
    rec = recs.parseRecord(stream)
    handler(rec)
    if rec.tag == tags.TAG_FILEHEADER:
      header = recs.parseFileHeader(rec.data)
      print header
      while True:
        rec = recs.parseRecord(stream)
        if rec.tag == tags.TAG_ENDOFFILE:
          handler(rec)
          break
        elif rec.tag == tags.TAG_STARTCOMPRESSION:
          stream = UnzipStream(fs)
        elif rec.tag == tags.TAG_ENDCOMPRESSION:
          stream.finish()
          stream = fs
          rec.data = stream.read(rec.size)
        handler(rec)

def main(args):
  if len(args) > 0:
    print "Opening '%s'" % args[0]
    with open(args[0]) as fs:
      parseRecordStream(fs, handler=handleRecord)

if __name__ == '__main__':
  parseOptions()
  tags.parseTags()
  main(args)
