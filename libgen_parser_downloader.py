from fuzzywuzzy import fuzz
from libgenparser.parser import LibgenParser
import os
import socket
import urllib.request
import click

@click.command()
@click.option('--author', default=False, help='Author to search in Library Genesis and download all books in the database', type=str)
@click.option('--directory_path', default="./downloads/", help='Directory path to save all the books found', type=str)
def main(author, directory_path):
    # Scrape author in Library Genesis
    libgen = LibgenParser()
    if author:
        books = libgen.search_author(author)
    else:
        raise ValueError('Error: no author to search in Library Genesis')

    # Filter only books in preferred languages and extensions
    books_filtered = [d for d in books if d['Language'] in ['English', 'Spanish'] and d['Extension'] in ['pdf', 'epub', 'mobi']]

    # Apply fuzzy string matching logic to book titles with same language and extension to remove duplicates
    books_filtered_unique = []
    threshold = 80
    def has_matching_language_extension(dict1, dict2):
        return dict1['Language'] == dict2['Language'] and dict1['Extension'] == dict2['Extension']

    def is_similar_dict(new_dict, existing_dicts):
        for d in existing_dicts:
            if has_matching_language_extension(new_dict, d) and fuzz.token_set_ratio(new_dict['Title'].lower(), d['Title'].lower()) > threshold:
                return True
        return False

    for d in books_filtered[1:]:
        if not is_similar_dict(d, books_filtered_unique):
            books_filtered_unique.append(d)

    # Get active links to download filtered list of books
    for d in books_filtered_unique:
        d["active_link"] = libgen.resolve_download_link(md5=d['MD5'])

    # Download books and create local directory based on author
    timeout = 240
    for d in books_filtered_unique:
        try:
            author = d["Author"].replace(" ", "_")
            title = d["Title"].replace(" ", "_")
            filename = f'{author}_{title}'
            extension = d["Extension"]
            response = urllib.request.urlopen(d["active_link"], timeout=timeout)
            content = response.read()
            author_folder = os.path.join(directory_path, author)
            os.makedirs(author_folder, exist_ok=True)
            save_path = os.path.join(author_folder, f'{filename}.{extension}')
            with open(save_path, 'wb') as file:
                file.write(content)
            click.echo(f'{filename} saved to {save_path}')
        except urllib.error.URLError as e:
            click.echo(f"Download from {d['active_link']} mirror failed. Error: {e}.")
        except socket.timeout:
            click.echo(f"Download from {d['active_link']} mirror timed out.")

    # Apply fuzzy string matching logic to authors with similar names
    def find_similar_authors(authors):
        similar_authors = {}
        for i, author1 in enumerate(authors):
            for j, author2 in enumerate(authors):
                if i != j and fuzz.partial_ratio(author1, author2) >= 80:
                    similar_authors.setdefault(author1, []).append(author2)
        return similar_authors

    author_folders = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]
    similar_authors = find_similar_authors(author_folders)

    for main_author, similar_list in similar_authors.items():
        main_author_path = os.path.join(directory_path, main_author)
        if not os.path.exists(main_author_path):
            os.makedirs(main_author_path)
        for similar_author in similar_list:
            similar_author_path = os.path.join(directory_path, similar_author)
            for item in os.listdir(similar_author_path):
                item_path = os.path.join(similar_author_path, item)
                new_item_path = os.path.join(main_author_path, item)
                os.rename(item_path, new_item_path)
            os.rmdir(similar_author_path)
        click.echo(f"Merged {similar_list} into {main_author}")

    click.echo("Directory cleaning complete.")

if __name__ == "__main__":
    main()
