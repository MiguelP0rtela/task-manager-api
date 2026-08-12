from http.client import responses


def test_create_task_successfully(client):
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

    response = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
        headers={
            "Authorization": f"Bearer {token}"

        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Teste"
    assert data["content"] == "Lore ipsum etc"


def test_create_task_without_authentification(client):
    response = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
    )

    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Not authenticated"


def test_list_tasks_successfully(client):
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

    task_response = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert task_response.status_code == 201

    response = client.get(
        "/tasks/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Teste"
    assert data[0]["content"] == "Lore ipsum etc"


def test_get_tasks_without_authentification(client):
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

    task_response = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    assert task_response.status_code == 201

    response = client.get(
        "/tasks/",
    )

    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Not authenticated"


def test_get_task_by_id_successfully(client):
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

    task_created = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert task_created.status_code == 201

    task_id = task_created.json()["id"]

    response = client.get(
        f"/tasks/{task_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Teste"
    assert data["content"] == "Lore ipsum etc"


def test_get_task_by_id_unsuccessfully(client):
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

    task_created = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert task_created.status_code == 201

    response = client.get(
        "/tasks/2",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Task not found."


def test_update_task_successfully(client):
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

    task_created = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert task_created.status_code == 201

    task_id = task_created.json()["id"]

    response = client.patch(
        f"/tasks/{task_id}",
        json={
            "title": "New Title",
            "content": "New Content"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "New Title"
    assert data["content"] == "New Content"


def test_update_task_not_found(client):
    client.post(
        "/users",
        json={
            "username": "test",
            "email": "test@gmail.com",
            "password": "Test123!"
        }
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "test@gmail.com",
            "password": "Test123!"
        }
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]

    response = client.patch(
        "/tasks/9999",
        json={
            "title": "New Title",
            "content": "New Content"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404

    data = response.json()

    assert data["detail"] == "Task not found."


def test_update_task_without_authentification(client):
    response = client.patch(
        "/tasks/9999",
        json={
            "title": "New Title",
            "content": "New Content"
        },
    )

    data = response.json()

    assert response.status_code == 401
    assert data["detail"] == "Not authenticated"


def test_delete_task_successfully(client):
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

    task_created = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert task_created.status_code == 201

    task_id = task_created.json()["id"]

    deleted_task = client.delete(
        f"/tasks/{task_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert deleted_task.status_code == 204


def test_delete_unexisted_task(client):
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

    response = client.delete(
        f"/tasks/1",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 404


def test_delete_task_without_authentification(client):
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

    task_created = client.post(
        "/tasks/",
        json={
            "title": "Teste",
            "content": "Lore ipsum etc"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert task_created.status_code == 201

    task_id = task_created.json()["id"]

    deleted_task = client.delete(
        f"/tasks/{task_id}",

    )

    assert deleted_task.status_code == 401


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


def create_task(client, token, title="Test task", content="Test content"):
    response = client.post(
        "/tasks",
        json={
            "title": title,
            "content": content,
        },
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 201

    return response.json()


def test_user_can_create_task(client):
    token = create_user_and_get_token(
        client,
        "user1",
        "user1@gmail.com",
        "Teste123!",
    )

    response = client.post(
        "/tasks",
        json={
            "title": "My task",
            "content": "My task content",
        },
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "My task"
    assert data["content"] == "My task content"
    assert "id" in data


def test_user_only_sees_own_tasks(client):
    token1 = create_user_and_get_token(
        client,
        "user1",
        "user1@gmail.com",
        "Teste123!",
    )

    token2 = create_user_and_get_token(
        client,
        "user2",
        "user2@gmail.com",
        "Teste123!",
    )

    create_task(
        client,
        token1,
        "User 1 task",
        "Private task",
    )

    response = client.get(
        "/tasks",
        headers={
            "Authorization": f"Bearer {token2}"
        },
    )

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) == 0


def test_user_cannot_get_another_users_task(client):
    token1 = create_user_and_get_token(
        client,
        "user1",
        "user1@gmail.com",
        "Teste123!",
    )

    token2 = create_user_and_get_token(
        client,
        "user2",
        "user2@gmail.com",
        "Teste123!",
    )

    task = create_task(
        client,
        token1,
        "Private task",
        "User 1 content",
    )

    response = client.get(
        f"/tasks/{task['id']}",
        headers={
            "Authorization": f"Bearer {token2}"
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found."


def test_user_can_get_own_task(client):
    token = create_user_and_get_token(
        client,
        "user1",
        "user1@gmail.com",
        "Teste123!",
    )

    task = create_task(
        client,
        token,
        "My task",
        "My content",
    )

    response = client.get(
        f"/tasks/{task['id']}",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task["id"]
    assert data["title"] == "My task"


def test_user_cannot_update_another_users_task(client):
    token1 = create_user_and_get_token(
        client,
        "user1",
        "user1@gmail.com",
        "Teste123!",
    )

    token2 = create_user_and_get_token(
        client,
        "user2",
        "user2@gmail.com",
        "Teste123!",
    )

    task = create_task(
        client,
        token1,
        "Original title",
        "Original content",
    )

    response = client.patch(
        f"/tasks/{task['id']}",
        json={
            "title": "Hacked title",
        },
        headers={
            "Authorization": f"Bearer {token2}"
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found."


def test_user_can_update_own_task(client):
    token = create_user_and_get_token(
        client,
        "user1",
        "user1@gmail.com",
        "Teste123!",
    )

    task = create_task(
        client,
        token,
        "Original title",
        "Original content",
    )

    response = client.patch(
        f"/tasks/{task['id']}",
        json={
            "title": "Updated title",
        },
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated title"


def test_user_cannot_delete_another_users_task(client):
    token1 = create_user_and_get_token(
        client,
        "user1",
        "user1@gmail.com",
        "Teste123!",
    )

    token2 = create_user_and_get_token(
        client,
        "user2",
        "user2@gmail.com",
        "Teste123!",
    )

    task = create_task(
        client,
        token1,
        "Private task",
        "Private content",
    )

    response = client.delete(
        f"/tasks/{task['id']}",
        headers={
            "Authorization": f"Bearer {token2}"
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found."


def test_user_can_delete_own_task(client):
    token = create_user_and_get_token(
        client,
        "user1",
        "user1@gmail.com",
        "Teste123!",
    )

    task = create_task(
        client,
        token,
        "Task to delete",
        "Delete me",
    )

    response = client.delete(
        f"/tasks/{task['id']}",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 204
