import os
import urllib.request
import socket

def has_matching_language_extension(dict1, dict2) -> bool:
    ''' check if two dictionaries have matching language and extension '''
    return dict1['Language'] == dict2['Language'] and dict1['Extension'] == dict2['Extension']


def is_similar_dict(new_dict, existing_dicts) -> bool:
    for d in existing_dicts:
        if has_matching_language_extension(new_dict, d) and fuzz.token_set_ratio(new_dict['Title'].lower(), d['Title'].lower()) > 80:
            return True
    return False


def add_active_links_to_books(books_filtered_unique) -> dict:
    for d in books_filtered_unique:
        d["active_link"] = libgen.resolve_download_link(md5=d['MD5'])
    return books_filtered_unique


def download_books_using_mirrors(books_filtered_unique, timeout=240, download_path='./downloads') -> None:
    # DOWNLOAD FILES USING MIRRORS
    for d in books_filtered_unique:
        try:
            author    = d["Author"].replace(" ", "_")
            title     = d["Title"].replace(" ", "_")
            filename  = f'{author}_{title}'
            extension = d["Extension"]
            response  = urllib.request.urlopen(d["active_link"], timeout=timeout)
            content   = response.read()
            # Create the author-specific subfolder if it doesn't exist
            author_folder = os.path.join(download_path, author)
            os.makedirs(author_folder, exist_ok=True)
            save_path = os.path.join(author_folder, f'{filename}.{extension}')
            with open(save_path, 'wb') as file:
                file.write(content)
            print(f'{filename} SAVED TO {save_path}')
        except urllib.error.URLError as e:
            print(f"Download from {url} mirror failed. Error: {e}.")
        except socket.timeout:
            print(f"Download from {url} mirror timed out.")