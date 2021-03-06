# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve a binary by its MD5 Hash"


class Input:
    HASH = "hash"
    

class Output:
    BINARY = "binary"
    

class GetBinaryInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "hash": {
      "type": "string",
      "title": "Hash",
      "description": "An MD5 hash",
      "order": 1
    }
  },
  "required": [
    "hash"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetBinaryOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "binary": {
      "type": "string",
      "title": "Binary",
      "displayType": "bytes",
      "description": "A resulting binary, Base64-encoded",
      "format": "bytes",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
