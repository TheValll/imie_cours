from mongo_requests import get_adresse_paris
from compare_two_coords import compare_two_coords

def compare_coords(coord_x, coord_y):
    adresse_paris = get_adresse_paris()
    for adresse in adresse_paris:
        coord = adresse["fields"].get("geom_x_y")
        if not coord:
            continue
        if compare_two_coords((coord_y, coord_x), tuple(coord)):
            return adresse["fields"].get("n_sq_ad") 
    return None