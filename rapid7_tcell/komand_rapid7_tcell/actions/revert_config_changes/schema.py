# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Revert configuration from previous iteration"


class Input:
    APP_ID = "app_id"
    ID = "id"
    

class Output:
    SUCCESS = "success"
    

class RevertConfigChangesInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "app_id": {
      "type": "string",
      "title": "App ID",
      "description": "App ID",
      "order": 1
    },
    "id": {
      "type": "integer",
      "title": "ID",
      "description": "The ID of the configuration to use",
      "order": 2
    }
  },
  "required": [
    "app_id",
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class RevertConfigChangesOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "success": {
      "type": "boolean",
      "title": "Success",
      "description": "Revert configuration successful",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
