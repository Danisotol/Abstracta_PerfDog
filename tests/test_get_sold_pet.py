import requests
import pytest

BASE_URL = "https://petstore.swagger.io/v2"

#Mascota con estado 'sold'
def test_get_sold_pet():
    pet_id = 99
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url)
    
    assert response.status_code == 200, f"Failed to get pet with id {pet_id}"
    
    pet_data = response.json()
    assert pet_data["status"] == "sold", f"Pet status is not 'sold', found {pet_data['status']}"
    
#Detalles adicionales de la mascota
    pet_name = pet_data.get("name", "No name available")
    pet_category = pet_data.get("category", {}).get("name", "No category available")
    print(f"Pet Details:\n- ID: {pet_id}\n- Name: {pet_name}\n- Category: {pet_category}\n- Status: {pet_data['status']}")

#Ejecutar
if __name__ == "__main__":
    test_get_sold_pet()

