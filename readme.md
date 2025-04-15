# Endpoints

## Endpoints de autenticacion y token:

- Crear usuario: https://www.compu-finder.com/api/v1/auth/user/register/

- generar token: https://www.compu-finder.com/api/v1/auth/token/

- Refrescar el token, cuando este expira: https://www.compu-finder.com/api/v1/auth/token/refresh/


## Endpoint para consultar productos:

- Consultar productos en lista: https://www.compu-finder.com/api/v1/products/products-list/?offset=0&limit=10

- Consultar producto unico: https://www.compu-finder.com/api/v1/products/code/

- Consultar producto con texto contenido en el nombre del producto: https://www.compu-finder.com/api/v1/products/search/?name=texto

- Consultar productos en lista con filtros adicionales: https://www.compu-finder.com/api/v1/products/products-list/?company=name&category=name&brand=name&offset=0&limit=10

## Endpoint para consultar precios y stock:

- Consultar historico de precios: https://www.compu-finder.com/api/v1/products/prices/?code=1234567/

- Consultar historico de stock: https://www.compu-finder.com/api/v1/products/stock/?code=1234567/

# Consulta post y get a los endpoints (Python):

## Generar nuevo usuario:

```python
# data -> json con los datos necesarios para el post
# url -> url del endpoint

data = {
    "username": username,
    "password": password,
    "email": email  # Opcional
}

json_data = json.dumps(data)

# Headers (si el API espera JSON)
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

response = requests.post(url, data=json_data, headers=headers)
```

## Generar token:

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

## Solicitud get a los endpoints, consultart productos, precio stock
```python
# token -> Token generado con el usurario
# url -> endpoint a consultar

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
```