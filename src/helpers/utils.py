import os
from tempfile import NamedTemporaryFile
from typing import Any
import streamlit as st
from langchain import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.schema import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.vectorstores.base import VectorStoreRetriever


def get_text():
    """Get text from user"""
    input_text = st.text_input("You: ")
    return input_text


def generate_response(query: str, chain_type: str, retriever: VectorStoreRetriever) -> dict[str, Any]:
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type=chain_type,
        retriever=retriever,
        return_source_documents=True
    )
    result = qa({'query': query})
    return result


def transform_document_into_chunks(document: list[Document]) -> list[Document]:
    """Transform document into chunks of {1000} tokens"""
    splitter = CharacterTextSplitter(
        chunk_size=int(os.environ.get('CHUNK_SIZE', 1000)),
        chunk_overlap=int(os.environ.get('CHUNK_OVERLAP', 0))
    )
    return splitter.split_documents(document)


def transform_chunks_into_embeddings(text: list[Document], k: int) -> VectorStoreRetriever:
    """Transform chunks into embeddings"""
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(text, embeddings)
    return db.as_retriever(search_type='similarity', search_kwargs={'k': k})


def get_file_path(file) -> str:
    """Obtain the file full path."""
    with NamedTemporaryFile(dir='/tmp/', suffix='.pdf', delete=False) as f:
        f.write(file.getbuffer())
        return f.name


def setup(file: str, number_of_relevant_chunk: int) -> VectorStoreRetriever:
    # load the document
    loader = PyPDFLoader(file)
    document = loader.load()
    # transform the document into chunks
    chunks = transform_document_into_chunks(document)
    # transform the chunks into embeddings
    return transform_chunks_into_embeddings(chunks, number_of_relevant_chunk)
