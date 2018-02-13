import json
import pandas as pd
import numpy as np
import math
import copy
from operator import mul
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from joblib import Parallel, delayed
import multiprocessing
num_cores = multiprocessing.cpu_count()


def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

data=pd.read_json('PreparingDataForCF/training_data_CF.json',orient='records')
Mean=data.groupby(['user_id'],as_index=False,sort=False).mean().rename(columns={'rating':'rating_mean'})[['user_id','rating_mean']]
Ratings=pd.merge(data,Mean,on='user_id',how='left',sort=False)
Ratings['rating_adjusted']=Ratings['rating']-Ratings['rating_mean']

rp=Ratings.pivot_table(columns=['movie_id'],index=['user_id'],values='rating_adjusted')
rp=rp.fillna(0)
#print(rp.head())
#print(rp[6][5])
def default(o):
	if isinstance(o,np.integer):return int(o)
	raise TypeError


for i in range(46,6041):
#inputs = range(1,6041)
#def example_multiprocessing(it):
	user_dic=[]
	a=Ratings.loc[Ratings['user_id']==i]["movie_id"]
	a_list=list(a)
		
	for item in a_list:
		temp_a_list=[]
		temp_a_list=a_list[:]
		temp_a_list.remove(item)
		correlation_coeff={}
		temp_attach={}
		for j in range(1,6041):
			if i==j:
				continue
			b=Ratings.loc[Ratings['user_id']==j]['movie_id']
			b_list=list(b)
			temp=intersect(temp_a_list,b_list)

			check=Ratings.loc[Ratings['user_id']==j]['movie_id']
			check_list=list(check)
			#print(check)
			##print(check_list)
			#exit(0)
			if len(temp)>=10 and item in check_list:

				user_1=copy.deepcopy(rp[i-1:i])
				user_1[item][i]=0
				user_2=copy.deepcopy(rp[j-1:j])
				multiplier_1=user_1.values.tolist()[0][:]
				multiplier_2=user_2.values.tolist()[0][:]
				#print(multiplier_1)
				#print(multiplier_2)
				#exit(0)
				output_list_multiplication=list(map(mul,user_1.values.tolist()[0],user_2.values.tolist()[0]))
				numerator=sum(output_list_multiplication)
				denom_1=np.square(multiplier_1)
				sum_denom_1=np.sum(denom_1)
				denom_part_1=math.sqrt(sum_denom_1)
				denom_2=np.square(multiplier_2)
				sum_denom_2=np.sum(denom_2)
				denom_part_2=math.sqrt(sum_denom_2)
				#print(denom_part_1)
				#print(denom_part_2)
				#exit(0)
				if denom_part_2==0:
					#print(user_1)
					#print(user_2)
					#exit(0)
					correlation_coeff[j]=0
				else:
					denominator=denom_part_1*denom_part_2
				
					correlation_coeff[j]=numerator/denominator
		correlation_coeff_sorted_keys = sorted(correlation_coeff, key=correlation_coeff.get, reverse=True)
		#print(correlation_coeff_sorted_keys)
		#print(len(correlation_coeff_sorted_keys))
		#exit(0)
		#print(type(Ratings.loc[Ratings['user_id']==i]["rating_mean"]))
		avg_i=Ratings.loc[Ratings['user_id']==i]["rating_mean"].iloc[0]
		#print(avg_i)
		#exit(0)
		cal_numerator_rating=0
		cal_denominator_rating=0
		if len(correlation_coeff_sorted_keys)<30:
			iterator=len(correlation_coeff_sorted_keys)
		else:
			iterator=30
		#print(iterator)
		#exit(0)
		for u in range(0,iterator):
			user_id_p=correlation_coeff_sorted_keys[u]
			rating_id_p=rp[item][user_id_p]
			#print(rating_id_p)
			coeff=correlation_coeff[user_id_p]
			cal_numerator_rating=cal_numerator_rating+coeff*(rating_id_p)
			cal_denominator_rating=cal_denominator_rating+coeff
		predicted_rating=0
		if cal_denominator_rating>0:
			predicted_rating=avg_i+(cal_numerator_rating/cal_denominator_rating)
		else:
			predicted_rating=avg_i
		#print(predicted_rating)
		probability_like=0
		probability_like=round(predicted_rating*1/6,1)
		if predicted_rating>3:
			predicted_liked=1
		else:
			predicted_liked=0
		#original_rating=rp[item][i]
		original_rating_pd=pd.DataFrame()
		original_rating_pd=Ratings.loc[Ratings['user_id']==i]
		original_rating=list(original_rating_pd.loc[original_rating_pd['movie_id']==item]['rating'])
		#print(type(original_rating))
		#print(original_rating)
		#exit(0)
		if original_rating[0]>3:
			original_liked=1
		else:
			original_liked=0
		#user_id_append=i
		#movie_id_append=item
		array_1=[]
		array_2=[]
		array_1.append(original_liked)
		array_2.append(predicted_liked)
		acc=0
		acc=accuracy_score(array_1,array_2)
		#print(acc)
		pres=0
		pres=precision_score(array_1,array_2)
		#print(pres)
		recall=0
		recall=recall_score(array_1,array_2)
		#print(recall)
		temp_attach["Probability_like"]=probability_like
		temp_attach["pres"]=pres
		temp_attach["recall"]=recall
		temp_attach["actual_value"]=original_liked
		temp_attach["acc"]=acc
		temp_attach["movie_id"]=item
		user_dic.append(temp_attach)
		#print(user_dic)
	file_name_save="OutputOfCollaborativeFiltering/user_output"+str(i)+".json"
	json_a = json.dumps(user_dic,default=default)
	f = open(file_name_save,"w")
	f.write(json_a)
	f.close()
	print(i)
	#exit(0)
#Parallel(n_jobs=3)(delayed(example_multiprocessing)(dude) for dude in inputs)
