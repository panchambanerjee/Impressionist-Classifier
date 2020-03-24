# Impressionist-Classifier
Training a Multi-Class Classifier to distinguish between Impressionist Painters

#### The aim of this project is to build a multi-class classifier for 10 Impressionist painters, namely:
* Camille Pisarro
* Childe Hassam
* Claude Monet
* Edgar Degas
* Henri Matisse
* John Singer-Sargent
* Paul Cezanne
* Paul Gauguin
* Pierre-Auguste Renoir
* Vincent van Gogh

#### We have downloaded the relevant datasets from Wikiart using https://github.com/lucasdavid/wikiart
-- This comprises all the downloadable paintings from wikiart for all the above 10 artists (they were chosen based on having > 500 paintings each in the WikiArt database. The paintings are downloaded into folders for each artist separated by year.


#### Briefly, the data acquisition process is as follows:
* We download the Wikiart files for the relevant artists using lucasdavid's extremely useful script (Please star the project if you can). 
* The downloaded files for each artist are split into years. We write a simple script to copy all the files for one artist into one dedicated folder.
* Then we create the train and validation sets, with 400 train images and 100 validation images respectively for each of the 10 artists. 
* For anyone looking to replicate the dataset creation process, downloading the images from Wikiart, and then replacing the local directory references in the two scripts in create_dataset/ will suffice.
* Alternatively, the dataset may be downloaded from Kaggle: www.kaggle.com/delayedkarma/impressionist-classifier-data

