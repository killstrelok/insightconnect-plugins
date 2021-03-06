# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Gather the lists of domains already added to the shared customer's domain list"


class Input:
    pass

class Output:
    DATA = "data"
    META = "meta"
    

class DomainsInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DomainsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "array",
      "title": "Domain List Query Results",
      "description": "The data array contains the domains in the domain list, along with a unique ID number for each domain",
      "items": {
        "$ref": "#/definitions/data"
      },
      "order": 2
    },
    "meta": {
      "$ref": "#/definitions/meta",
      "title": "Meta",
      "description": "The meta array shows which page of results is available, the number of results and next and previous available pages to query",
      "order": 1
    }
  },
  "required": [
    "data",
    "meta"
  ],
  "definitions": {
    "data": {
      "type": "object",
      "title": "data",
      "properties": {
        "ID": {
          "type": "integer",
          "title": "ID",
          "description": "Unique ID number",
          "order": 1
        },
        "lastSeenAt": {
          "type": "string",
          "title": "Last seen malware",
          "description": "Unix timestamp last seen",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Domain name",
          "order": 2
        }
      },
      "required": [
        "ID",
        "lastSeenAt",
        "name"
      ]
    },
    "meta": {
      "type": "object",
      "title": "meta",
      "properties": {
        "limit": {
          "type": "integer",
          "title": "Limit",
          "description": "The number of results",
          "order": 2
        },
        "next": {
          "type": "string",
          "title": "Next",
          "description": "If next is false, this is the last available page of results. Otherwise, it will provide a query formatted to show the next set of results",
          "order": 4
        },
        "page": {
          "type": "integer",
          "title": "Page",
          "description": "The page of results is available",
          "order": 1
        },
        "prev": {
          "type": "string",
          "title": "Prev",
          "description": "If prev is false, this is the first available page of results. Otherwise, it will provide a query formatted to show the next set of results",
          "order": 3
        }
      },
      "required": [
        "limit",
        "next",
        "page",
        "prev"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
