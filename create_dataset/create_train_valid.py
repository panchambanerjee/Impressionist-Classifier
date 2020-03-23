"""
Script to create train and valid splits for each individual artist
"""

__author__ = 'pancham_banerjee'

import os
import random
from shutil import copy2
from tqdm import tqdm


def split_data(root, artist_name, train_split_idx, valid_split_idx):
    """
    Split data into train and valid sets
    :param root: Root directory
    :type root: str
    :param artist_name: Artist name
    :type artist_name: str
    :param train_split_idx: Index of train file split
    :type train_split_idx: int
    :param valid_split_idx: Index of valid file split
    :type valid_split_idx: int
    :return: None
    """
    print(f"Creating train and validation splits for {artist_name}")

    src = os.path.join(root, artist_name)
    train_dir = os.path.join(root, 'training', artist_name)
    valid_dir = os.path.join(root, 'validation', artist_name)

    # Check for zero length files
    files = []
    for file in os.listdir(src):
        if os.path.getsize(f"{src}/{file}") > 0:
            files.append(file)
        else:
            print(f"{file} is zero length, so ignoring.")

    # Shuffle files
    files_shuffled = random.sample(files, len(files))

    for file in tqdm(files_shuffled[:train_split_idx]):
        path_file = os.path.join(src, file)
        copy2(path_file, train_dir)

    for file in tqdm(files_shuffled[-valid_split_idx:]):
        path_file = os.path.join(src, file)
        copy2(path_file, valid_dir)


if __name__ == "__main__":

    root_dir = '/Users/panchamb/Documents/Wikiart/wikiart/Impressionists/'

    artist_lst = ['Pissarro', 'Hassam', 'Monet', 'Degas', 'Matisse',
                  'Sargent', 'Cezanne', 'Gauguin', 'Renoir', 'VanGogh']

    num_train = 399
    num_valid = 99

    for artist in artist_lst:
        split_data(root_dir, artist, num_train, num_valid)



