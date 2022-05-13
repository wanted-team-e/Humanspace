import pytest

from studies.tests.factories import StudyFactory, InstituteFactory
from pytest_factoryboy import register

from django.core.management import call_command
from rest_framework.test import APIClient

"""
    작성자 : 강정희
"""


register(StudyFactory)
register(InstituteFactory)


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'testdata.json')


@pytest.fixture()
def client():
    return APIClient()


# test error message custom
def pytest_assertrepr_compare(left, right, op):
    print("Assertion 왼쪽 값은 {0}, 오른쪽 값은 {1}, 비교 값은 {2}".format(left, right, op))
