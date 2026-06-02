from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
import os


def load_documents():

    docs = []

    pdf_path = "knowledge/resume.pdf"

    loader = PyPDFLoader(pdf_path)

    docs.extend(loader.load())

    for file in os.listdir("knowledge"):

        if file.endswith(".md"):

            with open(
                f"knowledge/{file}",
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

            docs.append(
                Document(page_content=text)
            )

    return docs