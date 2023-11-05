import orjson
import csv

relevant_routes = {}

with open("relevant_routes.json", "rb") as relevant_routes_json:
    relevant_routes = orjson.loads(relevant_routes_json.read())
relevant_routes_json.close()

relevant_bus_routes = relevant_routes['relevant_bus_routes']
relevant_rail_routes = relevant_routes['relevant_rail_routes']

all_existing_routes = {}
with open('routes[8-8-23].csv', newline='') as csvfile:
    all_existing_routes = list(csv.reader(csvfile, delimiter=','))

relevant_trips = {
    "relevant_bus_trips": [],
    "relevant_rail_trips": []
}
for relevant_bus_route in relevant_bus_routes:
    for row in all_existing_routes:
        if row[1] == relevant_bus_route:
            relevant_trips["relevant_bus_trips"].append({
                "route_id": row[0],
                "route_num": row[1],
                "route_long_name": row[2],
                "route_desc": row[3],
                "route_type": "Bus"
            })


trip_updates = {}

with open("relevant_routes.json", "rb") as relevant_routes_json:
    relevant_routes = orjson.loads(relevant_routes_json.read())
relevant_routes_json.close()

with open("trip_updates_example.json", "rb") as trip_updates_test:
    trip_updates = orjson.loads(trip_updates_test.read())
trip_updates_test.close()