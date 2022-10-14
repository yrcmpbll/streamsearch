curl -XPUT "http://localhost:9200/indexname" -H 'Content-Type: application/json' -d'{
  "mappings": {
    "properties": {
      "tags": {
        "type": "text",
        "fielddata": true
      }
    }
  }
}'