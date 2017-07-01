# TumTumTracker API
The api is build to store and update the data i.e. the locations of the buses into the server.

#Fetching Data
For fetching purposes send a http get request to the ip address:
"http://139.59.36.85/?format=json"
The server would return a json object which would basically be a list or vector of location objects. Each location object consists of bus id,nfc id,latitude and longitude of the corresponding bus

#Posting Data
At the time of posting, as you would have only the nfc id of the bus you would be in, first make a get call to the same url and through loops find the bus id corresponding nfc id in hand.Store the bus id in a variable and then make a post request to the same ip adress 

#Things to Work On
We are finding a way so that we can make posting easier but have been getting an error for quite long.And we still have to do the authentication of it


