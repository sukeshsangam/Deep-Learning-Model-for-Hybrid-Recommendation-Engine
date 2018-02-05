import os
from os import listdir
from os.path import isfile, join
from gensim import models
from gensim.models.doc2vec import TaggedDocument
import gensim
import urllib.request, json
import re
import time
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn import ensemble, cross_validation, datasets
from sklearn.model_selection import LeaveOneOut
from collections import OrderedDict
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score


class DocIterator(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list
		
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            # print 'creating tagged document...%d' % idx
            yield TaggedDocument(words=doc.split(), tags=[self.labels_list[idx]])
			

with open("DataWithPlot/final_cleaned_movies.json") as json_data:
	data_set = json.load(json_data, object_pairs_hook=OrderedDict)
	#print(data_set["1"])
	for i in range(1,6041):
		file_name="DataWithPlot/user"+str(i)+".json"
		#print(file_name)
		with open(file_name) as json_data:
			data_set_user = json.load(json_data,object_pairs_hook=OrderedDict)
			#print(data_set_user)
			#exit(0)
			
			
			#print(data_set_user)
			#exit(0)
			data=[]
			data_label=[]
			liked=[]
			temp_movie_id=[]
			for k in data_set_user:
				#for k1 in data_set_user[k]:
				##print(data_set_user[k]["train"])
				for k2 in data_set_user[k]["train"]:
					#for k3 in data_set_user[k]["train"][k2]:
					movie_id=data_set_user[k]["train"][k2]['movie_id']
					temp_movie_id.append(movie_id)
					data_label.append("movie_id"+str(movie_id))
					
					movie_plot=data_set_user[k]["train"][k2]['movie_plot']
					rating=data_set_user[k]["train"][k2]['rating']
					if rating>3:
						liked.append(1)
					else:
						liked.append(0)
					data.append(movie_plot)
		#print(data)
		#print(data_label)
		#print(liked)
		iterator = DocIterator(data, data_label)
		#pri
		model = gensim.models.Doc2Vec(size=300, window=10, min_count=5, workers=4, alpha=0.025, min_alpha=0.025)
		model.build_vocab(iterator)

		#print("done building vocabulary")
		#print ("start training the model")

		for epoch in range(10):
			#print 'epcho %d..' % (epoch+1)
			model.train(iterator, total_examples=model.corpus_count,epochs=model.iter)
			model.alpha -= 0.002
			model.min_alpha = model.alpha
			model.train(iterator, total_examples=model.corpus_count,epochs=model.iter)
		model.save("doc2vec.model")
		doc_vectors=[]
		y=[]
		#print(liked)
		for l in data_label:
			doc_vectors.append(model.docvecs[l])
			#print(i)
		#exit(0)
		for j in liked:
			y.append(j)
		#print("length of y")
		#print(len(y))
		#model.save("doc2vec.model")
		#print(data_label)
		#print(y)
		#exit(0)
		#clf = RandomForestClassifier()
		#clf.fit(doc_vectors, y)
		#y_pred=[]
		#pred=clf.predict(doc_vectors)
		#for i in pred:
		#	y_pred.append(i)
			
		#print(y_pred)
		loo = LeaveOneOut()
		loo.get_n_splits(doc_vectors)
		user_dic=[]
		for train_index, test_index in loo.split(doc_vectors):
			#print("TRAIN:", train_index,"TEST:", test_index)
			rf=RandomForestClassifier()
			temp_x=[]
			temp_y=[]
			temp_x_test=[]
			temp_y_test=[]
			temp_x=doc_vectors[:]
			temp_y=y[:]
			#print(doc_vectors[0])
			#exit(0)
			#print(test_index[0])
			temp_XX=doc_vectors[test_index[0]]
			temp_YY=y[test_index[0]]
			temp_x_test.append(temp_XX)
			temp_y_test.append(temp_YY)
			temp_x.pop(test_index[0])
			temp_y.pop(test_index[0])
			#print("lenght of x")
			#print(len(temp_x))
			#print("lenght of y")
			#print(len(temp_y))
			#print("length of the movie id's")
			#print(len(temp_movie_id))
			#print("lenght of data labels")
			#print(len(data_label))
			rf.fit(temp_x,temp_y)
			
			y_probability=rf.predict_proba(temp_x_test)
			y_test_pre=rf.predict(temp_x_test)
			#print(file_name)
			#print(temp_y)
			#print(y_probability)
			#print(y_test_pre)
			
			#print(temp_y_test)
			#print(y)
			#print("-----------------------------------------")
			acc=accuracy_score(temp_y_test,y_test_pre)
			#print("hello")
			pres=precision_score(temp_y_test, y_test_pre)
			#print("hello")
			recall=recall_score(temp_y_test, y_test_pre)
			#print("-----------------------------------------")
			temp_dic={}
			#print(temp_movie_id)
			#print(test_index)
			temp_dic["movie_id"]=temp_movie_id[test_index[0]]
			temp_dic["acc"]=acc
			temp_dic["pres"]=pres
			temp_dic["recall"]=recall
			temp_dic["actual_value"]=temp_y_test[0]
			try:
				temp_dic["Probability_like"]=y_probability[0][1]
			except:
				if file_name=="DataWithPlot/user20.json":
					temp_dic["Probability_like"]=y_probability[0][0]
					continue
			user_dic.append(temp_dic)
			#print(temp_dic)
		file_name_save="OutputOfContentBasedModel/user_output"+str(i)+".json"
		json_a = json.dumps(user_dic)
		f = open(file_name_save,"w")
		f.write(json_a)
		f.close()
			
		#exit(0)
		#print(cross_validation.LeaveOneOut(doc_vectors))
		#exit(0)
		
	



		