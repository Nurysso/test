import httpx

BASE = 'http://example.com'

def return_order_id():
    return '12345'

def poll(inc_id: str, label: str) -> None:
    for _ in range(60):
        try:
            r = httpx.get(f"{BASE}/incidents/{inc_id}/", timeout=10)
            data = r.json()
            if 'items' in data and len(data['items']) > 5:
                print(data['items'][5])
            else:
                print('No item at index 5')
        except httpx.RequestError as e:
            print(f'Request error: {e}')