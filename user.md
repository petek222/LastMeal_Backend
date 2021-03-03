
## API Reference: User

The User API contains a number of endpoints that are useful for providing basic profile and user mangement features

### Register

Used to create a new user account

**URL** : `/v1/user/register`

**Methods** : `POST`

**Auth required** : NO

**Data constraints**

```json
{
    "username": "[8 < length < 19]",
    "password": "[8 < length < 19]"
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

#### Success Response

**Code** : `200 OK`

**Content example**

```json
{
    "username": "pedrobabon"
    "email": "pedrobabon@myspace.com"
}
```



#### Error Response

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
