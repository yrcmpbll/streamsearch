import json


def parse_standard():
    # Opening JSON file
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    parsed_data = list()
    for _k in data.keys():
        record = dict()
        record['url'] = _k
        record.update(data[_k])
        parsed_data.append(record)
    
    with open("parsed_data.json", "w") as final:
        json.dump(parsed_data, final)


def parse_es():
    # Opening JSON file
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    data_objects = list()
    for _k in data.keys():
        record = dict()
        record['url'] = _k
        record.update(data[_k])
        record['content'] = ' '.join(data[_k]['content'])
        record['tags'] = ['_'.join(x.split('-')) for x in record['tags']]
        
        _record_data = json.dumps(record)
        data_objects += [_record_data]

    parsed_data = '\n{"index":{}}\n'.join(data_objects)
    parsed_data = '{"index":{}}\n' + parsed_data + '\n'
    
    with open("parsed_data.json", "w") as final:
        final.write(parsed_data)


if __name__ == '__main__':
    parse_es()


# {"index":{}}
# {"name": "bosch", "city": "berlin"}
# {"index":{}}
# {"name": "nextbike", "city": "leipzig"}
# {"index":{}}
# {"name": "profiroll", "city": "erfurt"}
