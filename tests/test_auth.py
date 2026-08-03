def test_login_successful(client):
    client.post(
        "/users",
        json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["access_token"] is not None
    assert data["token_type"] == "bearer"


def test_login_with_wrong_password(client):
    client.post(
        "/users",
        json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "test@gmail.com",
            "password": "Arroz123!"
        }
    )

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Invalid email or password."


def test_login_with_nonexistent_email(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "test@gmail.com",
            "password": "Arroz123!"
        }
    )

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Invalid email or password."


def test_access_protected_endpoint_without_token(client):
    response = client.get(
        "/tasks"
    )

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Not authenticated"
    assert response.headers["WWW-Authenticate"] == "Bearer"


def test_access_protected_endpoint_with_invalid_token(client):
    response = client.get(
        "/tasks",
        headers={
            "Authorization": "Bearer invalid_token"
        }
    )

    assert response.status_code == 401

    data = response.json()

    assert data["detail"] == "Could not validate credentials"
