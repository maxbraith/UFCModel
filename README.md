This project is a UFC predictive model using the Python requests and bs4 libraries to web scrape data to construct the datasets to serve as the database of the project. Because the data was created using a web scraping technique, functionality to update them as UFC fights take place is available.

The pandas library is used to format and combine these datasets for modelling. There are 4 major datasets that were web scraped, they were combined using the pandas library to result in two datasets. One is used to train the model, and the other is input data for the model.

The scikit-learn library to ensure data is represented correctly for modelling. Finally, the TensorFlow library is used to build a deep learning neural network to predict winners of fights. The model is trained on individual fight data, while the input data is career statistics of individual fighters.

At its current stage the model performs at around 86-88% accuracy, using a dataset consisting of 40 columns and 6142 rows in order to predict winners. The train and test data consists of individual fight statistics so this will not be indicative of performance in practice. 

The individual career fighter statistics dataset was used to construct a dataset representative of what will be inputted. This includes input data from fights since 2021. Using this data to test the model, the model achieves an accuracy of 65-66%.

Aiddition features planned include an easily interpretable front end consisting fo three pages, one where the next card of fights is displayed as well as the model's prediction of who will win, another where users can input custom fights to see who the model predicts to win, and one more page that tracks the model's actual performance. This front end will be created using React.

One final feature planned to add is to update the planned front end and the back end, whilst also having the capability to update a custom amount of UFC cards in case the database is not updated after a UFC card.
