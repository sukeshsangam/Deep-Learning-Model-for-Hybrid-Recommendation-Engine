import urllib.request, json
import re




for i in range(1,6041):
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
					movie_title=stringAfterReplace.replace(' ','+')
					print(movie_title)
					with urllib.request.urlopen("http://www.omdbapi.com/?t="+movie_title+"&apikey=706d084e") as url:
						data = json.loads(url.read().decode())
						try:
							print(data['Plot'])
						except:
							temp_check_str=", The"
							if temp_check_str in stringAfterReplace:
								movie_title_1=stringAfterReplace.replace(", The","")
								with urllib.request.urlopen("http://www.omdbapi.com/?t="+movie_title_1+"&apikey=706d084e") as url:
									data = json.loads(url.read().decode())
									print(data['Plot'])
 
'''
	
s = "Risky Business (1983)"
firstDelPos=s.find("(") # get the position of [
secondDelPos=s.find(")") # get the position of ]
stringAfterReplace = s.replace(s[firstDelPos:secondDelPos+1], "")

#t = re.sub('(.*?)', '', s)

if stringAfterReplace.endswith(' '):
    stringAfterReplace = stringAfterReplace[:-1]

print(stringAfterReplace.replace(' ','+'))
'''
