
# API Reference: Favorite

The Favorite API supports basic CRUD operations favorited recipes

## Register

Used to create a new favorite recipe

**URL** : `/v1/favorite/create/<username>`

**Methods** : `POST`

**Auth required** : YES

**Data constraints**

```json
{
    "recipe_name": "recipe name",
    "recipe_id": "unique recipe id",
    "picture": "url of recipe picture"
}
```

**Data example**

```json
{
    "recipe_name": "chicken",
    "recipe_id": "400",
    "picture": "google.com"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "recipe_name": "chicken",
    "recipe_id": "400",
    "picture": "google.com"
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

**Condition** : If favorite recipe couldn't be created or saved

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "could not favorite requested recipe"
}
```


## Read

Used to get all favorite recipes associated with a given user

**URL** : `/v1/favorite/<username>`

**Methods** : `GET`

**Auth required** : YES

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "favorites": [{
        "picture": "google.com",
        "recipe_id": 400,
        "recipe_name": "chicken"
    }, {
        "picture": "google.com",
        "recipe_id": 401,
        "recipe_name": "chicken"
    }, {
        "picture": "google.com",
        "recipe_id": 402,
        "recipe_name": "chicken"
    }]
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


## Delete

Removes favorited recipe from the database for a particular user

**URL** : `/v1/favorite/delete/<username>?recipe_id=<recipe_id>`

**Methods** : `DELETE`

**Auth required** : YES

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "deleted": "<recipe_id>"
}
```

### Error Response

**Condition** : If the username passed does not correspond to a user in the db

**Code** : `404 NOT FOUND`

**Content** :

```json
{
    "error": "requested user not found"
}
```

**Condition** : The requested favorited recipe could not be deleted

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Deletion unsuccessful"
}
```
