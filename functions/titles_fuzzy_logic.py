import os
import urllib.request
import http.client
import socket
import click
from libgenparser.parser import LibgenParser
from fuzzywuzzy import fuzz

def has_matching_language_extension(dict1: dict, dict2: dict) -> bool:
    ''' check if two dictionaries have matching language and extension '''
    return dict1['Language'] == dict2['Language'] and dict1['Extension'] == dict2['Extension']


def is_similar_dict(new_dict: dict, existing_dicts: dict) -> bool:
    ''' check similarity of two dictionaries '''
    threshold = 80
    for d in existing_dicts:
        if has_matching_language_extension(new_dict, d) and fuzz.token_set_ratio(new_dict['Title'].lower(), d['Title'].lower()) > threshold:
            return True
    return False


def download_books_using_mirrors(books_filtered_unique: list, directory_path, timeout=240) -> None:
    ''' download files using active link '''
    for d in books_filtered_unique:
        try:
            author    = d["Author"].replace(" ", "_")
            title     = d["Title"].replace(" ", "_")
            filename  = f'{author}_{title}'
            extension = d["Extension"]
            response  = urllib.request.urlopen(d["active_link"], timeout=timeout)
            content   = response.read()
            # Create the author-specific subfolder if it doesn't exist
            author_folder = os.path.join(directory_path, author)
            os.makedirs(author_folder, exist_ok=True)
            save_path = os.path.join(author_folder, f'{filename}.{extension}')
            with open(save_path, 'wb') as file:
                file.write(content)
            click.secho(f'{filename} saved to {save_path}', fg='green')
        except urllib.error.URLError as e:
            click.secho(f"Download from {d['active_link']} mirror failed. Error: {e}.", fg='red')
            continue
        except socket.timeout:
            click.secho(f"Download from {d['active_link']} mirror timed out.", fg='red')
            continue
        except http.client.IncompleteRead as ic:
            click.secho(f"IncompleteRead error. Skipping...", fg='red')
            continue