import os
import re
from pathlib import Path
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import numpy as np
from langchain.schema import Document
import csv
MODEL = "intfloat/e5-base"


def extract_text_from_markdown(book_dir):
    texts = []
    skip_files = {"README.md", "index.md", "toc.md"}  # add filenames you want to skip

    for root, _, files in os.walk(book_dir):
        for file in files:
            if file.endswith(".md") and file not in skip_files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = [line.strip() for line in f.readlines()]
                    # Remove empty lines and join
                    clean_text = "\n".join(line for line in lines if line)
                    clean_text = re.sub(r"<[^>]+>", "", clean_text)  # strip HTML tags
                    clean_text = re.sub(r"```.*?```", "", clean_text, flags=re.DOTALL)
                    texts.append(clean_text)

    return texts


# Split the markdown (.md) text into chunks.
# Split in paragraphs using headers
def split_markdown_by_headers(texts, headers_to_split_on=None):
    """Split markdown texts into chunks based on header levels."""
    if headers_to_split_on is None:
        headers_to_split_on = [("#", "Header 1"), ("##", "Header 2")]

    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    chunks = []
    for text in texts:
        chunks.extend(splitter.split_text(text))

    # Filter out unwanted chunks (example given in original code)
    chunks = [
        chunk for chunk in chunks if chunk.page_content.strip() != "---\nbibliography: references.bib\n---"
    ]
    return chunks


def combine_headers(doc):
    """Combine all headers in metadata and prepend to page_content with 'passage:' prefix."""
    headers = " | ".join(doc.metadata.values())
    content = f"{headers}\n\n{doc.page_content}"
    return Document(page_content=f"passage: {content}", metadata=doc.metadata)


def build_and_save_vectorstore(chunks, embedding_model, save_path="vectorstore_jupyterbook"):
    """Create a FAISS vectorstore from documents and save it locally."""
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(save_path)
    return vectorstore


# Step 1: Extract markdown texts
markdown_dir = Path(__file__).parent.parent / "contents"
texts = extract_text_from_markdown(str(markdown_dir.as_posix()))

# Step 2: Split texts into header-based chunks
header_chunks = split_markdown_by_headers(texts)

# Step 3: Prefix chunks with headers and 'passage:'
formatted_chunks = [combine_headers(doc) for doc in header_chunks]

# Step 4: Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name=MODEL, encode_kwargs={"normalize_embeddings": True})

# Step 5: Build and save vectorstore
build_and_save_vectorstore(formatted_chunks, embedding_model)



## Printo to output.csv
# with open('output.csv', mode='w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['text'])  # header
#
#     for chunk in header_chunks:
#         # Split content by lines (or you can split by paragraphs or sentences)
#         lines = chunk.page_content.split('\n')
#         writer.writerow([lines])

# Add headers to chunks
# formatted_chunks = []

# for chunk in header_chunks:
#     # Reconstruct header path from metadata
#     headers_1 = []
#     headers_2 = []
#     if 'Header 1' in chunk.metadata:
#         headers_1.append(chunk.metadata['Header 1'])
#     if 'Header 2' in chunk.metadata:
#         headers_2.append(chunk.metadata['Header 2'])
#
#     # Combine headers and content
#     header_str = " ".join(headers_1)
#     header_str_weighted = " ".join(headers_2 * 3)  # Repeat headers 3 times for extra relevance
#     full_content = f"{header_str}\n{header_str_weighted}\n{chunk.page_content}"
#
#     # Recreate the chunk with updated content
#     chunk.page_content = full_content
#     formatted_chunks.append(chunk)


# for i, chunk in enumerate(formatted_chunks):
#
#     print(chunk.metadata)
#     print(f"--- Chunk {i+1} ---")
#     print(chunk.page_content)
#     print()  # extra newline between chunks

