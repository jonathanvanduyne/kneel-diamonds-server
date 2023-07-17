"""This module is responsible for creating the database, storing, and accessing data."""

DATABASE = {
    "metals": [
        {
            "id": 1,
            "metal": "Sterling Silver",
            "price": 12.42
        },
        {
            "id": 2,
            "metal": "14K Gold",
            "price": 736.4
        },
        {
            "id": 3,
            "metal": "24K Gold",
            "price": 1258.9
        },
        {
            "id": 4,
            "metal": "Platinum",
            "price": 795.45
        },
        {
            "id": 5,
            "metal": "Palladium",
            "price": 1241
        }
    ],
    "sizes": [
        {
            "id": 1,
            "carats": 0.5,
            "price": 405
        },
        {
            "id": 2,
            "carats": 0.75,
            "price": 782
        },
        {
            "id": 3,
            "carats": 1,
            "price": 1470
        },
        {
            "id": 4,
            "carats": 1.5,
            "price": 1997
        },
        {
            "id": 5,
            "carats": 2,
            "price": 3638
        }
    ],
    "styles": [
        {
            "id": 1,
            "style": "Classic",
            "price": 500
        },
        {
            "id": 2,
            "style": "Modern",
            "price": 710
        },
        {
            "id": 3,
            "style": "Vintage",
            "price": 965
        }
    ],
    "orders": [
        {
            "metalId": 1,
            "sizeId": 1,
            "styleId": 1,
            "jewelryId": 1,
            "id": 1
        },
        {
            "metalId": 5,
            "sizeId": 5,
            "styleId": 3,
            "jewelryId": 3,
            "id": 2
        },
        {
            "metalId": 3,
            "sizeId": 3,
            "styleId": 2,
            "jewelryId": 2,
            "id": 3
        },
        {
            "metalId": 2,
            "sizeId": 1,
            "styleId": 1,
            "jewelryId": 1,
            "id": 4
        }
    ]
}

def get_all(resource):
    """To get all of a resource"""
    return DATABASE[resource]

def retrieve(retrieve_resource, _id):
    """To get a single resource"""
    if retrieve_resource == "orders":
        requested_order = None

        for order in DATABASE[retrieve_resource]:
            if order["id"] == _id:
                requested_order = order
                break

        if requested_order is not None:
            matching_metal = next((item for item in DATABASE["metals"] if item["id"] == requested_order["metalId"]), None)
            matching_size = next((item for item in DATABASE["sizes"] if item["id"] == requested_order["sizeId"]), None)
            matching_style = next((item for item in DATABASE["styles"] if item["id"] == requested_order["styleId"]), None)

            if matching_metal is not None:
                requested_order["metal"] = matching_metal
            if matching_size is not None:
                requested_order["size"] = matching_size
            if matching_style is not None:
                requested_order["style"] = matching_style

            # Remove the foreign key properties
            del requested_order["metalId"]
            del requested_order["sizeId"]
            del requested_order["styleId"]

            requested_order["total"] = (
                requested_order["metal"]["price"]
                + requested_order["size"]["price"]
                + requested_order["style"]["price"]
            )

        return requested_order

    else:
        requested_resource = None

        for item in DATABASE[retrieve_resource]:
            if item["id"] == _id:
                requested_resource = item
                break

        return requested_resource

def update(update_resource, _id):
    """To change a single resource"""
    if update_resource == "metals":
        for index, item in enumerate(DATABASE[update_resource]):
            if item["id"] == _id:
                DATABASE[update_resource][index]["price"] = update_resource[index]["price"]
                break
    elif update_resource in ('styles', 'orders'):
        pass
    else:
        for index, item in enumerate(DATABASE[update_resource]):
            if item["id"] == _id:
                DATABASE[update_resource][index] = update_resource
                break


def delete(delete_resource, _id):
    """To delete a single resource"""
    if delete_resource in ('styles', 'orders', 'metals'):
        pass
    else:
        for index, item in enumerate(DATABASE[delete_resource]):
            if item["id"] == _id:
                DATABASE[delete_resource].pop(index)
                break

def create(create_resource):
    """To create a new resource"""
    if create_resource in ('styles', 'orders', 'metals'):
        pass
    else:
        max_id = DATABASE[create_resource][-1]["id"]
        new_id = max_id + 1
        create_resource["id"] = new_id
        DATABASE[create_resource].append(create_resource)
        return create_resource
