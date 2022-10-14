curl -XPUT "http://localhost:9200/indexname" -H 'Content-Type: application/json' -d'{ 
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