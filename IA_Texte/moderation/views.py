from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from sklearn.feature_extraction.text import TfidfVectorizer
from pandas import DataFrame
import pandas as pd
import pickle
# Create your views here.

MODEL_ARRAY = [
        ('toxic','IA_model_toxic.sav','tfidf_vectorizer_toxic.pkl'),
        ('threat','IA_model_threat.sav','tfidf_vectorizer_threat.pkl'),
        ('severe_toxic','IA_model_severe_toxic.sav','tfidf_vectorizer_severe_toxic.pkl'),
        ('obscene','IA_model_obscene.sav','tfidf_vectorizer_obscene.pkl'),
        ('insult','IA_model_insult.sav','tfidf_vectorizer_insult.pkl'),
        ('identity_hate','IA_model_identity_hate.sav','tfidf_vectorizer_identity_hate.pkl')
    ]

@api_view(['GET'])
def getData(request):
    print('|||||||||||||||||||||||||||||||||||||||||||||||||||')
    comment = request.GET['comment']
    result = []
    for model in MODEL_ARRAY:
        with open('../IA/model/'+model[1],'rb') as model_file:
            loaded_model = pickle.load(model_file)
        # Load the TF-IDF vectorizer
        with open('../IA/vectorizer/'+model[2], 'rb') as vectorizer_file:
            loaded_vectorizer = pickle.load(vectorizer_file)

        new = loaded_vectorizer.transform([comment])
        predict = loaded_model.predict(new)
        if predict :
            result.append({ 'label':model[0], 'result': predict[0]})
    print("x", result)

    return Response({'result':result})
