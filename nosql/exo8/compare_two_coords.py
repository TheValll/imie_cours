from haversine import haversine

def compare_two_coords(coord1, coord2, threshold_km=0.3):
    return haversine(coord1, coord2) <= threshold_km
