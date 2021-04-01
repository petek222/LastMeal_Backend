
# API Reference: Photos

The photos API lets you search for photos

## Search

Used to find a photo given an ingredient keyword

**URL** : `/v1/photos?ingredient=<ingredient>`

**Methods** : `GET`

**Auth required** : YES

**Data constraints**

`ingredient` in querystring is passed as plaintext (url-encoded, if necessary), no quotes

**Data example**

`GET <ip>/v1/photos?ingredient=raw%20chicken`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "src": "https://images.pexels.com/photos/3688/food-dinner-lunch-chicken.jpg?auto=compress&cs=tinysrgb&h=130"
}
```

### Error Response

**Condition** : If <ingredient> wasn't passed in the querystring

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "no ingredient was passed"
}
```

**Condition** : If a photo couldn't be found or returned from pexels

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Image could not be retrieved"
}
```