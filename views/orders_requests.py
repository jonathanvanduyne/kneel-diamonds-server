""" This module handles all requests for the orders resource. """
from .metals_requests import get_single_metal
from .sizes_requests import get_single_size
from .styles_requests import get_single_style

ORDERS = [
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

def get_all_orders():
    """Returns the list of orders"""
    return ORDERS

def get_single_order(id):
    """Gets a single order by id"""
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

            matching_metal = get_single_metal(requested_order["metalId"])
            requested_order["metal"] = matching_metal

            matching_size = get_single_size(requested_order["sizeId"])
            requested_order["size"] = matching_size

            matching_style = get_single_style(requested_order["styleId"])
            requested_order["style"] = matching_style

            # remove the foreign key properties
            del requested_order["metalId"]
            del requested_order["sizeId"]
            del requested_order["styleId"]

    return requested_order

def create_order(order):
    """Creates a new order"""
    max_id = ORDERS[-1]["id"]

    new_id = max_id + 1

    order["id"] = new_id

    ORDERS.append(order)

    return order

def delete_order(id):
    """Deletes an order by id"""
    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index

    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    """Updates an order by id"""
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
