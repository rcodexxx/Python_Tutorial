import os

import pytest

from src.scripts.task_flow.check_member_folder import check_member_folder


@pytest.fixture
def student_id():
    return "123456"

def test_folder_does_not_exist(student_id):
    success, errors = check_member_folder(student_id)
    assert success is False
    assert len(errors) == 1
    assert errors