def contains_zipcode(address):
    parts = address.split(',')
    for part in parts:
        part = part.strip()
        if part.isdigit() and len(part) == 5:
            return True
    return False