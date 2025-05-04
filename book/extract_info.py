from bs4 import BeautifulSoup
import os

def extract_text_from_html(book_dir):
    texts = []
    skip_files = {"index.html", "sbt-webpack-macros.html", "search.html", "toc.html"}  # filenames to skip
    for root, _, files in os.walk(book_dir):
        for file in files:
            if file.endswith(".html"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, "html.parser")
                    article_div = soup.find("article", class_="bd-article")
                    try:
                        text = article_div.get_text(separator="\n", strip=True)
                        texts.append(text)
                        lines = [line.strip() for line in text.splitlines()]
                        clean_text = "\n".join(line for line in lines if line)
                    except AttributeError:
                        continue
    return texts


# Example usage:
jupyter_book_texts = extract_text_from_html("C:/Users/casper/OneDrive/Documenten/Persoonlijk/Notebookllm/Notebook/FloatingSubmergedStructures/book/_build/html")
print(jupyter_book_texts[1])