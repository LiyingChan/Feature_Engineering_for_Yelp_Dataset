# encoding:utf-8
import pickle
from collections import defaultdict
def matrix2dict(sim_file_name, nei_file_name):

    sim_dic = defaultdict(dict)
    sim_mat = pickle.load(open(sim_file_name, 'rb'))
    print(sim_mat[0]) # [1. 0.10148169 0.35384975 ... 0.17206752 0.24394436 0.34907756]
    for i in range(sim_mat.shape[0]):
        for j in range(len(sim_mat[i])):
            if i!= j:
                sim_dic[i][j] = sim_mat[i][j]
    user_nei = {}
    for user in sim_dic.keys():
        matchUsers = sorted(sim_dic[user].items(),key = lambda x:x[1],reverse=True)[:100]
        matchUsers = matchUsers[:100]
        user_nei[user]=dict(matchUsers)
    print(user_nei[0]) # {3085: '0.44331710907014077', 2136: '0.4357890162762208',...}
    pickle.dump(user_nei,open(nei_file_name,'wb'))

# user
uu_sim_hash = 'montreal_users_hashing_SimMatrix.pkl'
uu_nei_hash = 'yelp_uu_100_hash_neibor.pkl'
matrix2dict(uu_sim_hash,uu_nei_hash)
#
# uu_sim_tfidf = 'montreal_users_tfidf_SimMatrix.pkl'
# uu_nei_tfidf = 'yelp_uu_100_tfidf_neibor.pkl'
# matrix2dict(uu_sim_tfidf,uu_nei_tfidf)

# item
# ii_sim_hash = 'montreal_restaurants_hashing_SimMatrix.pkl'
# ii_nei_hash = 'yelp_ii_100_hash_neibor.pkl'
# matrix2dict(ii_sim_hash,ii_nei_hash)
#
# ii_sim_tfidf = 'montreal_restaurants_tfidf_SimMatrix.pkl'
# ii_nei_tfidf = 'yelp_ii_100_tfidf_neibor.pkl'
# matrix2dict(ii_sim_tfidf,ii_nei_tfidf)