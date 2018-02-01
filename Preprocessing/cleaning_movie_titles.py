import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib.request, json
import re
import time
import os

movies_headers = ['movie_id', 'movie_name', 'Genre']
movies = pd.read_table('movies.dat', sep='::', header=None, names=movies_headers)

#for i in range(29,3952):
data_set_dic_movie={}
#movies_data=movies.loc[movies['movie_id'] == i]
for index,row in movies.iterrows():
	#if index<3779:
	#	continue
	dataset_dic_movie={}
	movie_title=row['movie_name']
	#print(movies_data)
	#if(index>1260):
	#	exit(0)
	print(movie_title)
	if "M (1931)" in movie_title:
		print(row['movie_id'])
		print("hello")
		exit(0)
		data_link="http://www.omdbapi.com/?i="+"tt0022100"+"&apikey=706d084e"
		with urllib.request.urlopen(data_link) as url:
			data_plot = json.loads(url.read().decode())
			dataset_dic_movie['movie_id']=row['movie_id']
			dataset_dic_movie['movie_name']=row['movie_name']
			dataset_dic_movie['Genre']=row['Genre']
			dataset_dic_movie['imdbID']="tt0022100"
			dataset_dic_movie['movie_plot']=data_plot['Plot']
			continue
	firstDelPos=movie_title.find("(")
	secondDelPos=movie_title.find(")") 
	stringAfterReplace = movie_title.replace(movie_title[firstDelPos:secondDelPos+1], "")
	firstDelPos=stringAfterReplace.find("(")
	secondDelPos=stringAfterReplace.find(")") 
	stringAfterReplace = stringAfterReplace.replace(stringAfterReplace[firstDelPos:secondDelPos+1], "")
	#print(stringAfterReplace)
	#exit(0)
	if stringAfterReplace.endswith(' '):
		stringAfterReplace = stringAfterReplace[:-1]
	if ' - ' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace(' - ','-')
	if ' & ' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace(' & ','&')
	if 'U.S. Marshalls' in stringAfterReplace:
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
	if 'Shanghai Triad  (1995)' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace('Shanghai Triad  (1995)','Shanghai Triad')
	if 'Seven  (1995)' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace('Seven  (1995)','Se7en')
	if 'Postino, Il  (1994)' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace('Postino, Il  (1994)','Postino')
	if 'Confessional  (1995)' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace('Confessional  (1995)','Confessional')
	if 'French Twist  (1995)' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace('French Twist  (1995)','French Twist')
	if 'White Balloon ' in stringAfterReplace:
		stringAfterReplace.replace('White Balloon ','White Balloon')
	
	
	if ', The' in stringAfterReplace:
		stringAfterReplace.replace(', The','')
	
	if movie_title.endswith(' '):
		movie_title = movie_title[:-1]
	#print(movie_title)
	#exit(0)
	if 'Silence of the Palace' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace('Silence of the Palace','The Silences of the Palace')
	if 'Farinelli: il castrato' in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace('Farinelli: il castrato','Farinelli')
	if "Enfer, L'" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Enfer, L'","L'Enfer")
	if "National Lampoon's Senior Trip" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("National Lampoon's Senior Trip","Senior%20Trip")
	if "Tales From the Crypt Presents: Demon Knight" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Tales From the Crypt Presents: Demon Knight","Tales from the Crypt: Demon Knight")
	if "Wes Craven's New Nightmare" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Wes Craven's New Nightmare","New Nightmare")
	if "Robert A. Heinlein's The Puppet Masters" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Robert A. Heinlein's The Puppet Masters","The Puppet Masters")
	if "Hour of the Pig" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Hour of the Pig","The%20Advocate&y=1993")
	if "Wooden Man's Bride" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Wooden Man's Bride","Wu Kui")
	if "Asfour Stah" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Asfour Stah","Halfaouine: Boy of the Terraces")
	if "Und keiner weint mir nach" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Und keiner weint mir nach","And Nobody Weeps for Me")
	if "Mutters Courage" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Mutters Courage","My Mother's Courage")
	if "Eye of Vichy" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Eye of Vichy","L'oeil de Vichy")
	if "Under the Domin Tree" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Under the Domin Tree","Under the Domim Tree")
	if "Institute Benjamenta, or This Dream People Call Human Life" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Institute Benjamenta, or This Dream People Call Human Life","Institute Benjamenta, or This Dream That One Calls Human Life")
	if "Gate of Heavenly Peace" in stringAfterReplace:
		data_link="http://www.omdbapi.com/?i="+"tt0113147"+"&apikey=706d084e"
		with urllib.request.urlopen(data_link) as url:
			data_plot = json.loads(url.read().decode())
			dataset_dic_movie['movie_id']=row['movie_id']
			dataset_dic_movie['movie_name']=row['movie_name']
			dataset_dic_movie['Genre']=row['Genre']
			dataset_dic_movie['imdbID']="tt0113147"
			dataset_dic_movie['movie_plot']=data_plot['Plot']
			continue
	if "Bewegte Mann, Der" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Bewegte Mann, Der","Maybe... Maybe Not")
	if "Echte Kerle" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Echte Kerle","Regular Guys")
	if "Story of Xinghua" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Story of Xinghua","Xinghua san yue tian")
	if "Day the Sun Turned Cold" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Day the Sun Turned Cold","Tian guo ni zi")
	if "Aiqing wansui" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Aiqing wansui","Vive L'Amour")
	if "Police Story 4: Project S" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Police Story 4: Project S","Once a Cop")
	if "In the Line of Duty 2" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("In the Line of Duty 2","In the Line of Duty: The Price of Vengeance")
	if "Schlafes Bruder" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Schlafes Bruder","Brother of Sleep")
	if "Woman in Question" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Woman in Question","Five Angles on Murder")
	if "Sexual Life of the Belgians" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Sexual Life of the Belgians","The Sex Life of the Belgians")
	if "Children of the Corn IV: The Gathering" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Children of the Corn IV: The Gathering","Children of the Corn: The Gathering")
	if "Tashunga" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Tashunga","North Star")
	if "Charm's Incidents" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Charm's Incidents","Charms Zwischenfalle")
	if "JLG/JLG-autoportrait de décembre" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("JLG/JLG-autoportrait de décembre","JLG/JLG: Self-Portrait in December")
	if "Symphonie pastorale, La" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Symphonie pastorale, La","Pastoral Symphony")
	if "Amityville 1992: It's About Time" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Amityville 1992: It's About Time","Amityville: It's About Time")
	if "Nosferatu a Venezia" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Nosferatu a Venezia","Vampire in Venice")
	if "Garden of Finzi-Contini" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Garden of Finzi-Contini","The Garden of the Finzi-Continis")
	if "Forbidden Christ" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Forbidden Christ","Strange Deception")
	if "Forbidden Christ" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Forbidden Christ","Strange Deception")
	if "Salut cousin!" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Salut cousin!","Hi Cousin!")
	if "Jungle2Jungle" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Jungle2Jungle","Jungle 2 Jungle")
	if "To Have, or Not" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("To Have, or Not","To Have and Have Not")
	if "Swept from the Sea" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Swept from the Sea","Amy Foster")
	if "Nénette et Boni" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Nénette et Boni","Nenette and Boni")
	if "My Life in Pink" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("My Life in Pink","Ma Vie en Rose")
	if "Duoluo tianshi" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Duoluo tianshi","Fallen Angels")
	if "Mat' i syn" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Mat' i syn","Mother and Son")
	if "Further Gesture, A" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Further Gesture, A","The Break&y=1997")
	if "Callejón de los milagros, El" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Callejón de los milagros, El","Midaq Alley")
	if "Hana-bi" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Hana-bi","Fireworks")
	if "Marie Baie Des Anges" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Marie Baie Des Anges","Marie from the Bay of Angels")
	if "Life of Émile Zola" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Life of Émile Zola","The Life of Emile Zola")
	if "Nightmare on Elm Street Part 2: Freddy's Revenge, A" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Nightmare on Elm Street Part 2: Freddy's Revenge, A","A Nightmare on Elm Street 2: Freddy's Revenge")
	if "Halloween 5: The Revenge of Michael Myers" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Halloween 5: The Revenge of Michael Myers","Halloween 5")
	if "Hello Mary Lou: Prom Night II" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Hello Mary Lou: Prom Night II","Prom Night II")
	if "This Worldn the Fireworks" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("This Worldn the Fireworks","This World, Then the Fireworks")
	if "Seven Samurai   (1954)" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Seven Samurai   (1954)","Seven Samurai")
	if "$1,000,000 Duck" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("$1,000,000 Duck","The Million Dollar Duck")
	if "Saltmen of Tibet" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Saltmen of Tibet","Die Salzmanner von Tibet")
	if "Henry: Portrait of a Serial Killer, Part 2" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Henry: Portrait of a Serial Killer, Part 2","Henry II: Portrait of a Serial Killer")
	if "Déjà Vu" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Déjà Vu","Deja Vu")
	if "Waltzes from Vienna" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Waltzes from Vienna","Strauss' Great Waltz")
	if "Number Seventeen" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Number Seventeen","Number 17")
	if "Master Ninja I" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Master Ninja I","The Master")
	if "Jerry Springer: Ringmaster" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Jerry Springer: Ringmaster","Ringmaster")
	if "24 7: Twenty Four Seven" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("24 7: Twenty Four Seven","TwentyFourSeven")
	if "Gate II: Trespassers" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Gate II: Trespassers","Gate 2: The Trespassers")
	if "Mighty Peking Man" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Mighty Peking Man","Goliathon")
	if "Nô" in stringAfterReplace:
		data_link="http://www.omdbapi.com/?i="+"tt0128370"+"&apikey=706d084e"
		with urllib.request.urlopen(data_link) as url:
			data_plot = json.loads(url.read().decode())
			dataset_dic_movie['movie_id']=row['movie_id']
			dataset_dic_movie['movie_name']=row['movie_name']
			dataset_dic_movie['Genre']=row['Genre']
			dataset_dic_movie['imdbID']="tt0128370"
			dataset_dic_movie['movie_plot']=data_plot['Plot']
			continue
	if "Dinner Game" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Dinner Game","Le Diner de Cons")
	if "Autumn Tale, An" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Autumn Tale, An","Autumn Tale")
	if "Marcello Mastroianni: I Remember Yes, I Remember" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Marcello Mastroianni: I Remember Yes, I Remember","Marcello Mastroianni: I Remember")
	if "Fright Night Part II" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Fright Night Part II","Fright Night Part 2")
	if "Ennui, L'" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Ennui, L'","L'ennui")
	if "Love Bewitched, A" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Love Bewitched, A","El amor brujo")
	if "March of the Wooden Soldiers" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("March of the Wooden Soldiers","Babes in Toyland")
	if "Spring Fever USA" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Spring Fever USA","Lauderdale")
	if "I'll Never Forget What's 'is Name" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("I'll Never Forget What's 'is Name","I'll Never Forget What's'isname")
	if "Carriers Are Waiting" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Carriers Are Waiting","Les convoyeurs attendent")
	if "Two Moon Juction" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Two Moon Juction","Two Moon Junction")
	if "G. I. Blues" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("G. I. Blues","G.I. Blues")
	if "Puppet Master 5: The Final Chapter" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Puppet Master 5: The Final Chapter","Puppet Master 5")
	if "Retro Puppetmaster" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Retro Puppetmaster","Retro Puppet Master")
	if "Daughter of Dr. Jeckyll" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Daughter of Dr. Jeckyll","Daughter of Dr. Jekyll")
	if "Wisdom of Crocodiles" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Wisdom of Crocodiles","Immortality")
	if "Make Them Die Slowly" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Make Them Die Slowly","Cannibal Ferox")
	if "Whatever Happened to Aunt Alice?" in stringAfterReplace:
		stringAfterReplace=stringAfterReplace.replace("Whatever Happened to Aunt Alice?","What Ever Happened to Aunt Alice?")

	movie_title=stringAfterReplace.replace(' ','%20')
	if movie_title.endswith('%20'):
		movie_title = movie_title[:-3]
	#print(movie_title)
	#exit(0)
	
	movie_title="http://www.omdbapi.com/?s="+movie_title+"&apikey=706d084e"
	print(movie_title)
	if movie_title.find('é'):
		movie_title=movie_title.replace('é','e')
		#print(movie_title)
	if movie_title.find('³'):
		movie_title=movie_title.replace('³','%203')
		#print(movie_title)
	#print(movie_title)
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
			dataset_dic_movie['movie_id']=row['movie_id']
			dataset_dic_movie['movie_name']=row['movie_name']
			dataset_dic_movie['Genre']=row['Genre']
			dataset_dic_movie['imdbID']=id
			dataset_dic_movie['movie_plot']=data_plot['Plot']
		print("movie id")
		print(index)
	data_set_dic_movie[row['movie_id']]=dataset_dic_movie
json_a = json.dumps(data_set_dic_movie,sort_keys=False )
path = "DataWithPlot/"
file_name_final = "final_cleaned_movies"
file_name_final = os.path.join(path, file_name_final)
#print(file_name)
f = open('%s' % file_name_final,"w")
f.write(json_a)
f.close()
#print("movie No.")
#print(i)
exit(0)	