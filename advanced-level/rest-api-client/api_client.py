# REST API Client
# Demonstrates making HTTP requests to a public REST API,
# parsing JSON responses, and handling errors gracefully.
# Uses the free JSONPlaceholder API (https://jsonplaceholder.typicode.com).

try:
    import requests
except ImportError:
    print("This example requires the 'requests' library.")
    print("Install it with:  pip install requests")
    exit(1)


BASE_URL = "https://jsonplaceholder.typicode.com"


def get_posts(limit=5):
    """Fetch a list of posts."""
    response = requests.get(f"{BASE_URL}/posts", params={"_limit": limit}, timeout=10)
    response.raise_for_status()
    return response.json()


def get_post(post_id):
    """Fetch a single post by ID."""
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=10)
    response.raise_for_status()
    return response.json()


def get_comments(post_id):
    """Fetch comments for a specific post."""
    response = requests.get(f"{BASE_URL}/posts/{post_id}/comments", timeout=10)
    response.raise_for_status()
    return response.json()


def create_post(title, body, user_id=1):
    """Create a new post (simulated — JSONPlaceholder returns the object but doesn't persist it)."""
    payload = {"title": title, "body": body, "userId": user_id}
    response = requests.post(f"{BASE_URL}/posts", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


def get_user(user_id):
    """Fetch user details."""
    response = requests.get(f"{BASE_URL}/users/{user_id}", timeout=10)
    response.raise_for_status()
    return response.json()


def safe_request(func, *args, **kwargs):
    """Wrapper that handles common HTTP errors."""
    try:
        return func(*args, **kwargs)
    except requests.ConnectionError:
        print("  Error: Could not connect to the API. Check your internet connection.")
    except requests.Timeout:
        print("  Error: Request timed out.")
    except requests.HTTPError as e:
        print(f"  Error: HTTP {e.response.status_code} — {e.response.reason}")
    except requests.RequestException as e:
        print(f"  Error: {e}")
    return None


print("REST API Client")
print("-" * 30)
print(f"API: {BASE_URL}\n")

print("--- GET: Fetching 3 posts ---")
posts = safe_request(get_posts, limit=3)
if posts:
    for post in posts:
        print(f"  [{post['id']}] {post['title'][:60]}")

print("\n--- GET: Single post (#1) ---")
post = safe_request(get_post, 1)
if post:
    print(f"  Title:  {post['title']}")
    print(f"  Body:   {post['body'][:80]}...")
    print(f"  Author: User #{post['userId']}")

print("\n--- GET: Comments on post #1 ---")
comments = safe_request(get_comments, 1)
if comments:
    print(f"  {len(comments)} comments found:")
    for c in comments[:3]:
        print(f"    • {c['name']} ({c['email']})")

print("\n--- POST: Creating a new post ---")
new_post = safe_request(create_post, "Hello from Python!", "This post was created by the REST API client example.")
if new_post:
    print(f"  Created post with ID: {new_post['id']}")
    print(f"  Title: {new_post['title']}")

print("\n--- GET: User details (#1) ---")
user = safe_request(get_user, 1)
if user:
    print(f"  Name:    {user['name']}")
    print(f"  Email:   {user['email']}")
    print(f"  Company: {user['company']['name']}")

print("\n--- Error handling demo ---")
safe_request(get_post, 99999)
