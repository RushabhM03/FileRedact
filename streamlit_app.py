# core packages
import streamlit as st
import os
import graphviz
# utils
from utils.nlp_utils import *
from utils.file_utils import *

def main():
    st.set_page_config(layout="wide")

    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">', unsafe_allow_html=True)
    st.title("Document Safety tool")
    st.text("Built with streamlit and SpaCy")

    activities = ["Redaction", "Downloads", "Redaction NLP Pipeline", "About"]

    choice = st.sidebar.selectbox("Select task", activities)

    if choice == "Redaction":
        st.subheader("Redaction of terms")
        raw_text = st.text_area("Enter text", "Type here")
        og_text = raw_text
        redaction_item = ['names', 'places', 'org', 'dates']
        redaction_choice = st.multiselect("Select the terms to classify", redaction_item)
        save_option = st.radio("Save to file", ("Yes", "No"))
        #st.info(redaction_choice)
        if st.button("Submit"):
            result = ""
            if "names" in redaction_choice:
                result = sanitize_names(raw_text)
                raw_text = result
                
            if "places" in redaction_choice:
                result = sanitize_place(raw_text)
                raw_text = result

            if "dates" in redaction_choice:
                result = sanitize_date(raw_text)
                raw_text = result

            if "org" in redaction_choice:
                result = sanitize_org(raw_text)
                raw_text = result

            st.subheader("Original text")
            st.write(render_entities(og_text), unsafe_allow_html=True)

            st.subheader("Redacted text")
            st.write(result)
            
            if save_option == "Yes":
                filename = generate_name()
                file_to_download = write_to_file(result, filename)
                st.info("Saved result as :: {}".format(filename))
                d_link = make_downloadable(file_to_download)
                st.markdown(d_link, unsafe_allow_html=True)
            


    elif choice == "Downloads":
        st.subheader("Download List")
        files = os.listdir(os.path.join("downloads"))
        file_to_download = st.selectbox("Select a file", files)
        st.info("File name: {}".format(file_to_download))
        d_link = make_downloadable(file_to_download)
        st.markdown(d_link, unsafe_allow_html=True)
    
    elif choice == "About":
        st.subheader("About US")
        st.text("Rushabh Maru")
        st.text("rushabh.maru123@gmail.com")
        st.text("Github: RushabhM03")
        st.markdown(render_html(FOOTER), unsafe_allow_html=True)

    elif choice == 'Redaction NLP Pipeline':
        st.subheader("NLP redaction pipeline")
        graph = graphviz.Digraph()
        
        
        
        graph.edge('Check ent type', 'Redact')
        graph.edge( 'Retokenize merge', 'Check ent type',)
        graph.edge('Tokenize', 'Retokenize merge')
        graph.edge('Start', 'Tokenize')
        st.graphviz_chart(graph)

    


if __name__ == "__main__":
    main() 