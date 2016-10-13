# xarapy
Parser for CorelXara files written in Python.
Should help to convert XAR files to another vector drawing format, e.g. SVG.

## Version 0.1
I am actually starting the implementation. Implemented functions:

* Parsing file ID and records.
* Support for TAG_STARTCOMPRESSION and TAG_ENDCOMPRESSION.
* Extraction of preview image.

**Example:** Preview extract

    $ ./main.py data/angelfish.xar -p preview
    Opening 'data/angelfish.xar'
    ID valid
    {'producer': 'CorelXARA', 'refinementFlags': 0, 'fileType': 'CXN', 'producerVersion': '1.5', 'webLink': 0, 'fileSize': 20159, 'producerBuild': '0.1028'}
    Saving preview to 'preview.gif'

**Example:** List file structure (verbose mode)

    $ ./main.py data/angelfish.xar -v
    Opening 'data/angelfish.xar'
    ID valid
    TAG_FILEHEADER TAG:2 SIZE:36 DATA:'CXN\xbfN\ ... '
    TAG_DOCUMENT TAG:40 SIZE:0 DATA:''
    TAG_DOWN TAG:1 SIZE:0 DATA:''
      TAG_STARTCOMPRESSION TAG:30 SIZE:4 DATA:'c\x00\x00\x00'
      TAG_VIEWPORT TAG:80 SIZE:16 DATA:'\xa0\xd0\x00\x00\x04h\x05\x00\xf98\x08\x00\xaf\xfa\x0b\x00'
      TAG_CHAPTER TAG:41 SIZE:0 DATA:''
      TAG_DOWN TAG:1 SIZE:0 DATA:''
        TAG_SPREAD TAG:42 SIZE:0 DATA:''
        TAG_DOWN TAG:1 SIZE:0 DATA:''
          TAG_SPREADINFORMATION TAG:45 SIZE:17 DATA:'M\x15\t\x00\xa3\xd8\x0c\x00\x01\xca\x08\x00\x00\x00\x00\x00\x02'
          TAG_SPREADSCALING_INACTIVE TAG:53 SIZE:24 DATA:'\x00\x00\x00\x00\x00\x00\xf0?\xfd\xff\xff\xff\x00\x00\x00\x00\x00\x00\xf0?\xf4\xff\xff\xff'
          TAG_LAYER TAG:43 SIZE:0 DATA:''
          TAG_DOWN TAG:1 SIZE:0 DATA:''
            TAG_LAYERDETAILS TAG:48 SIZE:17 DATA:'\rL\x00a\x00y\x00e\x00r\x00 \x001\x00\x00\x00'
            TAG_PATH_RELATIVE_FILLED_STROKED TAG:116 SIZE:36 DATA:'\x06\x00\x00\x02\x06J\xd0\x96T\x02\xff\xff\xff\xff\xff\xcd\xb3\x96\x02\x00\x00\x00\x00\x892@\xc1\x03\xff\xff\xff\xffw\xff\r\xa9'
            TAG_DOWN TAG:1 SIZE:0 DATA:''
              TAG_PATH_FLAGS TAG:111 SIZE:4 DATA:'\x04\x04\x04\x04'
              TAG_LINEWIDTH TAG:152 SIZE:4 DATA:'\xe8\x03\x00\x00'
              TAG_DEFINECOMPLEXCOLOUR TAG:51 SIZE:41 DATA:'\xff\xff\xff\x05\x00"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00W\x00h\x00i\x00t\x00e\x00\x00\x00'
              TAG_FLATFILL TAG:150 SIZE:4 DATA:'\x14\x00\x00\x00'
              TAG_DEFINECOMPLEXCOLOUR TAG:51 SIZE:31 DATA:'\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00'
              TAG_LINECOLOUR TAG:151 SIZE:4 DATA:'\x16\x00\x00\x00'
              TAG_UP TAG:0 SIZE:0 DATA:''
            TAG_TEXT_STORY_SIMPLE TAG:2100 SIZE:8 DATA:'u\xdd\x00\x00\xac\xad\x0b\x00'
            ...

      TAG_DOCUMENTVIEW TAG:82 SIZE:24 DATA:'\xb9\xfc\x00\x00\x60\xf7\xfe\xff."\x05\x00H\x1e\n\x00n7\x0c\x00\x01\x0c\x01\x00'
      TAG_ENDCOMPRESSION TAG:31 SIZE:8 DATA:'\x93\xb3\xde{\xc3?\x00\x00'
      TAG_UP TAG:0 SIZE:0 DATA:''
    TAG_ENDOFFILE TAG:3 SIZE:0 DATA:''
