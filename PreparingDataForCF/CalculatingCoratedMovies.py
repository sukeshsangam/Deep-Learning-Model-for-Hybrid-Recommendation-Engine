import json
from collections import OrderedDict

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

file_name="UsersMovieIds.json"
with open(file_name) as json_data:
	data_set_user = json.load(json_data,object_pairs_hook=OrderedDict)
	for j in data_set_user:
		dic={}
		for i in data_set_user:
			if i==j:
				continue
			temp=[]
			temp=intersect(data_set_user[j],data_set_user[i])
			#print(temp)
			k=0
			if len(temp)>10:
				dic[i]=temp
				k=1
			#exit(0)
			if k==1:
				print(dic)
				#exit(0)