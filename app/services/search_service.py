from app.scrapers.daraz_scraper import search_daraz


def search_products(query: str):
    results = search_daraz(query)

    # limit results (important)
    return results[:30]