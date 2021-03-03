
# API Reference: User

The User API contains a number of endpoints that are useful for providing basic profile and user mangement features

## Register

Used to create a new user account

**URL** : `/v1/user/register`

**Methods** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username": "[8 < length < 19]",
    "password": "[8 < length < 19]",
    "email": "[valid email address]""
} 
```

**Data example**

```json
{
    "username": "pedrobabon",
    "password": "1849Sicily",
    "email": "pedrobabon@myspace.com",
    "first_name": "Pedro",
    "last_name": "Babon"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "pedrobabon",
    "email": "pedrobabon@myspace.com"
}
```

### Error Response

**Condition** : If 'username'/'password'/etc invalid.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Invalid username/password"
}
```

**Condition** : If 'username'/'email' already exist in account.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "account with supplied username/email already exists"
}
```

## Login

Used to log a user in via username-password authentication

**URL** : `/v1/user/login`

**Methods** : `GET/POST`

**Auth required** : NO

**Data example**

```json
{
    "username": "pedrobabon",
    "password": "1849Sicily"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "pedrobabon",
    "email": "pedrobabon@myspace.com"
}
```

### Error Response

**Condition** : If 'username'/'password'/etc does not exist.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "supplied username does not exist"
}
```

**Condition** : If 'username'/'email' already exist in account.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "unauthorized"
}
```


## Update

Used to update a user's profile (not including password). Note that any desired fields can be passed in JSON, API figures out updates needed.

**URL** : `/v1/user/update/<username>`

**Methods** : `PUT`

**Auth required** : NO

**Data example**

```json
{
    "username": "PEDROBABON",
    "password": "1880China"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "data_updated": {
        "username": "PEDROBABON",
        "password": "1880China"
    }
}
```

### Error Response

**Condition** : If 'username' path parameter does not exist.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "supplied username does not exist"
}
```

**Condition** : If update unsucessful already exist in account.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Update Unsucessful"
}
```


## Change Password

Used to change a user's password associated with their account

**URL** : `/v1/user/password/<username>`

**Methods** : `PUT`

**Auth required** : NO

**Data example**

```json
{
    "password": "18NewEngland"
}
```

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "PEDROBABON"
}
```

### Error Response

**Condition** : If password change unsucessful

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "Invalid username/password"
}
```

## Fetch Account Information

Fetches all information associated with a user's profile

**URL** : `/v1/user/<username>`

**Methods** : `GET`

**Auth required** : NO

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "_id": {
        "$oid": "doc_id"
    },
    "first_name": "Pedro",
    "last_name": "Babon",
    "email": "pedro.babon@myspace.edu",
    "username": "pedrobabon",
    "hash": "random_hash",
    "salt": "salt_digits",
    "pantry": {
        "$oid": "pantry_id"
    }
}
```

### Error Response

**Condition** : If username supplied in path does not exist

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "error": "supplied username does not exist"
}
```

## Check if User Account Exists

Checks if account corresponding to username exists

**URL** : `/v1/user/<username>`

**Methods** : `HEAD`

**Auth required** : NO

### Success Response

**Code** : `200 OK`

### Error Response

**Code** : `400 BAD REQUEST`

