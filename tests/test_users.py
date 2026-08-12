def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_create_users_successfully(client):
    response = client.post(
        "/users",
        json={
            "username": "testpython",
            "email": "testpython@gmail.com",
            "password": "Teste123!"
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
        "password": "Teste123!"
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


def create_user_and_get_token(client, username, email, password):
    client.post(
        "/users",
        json={
            "username": username,
            "email": email,
            "password": password,
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": email,
            "password": password,
        },
    )

    assert response.status_code == 200

    return response.json()["access_token"]


def test_user_cannot_get_all_users(client):
    token = create_user_and_get_token(
        client,
        "normaluser",
        "normaluser@gmail.com",
        "Teste123!",
    )

    response = client.get(
        "/users",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Admin privileges required."


def test_user_cannot_get_user_by_id(client):
    token = create_user_and_get_token(
        client,
        "normaluser",
        "normaluser@gmail.com",
        "Teste123!",
    )

    response = client.get(
        "/users/1",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Admin privileges required."


def test_user_cannot_update_user(client):
    token = create_user_and_get_token(
        client,
        "normaluser",
        "normaluser@gmail.com",
        "Teste123!",
    )

    response = client.put(
        "/users/1",
        json={
            "username": "hacker",
            "email": "hacker@gmail.com",
        },
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Admin privileges required."


def test_user_cannot_delete_user(client):
    token = create_user_and_get_token(
        client,
        "normaluser",
        "normaluser@gmail.com",
        "Teste123!",
    )

    response = client.delete(
        "/users/1",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 403
    assert response.json()["detail"] == "Admin privileges required."


def test_user_can_access_own_profile(client):
    token = create_user_and_get_token(
        client,
        "normaluser",
        "normaluser@gmail.com",
        "Teste123!",
    )

    response = client.get(
        "/users/me",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "normaluser"
    assert data["email"] == "normaluser@gmail.com"


def test_admin_can_get_all_users(client, admin_user):
    response = client.post(
        "/auth/login",
        data={
            "username": "admin@gmail.com",
            "password": "Admin123!",
        },
    )

    assert response.status_code == 200

    token = response.json()["access_token"]

    response = client.get(
        "/users",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_admin_can_get_user(client, admin_user):
    response = client.post(
        "/auth/login",
        data={
            "username": "admin@gmail.com",
            "password": "Admin123!",
        },
    )

    token = response.json()["access_token"]

    response = client.get(
        "/users/1",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200
