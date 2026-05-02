from infrastructure.serp_api.serp_api_mapping import map_serpapi_to_offers

results = {
    "best_flights": [{"price": "123.45"}],
    "other_flights": [{"price": "233.12"}],
    "search_metadata": {"google_flights_url": "https://booking.test/serpapi-offer"}
}

def test_serp_api_mapping_best_and_other_flights():
    result = map_serpapi_to_offers(results)
    assert result[0].price == 123.45
    assert result[0].booking_link == "https://booking.test/serpapi-offer"
    assert result[1].price == 233.12
    assert result[1].booking_link == "https://booking.test/serpapi-offer"

results_no_best_flights = {
    "best_flights": [],
    "other_flights": [{"price": "233.12"}],
    "search_metadata": {"google_flights_url": "https://booking.test/serpapi-offer"}
}

def test_serp_api_mapping_other_flights_only():
    result = map_serpapi_to_offers(results_no_best_flights)
    assert result[0].price == 233.12
    assert result[0].booking_link == "https://booking.test/serpapi-offer"

results_no_other_flights = {
    "best_flights": [{"price": "123.45"}],
    "other_flights": [],
    "search_metadata": {"google_flights_url": "https://booking.test/serpapi-offer"}
}

def test_serp_api_mapping_best_flights_only():
    result = map_serpapi_to_offers(results_no_other_flights)
    assert result[0].price == 123.45
    assert result[0].booking_link == "https://booking.test/serpapi-offer"

results_missing_price = {
    "best_flights": [{"price": "123.45"}],
    "other_flights": [{"price": None}],
    "search_metadata": {"google_flights_url": "https://booking.test/serpapi-offer"}
}

def test_serp_api_mapping_price_missing():
    result = map_serpapi_to_offers(results_missing_price)
    assert result[0].price == 123.45
    assert result[0].booking_link == "https://booking.test/serpapi-offer"
    assert len(result) == 1