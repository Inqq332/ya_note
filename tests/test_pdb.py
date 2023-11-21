from pytest_django.asserts import assertRedirects
# test_pdb.py
def transform_list(x):
    x.append(1)
    x.extend([2, 3])
    return x


def test_list():
    a = []
    a = transform_list(a)
    a = [4] + a
    assert a == [4, 1, 2, 3]

def test_with_client(client):
    response = client.get('/')
    assert response.status_code == 200
    
def test_closed_page(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200

def test_with_authenticated_client(client, django_user_model):
    user = django_user_model.objects.create(username='yanote_user')
    # Логиним пользователя в клиенте без указания пароля:
    client.force_login(user)
    response = client.get('/')
    assert response.status_code == 200 