# REST API Client (using requests)

Demonstrates making HTTP GET and POST requests to a public REST API, parsing JSON responses, and handling errors gracefully. Uses the free [JSONPlaceholder](https://jsonplaceholder.typicode.com) API.

## Prerequisites

```bash
pip install requests
```

## How to Run

```bash
python api_client.py
```

Requires an internet connection.

## Example

```
REST API Client
------------------------------
API: https://jsonplaceholder.typicode.com

--- GET: Fetching 3 posts ---
  [1] sunt aut facere repellat provident occaecati excepturi opt
  [2] qui est esse
  [3] ea molestias quasi exercitationem repellat qui ipsa sit aut

--- GET: Single post (#1) ---
  Title:  sunt aut facere repellat provident occaecati excepturi optio reprehenderit
  Body:   quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nrepMDASH...
  Author: User #1

--- GET: Comments on post #1 ---
  5 comments found:
    • id labore ex et quam laborum (Eliseo@gardner.biz)
    • quo vero reiciendis velit similique earum (Jayne_Kuhic@sydney.com)
    • odio adipisci rerum aut animi (Nikita@garfield.biz)

--- POST: Creating a new post ---
  Created post with ID: 101
  Title: Hello from Python!

--- GET: User details (#1) ---
  Name:    Leanne Graham
  Email:   Sincere@april.biz
  Company: Romaguera-Crona
```

## What You'll Learn

- Making GET and POST requests with `requests`
- Query parameters and JSON payloads
- Parsing JSON responses into Python dictionaries
- Error handling for connection, timeout, and HTTP errors
- Using a wrapper function for consistent error handling
