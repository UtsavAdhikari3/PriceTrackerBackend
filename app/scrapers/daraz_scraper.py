import requests

BASE_URL = "https://www.daraz.com.np/catalog/"


def search_daraz(query: str, page: int = 1):
    params = {
        "ajax": "true",
        "isFirstRequest": "true",
        "page": page,
        "q": query
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(BASE_URL, params=params, headers=headers)

    if response.status_code != 200:
        return []

    data = response.json()

    # navigate into JSON
    items = data.get("mods", {}).get("listItems", [])

    products = []

    for item in items:
        try:
            title = item.get("name")
            price = float(item.get("price", 0))
            image = item.get("image")
            url = item.get("itemUrl")

            # fix URL (// → https://)
            if url and url.startswith("//"):
                url = "https:" + url

            products.append({
                "title": title,
                "price": price,
                "url": url,
                "image": image,
                "platform": "daraz"
            })

        except Exception:
            continue

    return products



result = search_daraz("iphone",1)

print(result)