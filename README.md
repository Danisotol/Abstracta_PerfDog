# Abstracta_PerfDog
API PerfDog Abstracta test.

# Swagger Petstore API Project

## Descripción
Este proyecto utiliza la API de Swagger Petstore para gestionar mascotas. Incluye scripts para crear mascotas, obtener sus detalles y crear órdenes para las mismas.
Ya que Swagger reestablece los datos creados cada cierto tiempo, incluyo archivo JSON con las 10 mascotas co sus respectivos estados, creados por mi.

## Estructura del Proyecto
- `export_pet_details.py`: Script para exportar los detalles de las mascotas a un archivo JSON.
- `test_create_orders.py`: Script para listar mascotas disponibles y crear órdenes para ellas.
- `test_get_sold_pet.py`: Prueba para obtener los detalles de la mascota con estado "sold".

## Requisitos
- Python 3.11
- Librerías de Python: `requests`, `pytest`

## Cómo Empezar

### 1. Clonar el repositorio - Para obtener una copia local del proyecto, ejecuta el siguiente comando en PowerShell:

```powershell
git clone https://github.com/Danisotol/Abstracta_PerfDog.git

### 2. Instalar dependencias - Crea un entorno virtual, activalo e instala dependencias necesarias:

cd Abstracta_PerfDog
python -m venv env
.\env\Scripts\Activate
pip install -r requirements.txt

### 3. Configura Git 
git config user.email "dansoto1092@gmail.com"
git config user.name "Daniela Soto"

### 4. Realiza el commit
git commit -m "Initial commit - adding all project files"

### 5. Subir al repositorio remoto
git push origin main

### 6. Ejecutar los scripts - Para ejecutar el script "export_pet_details.py" y exportar los detalles de las mascotas en powershell:
python export_pet_details.py
 
# Para ejecutar el script "test_create_orders.py" y crear las órdenes de las mascota en powershell:
python test_create_orders.py

# Para ejecutar el script "test_get_sold_pet.py" y obtener los detalles de la mascota con estado "sold" en powershell:
python test_get_sold_pet.py


