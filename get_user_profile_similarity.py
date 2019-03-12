import json
import pickle
import numpy as np

def Get_data():
    svector={}
    f = open('yelp_user_vector.pkl', 'rb')
    allvector = pickle.load(f)
    keys=allvector.keys()
    for key1 in keys:
        value1=allvector[key1]
        itemneighbor = {}
        itemneighbor2 = {}
        for key2 in keys:
            if key2!=key1:
                value2=allvector[key2]
                similarity=cos_sim(value1,value2)
                itemneighbor[key2]=similarity
        neighbor=sorted(itemneighbor.items(), key=lambda x: x[1], reverse=True)[:100]
        for n in neighbor:
            n1=n[0]
            n2=n[1]
            itemneighbor2[n1]=n2
        svector[key1]=itemneighbor2
    pickle.dump(svector, open('yelp_uu_100_pro_neibor.pkl', 'wb'))


def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a
    :param vector_b: 向量 b
    :return: sim
    """
    vector_a = np.mat(vector_a)
    vector_b = np.mat(vector_b)
    num = float(vector_a * vector_b.T)
    denom = np.linalg.norm(vector_a) * np.linalg.norm(vector_b)
    cos = num / denom
    sim = 0.5 + 0.5 * cos
    return sim

if __name__ == '__main__':
    print('calculate simalarity...')
    Get_data()