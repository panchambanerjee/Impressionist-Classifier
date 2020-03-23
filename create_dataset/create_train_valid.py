import os
import random
import shutil
from shutil import copyfile, copy2
from os import getcwd
from tqdm import tqdm

def split_data(artist, num_train, num_valid):

    print(f"Creating train and validation splits for {artist}")
    
    src = os.path.join(root_dir, artist)
    train_dir = os.path.join(root_dir, 'training', artist)
    valid_dir = os.path.join(root_dir, 'validation', artist)

    files = []
    for file in os.listdir(src):
        if os.path.getsize(f"{src}/{file}") > 0:
            files.append(file)
        else:
            print(f"{file} is zero length, so ignoring.")
            
    
    files_shuffled = random.sample(files, len(files))
    
    for file in tqdm(files_shuffled[:num_train]):
            path_file = os.path.join(src, file)
            copy2(path_file, train_dir) 
        
    for file in tqdm(files_shuffled[-num_valid:]):
            path_file = os.path.join(src, file)
            copy2(path_file, valid_dir) 
            

root_dir = '/Users/panchamb/Documents/Wikiart/wikiart/Impressionists/'


artist_lst = ['Pissarro', 'Hassam', 'Monet', 'Degas', 'Matisse', \
                   'Sargent', 'Cezanne', 'Gauguin', 'Renoir', 'VanGogh']

num_train = 399
num_valid = 99

for artist in artist_lst:
    split_data(artist, num_train, num_valid)
    
    
    
    
    
