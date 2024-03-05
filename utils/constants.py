# API Constants

API_NAME = "Chatter Bot"


# Pinecone Constants

PROPERTIES_NAMESPACE = "properties"


# Self Query Retriever Attribute Dictionary


ATTRIBUTE_INFO_DICT = {
    # "site_view": {
    #     "description": "The preferred site view.",
    #     "type": "string",
    # },
    "propertytype": {
        "description": "Type of the property.",
        "type": "string",
    },
    "month": {
        "description": "The month the listing was added (in lowercase)",
        "type": "string",
    },
    "unix-epoch-time": {
        "description": "The unix-epoch timestamp",
        "type": "integer",
    },
    "day": {
        "description": "The day the listing was added",
        "type": "integer",
    },
    "locality": {
        "description": "Locality of the property (in lowercase).",
        "type": "string",
    },
    "totalprice": {
        "description": "This is the price of the property",
        "type": "integer",
    },
    "furnishing_status": {
        "description": "This is the furnishing status of the property, which might be either unfurnished, semi-furnished, furnished (in lowercase)",
        "type": "string",
    },
    "areainsqft": {
        "description": "This is the size of the property in square feet or sq ft",
        "type": "integer",
    },
    "number_of_bathroom": {
        "description": "This is the number of bathrooms in the property",
        "type": "integer",
    },
    "property_class": {
        "description": "This is either 'resale' or 'rental'. 'resale' when the intent is to buy a property or 'rental' if the intent is to rent a property (in lowercase)",
        "type": "string",
    },
    "number_of_rooms": {
        "description": "This is the number of rooms/bedrooms in the property, usually mentioned as a number before 'bhk' Example: for 1bhk, 2 bhk and 3bhk, number_of_rooms must be set to 1, 2 and 3 respectively",
        "type": "float",
    },
    "unix_epoch_time": {
        "description": "The unix epoch time",
        "type": "integer",
    },
    "cityname": {
        "description": "Name of the city (in lowercase)",
        "type": "string",
    },
}
