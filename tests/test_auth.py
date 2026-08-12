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

def test_refresh_token_successful(client):
    client.post(
        "/users",
        json={
            "username": "refreshuser",
            "email": "refresh@gmail.com",
            "password": "Teste123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "refresh@gmail.com",
            "password": "Teste123!",
        },
    )

    assert login_response.status_code == 200

    refresh_token = login_response.json()["refresh_token"]

    response = client.post(
        "/auth/refresh",
        json={
            "refresh_token": refresh_token,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["access_token"] is not None
    assert data["refresh_token"] is not None
    assert data["token_type"] == "bearer"

    assert data["refresh_token"] != refresh_token

def test_old_refresh_token_cannot_be_reused(client):
    client.post(
        "/users",
        json={
            "username": "refreshuser",
            "email": "refresh@gmail.com",
            "password": "Teste123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "refresh@gmail.com",
            "password": "Teste123!",
        },
    )

    refresh_token = login_response.json()["refresh_token"]

    first_response = client.post(
        "/auth/refresh",
        json={
            "refresh_token": refresh_token,
        },
    )

    assert first_response.status_code == 200

    second_response = client.post(
        "/auth/refresh",
        json={
            "refresh_token": refresh_token,
        },
    )

    assert second_response.status_code == 401
    assert second_response.json()["detail"] == "Refresh token revoked."

def test_refresh_with_invalid_token(client):
    response = client.post(
        "/auth/refresh",
        json={
            "refresh_token": "invalid_refresh_token",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid refresh token."

def test_logout_successful(client):
    client.post(
        "/users",
        json={
            "username": "logoutuser",
            "email": "logout@gmail.com",
            "password": "Teste123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "logout@gmail.com",
            "password": "Teste123!",
        },
    )

    assert login_response.status_code == 200

    refresh_token = login_response.json()["refresh_token"]

    response = client.post(
        "/auth/logout",
        json={
            "refresh_token": refresh_token,
        },
    )

    assert response.status_code == 200
    assert response.json()["message"] == "Logged out successfully."

def test_refresh_token_cannot_be_used_after_logout(client):
    client.post(
        "/users",
        json={
            "username": "logoutuser",
            "email": "logout@gmail.com",
            "password": "Teste123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "logout@gmail.com",
            "password": "Teste123!",
        },
    )

    refresh_token = login_response.json()["refresh_token"]

    logout_response = client.post(
        "/auth/logout",
        json={
            "refresh_token": refresh_token,
        },
    )

    assert logout_response.status_code == 200

    refresh_response = client.post(
        "/auth/refresh",
        json={
            "refresh_token": refresh_token,
        },
    )

    assert refresh_response.status_code == 401
    assert refresh_response.json()["detail"] == "Refresh token revoked."

def test_logout_with_invalid_token(client):
    response = client.post(
        "/auth/logout",
        json={
            "refresh_token": "invalid_refresh_token",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid refresh token."

def test_logout_already_revoked_token(client):
    client.post(
        "/users",
        json={
            "username": "logoutuser",
            "email": "logout@gmail.com",
            "password": "Teste123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "logout@gmail.com",
            "password": "Teste123!",
        },
    )

    refresh_token = login_response.json()["refresh_token"]

    first_logout = client.post(
        "/auth/logout",
        json={
            "refresh_token": refresh_token,
        },
    )

    assert first_logout.status_code == 200

    second_logout = client.post(
        "/auth/logout",
        json={
            "refresh_token": refresh_token,
        },
    )

    assert second_logout.status_code == 401
    assert second_logout.json()["detail"] == "Refresh token already revoked."