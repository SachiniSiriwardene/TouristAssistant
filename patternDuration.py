import MongoDBConnect

def durationOneQuerry(entity,client):
    duration =""
    # db connection
    #client = MongoDBConnect.mongoConnect()
    # db querry
    doc = client.find({"attractionName": entity})

    #duration = doc.suggestedDuration
    for document in doc:
       duration = document["suggestedDuration"]

    reply = "It will take "+ duration + " to visit "+ entity
    print(reply)

def durationTwoQuery(entity,duration,client):
    suggestedDuration = ""

    # db querry
    doc = client.find({"attractionName": entity})

    # duration = doc.suggestedDuration
    for document in doc:
        suggestedDuration = document["suggestedDuration"]
    if('hour' in suggestedDuration):
     suggestedDuration = suggestedDuration.split("hour")[0]
    else:
     suggestedDuration = suggestedDuration.split("hours")[0]
    if('<' in suggestedDuration):
      suggestedDuration = suggestedDuration.split("<")[1]
