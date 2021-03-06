# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Search for data related to URLs"


class Input:
    DIRECTION = "direction"
    FROM = "from"
    LIMIT = "limit"
    ORDERBY = "orderby"
    RISKRULE = "riskRule"
    RISKSCORE = "riskScore"
    

class Output:
    DATA = "data"
    

class SearchUrlsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "direction": {
      "type": "string",
      "title": "Result Direction",
      "description": "Sort results ascending/descending",
      "enum": [
        "asc",
        "desc"
      ],
      "order": 4
    },
    "from": {
      "type": "number",
      "title": "Offset",
      "description": "Number of initial records to skip",
      "order": 2
    },
    "limit": {
      "type": "number",
      "title": "Limit",
      "description": "Number of results to retrieve, up to 100",
      "default": 10,
      "order": 1
    },
    "orderby": {
      "type": "string",
      "title": "Order By",
      "description": "Which property to sort the results by",
      "enum": [
        "Created",
        "Criticality",
        "Lastseen",
        "Firstseen",
        "Modified",
        "Riskscore",
        "Rules",
        "Sevendayshits",
        "Sixtydayshits",
        "Totalhits"
      ],
      "order": 3
    },
    "riskRule": {
      "type": "string",
      "title": "Risk Rule",
      "description": "Risk rule od data",
      "enum": [
        "Historically Reported by Insikt Group",
        "C\\u0026C URL",
        "Compromised URL",
        "Historically Reported as a Defanged URL",
        "Historically Reported by DHS AIS",
        "Historically Reported Fraudulent Content",
        "Historically Reported in Threat List",
        "Historically Detected Malicious Browser Exploits",
        "Historically Detected Malware Distribution",
        "Historically Detected Cryptocurrency Mining Techniques",
        "Historically Detected Phishing Techniques",
        "Active Phishing URL",
        "Positive Malware Verdict",
        "Ransomware Distribution URL",
        "Recently Reported by Insikt Group",
        "Recently Reported as a Defanged URL",
        "Recently Reported by DHS AIS",
        "Recently Reported Fraudulent Content",
        "Recently Detected Malicious Browser Exploits",
        "Recently Detected Malware Distribution",
        "Recently Detected Cryptocurrency Mining Techniques",
        "Recently Detected Phishing Techniques",
        "Recently Referenced by Insikt Group",
        "Recently Reported Spam or Unwanted Content",
        "Recently Detected Suspicious Content",
        "Recently Active URL on Weaponized Domain",
        "Historically Referenced by Insikt Group",
        "Historically Reported Spam or Unwanted Content",
        "Historically Detected Suspicious Content"
      ],
      "order": 6
    },
    "riskScore": {
      "type": "string",
      "title": "Risk Score",
      "description": "Risk score of data",
      "order": 5
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchUrlsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "$ref": "#/definitions/search_data",
      "title": "Data",
      "description": "Search result",
      "order": 1
    }
  },
  "required": [
    "data"
  ],
  "definitions": {
    "counts": {
      "type": "object",
      "title": "counts",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "order": 1
        },
        "date": {
          "type": "string",
          "title": "Date",
          "order": 2
        }
      }
    },
    "entities": {
      "type": "object",
      "title": "entities",
      "properties": {
        "count": {
          "type": "integer",
          "title": "Count",
          "order": 1
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "order": 2
        }
      },
      "definitions": {
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "entity": {
      "type": "object",
      "title": "entity",
      "properties": {
        "description": {
          "type": "string",
          "title": "Description",
          "order": 4
        },
        "id": {
          "type": "string",
          "title": "Id",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Name",
          "order": 2
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 3
        }
      }
    },
    "evidenceDetails": {
      "type": "object",
      "title": "evidenceDetails",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "order": 2
        },
        "evidenceString": {
          "type": "string",
          "title": "Evidence String",
          "order": 3
        },
        "rule": {
          "type": "string",
          "title": "Rule",
          "order": 4
        },
        "timestamp": {
          "type": "string",
          "title": "Timestamp",
          "order": 5
        }
      }
    },
    "metrics": {
      "type": "object",
      "title": "metrics",
      "properties": {
        "type": {
          "type": "string",
          "title": "Type",
          "order": 1
        },
        "value": {
          "type": "number",
          "title": "Value",
          "order": 2
        }
      }
    },
    "relatedEntities": {
      "type": "object",
      "title": "relatedEntities",
      "properties": {
        "entities": {
          "type": "array",
          "title": "Entities",
          "items": {
            "$ref": "#/definitions/entities"
          },
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 2
        }
      },
      "definitions": {
        "entities": {
          "type": "object",
          "title": "entities",
          "properties": {
            "count": {
              "type": "integer",
              "title": "Count",
              "order": 1
            },
            "entity": {
              "$ref": "#/definitions/entity",
              "title": "Entity",
              "order": 2
            }
          },
          "definitions": {
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        }
      }
    },
    "risk": {
      "type": "object",
      "title": "risk",
      "properties": {
        "criticality": {
          "type": "number",
          "title": "Criticality",
          "order": 1
        },
        "criticalityLabel": {
          "type": "string",
          "title": "Criticality Label",
          "order": 2
        },
        "evidenceDetails": {
          "type": "array",
          "title": "Evidence Details",
          "items": {
            "$ref": "#/definitions/evidenceDetails"
          },
          "order": 3
        },
        "riskSummary": {
          "type": "string",
          "title": "Risk Summary",
          "order": 4
        },
        "rules": {
          "type": "integer",
          "title": "Rules",
          "order": 5
        },
        "score": {
          "type": "integer",
          "title": "Score",
          "order": 6
        }
      },
      "definitions": {
        "evidenceDetails": {
          "type": "object",
          "title": "evidenceDetails",
          "properties": {
            "criticality": {
              "type": "number",
              "title": "Criticality",
              "order": 1
            },
            "criticalityLabel": {
              "type": "string",
              "title": "Criticality Label",
              "order": 2
            },
            "evidenceString": {
              "type": "string",
              "title": "Evidence String",
              "order": 3
            },
            "rule": {
              "type": "string",
              "title": "Rule",
              "order": 4
            },
            "timestamp": {
              "type": "string",
              "title": "Timestamp",
              "order": 5
            }
          }
        }
      }
    },
    "search_data": {
      "type": "object",
      "title": "search_data",
      "properties": {
        "counts": {
          "type": "array",
          "title": "Counts",
          "items": {
            "$ref": "#/definitions/counts"
          },
          "order": 1
        },
        "entity": {
          "$ref": "#/definitions/entity",
          "title": "Entity",
          "order": 2
        },
        "hashAlgorithm": {
          "type": "string",
          "title": "Hash Algorithm",
          "order": 3
        },
        "intelCard": {
          "type": "string",
          "title": "Intel Card",
          "order": 4
        },
        "metrics": {
          "type": "array",
          "title": "Metrics",
          "items": {
            "$ref": "#/definitions/metrics"
          },
          "order": 5
        },
        "relatedEntities": {
          "type": "array",
          "title": "Related Entities",
          "items": {
            "$ref": "#/definitions/relatedEntities"
          },
          "order": 6
        },
        "risk": {
          "$ref": "#/definitions/risk",
          "title": "Risk",
          "order": 7
        },
        "sightings": {
          "type": "array",
          "title": "Sightings",
          "items": {
            "$ref": "#/definitions/sightings"
          },
          "order": 8
        },
        "threatLists": {
          "type": "array",
          "title": "Threat Lists",
          "items": {
            "type": "object"
          },
          "order": 9
        },
        "timestamps": {
          "$ref": "#/definitions/timestamps",
          "title": "Timestamps",
          "order": 10
        }
      },
      "definitions": {
        "counts": {
          "type": "object",
          "title": "counts",
          "properties": {
            "count": {
              "type": "integer",
              "title": "Count",
              "order": 1
            },
            "date": {
              "type": "string",
              "title": "Date",
              "order": 2
            }
          }
        },
        "entities": {
          "type": "object",
          "title": "entities",
          "properties": {
            "count": {
              "type": "integer",
              "title": "Count",
              "order": 1
            },
            "entity": {
              "$ref": "#/definitions/entity",
              "title": "Entity",
              "order": 2
            }
          },
          "definitions": {
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "entity": {
          "type": "object",
          "title": "entity",
          "properties": {
            "description": {
              "type": "string",
              "title": "Description",
              "order": 4
            },
            "id": {
              "type": "string",
              "title": "Id",
              "order": 1
            },
            "name": {
              "type": "string",
              "title": "Name",
              "order": 2
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 3
            }
          }
        },
        "evidenceDetails": {
          "type": "object",
          "title": "evidenceDetails",
          "properties": {
            "criticality": {
              "type": "number",
              "title": "Criticality",
              "order": 1
            },
            "criticalityLabel": {
              "type": "string",
              "title": "Criticality Label",
              "order": 2
            },
            "evidenceString": {
              "type": "string",
              "title": "Evidence String",
              "order": 3
            },
            "rule": {
              "type": "string",
              "title": "Rule",
              "order": 4
            },
            "timestamp": {
              "type": "string",
              "title": "Timestamp",
              "order": 5
            }
          }
        },
        "metrics": {
          "type": "object",
          "title": "metrics",
          "properties": {
            "type": {
              "type": "string",
              "title": "Type",
              "order": 1
            },
            "value": {
              "type": "number",
              "title": "Value",
              "order": 2
            }
          }
        },
        "relatedEntities": {
          "type": "object",
          "title": "relatedEntities",
          "properties": {
            "entities": {
              "type": "array",
              "title": "Entities",
              "items": {
                "$ref": "#/definitions/entities"
              },
              "order": 1
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 2
            }
          },
          "definitions": {
            "entities": {
              "type": "object",
              "title": "entities",
              "properties": {
                "count": {
                  "type": "integer",
                  "title": "Count",
                  "order": 1
                },
                "entity": {
                  "$ref": "#/definitions/entity",
                  "title": "Entity",
                  "order": 2
                }
              },
              "definitions": {
                "entity": {
                  "type": "object",
                  "title": "entity",
                  "properties": {
                    "description": {
                      "type": "string",
                      "title": "Description",
                      "order": 4
                    },
                    "id": {
                      "type": "string",
                      "title": "Id",
                      "order": 1
                    },
                    "name": {
                      "type": "string",
                      "title": "Name",
                      "order": 2
                    },
                    "type": {
                      "type": "string",
                      "title": "Type",
                      "order": 3
                    }
                  }
                }
              }
            },
            "entity": {
              "type": "object",
              "title": "entity",
              "properties": {
                "description": {
                  "type": "string",
                  "title": "Description",
                  "order": 4
                },
                "id": {
                  "type": "string",
                  "title": "Id",
                  "order": 1
                },
                "name": {
                  "type": "string",
                  "title": "Name",
                  "order": 2
                },
                "type": {
                  "type": "string",
                  "title": "Type",
                  "order": 3
                }
              }
            }
          }
        },
        "risk": {
          "type": "object",
          "title": "risk",
          "properties": {
            "criticality": {
              "type": "number",
              "title": "Criticality",
              "order": 1
            },
            "criticalityLabel": {
              "type": "string",
              "title": "Criticality Label",
              "order": 2
            },
            "evidenceDetails": {
              "type": "array",
              "title": "Evidence Details",
              "items": {
                "$ref": "#/definitions/evidenceDetails"
              },
              "order": 3
            },
            "riskSummary": {
              "type": "string",
              "title": "Risk Summary",
              "order": 4
            },
            "rules": {
              "type": "integer",
              "title": "Rules",
              "order": 5
            },
            "score": {
              "type": "integer",
              "title": "Score",
              "order": 6
            }
          },
          "definitions": {
            "evidenceDetails": {
              "type": "object",
              "title": "evidenceDetails",
              "properties": {
                "criticality": {
                  "type": "number",
                  "title": "Criticality",
                  "order": 1
                },
                "criticalityLabel": {
                  "type": "string",
                  "title": "Criticality Label",
                  "order": 2
                },
                "evidenceString": {
                  "type": "string",
                  "title": "Evidence String",
                  "order": 3
                },
                "rule": {
                  "type": "string",
                  "title": "Rule",
                  "order": 4
                },
                "timestamp": {
                  "type": "string",
                  "title": "Timestamp",
                  "order": 5
                }
              }
            }
          }
        },
        "sightings": {
          "type": "object",
          "title": "sightings",
          "properties": {
            "fragment": {
              "type": "string",
              "title": "Fragment",
              "order": 1
            },
            "published": {
              "type": "string",
              "title": "Published",
              "order": 2
            },
            "source": {
              "type": "string",
              "title": "Source",
              "order": 3
            },
            "title": {
              "type": "string",
              "title": "Title",
              "order": 4
            },
            "type": {
              "type": "string",
              "title": "Type",
              "order": 5
            },
            "url": {
              "type": "string",
              "title": "Url",
              "order": 6
            }
          }
        },
        "timestamps": {
          "type": "object",
          "title": "timestamps",
          "properties": {
            "firstSeen": {
              "type": "string",
              "title": "First Seen",
              "order": 1
            },
            "lastSeen": {
              "type": "string",
              "title": "Last Seen",
              "order": 2
            }
          }
        }
      }
    },
    "sightings": {
      "type": "object",
      "title": "sightings",
      "properties": {
        "fragment": {
          "type": "string",
          "title": "Fragment",
          "order": 1
        },
        "published": {
          "type": "string",
          "title": "Published",
          "order": 2
        },
        "source": {
          "type": "string",
          "title": "Source",
          "order": 3
        },
        "title": {
          "type": "string",
          "title": "Title",
          "order": 4
        },
        "type": {
          "type": "string",
          "title": "Type",
          "order": 5
        },
        "url": {
          "type": "string",
          "title": "Url",
          "order": 6
        }
      }
    },
    "timestamps": {
      "type": "object",
      "title": "timestamps",
      "properties": {
        "firstSeen": {
          "type": "string",
          "title": "First Seen",
          "order": 1
        },
        "lastSeen": {
          "type": "string",
          "title": "Last Seen",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
