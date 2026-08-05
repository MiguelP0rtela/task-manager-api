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
