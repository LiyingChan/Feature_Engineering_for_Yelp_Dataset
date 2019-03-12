# encoding:utf-8
# save the vectorized reviews to future use

import json
import utils
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np

file_city_name = utils.file_city_name

# get the corpus
with open(file_city_name + '_users_concat_reviews.txt') as data_file:
	user_corpus = json.load(data_file)

with open(file_city_name + '_restaurants_concat_reviews.txt') as data_file:
	restaurant_corpus = json.load(data_file)
# ["abcde fghij","klmno pqrst",...]

# directly to tf-idf matrix
#
# restaurant
# print 'constructing tf-idf matrix for the restaurants'
print('constructing tf-idf matrix for the restaurants')
tfidf_vectorizer1 = TfidfVectorizer(sublinear_tf=True, min_df=1, stop_words='english')
restaurants_tfidf_X = tfidf_vectorizer1.fit_transform(restaurant_corpus)
# print restaurants_tfidf_X
pickle.dump(restaurants_tfidf_X, open(file_city_name + '_restaurants_tfidf_X.pkl', 'wb'))

# print 'constructing Hashing matrix for the restaurants'
print('constructing Hashing matrix for the restaurants')
vectorizer1 = HashingVectorizer(stop_words='english', non_negative=True, n_features=10000)
restaurants_hashing_X = vectorizer1.transform(restaurant_corpus)
# print restaurants_hashing_X
pickle.dump(restaurants_hashing_X, open(file_city_name + '_restaurants_hashing_X.pkl', 'wb'))

# print 'computing restaurants tfidf similarities'
print('computing restaurants tfidf similarities')
restaurants_tfidf_SimMatrix = linear_kernel(restaurants_tfidf_X, restaurants_tfidf_X)
# print restaurants_tfidf_SimMatrix
pickle.dump(restaurants_tfidf_SimMatrix, open(file_city_name + '_restaurants_tfidf_SimMatrix.pkl', 'wb'))

# print 'computing restaurants hashing similarities'
print('computing restaurants hashing similarities')
restaurants_hashing_SimMatrix = linear_kernel(restaurants_hashing_X, restaurants_hashing_X)
# print restaurants_hashing_SimMatrix
pickle.dump(restaurants_hashing_SimMatrix, open(file_city_name + '_restaurants_hashing_SimMatrix.pkl', 'wb'))

# user
# print 'constructing tf-idf matrix for the users'
print('constructing tf-idf matrix for the users')
tfidf_vectorizer2 = TfidfVectorizer(sublinear_tf = True, min_df = 1, stop_words = 'english')
users_tfidf_X = tfidf_vectorizer2.fit_transform(user_corpus)
# print users_tfidf_X
pickle.dump(users_tfidf_X, open( file_city_name + '_users_tfidf_X.pkl', 'wb'))

# print 'computing users tfidf similarities'
print('computing users tfidf similarities')
users_tfidf_SimMatrix = linear_kernel(users_tfidf_X, users_tfidf_X)
# print users_tfidf_SimMatrix
pickle.dump(users_tfidf_SimMatrix, open(file_city_name + '_users_tfidf_SimMatrix.pkl', 'wb'))

# print 'constructing hashing matrix for the users'
print('constructing hashing matrix for the users')
vectorizer2 = HashingVectorizer(stop_words = 'english', non_negative = True, n_features = 10000)
users_hashing_X = vectorizer2.transform(user_corpus)
# print users_hashing_X
pickle.dump(users_hashing_X, open( file_city_name + '_users_hashing_X.pkl', 'wb'))

# print 'computing users hashing similarities'
print('computing users hashing similarities')
users_hashing_SimMatrix = linear_kernel(users_hashing_X, users_hashing_X)
pickle.dump(users_hashing_SimMatrix, open( file_city_name + '_users_hashing_SimMatrix.pkl', 'wb'))

# print 'computing users tfidf similarities'
# users_tfidf_SimMatrix = (users_tfidf_X, users_tfidf_X)
# print users_tfidf_SimMatrix
# pickle.dump(users_tfidf_SimMatrix, open( file_city_name + '_users_tfidf_SimMatrix.pkl', 'wb'))
# vectorizer = TfidfVectorizer(min_df = 1, stop_words = 'english')
#
# print 'constructing tf-idf matrix for the restaurants'
# restaurants_X = vectorizer.fit_transform(restaurant_corpus)
#
# print 'constructing tf-idf matrix for the users'
# user_X = vectorizer.transform(user_corpus)
#
# print 'computing similarities'
# uu_cosine_similarities = linear_kernel(user_X, user_X)
# ii_cosine_similarities = linear_kernel(restaurants_X, restaurants_X)
#
# with open(file_city_name + '_user_X.np', 'w') as file:
# 	np.save(file, user_X)
#
# with open(file_city_name + '_restaurants_X.np', 'w') as file:
# 	np.save(file, restaurants_X)
#
# with open(file_city_name + '_cosine_similarities.np', 'w') as file:
# 	np.save(file, cosine_similarities)
