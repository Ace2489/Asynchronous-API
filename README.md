# Asynchronous-API
Asynchronous Combined API Endpoint
Endpoint: /combined

Method: GET

Description: This endpoint is used to asynchronously fetch JSON data from multiple URLs and combine the responses into a single JSON response.

Request Parameters:
This endpoint does not require any request parameters.

Response:
200 OK: If the JSON data is successfully fetched from all URLs.

json
Copy code
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
500 Internal Server Error: If an error occurs during the asynchronous fetch process.

json
Copy code
{
    "error": "Internal Server Error"
}
Example Usage:
bash
Copy code
curl -X GET http://your-domain.com/combined
Notes:
This endpoint asynchronously fetches JSON data from the following URLs:

https://quotable.io/quotes?page=1
https://randomuser.me/api/
The JSON data from each URL is included in the response under the keys quotes and results respectively.

The endpoint uses the aiohttp library for asynchronous HTTP requests and asyncio for managing asynchronous tasks.
