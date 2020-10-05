# Restaurant-Reviews-Sentiment-Analysis

## Table of contents
* [Motivation](#Motivation)
* [Technologies](#Technologies)
* [Setup](#setup)

## Motivation
* Almost all restaurants have review system to take input from their customers about food and services. Here, a customer either writes about their experience or gives star ratings.
* In general, textual data hold crucial information about customer experience, even causality for star ratings. 
Currently, there isn't any system to validate the reviews i.e. whether a customer is writing proper reviews related to their restaurant experience.
* For example, I can write anything rubbish which is not related to my restaurant experience *(for instance, "xyz", "qwertyjafjwebfliu", "I like to play cricket")* and can submit my review.This limits a restaurants ability to focus on their areas of improvement.
* This project nudges customers to write relevant reviews using **_Natural Language Processing_** and **_Machine Learning_** with end-to-end API call using _Flask_ & _Python_.
* Furthermore, it classifies the reviews into positive, negative & irrelevant reviews. Thus, helping restaurants to get insights on customer experience.

## Technologies
Project is created with:
* Python3.7 
* Flask
* BERT : _(bert-base-nli-mean-tokens)_
* Machine Learning Model : _(Naive Bayes)_
* Postman
