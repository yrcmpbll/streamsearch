curl -XPUT $ES_URL_INDEX -H 'Content-Type: application/json' -d'{ 
                    "mappings": {
                        "properties": { 
                          "url":     { "type": "text"  },
                          "author":    { "type": "text" },
                          "length":      { "type": "text" },
                          "title":      { "type": "text" },
                          "content":      { "type": "text"},
                          "tags":      { "type": "text", "fielddata": true}  
                        }
                    }
                  }'