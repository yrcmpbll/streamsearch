# curl -H "Content-Type: application/x-ndjson" -XPOST "http://localhost:9200/indexname/typename/_bulk?pretty" --data-binary @data/parsed_data.json
# curl -H 'Content-Type: application/x-ndjson' -XPOST http://localhost:9200/indexname/typename/ --data-binary @data/parsed_data.json
# curl -H 'Content-Type: application/json' -XPOST http://localhost:9200/indexname/typename/ --data-binary @data/parsed_data.json
# curl -H 'Content-Type: application/json' -XPOST http://localhost:9200/indexname/typename/ -d @data/parsed_data.json
curl -H 'Content-Type: application/json' -XPOST 'http://localhost:9200/indexname/_doc/_bulk?pretty' --data-binary @data/parsed_data.json