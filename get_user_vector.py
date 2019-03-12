import utils
import json
import csv
import pickle
import time
import re
import numpy as np
from collections import defaultdict

file_city_name = utils.file_city_name
city_name = utils.city_name
count = 0
# 功能：将一字典写入到csv文件中
# 输入：文件名称，数据字典
pklFile = file_city_name + '_user_filtered.pkl'
csvFile = file_city_name + '_user_filtered.csv'
def createDictCSV(count, file_name,buss):
    with open(file_name, "a",newline='') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=list(buss))
        if count == 0:
            writer.writeheader()
        writer.writerow(buss)
    return csvFile

def create_fea_dic(buss, fea_dic):
    fea_list = []
    fea_list.append(buss['yelping_since'])
    fea_list.append(buss['elite'])
    fea_list.append(buss['review_count'])
    fea_list.append(buss['fans'])
    fea_list.append(buss['average_stars'])
    fea_list.append(buss['useful'])
    fea_list.append(buss['funny'])
    fea_list.append(buss['cool'])
    fea_list.append(buss['compliment_hot'])
    fea_list.append(buss['compliment_more'])
    fea_list.append(buss['compliment_profile'])
    fea_list.append(buss['compliment_cute'])
    fea_list.append(buss['compliment_list'])
    fea_list.append(buss['compliment_note'])
    fea_list.append(buss['compliment_plain'])
    fea_list.append(buss['compliment_cool'])
    fea_list.append(buss['compliment_funny'])
    fea_list.append(buss['compliment_writer'])
    fea_list.append(buss['compliment_photos'])
    fea_dic[buss['user_id']] = fea_list
    return fea_dic

fea_dic = defaultdict(list)
with open('montreal_filtered_user_index.pkl', 'rb') as rest_idx_file:
    i_index = pickle.load(rest_idx_file)
for key in i_index.keys():
        with open('yelp_academic_dataset_user.json', encoding='utf-8') as data_file:
            for line in data_file:
                buss = json.loads(line)
                # getSortedValues(buss)
                # print(buss)
                if buss['user_id'] == key:
                    buss['user_id'] = i_index[key]
                    date_time = buss['yelping_since']
                    timeArray = time.strptime(date_time, "%Y-%m-%d")
                    date_year = timeArray.tm_year
                    since_time = 2019 - date_year
                    buss['yelping_since'] = since_time
                    elite_max = 0
                    for elite_data in buss['elite'][0:len(buss['elite'])]:
                        pl = r"[0-9]+"
                        r = re.compile(pl)
                        if len(r.findall(elite_data)) != 0:
                            number = list(map(int, r.findall(elite_data)))
                            elite_max = int(np.max(number))
                        else:
                            elite_max = date_year
                    elite_since = elite_max - date_year
                    buss['elite'] = elite_since
                    fea_dic = create_fea_dic(buss, fea_dic)
                    # print(buss)
                    # # csvWriter.writerow(buss)
                    # for k, v in buss.items():
                    #     csvWriter.writerow([k, v])
                    print(count)
                    count = count + 1
pickle.dump(fea_dic, open('yelp_user_vector.pkl', 'wb'))