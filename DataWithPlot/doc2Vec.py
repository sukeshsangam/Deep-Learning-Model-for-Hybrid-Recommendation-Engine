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

data=[]
data_label=[]
liked=[]
class DocIterator(object):
    def __init__(self, doc_list, labels_list):
        self.labels_list = labels_list
        self.doc_list = doc_list
		
    def __iter__(self):
        for idx, doc in enumerate(self.doc_list):
            # print 'creating tagged document...%d' % idx
            yield TaggedDocument(words=doc.split(), tags=[self.labels_list[idx]])
			

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
			
			
			#print(data_set_user)
			#exit(0)
			for k in data_set_user:
				#for k1 in data_set_user[k]:
				##print(data_set_user[k]["train"])
				for k2 in data_set_user[k]["train"]:
					#for k3 in data_set_user[k]["train"][k2]:
					movie_id=data_set_user[k]["train"][k2]['movie_id']
					data_label.append("movie_id"+str(movie_id))
					movie_plot=data_set_user[k]["train"][k2]['movie_plot']
					rating=data_set_user[k]["train"][k2]['rating']
					if rating>3:
						liked.append(1)
					else:
						liked.append(0)
					data.append(movie_plot)
		print(data)
		print(data_label)
		print(liked)
		iterator = DocIterator(data, data_label)
		#pri
		model = gensim.models.Doc2Vec(size=300, window=10, min_count=5, workers=4, alpha=0.025, min_alpha=0.025)
		model.build_vocab(iterator)

		print("done building vocabulary")
		print ("start training the model")

		for epoch in range(10):
			#print 'epcho %d..' % (epoch+1)
			model.train(iterator, total_examples=model.corpus_count,epochs=model.iter)
			model.alpha -= 0.002
			model.min_alpha = model.alpha
			model.train(iterator, total_examples=model.corpus_count,epochs=model.iter)
		model.save("doc2vec.model")
		doc_vectors=[]
		y=[]
		for i in data_label:
			doc_vectors.append(model.docvecs[i])
		for i in liked:
			y.append(liked[i])
		#model.save("doc2vec.model")
		clf = RandomForestClassifier()
		clf.fit(doc_vectors, y)
		print(cross_validation.LeaveOneOut(doc_vectors))
		exit(0)
		
	



		