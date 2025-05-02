from bs4 import BeautifulSoup
import os

def extract_text_from_html(book_dir):
    texts = []
    for root, _, files in os.walk(book_dir):
        for file in files:
            if file.endswith(".html"):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, "html.parser")
                    main = soup.find("main") or soup.body
                    text = main.get_text(separator="\n", strip=True)
                    texts.append(text)
    return texts

# Example usage:
jupyter_book_texts = extract_text_from_html("_build/html")