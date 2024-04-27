import streamlit as st 
import chromadb
from sentence_transformers import SentenceTransformer

collection_name = "Search_Engine"

chroma_client = chromadb.PersistentClient(path='Search_Engine')

# get or create the collection
collection = chroma_client.get_or_create_collection(
    name="Search_Engine",
    embedding_function=collection_name,
    metadata={"hnsw:space": "cosine"},
)
st.set_page_config(page_title="SubHunt", page_icon="🎬", layout="wide")
#st.title("🎬Welcome to SubHunt 🍿")
st.markdown(
    f"""
    <h1 style='color: red;'>🎬Welcome to SubHunt 🍿</h1>
    <h2 style='color: green;'>Find Your Favorite Subtitles Easily!</h2>
    """,
    unsafe_allow_html=True
)

query = st.text_input("Enter a dialogue/ movie name:", key="query")
search_button_clicked = st.button("Hunt")

if search_button_clicked:
    search_query_cleaned = cleaned_data(query)
    query_embedding = model.encode(search_query_cleaned).tolist()

    results = collection.query(query_embeddings=query_embedding, n_results=10)
    id_list = results['ids'][0]

    id_list_extracted = extract_id(id_list)

    with st.expander("Relevant Subtitle Files", expanded=True):
        for index, id in enumerate(id_list_extracted, start=1):
            file_name = collection.get(ids=f"{id}")["documents"][0]
            st.markdown(f"{index} - [{file_name}](https://www.opensubtitles.org/en/subtitles/{id})")




