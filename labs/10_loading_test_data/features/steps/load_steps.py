# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Pet Steps

Steps file for Pet.feature

"""
import requests
from behave import given


@given('the following pets')
def step_impl(context):
    """Load the provided pet data into the system"""
    pet_data = []
    for row in context.table:
        pet_data.append({
            "name": row["name"],
            "category": row["category"],
            "available": row["available"].lower() == "true",
            "gender": row["gender"],
            "birthday": row["birthday"],
        })
    
    # Assuming an API is available to load pets into the system
    for pet in pet_data:
        response = requests.post(f"{context.base_url}/pets", json=pet)
        if response.status_code != 201:
            raise RuntimeError(f"Failed to create pet: {pet} - {response.text}")
