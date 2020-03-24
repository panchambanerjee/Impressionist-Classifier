"""
Script to extract files from the Wikiart dump
"""

__author__ = 'pancham_banerjee'

import os
from shutil import copy2
from tqdm import tqdm


def copy_files(src_artist, dest_artist):
    """
    Copy files from individual folders into one folder for each artist
    :param src_artist: Source artist folder (from the Wikiart dump, divided into years)
    :arg src_artist: str
    :param dest_artist: Destination folder where all of the artist images are copied
    :arg dest_artist: str
    :return: None
    """
    
    artist_src_dir = os.path.join(root_dir, src_artist)
    artist_destination_dir = os.path.join(destination_dir, dest_artist)
    
    print(f"Copying files for {src_artist}")
    for root, dirs, files in os.walk(artist_src_dir):
        for file in tqdm(files):
            path_file = os.path.join(root, file)
            copy2(path_file, artist_destination_dir)
            
    print("Done")


if __name__ == "__main__":

    src_artist_lst = ['camille-pissarro', 'childe-hassam', 'claude-monet', 'edgar-degas', 'henri-matisse',
                      'john-singer-sargent', 'paul-cezanne', 'paul-gauguin', 'pierre-auguste-renoir',
                      'vincent-van-gogh']

    dest_artist_lst = ['Pissarro', 'Hassam', 'Monet', 'Degas', 'Matisse',
                       'Sargent', 'Cezanne', 'Gauguin', 'Renoir', 'VanGogh']

    root_dir = '/Users/panchamb/Documents/Wikiart/wikiart/wikiart-saved/images/'
    destination_dir = '/Users/panchamb/Documents/Wikiart/wikiart/Impressionists/'

    zip_lst = list(zip(src_artist_lst, dest_artist_lst))

    for (src, dest) in zip_lst:
        copy_files(src, dest)
