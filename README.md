# Asynchronous Combined API Documentation

## Overview

This API endpoint is designed to asynchronously fetch JSON data from multiple URLs and combine the responses into a single JSON response. It utilizes the `aiohttp` library for making asynchronous HTTP requests and `asyncio` for managing asynchronous tasks. The response is returned as a JSON object using Django's `JsonResponse`.

## Endpoint

- **URL:** `/combined`
- **Method:** `GET`

## Request

This endpoint does not require any request parameters.

## Response

### Success Response

- **Status Code:** 200 OK
- **Content-Type:** application/json

```
{
    "Response": [
        {
            "quotes": [ ... ] // JSON data from 'https://quotable.io/quotes?page=1'
        },
        {
            "results": [ ... ] // JSON data from 'https://randomuser.me/api/'
        }
    ]
}
```
### Error Response
 - Status Code: 500 Internal Server Error
 - Content-Type: application/json

```
{
    "error": "Internal Server Error"
}
```

## Notes
- This endpoint asynchronously fetches JSON data from the following URLs:
    - https://quotable.io/quotes?page=1: Retrieves a list of quotes.
    - https://randomuser.me/api/: Retrieves random user data.
- The JSON data from each URL is included in the response under the keys quotes and results respectively.
