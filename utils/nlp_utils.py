# NLP packages
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

import streamlit as st

# constants
from constants.HTML_constants import *

def sanitize_names(text):
    doc = nlp(text)
    redacted_sentences = []
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(ent)
    for token in doc:
        if token.ent_type_ == "PERSON":
            redacted_sentences.append("[REDACTED NAME] ")
        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences)

def sanitize_place(text):
    doc = nlp(text)
    redacted_sentences = []
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(ent)
    for token in doc:
        if token.ent_type_ == "GPE":
            redacted_sentences.append("[REDACTED PLACE] ")
        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences)


def sanitize_org(text):
    doc = nlp(text)
    redacted_sentences = []
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(ent)
    for token in doc:
        if token.ent_type_ == "ORG":
            redacted_sentences.append("[REDACTED ORGANIZATION] ")
        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences)


def sanitize_date(text):
    doc = nlp(text)
    redacted_sentences = []
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(ent)
    for token in doc:
        if token.ent_type_ == "DATE":
            redacted_sentences.append("[REDACTED DATE] ")
        else:
            redacted_sentences.append(token.text)
    return " ".join(redacted_sentences)

# display entities
@st.cache_data
def render_entities(raw_text):
    doc = nlp(raw_text)
    html = displacy.render(doc, style='ent')
    html = html.replace('\n\n', '\n')
    result = HTML_WRAPPER.format(html)
    return result

def render_html(wrapper):
    wrapper=wrapper.replace('\n\n', '\n')
    return wrapper