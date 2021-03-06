# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Set a key"


class Input:
    EXPIRE = "expire"
    KEY = "key"
    VALUE = "value"
    

class Output:
    REPLY = "reply"
    

class SetInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "expire": {
      "type": "integer",
      "title": "Expire",
      "description": "Expiration in seconds",
      "order": 3
    },
    "key": {
      "type": "string",
      "title": "Key",
      "description": "Key to set",
      "order": 1
    },
    "value": {
      "type": "string",
      "title": "Value",
      "description": "Value to set",
      "order": 2
    }
  },
  "required": [
    "key",
    "value"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SetOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "reply": {
      "type": "string",
      "title": "Reply",
      "description": "Reply (usually OK)",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
