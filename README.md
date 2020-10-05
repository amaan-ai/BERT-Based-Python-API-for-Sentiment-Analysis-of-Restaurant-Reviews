# Restaurant-Reviews-Sentiment-Analysis
<a id="top"></a>
## Table of contents
* <a href="#motivation">Motivation</a>
* <a href="#technologies_&_framework">Technologies & Framework</a>
* <a href="#illustrations">Illustrations</a>
* <a href="#setup-&-installation">Setup & Installation</a>

<a id="motivation"></a>
## Motivation 

* Almost all restaurants have review system to take input from their customers about food and services. Here, a customer either writes about their experience or gives star ratings.
* In general, textual data hold crucial information about customer experience, even causality for star ratings. 
Currently, there isn't any system to validate the reviews i.e. whether a customer is writing proper reviews related to their restaurant experience.
* For example, I can write anything rubbish which is not related to my restaurant experience *(for instance, "xyz", "qwertyjafjwebfliu", "I like to play cricket")* and can submit my review. This limits a restaurants ability to focus on their areas of improvement.
* This project nudges customers to write relevant reviews using **_Natural Language Processing_** and **_Machine Learning_** with end-to-end API call using _Flask_ & _Python_.
* Furthermore, it classifies the reviews into _Positive_, _Negative_ & _Irrelevant_ reviews. Thus, helping restaurants to get insights on customer experience.

<a id="technologies_&_framework"></a>
## Technologies & Framework  
This Project is created with:
* Python3.7 
* BERT
* Machine Learning
* Flask
* Postman

<a id="illustrations"></a>
## Illustrations  
* Below are the three images (Fig. 1, Fig. 2, Fig. 3) for three different categories of user input namely, Positive, Negative & Irrelevant review. 
* The input data is taken in JSON format with _"input_data"_ as key.
* Similarly the corresponding output is shown in JSON format with _"result"_ as key

<p align="center">
  <img src="https://github.com/amaan-ai/Restaurant-Reviews-Sentiment-Analysis/blob/master/images/Positive_review.png" alt="Positive Review Sample API"  width="700" height="400"/>
  <br>
  <em>Fig. 1: Positive Review Sample API</em>
</p>
<br>
<br>
<p align="center">
  <img src="https://github.com/amaan-ai/Restaurant-Reviews-Sentiment-Analysis/blob/master/images/Negative_review.png" alt="Negative Review Sample API"  width="700" height="400"/>
  <br>
  <em>Fig. 2: Negative Review Sample API</em>
</p>
<br>
<br>
<p align="center">
  <img src="https://github.com/amaan-ai/Restaurant-Reviews-Sentiment-Analysis/blob/master/images/Irrelevant_review.png" alt="Irrelevant Review Sample API"  width="700" height="400"/>
  <br>
  <em>Fig. 3: Irrelevant Review Sample API</em>
</p>


<a id="setup-&-installation"></a>
## Setup & Installation (For Ubuntu)  <a id="setup-&-installation"></a>
To run this project, you first need to clone this repository in your local system then follow the below mentioned steps:
#### Step 1
* Create a virtual environment using python3 and activate it: 
  ```
  $ sudo apt-get install python3-venv
  $ python3 -m venv proj_env
  $ source proj_env/bin/activate
  ```
  (Here, 'proj_env' is custom, you can change it as per your choice)<br>
  You can visit this <a href="https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/">link</a> for more information on virtual environment installation.
  
#### Step 2
* Install the sentence-transformers with pip:
  ```
  (proj_env)$ pip install -U sentence-transformers
  ```
  Alternatively, you can visit this <a href="https://pypi.org/project/sentence-transformers/">sentence-transformers</a> link for more information.
  
#### Step 3
* Export **PYTHONPATH** to the cloned directory address:
  ```
  (proj_env)$ export PYTHONPATH="<your_custom_path>/Restaurant-Reviews-Sentiment-Analysis"
  ```
  (Here, <your_custom_path> is the address where the Restaurant-Reviews-Sentiment-Analysis repository has been cloned)
  
* You need to change the PATH in two _.py_ files namely : _main_file.py_ &  _server.py_ . I will update the _config file_ for changing PATH without any difficulty in the next update.  
  ```
  In main_file.py:
    (line 4) : sys.path.append(<your_custom_path>/Restaurant-Reviews-Sentiment-Analysis)
    (line 19): filename   = <your_custom_path>/Restaurant-Reviews-Sentiment-Analysis/Train_data_BERT_Embeddings/RR_Positive_Train_data_Bert_embeddings.sav
    (line 23): filename_2 = <your_custom_path>/Restaurant-Reviews-Sentiment-Analysis/Train_data_BERT_Embeddings/RR_Positive_Train_data_Bert_embeddings.sav
    (line 24): filename_3 = <your_custom_path>/Restaurant-Reviews-Sentiment-Analysis/Train_data_BERT_Embeddings/RR_Negative_Train_data_Bert_embeddings.sav
    
  In server.py:
    (line 4) : sys.path.append(<your_custom_path>/Restaurant-Reviews-Sentiment-Analysis)
  ```
<br>

#### Step 4
* Go inside: <your_custom_path/Restaurant-Reviews-Sentiment-Analysis> directory through terminal and write the below mentioned command:
  ```
  (proj_env)$ python server.py
  ```

#### Step 5
* Install **Postman** or any other API client for sending and receiving API calls.
* Start Postman,go to POST request and paste the below mentioned URL:
  ```
  http://127.0.0.1:7000/validate
  ```
* Refer Fig. 1, Fig. 2 and Fig. 3 for Input JSON format and click on **Send**, you'll get the desired results.

<br>

***Congratulations!*** All done... this project should work smoothly. Incase of any doubts, feel free to contact me. I'll reply as soon as possible.
<br>
<p>
<a href="#top">Go back to top</a>
