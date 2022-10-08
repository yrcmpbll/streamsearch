import sys
import streamlit as st
from elasticsearch import Elasticsearch
sys.path.append('srcs')
from streamlit_app import utils, templates

INDEX = 'medium_data'
PAGE_SIZE = 5
DOMAIN = '0.0.0.0'
es = Elasticsearch(host=DOMAIN)
utils.check_and_create_index(es, INDEX)

def main():
    st.write(templates.load_css(), unsafe_allow_html=True)
    st.title('Search Medium Story')
    search = st.text_input('Enter search words:')
    if search:
        results = utils.index_search(es, INDEX, search, None, 0, PAGE_SIZE)
        total_hits = results['aggregations']['match_count']['value']
        # show number of results and time taken
        st.write(templates.number_of_results(total_hits, results['took'] / 1000),
                 unsafe_allow_html=True)
        # render popular tags as filters
        st.write(templates.tag_boxes(search, results['sorted_tags'][:10], ''),
                 unsafe_allow_html=True)
        # search results
        for i in range(len(results['hits']['hits'])):
            result = results['hits']['hits'][i]
            res = result['_source']
            res['url'] = result['_id']
            res['highlights'] = '...'.join(result['highlight']['content'])
            st.write(templates.search_result(i, **res), unsafe_allow_html=True)
            st.write(templates.tag_boxes(search, res['tags'], ''),
                     unsafe_allow_html=True)

if __name__ == '__main__':
    main()