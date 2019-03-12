import json
import pickle
def Get_data():
    svector={}
    f = open('yelp_business_vector.pkl', 'rb')
    allvector = pickle.load(f)
    keys=allvector.keys()
    for key1 in keys:
        value1=allvector[key1]
        itemneighbor = {}
        itemneighbor2 = {}
        for key2 in keys:
            if key2!=key1:
                value2=allvector[key2]
                similarity=Get_similarity(value1,value2)
                itemneighbor[key2]=similarity
        neighbor=sorted(itemneighbor.items(), key=lambda x: x[1], reverse=True)[:100]
        for n in neighbor:
            n1=n[0]
            n2=n[1]
            itemneighbor2[n1]=n2
        svector[key1]=itemneighbor2
    pickle.dump(svector, open('yelp_ii_100_pro_neibor.pkl', 'wb'))
def Get_similarity(value1,value2):
    similarity=0
    count=-1
    p=[]
    sum=0
    for i in value1:
        count+=1
        p.append(i-value2[count])
    for j in p:
        sum+=j*j
    similarity=1/(sum+1)
    return similarity
# def sum():
#     a=[1,0,0,0,1,2,0]
#     b=[1,1,1,0,0,0,0]
#     c=[1,0,0,0,1,2,0]
#     d=[1,1,0,0,1,2,0]
#     d1=Get_similarity(a,b)
#     d2=Get_similarity(a,c)
#     d3=Get_similarity(b,c)
#     d4=Get_similarity(a,d)
#     print(d1)
#     print(d2)
#     print(d3)
#     print(d4)

if __name__ == '__main__':
    print('calculate simalarity...')
    Get_data()