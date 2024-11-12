import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

#Detalles mascotas por ID
def get_pet_name_by_id(pet_id):
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)

    if response.status_code == 200:
        pet_data = response.json()
        return pet_data["name"], pet_data["status"]
    else:
        raise Exception(f"Failed to get pet with id {pet_id}. Status code: {response.status_code}")

#Almacenar mascotas disponibles
available_pets = []

#Listado de IDs de mascotas disponibles y guardadas
def test_create_orders_for_specific_pets():
    pet_ids = [90, 91, 92, 93, 94]
    for pet_id in pet_ids:
        pet_name, pet_status = get_pet_name_by_id(pet_id)

        if pet_status == "available":
            available_pets.append({"id": pet_id, "name": pet_name, "status": pet_status})

#Crear orden para una mascota
def create_order_for_pet(pet_id, pet_name):
    url = f"{BASE_URL}/store/order"
    order = {
        "id": pet_id,
        "petId": pet_id,
        "quantity": 1,
        "shipDate": "2024-11-11T00:00:00Z",
        "status": "placed",
        "complete": True
    }
    
    response = requests.post(url, json=order)
    if response.status_code == 200:
        print(f"Order created for pet: {pet_name} (ID: {pet_id})")
    else:
        print(f"Failed to create order for pet with id {pet_id}. Response: {response.status_code}")

#Ejecutar
if __name__ == "__main__":
    test_create_orders_for_specific_pets()
    print("Mascotas disponibles guardadas:", available_pets)