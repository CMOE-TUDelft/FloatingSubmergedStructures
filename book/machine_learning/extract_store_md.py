import os
from pathlib import Path
from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


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
                    texts.append(clean_text)

    return texts

# Example usage
markdown_dir = Path(__file__).parent.parent
markdown_texts = extract_text_from_markdown(str(markdown_dir.as_posix()))
#print(markdown_texts[0])  # Print extracted markdown file



# Split the markdown (.md) text into chunks.
# Split in paragraphs using headers

header_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "Header 1"), ("##", "Header 2")])
header_chunks = header_splitter.split_text(markdown_texts[0])
# print(header_chunks)

# Embed the chunks into tokens

model_name = "sentence-transformers/all-MiniLM-L6-v2"
embedding_model = HuggingFaceEmbeddings(model_name=model_name)

# Store in Vectore Store

vectorstore = FAISS.from_documents(header_chunks, embedding_model)
vectorstore.save_local("vectorstore_jupyterbook")

