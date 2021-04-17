
# API Reference: Exp

The expiration API lets you search for expiration dates

## Search

Used to find an expiration date given an ingredient keyword

**URL** : `/v1/exp?ingredient=<ingredient>`

**Methods** : `GET`

**Auth required** : YES

**Data constraints**

`ingredient` in querystring is passed as plaintext (url-encoded, if necessary), no quotes

**Data example**

`GET <ip>/v1/exp?ingredient=raw%20chicken`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
	"freezer_expiration": "2021-05-23",
	"fridge_expiration": "2021-05-02",
	"pantry_expiration": "2021-04-23",
	"ingredient_name": "raw chicken"
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

**Condition** : If an expiration date couldn't be found or returned from the database

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Expiration date could not be retrieved"
}
```
