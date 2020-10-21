import re

class clean:
	
	def clean_text(self, review):  # 'str' type 'value' will input as 'review'
		corpus = [] # corpus=["It was okay"]
		review = re.sub('[^a-zA-Z0-9]', ' ', review)
		review = review.lower()
		review = re.sub(' +', ' ', review)
		review = review.strip()
		corpus.append(review)
		
		return corpus		# 'corpus' is a list containing string 'review'       # corpus=["It was okay"]
		
		
	
	
	
	
	def main(self, data):
		# data = {"input_data": "It was okay"}
		# data is a dictionary here as the data comes in a JSON format from main_file.py
		processed_data = {}
		for key,value in data.items():
			processed_data[key] = self.clean_text(value) # processed_data becomes a dictionary containing corresponding 'values' as 'corpus' (list type)
		
		return processed_data # processed_data = {"input_data": ["It was okay"]}
