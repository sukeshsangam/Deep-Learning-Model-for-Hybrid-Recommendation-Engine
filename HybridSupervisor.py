from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD, Adam
import numpy as np
import json
import pickle
from keras.models import model_from_json
import os

from keras.utils.np_utils import to_categorical

for i in range(1,46):
	data_cb=json.load(open("OutputOfContentBasedModel/user_output"+str(i)+".json"))
	data_cf=json.load(open("OutputOfCollaborativeFiltering/user_output"+str(i)+".json"))
	#print(data_cb)
	#print(data_cf)
	#exit(0)
	X=[]
	Y=[]
	for d in data_cb:
		movie_id=d["movie_id"]
		for d1 in data_cf:
			if movie_id==d1["movie_id"]:
				temp=[]
				temp.append(d["Probability_like"])
				temp.append(d["pres"])
				temp.append(d["acc"])
				temp.append(d["recall"])
				temp.append(d1["Probability_like"])
				temp.append(d1["pres"])
				temp.append(d1["acc"])
				temp.append(d1["recall"])
				X.append(temp)
				if d["actual_value"]==d1["actual_value"]:
					Y.append(d["actual_value"])
				break
	X1_d=np.array(X)
	Y1_d_i=np.array(Y)
	Y1_d=to_categorical(Y1_d_i)
	#print(X1_d)
	#print(Y1_d)
	#print(Y1_d_i)
	model = Sequential()
	model.add(Dense(8, input_shape=(8,), activation='relu'))
	model.add(Dense(3, activation='relu'))
	model.add(Dense(2, activation='softmax'))
	model.compile(Adam(lr=0.05),loss='categorical_crossentropy',metrics=['accuracy'])
	model.fit(X1_d, Y1_d, epochs=20, verbose=2, validation_split=0.1)
	filename_json = "HybridModels/user_model_"+str(i)+".json"
	filename_h5 = "HybridModels/user_model_"+str(i)+".h5"
	scores = model.evaluate(X1_d, Y1_d, verbose=0)
	print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	model_json = model.to_json()
	with open(filename_json, "w") as json_file:
		json_file.write(model_json)
	model.save_weights(filename_h5)
	print("Saved model to disk")
	json_file = open(filename_json, 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	# load weights into new model
	loaded_model.load_weights(filename_h5)
	
	
	print("Loaded model from disk")
	
	# evaluate loaded model on test data
	loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
	score = loaded_model.evaluate(X1_d, Y1_d, verbose=0)
	print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
	#pickle.dump(model, open(filename, 'wb'))
	
	#exit(0)
	