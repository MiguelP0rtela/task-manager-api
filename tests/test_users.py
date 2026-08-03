from idlelib.rpc import response_queue


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_create_users(client):
    response = client.post(
        "/users",
        json={
            "username": "testpython",
            "email": "testpython@gmail.com",
            "password": "12345"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == "testpython"
    assert data["email"] == "testpython@gmail.com"
    assert "id" in data


def test_create_duplicated_user(client):
    user = {
        "username": "miguel",
        "email": "miguel@gmail.com",
        "password": "12345"
    }

    client.post(
        "/users",
        json=user
    )

    response = client.post("/users", json=user)

    assert response.status_code == 409
    assert response.json()["detail"] == "The email or username already exists."


def test_no_data(client):
    user = {
        "username": "miguel",
        "email": "miguel@gmail.com",
        "password": ""
    }

    response = client.post("/users", json=user)
    assert response.status_code == 422


