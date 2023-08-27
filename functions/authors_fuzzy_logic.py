import os
from fuzzywuzzy import fuzz
import click

def find_similar_authors(author_folders: list) -> dict:
    ''' Fuzzy string matching over author folders in local directory '''
    similar_authors = {}
    for i, author1 in enumerate(author_folders):
        for j, author2 in enumerate(author_folders):
            if i != j and fuzz.partial_ratio(author1, author2) >= 80:
                click.secho(f"Found similar authors: {author1} and {author2}", fg='yellow')
                similar_authors.setdefault(author1, []).append(author2)
    return similar_authors


def rename_author_folders(directory_path) -> None:
    ''' Local directory renaming and merging based on duplicated author folders '''
    # Get a list of author folders
    author_folders = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]

    # Find similar authors based on fuzzy matching
    similar_authors = find_similar_authors(author_folders)

    # Merge similar authors folders
    for main_author, similar_list in similar_authors.items():
        main_author_path = os.path.join(directory_path, main_author)

        # Create the main author directory if it doesn't exist
        if not os.path.exists(main_author_path):
            os.makedirs(main_author_path)

        for similar_author in similar_list:
            similar_author_path = os.path.join(directory_path, similar_author)

            for item in os.listdir(similar_author_path):
                item_path = os.path.join(similar_author_path, item)
                new_item_path = os.path.join(main_author_path, item)
                os.rename(item_path, new_item_path)

            os.rmdir(similar_author_path)
        click.secho(f"Merged {similar_list} into {main_author}", fg='blue')

    click.secho("Directory cleaning complete.", fg='green')