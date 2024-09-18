from pymongo import MongoClient
connection_string = "mongodb+srv://rajeev24shetty:HCDfKlodBlTaQI3C@cluster0.tk1tq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(connection_string)
db = client['sample_mflix']
collection = db['movies']

#result = collection.find_one({"tomatoes.viewer": {"rating": 4.3, "numReviews": 752, "meter": 91}})
#print(f" ***** result is : {result}")


#update_query = {"tomatoes.viewer.ranting": 4.3}

#update_query = {"tomatoes.viewer": {"rating": 4.3, "numReviews": 752, "meter": 91}}
#new_value = {"$set": {"tomatoes.viewer.numReviews":754} }

#udpated_Result = collection.update_one(update_query,new_value)

result = collection.find_one({"tomatoes.viewer": {"rating": 4.3, "numReviews": 754, "meter": 91}})
print(f" @@@@@@@@ result is : {result}")



# {"tomatoes.viewer": {"rating": 4.3, "numReviews": 753, "meter": 91}}

pipeline = [
    {
        "$match": {
        "rated":"TV-G",
        "genres":"Short"
        }
    }
    # ,{    
    #     "$group": {
    #     "_id": "$year",
    #     "count": { "$sum": 1}
    #     }
    # }
    , {
        "$sort":
        {
        "title": 1    
        }
    }
    ,{
        "$limit": 1        
    }
]

aggr_result = collection.aggregate(pipeline)
for ob in aggr_result:
    print(" * {title}, {first_castmember}, {year}".format(title = ob["title"],first_castmember = ob["cast"][0], year = ob["year"]))


client.close()
