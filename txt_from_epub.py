
"""
import sys
import os
import warnings
from bs4 import BeautifulSoup
import ebooklib
from ebooklib import epub
warnings.filterwarnings("ignore", category=UserWarning)
def extract_text_from_epub(epub_path):
    book = epub.read_epub(epub_path)
    chapters_text = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), "html.parser")
            text = soup.get_text(separator=" ", strip=True)
            if text:
                chapters_text.append(text)
    return "\n\n".join(chapters_text)
if __name__ == "__main__":


    epub_file = "fed.epub"


    output_file = os.path.splitext(epub_file)[0] + ".txt"
    try:
        full_text = extract_text_from_epub(epub_file)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_text)
        print(f"Successfully saved to: {output_file}")
    except FileNotFoundError:
        print(f"Error: The file '{epub_file}' was not found.")


"""

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def epub_to_txt(epub_path, txt_path):
    # Read the EPUB file
    book = epub.read_epub(epub_path)
    chapters = []

    # Loop through all items in the EPUB
    for item in book.get_items():
        # Filter for document items (chapters/HTML content)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Parse the HTML content and extract plain text
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text = soup.get_text(separator='\n', strip=True)
            
            if text:
                chapters.append(text)

    # Join all chapters and write to a UTF-8 text file
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(chapters))

    print(f"Successfully converted '{epub_path}' to '{txt_path}'")

# Example usage
epub_to_txt("fed.epub", "fed.txt")
