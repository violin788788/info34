import os
import html
from ebooklib import epub
def create_epub_from_txt(txt_path, epub_path, cover_image_path, title, author, words_per_chapter):
    book = epub.EpubBook()
    book.set_identifier("txt_to_epub_conversion_123456")
    book.set_title(title)
    book.set_language("en")
    book.add_author(author)
    if os.path.exists(cover_image_path):
        with open(cover_image_path, "rb") as img_file:
            cover_data = img_file.read()
        book.set_cover(cover_image_path, cover_data)
    else:
        print(f"Warning: Cover image {cover_image_path} not found. Proceeding without cover.")
    if not os.path.exists(txt_path):
        print(f"Error: The file {txt_path} does not exist.")
        return
    with open(txt_path, "r", encoding="utf-8") as f:
        text_content = f.read()
    all_words = text_content.split()
    if not all_words:
        print("Error: The text file is empty.")
        return
    chapters = []
    chapter_num = 1
    for i in range(0, len(all_words), words_per_chapter):
        chunk_words = all_words[i:i + words_per_chapter]
        chunk_text = " ".join(chunk_words)
        escaped_content = html.escape(chunk_text)
        formatted_html = "".join(f"<p>{line}</p>" for line in escaped_content.split("\n") if line.strip())
        chap_title = f"Chapter {chapter_num}"
        chap_file = f"chap_{chapter_num}.xhtml"
        chapter = epub.EpubHtml(title=chap_title, file_name=chap_file, lang="en")
        chapter.content = f"<html><body><h1>{chap_title}</h1>{formatted_html}</body></html>"
        book.add_item(chapter)
        chapters.append(chapter)
        chapter_num += 1
    book.toc = tuple(chapters)
    if os.path.exists(cover_image_path):
        book.spine = ["cover", "nav"] + chapters
    else:
        book.spine = ["nav"] + chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())
    epub.write_epub(epub_path, book, {})
    print(f"Success! Saved EPUB with {len(chapters)} chapters to: {epub_path}")
if __name__ == "__main__":

    txt_path="keynes.txt"
    title="How to Pay for the War"
    author="John Maynard Keynes"
    cover_image_path="keynes.png"
    words_per_chapter=9677

    epub_path=title+"-"+author+".epub"

    create_epub_from_txt(title=title,author=author,cover_image_path=cover_image_path,txt_path=txt_path,epub_path=title+"-"+author+".epub",words_per_chapter=words_per_chapter)

#--------------------------------------------------------------------------------