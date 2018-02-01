import urllib.request, json
import re
import time
import os

with open("final_cleaned_movies.json") as json_data:
	data_set = json.load(json_data)
	#print(data_set["1"])
	for i in range(1,6040):
		file_name="../user"+str(i)+".json"
		print(file_name)
		with open(file_name) as json_data:
			data_set_user = json.load(json_data)
			print(data_set_user)
			exit(0)
			for k in data_set_user:
				for k1 in data_set_user[k]:
					for k2 in data_set_user[k][k1]:
						movie_id=data_set_user[k][k1][k2]['movie_id']
						data_set_user[k][k1][k2]["movie_plot"]=data_set[str(movie_id)]["movie_plot"]
						data_set_user[k][k1][k2]["imdbID"]=data_set[str(movie_id)]["imdbID"]
		json_a = json.dumps(data_set_user)
		file_name_new="user"+str(i)+".json"
		f = open(file_name_new,"w")
		f.write(json_a)
		f.close()
