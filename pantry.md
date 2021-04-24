
# API Reference: Pantry

The pantry API supports basic CRUD operations on elements in user pantries, i.e. discrete ingredients

## Register

Used to create a new pantry ingredient

**URL** : `/v1/pantry/create/<username>`

**Methods** : `POST`

**Auth required** : YES

**Data constraints**

```json
{
    "name": "valid ingredient name",
    "quantity": "unitless number representing amount of ingredient",
    "expiration date": "date in Y-m-d format"
}
```

**Data example**

```json
{
    "name": "grilled chicken",
    "quantity": "3",
    "expiration date": "2021-3-4"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "name": "grilled chicken",
    "quantity": "3",
    "expiration date": "2021-3-4"
}
```

### Error Response

**Condition** : If <username> can't be found

**Code** : `404 Not Found`

**Content** :

```json
{
    "error": "requested user not found"
}
```

**Condition** : If ingredient couldn't be created or saved

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "could not save requested ingredient"
}
```


## Read

Used to get all ingredients associated with a given user

**URL** : `/v1/pantry/<username>`

**Methods** : `GET`

**Auth required** : YES

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "ingredients": [{"name": "grilled chicken", "quantity": 2, "expiration_date": "2021-3-4", "user": "$OBJID", "id": "$OBJID"}...]
}
```

### Error Response

**Condition** : If <username> can't be found

**Code** : `404 Not Found`

**Content** :

```json
{
    "error": "requested user not found"
}
```


## Update

Used to change the contents of an ingredient item

**URL** : `/v1/pantry/update/<ingredient_id>`

**Methods** : `PUT`

**Auth required** : YES

**Data example**

```json
{
    "name": "chicken, grilled",
    "quantity": "4"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "data_updated": {
        "name": "chicken, grilled",
        "quantity": "4"
    }
}
```

### Error Response

**Condition** : If ingredient with ObjectID <ingredient_id> can't be found

**Code** : `404 NOT FOUND`

**Content** :

```json
{
    "error": "requested ingredient not found"
}
```

**Condition** : If update unsucessful

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Update Unsucessful"
}
```


## Delete ingredient

Removes ingredient from the database

**URL** : `/v1/pantry/delete/<username>?ingredient=<ingredient_id>`

**Methods** : `DELETE`

**Auth required** : YES

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "deleted": "<ingredient_id>"
}
```

### Error Response

**Condition** : If <ingredient_id> is not a valid ObjectId

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "ingredient_id not a valid object id"
}
```

**Condition** : If the <ingredient_id> does not correspond to an ingredient in the db

**Code** : `404 NOT FOUND`

**Content** :

```json
{
    "error": "requested ingredient not found"
}
```

**Condition** : The requested ingredient could not be deleted

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Deletion unsuccessful"
}
```
