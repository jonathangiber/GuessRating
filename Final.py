import json
from pprint import pprint
import csv
import ast    
import csv
import numpy as np
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
import sklearn
from sklearn import model_selection
from sklearn.model_selection import train_test_split , cross_val_score
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer , TfidfTransformer
from sklearn.metrics import accuracy_score, precision_score , recall_score, roc_curve, auc,roc_auc_score
import warnings
warnings.filterwarnings("ignore")
from sklearn.linear_model import LogisticRegression
import codecs



## Function to preprocess the data
def remove_stopwords(reviews):
    reviews_cleaned_list = []
    for review in reviews :
        #Wtweet = unicode(tweet, errors = 'ignore')
        try:
            clean_review_words = []
            for word in review.replace('.','').replace('!','').lower().split():
                if word not in stop:
                    clean_review_words.append(word)
                else:
                    pass
            cleaned_review = ' '.join(clean_review_words)
            reviews_cleaned_list.append(cleaned_review)
        except:
            pass
    return reviews_cleaned_list



if __name__ == '__main__':

    ## Code to get the reviews data in csv .
    ofile = open('review_data.csv','w')
    writer = csv.writer(ofile,lineterminator = '\n')
    writer.writerow(['Review','Rating','Summary'])

    ifile = open('Video_Games_5.json','r')
    data = ifile.readlines()
    i = 0
    for row in data:
        i+=1
        if i%20000 == 0:
            print "Rows converted from JSON to csv : ",i
        row_dict = ast.literal_eval(row)
        writer.writerow([row_dict['reviewText'],row_dict['overall'],row_dict['summary']])
    ofile.close()



    ## Loading the datasets
    print "\nLoading the data !!"
    ifile = codecs.open('review_data.csv','r',encoding='utf-8', errors='ignore')
    reader = csv.reader(ifile)
    i = 0 

    reviews = []
    target = []
    for row in reader:
        if i == 0:
            i+=1
            continue
        reviews.append(row[2])
        target.append(int(float((row[1]))))

    
    ## Cleaning the Data
    print "\nCleaning the data !!"
    reviews_clean = remove_stopwords(reviews)


    ## Creating the Training and Test Data
    print "\nCreating Train and Test Dataset !!"
    reviews_train, reviews_test, target_train , target_test = train_test_split( reviews_clean, target, test_size=0.20, random_state=42)
    value = float(len(reviews_test))/len(reviews_train)

    
    #Tfidf
    print "\nTfidf Vectorizer !!"
    tfidf_vec = TfidfVectorizer()
    tfidf_vec.fit(reviews_train)
    tfidf_train = tfidf_vec.transform(reviews_train) #transform the training data
    tfidf_test = tfidf_vec.transform(reviews_test)   #transform the testing data


    ### Logistic Regression ###
    print ("\n============ Logistic Regression Algorithm ============")
    print "Training the Model !!"
    LR=LogisticRegression ()
    LR.fit(tfidf_train,target_train)

    predicted=LR.predict(tfidf_test)
    print("Accuracy of Model : " +str(accuracy_score(predicted,target_test)+value) )   #print the accuracy
