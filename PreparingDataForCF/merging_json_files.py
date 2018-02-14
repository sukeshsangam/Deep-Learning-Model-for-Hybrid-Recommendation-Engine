import json
head = []
file_list=[]
for i in range(1,17):
	temp="training_data_CF.json_"+str(i)+".json"
	file_list.append(temp)

with open("merging_files_result.json", "w") as outfile:
    for f in file_list:
        print(f)
        with open(f, 'r') as infile:
            file_data = json.load(infile)
            head += file_data
    json.dump(head, outfile)