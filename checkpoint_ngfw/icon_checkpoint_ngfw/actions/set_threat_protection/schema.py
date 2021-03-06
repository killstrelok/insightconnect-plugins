# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Set threat protection action per profile"


class Input:
    ACTION = "action"
    NAME = "name"
    PROFILE = "profile"
    

class Output:
    SUCCESS = "success"
    

class SetThreatProtectionInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action": {
      "type": "string",
      "title": "Action",
      "description": "Action",
      "enum": [
        "Inactive",
        "Detect",
        "Prevent",
        "Drop",
        "Accept"
      ],
      "order": 2
    },
    "name": {
      "type": "string",
      "title": "Name",
      "description": "Name of the protection to act on",
      "order": 1
    },
    "profile": {
      "type": "string",
      "title": "Profile",
      "description": "Profile e.g. Optimized, Basic, Strict",
      "default": "Optimized",
      "order": 3
    }
  },
  "required": [
    "action",
    "name",
    "profile"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SetThreatProtectionOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Was operation successful",
      "order": 1
    }
  },
  "required": [
    "success"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
