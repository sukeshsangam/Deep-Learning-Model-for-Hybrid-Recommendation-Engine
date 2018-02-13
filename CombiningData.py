import json

combined_data=[]
for i in range(1,6041):
	file_name="DataWithPlot/user"+str(i)+".json"
	#print(file_name)
	with open(file_name) as json_data:
		data_set_user = json.load(json_data)
		#print(data_set_user[str(i)]["train"])
		for k in data_set_user[str(i)]["train"]:
			#print(data_set_user[str(i)]["train"][k])
			data_set_user[str(i)]["train"][k]["user_id"]=i
			#print(data_set_user[str(i)]["train"][k])
			combined_data.append(data_set_user[str(i)]["train"][k])
	print(i)
	#print(combined_data)
	#exit(0)
file_name_save="PreparingDataForCF/training_data_CF.json"
json_a = json.dumps(combined_data)
f = open(file_name_save,"w")
f.write(json_a)
f.close()      	
        
		