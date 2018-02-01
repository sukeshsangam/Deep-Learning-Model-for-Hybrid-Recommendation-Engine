import urllib.request, json
import re
import time
import os
for i in range(40,500):
	file_name="user"+str(i)+".json"
	with open(file_name) as json_data:
		data_set = json.load(json_data)
	for k in data_set:
		for k1 in data_set[k]:
			for k2 in data_set[k][k1]:
				movie_title=data_set[k][k1][k2]['movie_name']
				firstDelPos=movie_title.find("(") # get the position of [
				secondDelPos=movie_title.find(")") # get the position of ]
				stringAfterReplace = movie_title.replace(movie_title[firstDelPos:secondDelPos+1], "")
				if stringAfterReplace.endswith(' '):
					stringAfterReplace = stringAfterReplace[:-1]
					if ' - ' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace(' - ','-')
					if ' & ' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace(' & ','&')
					#print("before loop")
					#print(stringAfterReplace.find('U.S. '))
					if 'U.S. Marshalls' in stringAfterReplace:
						#print(stringAfterReplace.find('U.S. '))
						#exit(0)
						#print("hello")
						stringAfterReplace=stringAfterReplace.replace('U.S. Marshalls','Marshals')
					if 'Fistful of Dollars, A' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Fistful of Dollars, A','Fistful of Dollars')
					if 'Rosencrantz and Guildenstern Are Dead' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Rosencrantz and Guildenstern Are Dead','Rosencrantz&Guildenstern Are Dead')
					if ' and ' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace(' and ','&')
					if 'William Shakespeare\'s Romeo&Juliet' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('William Shakespeare\'s Romeo&Juliet','Romeo+Juliet')
					if 'Mission: Impossible 2' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Mission: Impossible 2','Mission: Impossible II')
					if 'Naked Gun 2 1/2: The Smell of Fear, The' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Naked Gun 2 1/2: The Smell of Fear, The','The Naked Gun 2: The Smell of Fear')
					if 'Monty Python\'s Life of Brian' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Monty Python\'s Life of Brian','Life of Brian')
					if 'Adventures of Buckaroo Bonzai Across the 8th Dimension, The' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Adventures of Buckaroo Bonzai Across the 8th Dimension, The','The Adventures of Buckaroo Banzai Across the 8th Dimension')
					if ', The' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace(', The','')
					if 'Navigator: A Mediaeval Odyssey' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Navigator: A Mediaeval Odyssey','The Navigator: A Medieval Odyssey')
					if 'Sesame Street Presents Follow That Bird' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Sesame Street Presents Follow That Bird','Follow That Bird')
					if '3 Ninjas: High Noon On Mega Mountain' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('3 Ninjas: High Noon On Mega Mountain','3 Ninjas: High Noon at Mega Mountain')
					if 'Highlander III: The Sorcerer' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Highlander III: The Sorcerer','Highlander: The Final Dimension')
					if 'Tales from the Crypt Presents: Bordello of Blood' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Tales from the Crypt Presents: Bordello of Blood','Bordello of Blood')
					if 'Nine 1/2 Weeks' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Nine 1/2 Weeks','9 Weeks')
					if 'Mouse Hunt' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Mouse Hunt','MouseHunt')
					if 'Friday the 13th Part 3: 3D' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Friday the 13th Part 3: 3D','Friday the 13th Part III')
					if 'Allan Quartermain&the Lost City of Gold' in stringAfterReplace:
						stringAfterReplace=stringAfterReplace.replace('Allan Quartermain&the Lost City of Gold','Allan Quatermain and the Lost City of Gold')
					movie_title=stringAfterReplace.replace(' ','%20')
					movie_title="http://www.omdbapi.com/?s="+movie_title+"&apikey=706d084e"
					#print(movie_title)
					if movie_title.find('é'):
						movie_title=movie_title.replace('é','e')
						#print(movie_title)
					if movie_title.find('³'):
						movie_title=movie_title.replace('³','%203')
						#print(movie_title)
					print(movie_title)
					with urllib.request.urlopen(movie_title) as url:
						data = json.loads(url.read().decode())
						#print(data)
						#time.sleep(2)
						data_search=data['Search']
						search_dic=data_search[0]
						id=search_dic['imdbID']
						data_link="http://www.omdbapi.com/?i="+id+"&apikey=706d084e"
						with urllib.request.urlopen(data_link) as url:
							data_plot = json.loads(url.read().decode())
							data_set[k][k1][k2]['movie_plot']=data_plot['Plot']
							data_set[k][k1][k2]['imdbID']=data_plot['Plot']
	json_a = json.dumps(data_set)
	path = "DataWithPlot/"
	file_name = os.path.join(path, file_name)
	#print(file_name)
	f = open('%s' % file_name,"w")
	f.write(json_a)
	f.close()
	print("User No.")
	print(i)