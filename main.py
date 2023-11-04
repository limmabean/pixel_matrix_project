import orjson
with open("trip_updates_example.json", "rb") as f:
    trip_updates = orjson.loads(f.read())
    print(trip_updates['entity'][0])