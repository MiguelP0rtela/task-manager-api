from app.database.database import get_db
from app.models.user import User
from app.core.security import hash_password
from tests.conftest import TestingSessionLocal


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


def create_admin():
    db = TestingSessionLocal()

    admin = User(
        username="admin",
        email="admin@test.com",
        password=hash_password("Admin123!"),
        role="admin",
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)
    db.close()

    return admin

def test_get_user_successfully(client):
    admin = create_admin()

    response = client.post(
        "/users",
        json={
            "username": "getuser",
            "email": "getuser@test.com",
            "password": "Teste123!",
        },
    )

    user_id = response.json()["id"]

    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin@test.com",
            "password": "Admin123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        f"/users/{user_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == user_id
    assert data["username"] == "getuser"
    assert data["email"] == "getuser@test.com"

def test_get_nonexistent_user(client):
    create_admin()

    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin@test.com",
            "password": "Admin123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/users/9999",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found."

def test_update_user_successfully(client):
    create_admin()

    user_response = client.post(
        "/users",
        json={
            "username": "olduser",
            "email": "old@test.com",
            "password": "Teste123!",
        },
    )

    user_id = user_response.json()["id"]

    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin@test.com",
            "password": "Admin123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.put(
        f"/users/{user_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "username": "newuser",
            "email": "new@test.com",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["username"] == "newuser"
    assert data["email"] == "new@test.com"

def test_update_nonexistent_user(client):
    create_admin()

    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin@test.com",
            "password": "Admin123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.put(
        "/users/9999",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "username": "newuser",
            "email": "new@test.com",
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_delete_user_successfully(client):
    create_admin()

    user_response = client.post(
        "/users",
        json={
            "username": "deleteuser",
            "email": "delete@test.com",
            "password": "Teste123!",
        },
    )

    user_id = user_response.json()["id"]

    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin@test.com",
            "password": "Admin123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.delete(
        f"/users/{user_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 204

    response = client.get(
        f"/users/{user_id}",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 404

def test_delete_nonexistent_user(client):
    create_admin()

    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin@test.com",
            "password": "Admin123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.delete(
        "/users/9999",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"

def test_change_password_with_wrong_current_password(client):
    client.post(
        "/users",
        json={
            "username": "passworduser",
            "email": "password@test.com",
            "password": "Teste123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "password@test.com",
            "password": "Teste123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.patch(
        "/users/me/password",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "old_password": "WrongPassword123!",
            "new_password": "NewPassword123!",
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Current password is incorrect."

def test_change_password_to_same_password(client):
    client.post(
        "/users",
        json={
            "username": "samepassword",
            "email": "samepassword@test.com",
            "password": "Teste123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "samepassword@test.com",
            "password": "Teste123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.patch(
        "/users/me/password",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "old_password": "Teste123!",
            "new_password": "Teste123!",
        },
    )

    assert response.status_code == 409
    assert response.json()["detail"] == (
        "The new password must be different from the current password."
    )

def test_change_password_successfully(client):
    client.post(
        "/users",
        json={
            "username": "changepassword",
            "email": "changepassword@test.com",
            "password": "Teste123!",
        },
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "changepassword@test.com",
            "password": "Teste123!",
        },
    )

    token = login_response.json()["access_token"]

    response = client.patch(
        "/users/me/password",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "old_password": "Teste123!",
            "new_password": "NewPassword123!",
        },
    )

    assert response.status_code == 204

    login_response = client.post(
        "/auth/login",
        data={
            "username": "changepassword@test.com",
            "password": "NewPassword123!",
        },
    )

    assert login_response.status_code == 200

