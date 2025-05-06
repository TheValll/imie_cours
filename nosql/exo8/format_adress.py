import re

def format_adress(adress):
    match = re.search(r'\b(\d{5})\b', adress)
    
    if match:
        zipcode = match.group(1)
        adresse_sans_zipcode = adress.replace(zipcode, '').strip(', ').replace(',,', ',')
        return zipcode, adresse_sans_zipcode
    else:
        return None, adress