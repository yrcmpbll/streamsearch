FROM python:3.7-slim

RUN apt-get update && apt-get install -y \
curl

COPY ./data/parsed_data.json /parsed_data.json
COPY ./src/docker_seeder/set_mapping.sh /set_mapping.sh
COPY ./src/docker_seeder/import_data.sh /import_data.sh

CMD ["sh", "-c", "bash set_mapping.sh; bash import_data.sh"]

# CMD ["sh", "-c", "curl -H 'Content-Type: application/json' -XPUT $ES_URL_INDEX -d $ES_MAPPING; curl -H 'Content-Type: application/json' -XPOST $ES_URL_IMPORT --data-binary @parsed_data.json"]
# curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/indexname/typename/_bulk?pretty" --data-binary @parsed_data.json
# curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/indexname/typename/" -d @parsed_data.json
# curl -H "Content-Type: application/x-ndjson" -XPOST "http://localhost:9200/indexname/typename/_bulk?pretty" --data-binary @parsed_data.json
# CMD ["sh", "-c", "curl -H 'Content-Type: application/json' -XPOST $ES_URL -d @parsed_data.json"]