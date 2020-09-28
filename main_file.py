# @author: Md Amaan Haque

import sys
sys.path.append("/home/ubuntu/Files/Restaurant_Reviews/Restaurant-Reviews-Sentiment-Analysis")

import numpy as np
from numpy import array, amax, amin, sum
import pickle
from scipy.spatial.distance import cdist

from preprocess import clean
clean_obj = clean()

from embeddings import Embedding
Embedding_obj = Embedding()


# load the model from disk
filename = '/home/ubuntu/Files/Restaurant_Reviews/Restaurant-Reviews-Sentiment-Analysis/ML_model_trained_weights/naive_bayes_model.sav' # (Acc. 91.5 % but Less responce time ~220ms)
loaded_model = pickle.load(open(filename, 'rb'))

# Loading the list containing 1000x768 BERT embeddings 
filename_2 = '/home/ubuntu/Files/Restaurant_Reviews/Restaurant-Reviews-Sentiment-Analysis/Train_data_BERT_Embeddings/RR_Positive_Train_data_Bert_embeddings.sav'   
filename_3 = '/home/ubuntu/Files/Restaurant_Reviews/Restaurant-Reviews-Sentiment-Analysis/Train_data_BERT_Embeddings/RR_Negative_Train_data_Bert_embeddings.sav'   

RR_Positive_dataset_emd = pickle.load(open(filename_2, 'rb'))  
RR_Negative_dataset_emd = pickle.load(open(filename_3, 'rb'))  


class  Restaurant_Reviews:
	
	def predict(self, df):
		sample_data = df.iloc[0,:]
		print('The shape of Input_sample_data_embd_is: ', np.shape(sample_data))
		
		# sample data is a 'Series' format we need to change it to 'array' format, then only we can apply array.reshape() function
		sample_data_np  = np.array(sample_data)  
		sample_data_2d  = sample_data_np.reshape(1,-1)
		print('The shape of Sample_data_2d: ', np.shape(sample_data_2d))
		#sample_data_2d_T = np.transpose(sample_data_2d) 
        
		
		# For positive train RR dataset 500 samples
		cosine_dist_pos = []
		for i_emd_p in RR_Positive_dataset_emd:
			score_matrix_p = cdist(sample_data_2d, i_emd_p, 'cosine')
			score_matrix_p = 1 - score_matrix_p
			cosine_dist_pos.append(score_matrix_p)
		    
		#filename_p = 'cosine_distances_positive_review.sav'
		#pickle.dump(cosine_dist_pos, open(filename_p, 'wb'))
		
		
		# For Negative train RR dataset 500 samples
		cosine_dist_neg = []
		for i_emd_n in RR_Negative_dataset_emd:
			score_matrix_n = cdist(sample_data_2d, i_emd_n, 'cosine')
			score_matrix_n = 1 - score_matrix_n
			cosine_dist_neg.append(score_matrix_n)
		    
		#filename_n = 'cosine_distances_negative_review.sav'
		#pickle.dump(cosine_dist_neg, open(filename_n, 'wb'))
		
		
		# Adding calculations to detect illogical reviews
		sum_pos = sum(cosine_dist_pos)
		sum_neg = sum(cosine_dist_neg)
		mean_pos = np.mean(cosine_dist_pos)
		mean_neg = np.mean(cosine_dist_neg)
		
		
		classifier = loaded_model
		result = classifier.predict(sample_data_2d)   # result will be either 0 or 1
		
		result_dict = {}
		
		# CONDITION FOR ILLOGICAL COMMENTS:  Based on experimentation, IF any one of the sum > 180.0 AND any one of the mean > 0.30 THEN proceed normally
		if((sum_pos>180 or sum_neg>180) and (mean_pos>0.30 or mean_neg>0.30)):
			if(result == 1):
				result_dict['result'] = 'Wow! its a Positive Review'
			elif(result == 0):
				result_dict['result'] = 'Oops.. its a Negative Review'
		else:
			result_dict['result'] = 'Please write proper reviews, related to your Restaurant experience'
			
		return result_dict
        	
		

	def main(self, request_data):  # 'request_data' (dict_format) comes from server.py
		# request_data = {"input_data": "It was okay"}
		# processed_data becomes a dictionary containing corresponding 'value' as a list containg a single sentence
		processed_data = clean_obj.main(request_data)  # sending 'request_data' to 'preprocess.py'  
		# processed_data = {"input_data": ["It was okay"]}
		print('processed_data is :', processed_data) 
		for key, value in processed_data.items():
			# Here extracting the input sentence from the processed_data dict and storing in 'sentence' variable
			sentence = processed_data[key]  # processed_data = {"input_data": ["It was okay"]}
			print('sentence is :', sentence) # sentence = ["It was okay"]
			
		# df is a 2D embedding matrix of input sample  
		df = Embedding_obj.get_embeddings(sentence) # 'sentence' is a single list containg one input text sample
		
		return self.predict(df)
	
	
