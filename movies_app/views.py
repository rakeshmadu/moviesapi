from django.shortcuts import render
from rest_framework.decorators import api_view
from pymongo import MongoClient
from django.http import JsonResponse
from django.shortcuts import render
#  from datetime import datetime,timedelta
# Create your views here.

client=MongoClient()
db= client['movies']


#1)director with max movies
@api_view(['GET'])
def get_maxd(request):
    collection=db['movies']
    cursor= collection.aggregate([{"$sortByCount":"$director"},{"$limit": 1}])
    data=list(cursor)
    return JsonResponse(data,safe=False)


#2)most popular genere watched by audiance
@api_view(['GET'])
def get_mostpop(request):
    collection = db['movies']
    cursor =db.movies.aggregate([{"$sortByCount":"$genre"},{"$limit": 1}])
    data=list(cursor)
    return JsonResponse(data,safe=False)

# 3)top ten movies according to imdb score
@api_view(['GET'])
def get_top_ten(request):
    collection = db['movies']
    cursor =collection.aggregate([{ "$group" :{ '_id': "$name",
    "score":{"$max":"$imdb_score"}}},{"$sort":{"score":-1}},{"$limit":10}])
    data=list(cursor)
    return JsonResponse(data,safe=False)

# 4)best director in the top hundred movies
@api_view(['GET'])
def get_best_dir(request):
    collection = db['movies']
    cursor =collection.aggregate([{ "$group" :{ '_id': "$director",
    "rating":{"$max":"$99popularity"}}},{"$sort":{"rating":-1}},{"$limit":1}])
    data=list(cursor)
    return JsonResponse(data,safe=False)
   

#5)Least watched movie by its imdb score.
@api_view(['GET'])
def get_least_watch(request):
    collection = db['movies']
    cursor = collection.aggregate([{ "$group" :{ '_id': "$name",
    "score":{"$max":"$imdb_score"}}},{"$sort":{"score":1}},{"$limit":1}])
    # cursor = collection.aggregate([{"$group": { "_id": "$imdb_score","least_watched": 
    # {"$push": "$$ROOT"}}},{"$sort":{"_id":1}},{"$limit":1}])
    data=list(cursor)
    return JsonResponse(data,safe=False)


#6)post fav movie
@api_view(['POST'])
def post_fav(request):
    print(request.data)
    collection = db['movies']
    data= []
    # cursor=collection.insert(request.data)
    cursor=collection.insert({"99popularity" : request.data['99popularity'], "director" :request.data['director'],"genre":request.data['genre'],"imdb_score":request.data['imdb_score'],"name":request.data['name']})
    return JsonResponse({"data":"success"},safe=False)    

