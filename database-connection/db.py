import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["med_data"]

my_collection = db["patient_data"]

# patient_record = {
#     "Name": "Maureen Skinner",
#     "Age": 87,
#     "Sex": "F",
#     "Blood pressure": [{"sys": 156}, {"dia": 82}],
#     "Heart rate": 82
# }
# my_collection.insert_one(patient_record)

document = {
    "firstname": "Di",
    "lastname": "Croix",
    "city": "Copenhagen",
    "country": "Luxembourg",
    "countryCode": "WS",
    "companyName": "XYZ",
    "email": "Di.Croix@gmail.com",
    "connections": ["Gabi", "Yolane", "Molli", "Elmira", "Yvonne"]
}

user_collection = db.user
user_collection.insert_one(document)
