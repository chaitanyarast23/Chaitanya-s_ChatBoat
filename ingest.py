from src.document_loader import load_documents
from src.chunking import split_documents
from src.vectorstore_builder import build_vectorstore

docs = load_documents()

chunks = split_documents(docs)

build_vectorstore(chunks)

print("Vector DB Created")