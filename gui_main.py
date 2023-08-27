from fuzzywuzzy import fuzz
from libgenparser.parser import LibgenParser
import os
import socket
import urllib.request
import click
from functions.titles_fuzzy_logic import *
from functions.authors_fuzzy_logic import *

def main(author, directory_path):
    # Scrape author in Library Genesis
    libgen = LibgenParser()
    if author:
        print(f'Execution started for author: {author}')
        books = libgen.search_author(author)
    else:
        raise ValueError('Error: no author to search in Library Genesis')

    # Filter only books in preferred languages and extensions
    books_filtered = [d for d in books if d['Language'] in ['English', 'Spanish'] and d['Extension'] in ['pdf', 'epub', 'mobi']]

    # Apply fuzzy string matching logic to book titles with same language and extension to remove duplicates
    books_filtered_unique = []
    for d in books_filtered[1:]:
        if not is_similar_dict(d, books_filtered_unique):
            books_filtered_unique.append(d)

    # Add active links to download filtered list of books
    for d in books_filtered_unique:
        d["active_link"] = libgen.resolve_download_link(md5=d['MD5'])

    # Download books and create local directory based on author
    download_books_using_mirrors(books_filtered_unique, directory_path)

    # Apply fuzzy string matching logic to authors with similar names
    rename_author_folders(directory_path)

#if __name__ == "__main__":
#    main()