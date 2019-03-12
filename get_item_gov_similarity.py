# encoding:utf-8
#加载所有商家的经纬度
#利用经纬度分别计算商家之间的相似度（计算距离差，利用距离差的倒数来表示相似度）
#将计算的相似度保存
import json
import pickle
import utils
import numpy as np
from math import radians,cos,sin,asin,sqrt

def Loaditemgov(i_index):
    businesses={}
    num = 0
    for key in i_index.keys():
        with open('yelp_filter/yelp_academic_dataset_business.json', encoding='utf-8') as data_file:
            for line in data_file:
                buss = json.loads(line)
                if buss['business_id'] == key:
                    num += 1
                    print(num)
                    business_id=buss['business_id']
                    longitude=buss['longitude']
                    latitude=buss['latitude']
                    bussidindex = i_index[business_id]
                    point=[]
                    point.append(longitude)
                    point.append(latitude)
                    businesses[bussidindex]=point
    return businesses # {0:[45,56],1:[78,90],...}
def GetDistance(lon1,lat1,lon2,lat2):
    distance1=0
     # 将十进制度数转化为弧度  
    lon1,lat1,lon2,lat2=map(radians,[lon1,lat1,lon2,lat2])
    dlon=lon2-lon1
    dlat=lat2-lat1
    a=sin(dlat/2) ** 2+cos(lat1)* cos(lat2)* sin(dlon/2) ** 2
    c=2* asin(sqrt(a))
    r=6371
    # 地球平均半径，单位为公里  
    distance1=c*r*1000
    return distance1

def ItemSimilarity(businesses):
    allsimilarity = {}
    keys = businesses.keys() # get all indices of business
    for key1 in keys:
        values1=businesses[key1] # get point of key1
        lon1=values1[0]
        lat1=values1[1] # get longitude and latitude of key1
        itemneighbor={}
        itemneighbor2={}
        for key2 in keys:
            if key2!=key1: # calculate sim of key2 and key1
                values2 = businesses[key2]
                lon2 = values2[0]
                lat2 = values2[1] # get longitude and latitude of key2
                distance=GetDistance(lon1, lat1, lon2, lat2) + 10
                similarity = 1 / distance
                itemneighbor[key2] = similarity
        neighbor = sorted(itemneighbor.items(), key=lambda x: x[1], reverse=True)[:100]
        for n in neighbor: # [(2,0.99),(3,0.89),...]
            n1=n[0]
            n2=n[1]
            itemneighbor2[n1]=n2
        allsimilarity[key1]=itemneighbor2
        print(allsimilarity)
    pickle.dump(allsimilarity, open('yelp_ii_100_gov_neibor.pkl', 'wb'))
    # pickle.dump(B_gov, open('B_gov.pkl', 'wb'))
if __name__ == '__main__':
    # file_city_name = utils.file_city_name
    # city_name = utils.city_name
    print('calculate simalarity...')
    with open('yelp_filter/montreal_filtered_item_index.pkl','rb') as rest_idx_file:
        i_index = pickle.load(rest_idx_file)
    businesses=Loaditemgov(i_index)
    ItemSimilarity(businesses)