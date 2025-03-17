# tests.py

import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Group
from .models import Product

@pytest.mark.django_db
def test_manager_access():
    # Create a user and assign to 'Manager' group
    user = User.objects.create_user(username='manageruser', password='password')
    manager_group = Group.objects.get(name='Manager')
    user.groups.add(manager_group)

    # Log in as the manager
    client = APIClient()
    client.login(username='manageruser', password='password')

    # Test accessing manager-only endpoint
    response = client.get('/products/')
    assert response.status_code == 200  # Should be allowed to access

@pytest.mark.django_db
def test_employee_access():
    # Create a user and assign to 'Employee' group
    user = User.objects.create_user(username='employeeuser', password='password')
    employee_group = Group.objects.get(name='Employee')
    user.groups.add(employee_group)

    # Log in as the employee
    client = APIClient()
    client.login(username='employeeuser', password='password')

    # Test accessing employee-only endpoint
    response = client.get('/products/')
    assert response.status_code == 200  # Should be allowed to access

@pytest.mark.django_db
def test_manager_access_denied_for_employee():
    # Create a user and assign to 'Employee' group
    user = User.objects.create_user(username='employeeuser', password='password')
    employee_group = Group.objects.get(name='Employee')
    user.groups.add(employee_group)

    # Log in as the employee
    client = APIClient()
    client.login(username='employeeuser', password='password')

    # Test accessing manager-only endpoint
    response = client.get('/products/')
    assert response.status_code == 403  # Should be denied access
