# tumtumbackend
The app consints of two folders tracker and tumtum.Tumtum is the main site host which includes settings.py and the tracker is the app which
consists of the database.During api calls first access is to tumtum.urls which calls tracker.urls which imports tracker.views that indeed 
imports location from models and LocationSerializer from serializer

