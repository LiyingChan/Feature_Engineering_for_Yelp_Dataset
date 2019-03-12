#加载商家的属性信息，
#将每一个商家的属性信息转换为向量
#分别计算商家向量之间的相似度（皮尔逊相似度）
#将相似度保存
import json
import pickle
import utils
from math import sqrt

def LoadData(i_index):
    # 加载商家属性信息
    # 将每一个商家的属性转换为向量元素
    businesses=set()
    reviewcount=[]
    attributeset=set()

    for key in i_index.keys():
        with open('yelp_filter/yelp_academic_dataset_business.json', encoding='utf-8') as data_file:
            for line in data_file:
                buss = json.loads(line)
                if buss['business_id'] == key:
                    review_count = buss['review_count']
                    reviewcount.append(review_count)
                    attribute = buss['attributes']
                    if attribute != None:
                        for k in attribute:
                            attributeset.add(k)
                    categories = buss['categories']
                    if categories!=None:
                        for c in categories:
                            businesses.add(c)
    maxreviewcount = max(reviewcount)
    minreviewcount = min(reviewcount)
    return businesses,attributeset,maxreviewcount,minreviewcount
def Vectoring(i_index, businesses,attributeset,maxreviewcount,minreviewcount):
    #正在将商家属性向量化...
    vectordict={}
    # businessvector = open('../Gov-similarity/yelp_academic_dataset_business.vector.pkl', mode='w', encoding='UTF-8')
    for key in i_index.keys():
        with open('yelp_filter/yelp_academic_dataset_business.json', encoding='utf-8') as data_file:
            for line in data_file:
                buss = json.loads(line)
                if buss['business_id'] == key:
                    bussid=buss['business_id']
                    # 获取stars的向量
                    stars = buss['stars']
                    # 进行归一化
                    stars=stars/5
                    #获取评论数
                    review_count=buss['review_count']
                    #进行归一化
                    review_count=MaxMinNormalization(review_count,maxreviewcount,minreviewcount)
                    #获取签到数
                    # checkin_all, checkin_work, checkin_relax=GetCheckin(bussid)
                    # checkin_all=checkin_all/500
                    # checkin_work=checkin_work/500
                    # checkin_relax=checkin_relax/500
                    #获取属性向量
                    attributes=buss['attributes']
                    vectorattr=[]
                    for ddd1 in attributeset:
                        vectorattr.append(0)
                    if attributes != None:
                        for k in attributes:
                            kka = -1
                            for ka in attributeset:
                                kka+=1
                                if k==ka:
                                    vectorattr[kka] = 1

                    #获取类别向量
                    categories = buss['categories']
                    vector = []
                    for ddd in businesses:
                        vector.append(0)
                    if categories!=None:
                        for c in categories:
                            kk=-1    #向量下标
                            for t in businesses:
                                kk += 1
                                if c==t:
                                    vector[kk]=1
                                else:
                                    vector[kk]=0
                    # 加入商家属性
                    for vr in vectorattr:
                        vector.append(vr)
                    # 加入评级数
                    vector.append(stars)
                    # 加入周评论数
                    vector.append(review_count)
                    #加入一周总的签到数
                    # vector.append(checkin_all)
                    # #加入工作日签到数
                    # vector.append(checkin_work)
                    # #加入休息日签到数
                    # vector.append(checkin_relax)
                    #print(vector)
                    bussidindex=i_index[bussid]
                    vectordict[bussidindex]=vector
                    print(vectordict)
    # businessvector.write(vectordict)
    pickle.dump(vectordict, open('yelp_business_vector.pkl', 'wb'))
    print('end vectoring...')
    return vectordict
def MaxMinNormalization(x,Max,Min):
    x = (x - Min) / (Max - Min)
    return x

if __name__ == '__main__':
    print('start vectoring...')
    with open('yelp_filter/montreal_filtered_item_index.pkl','rb') as rest_idx_file:
        i_index = pickle.load(rest_idx_file)
    businesses, attributeset, maxreviewcount, minreviewcount = LoadData(i_index)
    vectordict=Vectoring(i_index, businesses, attributeset, maxreviewcount, minreviewcount)

