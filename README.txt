How accurate can I guess the review of some product (from 1 to 5 stars) based on the content (words) of the review?
This program checks it for you in a dataset of 108 mb about video games (a json file from amazon) that can be downloaded from here
https://drive.google.com/file/d/0BzAGHKa-swBzOG9HYmRJU1hIckU/view?usp=sharing

Just put both files in the same folder and run it.


About the script:
I first extracted the reviews from JSON file and stored it in a CSV file.
After that, I iterated on each row of a CSV file which contains a review in first column and rating in second column .
I then cleaned the review using ntlk corpus of stopwords to prepare them for model training purposes.
Now I vectorised the review using TfidfVectorizer and transformed my test and train data using this vectoriser.
Finally, I trained my Logistic Regression model with this training data and tested on my test data and showed the accuracy of prediction.
