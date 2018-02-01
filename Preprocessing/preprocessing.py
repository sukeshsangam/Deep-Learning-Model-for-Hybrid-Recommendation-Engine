import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rating_headers = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rating_headers)
#ratings.head()
#ratings.size
movies_headers = ['movie_id', 'movie_name', 'Genre']
movies = pd.read_table('movies.dat', sep='::', header=None, names=movies_headers)
#movies.head()
data_set=ratings.merge(movies,on='movie_id')



for i in range(1,6041):
	final_Array=[]
	dataset_dic={}
	user_data=data_set.loc[data_set['user_id'] == i]
    #print(user_data)
    #break
	no_ratings=len(user_data.index)
	dataset_dic[i]={}
	split=round(no_ratings*0.75,0)
    #print(split)
    #break
    #exit(0)
	dataset_dic[i]['train']={}
	dataset_dic[i]['test']={}
	j=0
	for index,row in user_data.iterrows():
		if(j<split):
			dataset_dic[i]['train'][j]={}
			dataset_dic[i]['train'][j]["movie_id"]=row["movie_id"]
			dataset_dic[i]['train'][j]["rating"]=row["rating"]
			dataset_dic[i]['train'][j]["timestamp"]=row["timestamp"]
			dataset_dic[i]['train'][j]["movie_name"]=row["movie_name"]
			dataset_dic[i]['train'][j]["Genre"]=row["Genre"]
		else:
			dataset_dic[i]['test'][j]={}
			dataset_dic[i]['test'][j]["movie_id"]=row["movie_id"]
			dataset_dic[i]['test'][j]["rating"]=row["rating"]
			dataset_dic[i]['test'][j]["timestamp"]=row["timestamp"]
			dataset_dic[i]['test'][j]["movie_name"]=row["movie_name"]
			dataset_dic[i]['test'][j]["Genre"]=row["Genre"]
		j=j+1
	final_Array.append(dataset_dic)
	json_a = json.dumps(dataset_dic)
	print(json_a)
	file_name="user"+str(i)
	print(file_name)
	f = open('%s.json' % file_name,"w")
	f.write(json_a)
	f.close()
	i=i+1
#print(dataset_dic)
