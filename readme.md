# Endpoints

## Endpoints para crear un nuevo usuario:

-  https://www.compu-finder.com/api/v1/auth/user/register/

## Endpoints para generar token del usuario:

- https://www.compu-finder.com/api/v1/auth/token/

## Endpoints para volver a generar:

- https://www.compu-finder.com/api/v1/auth/token/refresh/


## Endpoint para consultar productos en lista:

- https://www.compu-finder.com/api/v1/products/products-list/?offset=0&limit=10


## Endpoint para consultar producto unico:

- https://www.compu-finder.com/api/v1/products/code/

## Endpoint para consultar producto con texto contenido en el nombre del producto:

- https://www.compu-finder.com/api/v1/products/search/?name=texto

## Consulta de productos en lista con filtros adicionales

- https://www.compu-finder.com/api/v1/products/products-list/?company=name&category=name&brand=name&offset=0&limit=10

# Codigo para el post y get de los endpoints:

## Codigo para hacer post y generar nuevo usuario:

```python
# data -> json con los datos necesarios para el post
# url -> url del endpoint

data = {
    "username": username,
    "password": password,
    "email": email  # Solo incluir si es obligatorio
}

json_data = json.dumps(data)

# Headers (si el API espera JSON)
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.post(url, data=json_data, headers=headers)
```

## Codigo para hacer post y generar token:

```python
# auth_data -> json con los datos necesarios para el post
# url -> url del endpoint

auth_data = {
    "username": username,
    "password": password
}

auth_json = json.dumps(auth_data)

# Headers (si el API espera JSON)
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.post(token_url, data=auth_json, headers=headers)
```

## Codigo para hacer solicitud get a los endpoints
```python
# token -> Token generado con el usurario
# url -> endpoint a consultar

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
```