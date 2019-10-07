# dotPyREST
REST API for DotPy round 3

### ROOT: /user/

> /user/create -> POST 

```json
// Params: 
data -> {
    "user" : "userID",
    "value": "output"
}

// RETURNS
data (stored in DB) -> {
    "user" : "userID",
    "value": "output"
}

```
> /user/delete-> DELETE
```json
// Params: 
data -> "user" = "userID"

// RETURNS
data  -> {
    "deleted": true
}

```
> /user/fetch -> GET
```json
// Params: 
data -> "user" = "userID"


// RETURNS
data (stored in DB) -> {
    "user" : "userID",
    "value": "output"
}

```
> /user/update-> POST 
```json 
// Params: 
data -> {
    "user" : "userID",
    "value": "output"
}

// RETURNS
data (stored in DB) -> {
    "user" : "userID",
    "value": "output"
}


```
