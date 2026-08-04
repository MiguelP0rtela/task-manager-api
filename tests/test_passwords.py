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


def test_change_password_successfully(client):
    client.post(
        "/users",
        json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.patch(
        "/users/me/password",
        json={
            "old_password": "Teste123!",
            "new_password": "NewTest123!"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 204


def test_change_password_incorrectly(client):
    client.post(
        "/users",
        json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.patch(
        "/users/me/password",
        json={
            "old_password": "AnotherTeste123!",
            "new_password": "NewTest123!"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    data = response.json()

    assert response.status_code == 400
    assert data["detail"] == "Current password is incorrect."


def test_change_equal_passwords(client):
    client.post(
        "/users",
        json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.patch(
        "/users/me/password",
        json={
            "old_password": "Teste123!",
            "new_password": "Teste123!"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    data = response.json()

    assert response.status_code == 409
    assert data["detail"] == "The new password must be different from the current password."


def test_change_new_password_disprove(client):
    client.post(
        "/users",
        json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@gmail.com",
            "password": "Teste123!"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.patch(
        "/users/me/password",
        json={
            "old_password": "Teste123!",
            "new_password": "Teste123"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 422
    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == "new_password" and "one special character" in error["msg"].lower()
        for error in errors
    )


def test_change_password_without_authentication(client):
    response = client.patch(
        "/users/me/password",
        json={
            "old_password": "Teste123!",
            "new_password": "NewTest123!"
        }
    )

    assert response.status_code == 401

    data = response.json()
    assert data["detail"] == "Not authenticated"