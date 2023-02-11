# HTTP API for getting building energy constumption data

## Fetch building list
```http
GET /buildings

[
    "b1",
    "b2",
    ...
]
```

## Fetch specific building data
```http
GET /building/{bdg}?resolution={hourly|daily}&type={min|max|avg}&timeFrom={timestamp}&timeTo={timestamp}

[
    {
        "timestamp": 76542137564172,
        "value": 69
    },
    ...
]
```
