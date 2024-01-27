from rest_framework.test import APIClient
import pytest
from model_bakery import baker

from students.models import Course, Student


# Фикстура для APIClient
@pytest.fixture
def client():
    return APIClient()


# Фикстура для создания курса
@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


# Фикстура для создания студента
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


# Тест для получения первого курса
@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    course = course_factory(_quantity=1)[0]
    response = client.get(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course.id
    assert data['name'] == course.name


# Тест для получения списка курсов
@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=5)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name


# Тест для фильтрации курсов по id
@pytest.mark.django_db
def test_filter_courses_by_id(client, course_factory):
    courses = course_factory(_quantity=50)[30].id
    response = client.get(f'/api/v1/courses/?id={courses}')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['id'] == courses


# Тест для фильтрации курсов по name
@pytest.mark.django_db
def test_filter_courses_by_name(client, course_factory):
    courses = course_factory(_quantity=50)[30].name
    response = client.get(f'/api/v1/courses/?name={courses}')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == courses


# Тест для успешного создания курса
@pytest.mark.django_db
def test_create_course(client):
    course = {
        'name': 'Python',
    }
    response = client.post('/api/v1/courses/', course)
    assert response.status_code == 201


# Тест для успешного обновления курса
@pytest.mark.django_db
def test_course_update(client, course_factory):
    courses = course_factory(_quantity=1)
    course_data = {
        'name': 'Python',
    }
    response = client.patch(f'/api/v1/courses/{courses[0].id}/', course_data)
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == course_data['name']


# Тест для успешного удаления курса
@pytest.mark.django_db
def test_course_delete(client, course_factory):
    courses = course_factory(_quantity=1)
    response = client.delete(f'/api/v1/courses/{courses[0].id}/')
    assert response.status_code == 204
