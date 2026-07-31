def validate_id(id):
    try:
        id = int(id)
    except ValueError:
        return None
    if id > 0:
        return id

def validate_quantity(qty):
    try:
        qty = int(qty)
    except ValueError:
        return None
    if qty > 0:
        return qty

test = validate_id("7")
