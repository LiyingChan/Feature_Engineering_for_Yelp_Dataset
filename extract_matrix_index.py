import os
import json
import pandas as pd
import pickle
import numpy as np

TP_file = os.path.join('montreal_reviews_filtered.json')

f = open(TP_file, encoding='utf-8')
users_id = []
items_id = []
ratings = []
reviews = []
np.random.seed(2019)

for line in f:
    js = json.loads(line)
    if str(js['user_id']) == 'unknown':
        print("unknown")
        continue
    if str(js['business_id']) == "unknown":
        print("unknown2")
        continue
    reviews.append(js['text'])
    users_id.append(str(js['user_id']))
    items_id.append(str(js['business_id']))
    ratings.append(str(js['stars']))

# get primal data
# ===================================================
data = pd.DataFrame(
    {'user_id': pd.Series(users_id),
     'item_id': pd.Series(items_id),
     'ratings': pd.Series(ratings),
     'reviews': pd.Series(reviews)}
)[['user_id', 'item_id', 'ratings', 'reviews']]


# trainsform data to index
# ==================================================
def get_count(tp, id):
    playcount_groupbyid = tp[[id, 'ratings']].groupby(id, as_index=False)
    count = playcount_groupbyid.size()
    return count


usercount, itemcount = get_count(data, 'user_id'), get_count(data, 'item_id')
unique_uid = usercount.index
unique_sid = itemcount.index

item2id = dict((sid, i) for (i, sid) in enumerate(unique_sid))
user2id = dict((uid, i) for (i, uid) in enumerate(unique_uid))

with open('montreal_filtered_item_index.pkl','wb') as res_idx:
    pickle.dump(item2id, res_idx)
with open('montreal_filtered_user_index.pkl','wb') as user_idx:
    pickle.dump(user2id, user_idx)