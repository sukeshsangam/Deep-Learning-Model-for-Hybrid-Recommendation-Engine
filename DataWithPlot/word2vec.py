import urllib.request, json
import re
import time
import os
import DocIterator as DocIt
from gensim.models import Doc2Vec

with open("final_cleaned_movies.json") as json_data:
	data_set = json.load(json_data)
	#print(data_set["1"])
	for i in range(1,6041):
		file_name="user"+str(i)+".json"
		#print(file_name)
		with open(file_name) as json_data:
			data_set_user = json.load(json_data)
			#print(data_set_user)
			#exit(0)
			data=[]
			data_label=[]
			#print(data_set_user)
			#exit(0)
			for k in data_set_user:
				#for k1 in data_set_user[k]:
				##print(data_set_user[k]["train"])
				for k2 in data_set_user[k]["train"]:
					#for k3 in data_set_user[k]["train"][k2]:
					movie_id=data_set_user[k]["train"][k2]['movie_id']
					data_label.append(movie_id)
					movie_plot=data_set_user[k]["train"][k2]['movie_plot']
					data.append(movie_plot)
		print(data)
		print(data_label)
		it = DocIt.DocIterator(data, data_label)
		print(it)
		model = Doc2Vec(size=300, window=10, min_count=5, workers=11,alpha=0.025, min_alpha=0.025) # use fixed learning rate
		model.build_vocab(it)
		for epoch in range(10):
			model.train(it)
			model.alpha -= 0.002 # decrease the learning rate
			model.min_alpha = model.alpha # fix the learning rate, no deca
			model.train(it)
		exit(0)
		#json_a = json.dumps(data_set_user)
		#file_name_new="user"+str(i)+".json"
		#f = open(file_name_new,"w")
		#f.write(json_a)
		#f.close()
#print(data)
#print(data_label)