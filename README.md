# API [Contatos - V1]

# Endpoint de contatos

### Listar todos contatos

**Definição/Request**

`GET /v1/contatos`

**Response**

- `200 OK` ao ter sucesso

```json
{
  "data": [
    {
      "canal": "email",
      "created_on": "2020-01-21T12:42:46.699843+00:00",
      "id": 1,
      "nome": "Sandro Carvalho",
      "obs": "nada a declarar",
      "password": "pbkdf2:sha256:150000$rTOofrGF$8a44e14c36506b924f6f2ff5705dd682eab2dd6a77c5501e083f8e01fc755211",
      "username": "sandro",
      "valor": "teste@gmail.com"
    }
  ],
  "message": "sucesso"
}
```
### Listar os contatos filtrando por nome

**Definição/Request**

`GET /v1/contatos?nome=S`

**Response**

- `200 OK` ao ter sucesso

```json
{
  "data": [
    {
      "canal": "email",
      "created_on": "2020-01-21T12:42:46.699843+00:00",
      "id": 1,
      "nome": "Sandro Carvalho",
      "obs": "nada a declarar",
      "password": "pbkdf2:sha256:150000$rTOofrGF$8a44e14c36506b924f6f2ff5705dd682eab2dd6a77c5501e083f8e01fc755211",
      "username": "sandro",
      "valor": "teste@gmail.com"
    }
  ],
  "message": "sucesso"
}
```


## Retornar um contato especifico

`GET /v1/contatos/<id>`

**Response**

- `404 Not Found` contato não existe

```json
{
    "data": {},
    "message": "contato nao existe"
}
```

- `200 OK` ao ter sucesso

```json
{
  "data": {
    "canal": "email",
    "created_on": "2020-01-21T12:42:46.699843+00:00",
    "id": 1,
    "nome": "Sandro Carvalho",
    "obs": "nada a declarar",
    "password": "pbkdf2:sha256:150000$rTOofrGF$8a44e14c36506b924f6f2ff5705dd682eab2dd6a77c5501e083f8e01fc755211",
    "username": "sandro",
    "valor": "teste@gmail.com"
  },
  "message": "sucesso"
}
```


### Registrando novos contatos

**Definição/Request**

`POST /v1/contatos`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api
- `"password":string` senha que será encriptada antes de ir para o banco
- `"nome":string` nome que descreva o contato
- `"canal":string` tipo de canal de contato, podendo ser email, celular ou fixo
- `"valor":string` valor para o canal de contato
- `"obs":string` qualquer observação que seja pertinente


**Response**

- `201 Created` ao ter sucesso

```json
{
  "data": {
    "canal": "email",
    "created_on": "2020-01-21T13:46:28.126591+00:00",
    "id": 2,
    "nome": "Sandro Carvalho",
    "obs": "nada a declarar",
    "password": "pbkdf2:sha256:150000$39FBeu3i$da5ee3acf39f40908128954dbf15dcfa83cee5fc70d8ccce372d26649748cfbf",
    "username": "sandro",
    "valor": "teste@gmail.com"
  },
  "message": "cadastro feito com sucesso"
}
```

- `200 Created` ao ter erro com usuario existente

```json
{
    "data": {
        },
    "message": "contato ja existe"
}
```

- `500 Internal error` ao ter erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "erro interno no servidor"
}
```


### Atualizando contatos

**Definição/Request**

`PUT /v1/contatos/<id>`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api
- `"password":string` senha que será encriptada antes de ir para o banco
- `"nome":string` nome que descreva o contato
- `"canal":string` tipo de canal de contato, podendo ser email, celular ou fixo
- `"valor":string` valor para o canal de contato
- `"obs":string` qualquer observação que seja pertinente

**Response**

- `201 Created` ao ter sucesso

```json
{
  "data": {
    "canal": "email",
    "created_on": "2020-01-21T12:42:46.699843+00:00",
    "id": 1,
    "nome": "Sandro Carvalho",
    "obs": "nada a declarar",
    "password": "pbkdf2:sha256:150000$RljHb8zt$c820e640ea90addc318b71f39edbb5ce912bb4734c27f6b843e665b1b9c4a117",
    "username": "sandro",
    "valor": "teste@gmail.com"
  },
  "message": "atualizacao feita com sucesso"
}
```

- `404 Not Found` contato não existe

```json
{
    "data": {},
    "message": "contato nao existe"
}
```

- `500 Internal error` ao ter erro com servidor ou sistema

```json
{
    "data": {},
    "message": "error interno no servidor"
}
```

## Deletar contato

**Definição**

`DELETE /v1/contatos/<id>`

**Response**

- `200 No Content` ao ter sucesso

```json
{
  "data": {
    "canal": "email",
    "created_on": "2020-01-21T12:42:46.699843+00:00",
    "id": 1,
    "nome": "Sandro Carvalho",
    "obs": "nada a declarar",
    "password": "pbkdf2:sha256:150000$RljHb8zt$c820e640ea90addc318b71f39edbb5ce912bb4734c27f6b843e665b1b9c4a117",
    "username": "sandro",
    "valor": "teste@gmail.com"
  },
  "message": "exclusao feita com sucesso"
}
```

- `404 Not Found` contato não existente

```json
{
    "data": {},
    "message": "contato nao existe"
}
```

- `500 Internal error` erro com servidor ou sistema

```json
{
    "data": {},
    "message": "error interno no servidor"
}
```

## Autenticação do token com servidor JWT

`POST /v1/authenticate`

**No header do seu JavaScript será necessário passar os dados do contato.**

***Authorization: 'Basic ' + btoa(username + ':' + password)***

**Response**

- `401 Not Found` caso não exista
- `200 OK` ao ter sucesso

```json
{
  "exp": "Wed, 22 Jan 2020 01:33:54 GMT",
  "message": "sucesso",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InNhbmRybyIsImV4cCI6MTU3OTY1NjgzNH0.-9DS1-IW_AxrKVV5PO002T-oXFpERVKSmKHo_x_PHGs"
}
```


