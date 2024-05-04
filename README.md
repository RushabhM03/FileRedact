# FileRedact
### An optimized NLP powered file redaction system


This is an nlp-powered streamlit app that takes the contents of the file as input and based on the selection redacts the keywords from the document.

## 🎱 Problem statement
Nowadays, file confidentiality is an issue. The task is to use NLP methods to help in file content redaction which will help organizations protect their data, which in turn may lead to better security
<br><br>


## 🚀 Features
- File redaction with no word reversal
- Categories: Names, Places, Date time, Organization names
- Option to save the file with download option
- A downloads folder that stores your history of redacted files
<br><br>

## 💻 Techstack
- Python
- HTML
- Streamlit
- Spacy
<br><br>

## 🉐 Streamlit and NLP pipeline
Streamlit
> Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc. With Streamlit, no callbacks are needed since widgets are treated as variables. Data caching simplifies and speeds up computation pipelines. Streamlit watches for changes on updates of the linked Git repository and the application will be deployed automatically in the shared link.

Docs: <br>
https://cheat-sheet.streamlit.app/ <br>
https://streamlit.io/ <br>

NLP pipeline
> The NLP Entity Redaction Pipeline is a versatile tool designed to automatically identify and redact specific types of entities within a given text using natural language processing (NLP) techniques. The primary purpose of this pipeline is to enhance privacy and data protection by obscuring sensitive information while preserving the overall structure and context of the original text.

> The pipeline is built upon the spaCy library, a widely-used NLP toolkit that offers state-of-the-art features for linguistic analysis, including named entity recognition (NER). By leveraging spaCy's capabilities, the pipeline can efficiently detect entities such as personal names, geographical locations, organizations, and dates within the input text.

Key Features of the NLP Entity Redaction Pipeline:

- Entity Identification: The pipeline employs spaCy's NER model to locate instances of specific entity types within the input text. It can accurately detect entities like personal names (e.g., "John Smith"), places (e.g., "New York"), organizations (e.g., "ABC Corp"), and dates (e.g., "September 15, 2023").

- Redaction: Once the pipeline identifies the target entities, it redacts them by replacing the entity's text with a standardized placeholder, such as "[REDACTED NAME]" for personal names or "[REDACTED PLACE]" for locations. This process helps protect sensitive information from being disclosed while maintaining the overall text structure.

- Customization: The pipeline is designed to be flexible and customizable. It provides separate functions for redacting each entity type, allowing users to selectively redact specific types of entities based on their needs. Users can also extend the pipeline to include additional entity categories if required.

- Ease of Integration: The pipeline can be easily integrated into various applications, scripts, or data processing pipelines. It follows a straightforward approach that involves loading the spaCy language model, invoking the redaction functions, and obtaining the redacted text.



<br><br>

## 🎯 Project setup

Clone the project

```
git clone https://github.com/RushabhM03/FileRedact.git
```

Setup the Virtual environment
(Run the commands in the base folder)
```
virtualenv venv
cd venv/Scripts
& "Activate.psl"
cd.. cd ..
```

Install the packages required
```
pip install requirements.txt
```

UI setup
```
streamlit run streamlit_app.py
```


<br><br>

## ⚓ Host
https://fileredact.streamlit.app/

<br><br>

## 👩 Contributors
Team members

- [**R**ushabh Maru](https://github.com/RushabhM03) - rushabh.maru123@gmail.com
