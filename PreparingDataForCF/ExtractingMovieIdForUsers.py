import json
from collections import OrderedDict
user_rated_movie_id={}
for i in range(1,6041):
	file_name="../DataWithPlot/user"+str(i)+".json"
	with open(file_name) as json_data:
		data_set_user = json.load(json_data,object_pairs_hook=OrderedDict)
		#print(data_set_user)
		#exit(0)
		
		
		#print(data_set_user)
		#exit(0)
		#data=[]
		#data_label=[]
		#liked=[]
		temp_movie_id=[]
		for k in data_set_user:
			#for k1 in data_set_user[k]:
			##print(data_set_user[k]["train"])
			for k2 in data_set_user[k]["train"]:
				#for k3 in data_set_user[k]["train"][k2]:
				movie_id=data_set_user[k]["train"][k2]['movie_id']
				temp_movie_id.append(movie_id)
		#print(len(temp_movie_id))
		user_rated_movie_id[i]=temp_movie_id
		#exit(0)
file_name="UsersMovieIds.json"
json_a = json.dumps(user_rated_movie_id)
f = open(file_name,"w")
f.write(json_a)
f.close()
			