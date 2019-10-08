# dotPyREST
REST API for DotPy round 3


> /user/show

<img src ="https://cdn.discordapp.com/attachments/542955763472007188/631036888580358155/unknown.png">

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

> /user/fetchall-> GET
```json 
// Params: 
NONE

// RETURNS
data (stored in DB) -> {
    "user1": {
        "output": "codeOP"
    },
    "user2": {
        "output": "codeOP"
    },
    "user3": {
        "output": "codeOP"
    }
    .
    .
    .
}

```