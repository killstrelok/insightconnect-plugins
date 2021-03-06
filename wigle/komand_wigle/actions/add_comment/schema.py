# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Add a comment to the network"


class Input:
    COMMENT = "comment"
    NETID = "netid"
    

class Output:
    COMMENT = "comment"
    NETID = "netid"
    

class AddCommentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "The comment to attach",
      "order": 2
    },
    "netid": {
      "type": "string",
      "title": "Network ID",
      "description": "The BSSID of the network for the comment, e.g. '0A:2C:EF:3D:25:1B'",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddCommentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment",
      "order": 2
    },
    "netid": {
      "type": "string",
      "title": "Network ID",
      "description": "Network ID",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
