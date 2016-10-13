#!/usr/bin/python

"""
Parser for Xara File Records.
"""

from StringIO import StringIO
from struct import Struct

ID_XARA   = 0x41524158
ID_POUNDS = 0x0a0dA3A3
STRING_TERMINATOR = "\0\0"
ASCII_STRING_TERMINATOR = "\0"

# End of compressin requires special handling
TAG_ENDCOMPRESSION = 31

INTINT = Struct("<II")

def parseID(fs):
  "Tries to read and check the file ID (magic number). Returns True if correct, raises IOError when not correct."
  buf = fs.read(INTINT.size)
  if len(buf) < INTINT.size:
    raise IOError("Unexpected end of file")
  data = INTINT.unpack(buf)
  if data[0] == ID_XARA and data[1] == ID_POUNDS:
    return True
  else:
    raise IOError("Invalid file format: ID does not match")

def parseRecord(fs):
  "Reads common record from given file stream."
  buf = fs.read(INTINT.size)
  if len(buf) < INTINT.size:
    raise IOError("Unexpected end of file reading record header")
  (tag, size) = INTINT.unpack(buf)
  if size > 0 and not tag == TAG_ENDCOMPRESSION:
    data = fs.read(size)
    if len(data) < size:
      raise IOError("Unexpected end of file reading TAG:%d record data (%d < %d) %s" % (tag, len(data), size, repr(data)))
  else:
    data = ""
  return Record(tag, size, data)

class Record(object):
  "Holder for tag, size and data members."
  def __init__(self, tag, size, data):
    self.tag = tag
    self.size = size
    self.data = data

  def __str__(self):
    return "TAG:%d SIZE:%d DATA:%s" % (self.tag, self.size, repr(self.data))

class objdict(dict):
  def __getattr__(self, name):
    if name in self:
      return self[name]
    else:
      raise AttributeError("No such attribute: " + name)

  def __setattr__(self, name, value):
    self[name] = value

  def __delattr__(self, name):
    if name in self:
        del self[name]
    else:
        raise AttributeError("No such attribute: " + name)

def readString(fs, terminator=STRING_TERMINATOR):
  buffer = StringIO()
  while True:
    c = fs.read(len(terminator))
    if c == terminator or len(c) == 0:
      break
    buffer.write(c)
  return buffer.getvalue()

def parseFileHeader(data):
  res = objdict()
  s = Struct("<3sIII")
  (res.fileType, res.fileSize, res.webLink, res.refinementFlags) = s.unpack(data[:s.size])
  buf = StringIO(data[s.size:])
  res.producer = readString(buf, ASCII_STRING_TERMINATOR)
  res.producerVersion = readString(buf, ASCII_STRING_TERMINATOR)
  res.producerBuild = readString(buf, ASCII_STRING_TERMINATOR)
  return res

def parseEndCompression(data):
  res = objdict()
  s = Struct("<II")
  (res.compressionCRC, res.numBytes) = s.unpack(data)
  return res
