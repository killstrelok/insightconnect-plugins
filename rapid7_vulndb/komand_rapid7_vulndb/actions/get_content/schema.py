# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Fetch content record for  vulnerability or module"


class Input:
    IDENTIFIER = "identifier"
    

class Output:
    CONTENT_RESULT = "content_result"
    

class GetContentInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "identifier": {
      "type": "string",
      "title": "Identifier",
      "description": "Rapid7 vulnerability/module identifier",
      "order": 1
    }
  },
  "required": [
    "identifier"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetContentOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content_result": {
      "$ref": "#/definitions/content",
      "title": "Result",
      "description": "Content record for the vulnerability or module",
      "order": 1
    }
  },
  "required": [
    "content_result"
  ],
  "definitions": {
    "content": {
      "type": "object",
      "title": "content",
      "properties": {
        "alternate_ids": {
          "type": "string",
          "title": "Alternative Identifiers",
          "description": "List of alternative identifiers for the vulnerability",
          "order": 12
        },
        "architectures": {
          "type": "string",
          "title": "architectures",
          "description": "List of applicable architectures for the module",
          "order": 4
        },
        "authors": {
          "type": "string",
          "title": "Authors",
          "description": "List of module authors",
          "order": 7
        },
        "content_type": {
          "type": "string",
          "title": "Content type",
          "description": "Type of returned content for module or vulnerability",
          "order": 3
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Brief summary of the returned content",
          "order": 2
        },
        "published_at": {
          "type": "string",
          "title": "Published_at",
          "description": "Published date of vulnerability",
          "order": 5
        },
        "rank": {
          "type": "integer",
          "title": "Rank",
          "description": "Rank of module",
          "order": 8
        },
        "references": {
          "type": "string",
          "title": "References",
          "description": "List of references",
          "order": 6
        },
        "reliability": {
          "type": "string",
          "title": "Reliability",
          "description": "Reliability of module",
          "order": 9
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity of vulnerability",
          "order": 10
        },
        "solutions": {
          "type": "string",
          "title": "Solutions",
          "description": "List of possible solutions for the vulnerability",
          "order": 11
        },
        "title": {
          "type": "string",
          "title": "Title",
          "description": "Title of Vulnerability",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
