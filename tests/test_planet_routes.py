
def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, one_planet):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "name": "planet_x",
        "description": "xxxx",
        "star": "x stars"
    }



def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "planet_y",
        "description": "yyyy",
        "star": "y stars"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "name": "planet_y",
        "description": "yyyy",
        "star": "y stars"
    }