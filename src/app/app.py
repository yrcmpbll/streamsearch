import sys
import streamlit as st
from elasticsearch import Elasticsearch
sys.path.append('srcs')
from streamlit_app import utils

INDEX = 'medium_data'
DOMAIN = '0.0.0.0'
es = Elasticsearch(host=DOMAIN)
utils.check_and_create_index(es, INDEX)

def main():
    st.title('Search Medium Story')
    search = st.text_input('Enter search words:')
    if search:
        results = utils.index_search(es, INDEX, search, '', 0, PAGE_SIZE)

if __name__ == '__main__':
    main()