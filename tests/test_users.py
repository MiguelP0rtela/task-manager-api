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


def test_password_too_short(client):
    user = {
        "username": "miguel",
        "email": "miguel@gmail.com",
        "password": "Test12!"
    }

    response = client.post("/users", json=user)

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == "password" and "at least 8 characters" in error["msg"].lower()
        for error in errors
    )


def test_password_without_uppercase_letter(client):
    user = {
        "username": "miguel",
        "email": "miguel@gmail.com",
        "password": "test123!"
    }
    response = client.post("/users", json=user)

    assert response.status_code == 422
    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == "password" and "one uppercase letter" in error["msg"].lower()
        for error in errors
    )


def test_password_without_lowercase_letter(client):
    user = {
        "username": "miguel",
        "email": "miguel@gmail.com",
        "password": "TEST123!"
    }
    response = client.post("/users", json=user)

    assert response.status_code == 422
    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == "password" and "one lowercase letter" in error["msg"].lower()
        for error in errors
    )


def test_password_without_number(client):
    user = {
        "username": "miguel",
        "email": "miguel@gmail.com",
        "password": "Teste!@#%!"
    }
    response = client.post("/users", json=user)

    assert response.status_code == 422
    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == "password" and "one number" in error["msg"].lower()
        for error in errors
    )


def test_password_without_special_characters(client):
    user = {
        "username": "miguel",
        "email": "miguel@gmail.com",
        "password": "Teste12345"
    }
    response = client.post("/users", json=user)

    assert response.status_code == 422
    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == "password" and "one special character" in error["msg"].lower()
        for error in errors
    )
