import pymongo
import dateparser
import sys
import datetime

# python -m pip install pymongo dnspython

def write_to_db(title, date, lat=0, lon=0, desc="", url="", image="", auth=None):
    if auth:
        client = pymongo.MongoClient("mongodb+srv://{}:{}@skarcluster-zb6ru.gcp.mongodb.net/events".format(auth[0], auth[1]))
    else:
        client = pymongo.MongoClient("mongodb+srv://skarcluster-zb6ru.gcp.mongodb.net/events")
    db = client.events
    event = {
        "title": title,
        "date": date,
        "location": {
            "lat": lat,
            "lon": lon,
        },
        "description": desc,
        "url": url,
        "image": image,
    }
    db.events.insert_one(event)

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    write_to_db("Boilermake", datetime.datetime(2018, 1, 25, 12), lat=40.2, lon=-86.9, desc="the best hackathon evaaa", auth=(username, password))
