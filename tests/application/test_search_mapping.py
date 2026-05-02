from application.search_mapping import map_search

def test_map_search():

    result = map_search("ICN", "CDG", 15, 30)
    assert result["origin"] == "ICN"
    assert result["destination"] == "CDG"
    assert result["stay_duration"] == 15
    assert result["search_period"] == 30
    assert "created_at" in result