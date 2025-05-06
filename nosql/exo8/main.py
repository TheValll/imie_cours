from mongo_requests import get_adresse_paris_tour, get_adresse_paris
from contains_zipcode import contains_zipcode
from haversine import haversine
from compare_two_coords import compare_two_coords
from save_bdd import save_bdd
from format_adress import format_adress

adresse_paris = get_adresse_paris()
adresse_paris_tour = get_adresse_paris_tour()

notre_dame_coords = (48.852737, 2.350699)

def compare_coords(coord_x, coord_y):
    for adresse in adresse_paris:
        coord = adresse["fields"].get("geom_x_y")
        if not coord:
            continue
        if compare_two_coords((coord_y, coord_x), tuple(coord)):
            return adresse["fields"].get("n_sq_ad") 
    return None

adresses_proches = []
for x in adresse_paris_tour:
    location = x.get("location", {})
    address = location.get("address", "")

    if contains_zipcode(address):  
        address, zipcode = format_adress(address)
        x["location"]["zipcode"] = str(zipcode)
        adresses_proches.append(x)
        continue

    if address and "coord" in location and "coordinates" in location["coord"]:
        coord_x = location["coord"]["coordinates"][0]
        coord_y = location["coord"]["coordinates"][1]

        distance = haversine(notre_dame_coords, (coord_y, coord_x))
        if distance <= 2:
            zipcode = compare_coords(coord_x, coord_y)
            if zipcode:
                x["location"]["zipcode"] = str(zipcode)[:5]
                adresses_proches.append(x)

save_bdd(adresses_proches)