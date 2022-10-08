# srcs/streamlit_app/app.py
import sys
import urllib.parse
import streamlit as st
from elasticsearch import Elasticsearch
sys.path.append('srcs')
from streamlit_app import utils, templates

INDEX = 'medium_data'
PAGE_SIZE = 5
DOMAIN = '0.0.0.0'
es = Elasticsearch(host=DOMAIN)
utils.check_and_create_index(es, INDEX)

def set_session_state():
    # set default values
    if 'search' not in st.session_state:
        st.session_state.search = None
    if 'tags' not in st.session_state:
        st.session_state.tags = None

    # get parameters in url
    para = st.experimental_get_query_params()
    if 'search' in para:
        st.experimental_set_query_params()
        # decode url
        new_search = urllib.parse.unquote(para['search'][0])
        st.session_state.search = new_search
    if 'tags' in para:
        st.experimental_set_query_params()
        st.session_state.tags = para['tags'][0]

def main():
    set_session_state()
    st.write(templates.load_css(), unsafe_allow_html=True)
    st.title('Search Medium Story')
    if st.session_state.search is None:
        search = st.text_input('Enter search words:')
    else:
        search = st.text_input('Enter search words:', st.session_state.search)
    if search:
        results = utils.index_search(es, INDEX, search, st.session_state.tags,
                                     0, PAGE_SIZE)
        total_hits = results['aggregations']['match_count']['value']
        # show number of results and time taken
        st.write(templates.number_of_results(total_hits, results['took'] / 1000),
                 unsafe_allow_html=True)
        # show popular tags
        popular_tags_html = templates.tag_boxes(search, results['sorted_tags'][:10],
                                                st.session_state.tags)
        st.write(popular_tags_html, unsafe_allow_html=True)
        # search results
        for i in range(len(results['hits']['hits'])):
            result = results['hits']['hits'][i]
            res = result['_source']
            res['url'] = result['_id']
            res['highlights'] = '...'.join(result['highlight']['content'])
            st.write(templates.search_result(i, **res), unsafe_allow_html=True)
            st.write(templates.tag_boxes(search, res['tags'], st.session_state.tags),
                     unsafe_allow_html=True)

if __name__ == '__main__':
    main()