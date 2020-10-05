# Restaurant-Reviews-Sentiment-Analysis

## Table of contents
* [Motivation](#motivation)
* [Technologies & Framework](#technologies-&-framework)
* [Illustrations](#Illustrations)
* [Setup & Installation](#setup-&-installation)

## Motivation
* Almost all restaurants have review system to take input from their customers about food and services. Here, a customer either writes about their experience or gives star ratings.
* In general, textual data hold crucial information about customer experience, even causality for star ratings. 
Currently, there isn't any system to validate the reviews i.e. whether a customer is writing proper reviews related to their restaurant experience.
* For example, I can write anything rubbish which is not related to my restaurant experience *(for instance, "xyz", "qwertyjafjwebfliu", "I like to play cricket")* and can submit my review.This limits a restaurants ability to focus on their areas of improvement.
* This project nudges customers to write relevant reviews using **_Natural Language Processing_** and **_Machine Learning_** with end-to-end API call using _Flask_ & _Python_.
* Furthermore, it classifies the reviews into _Positive_, _Negative_ & _Irrelevant_ reviews. Thus, helping restaurants to get insights on customer experience.

## Technologies & Framework 
This Project is created with:
* Python3.7 
* BERT
* Machine Learning
* Flask
* Postman

## Illustrations
* Below are the three images for three different categories of user input namely, Positive, Negative & Irrelevant review. 
* The input data is taken in JSON format with _"input_data"_ as key.
* Similarly the corresponding output is shown in JSON format with _"result"_ as key

<p align="center">
  <img src="https://github.com/amaan-ai/Restaurant-Reviews-Sentiment-Analysis/blob/master/images/Positive_review.png" alt="Positive Review Sample API"  width="800" height="500"/>
  <br>
  <em>Fig. 1: Positive Review Sample API</em>
</p>
<br>
<br>
<p align="center">
  <img src="https://github.com/amaan-ai/Restaurant-Reviews-Sentiment-Analysis/blob/master/images/Negative_review.png" alt="Negative Review Sample API"  width="800" height="500"/>
  <br>
  <em>Fig. 2: Negative Review Sample API</em>
</p>
<br>
<br>
<p align="center">
  <img src="https://github.com/amaan-ai/Restaurant-Reviews-Sentiment-Analysis/blob/master/images/Irrelevant_review.png" alt="Irrelevant Review Sample API"  width="800" height="500"/>
  <br>
  <em>Fig. 3: Irrelevant Review Sample API</em>
</p>



## Setup & Installation
To run this project, you need to clone this repository in your local system
