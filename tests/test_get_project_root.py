import os
from src.utils import get_project_root


def test_get_project_root_correct_project_name():
    """
    Test get_project_root utility function with correct project name.
    """
    project_name = os.path.basename(os.getcwd())
    expected_result = os.getcwd()
    assert get_project_root.get_project_root(project_name) == expected_result


def test_get_project_root_incorrect_project_name(capfd):
    """
    Test get_project_root utility function with incorrect project name.
    """
    incorrect_project_name = 'nonexistent_project_name'
    assert get_project_root.get_project_root(incorrect_project_name) == os.getcwd()

    # Check output warning message
    out, err = capfd.readouterr()
    expected_err_mess = f"Incorrect project name sent to get_project_root function. " \
                        f"Argument given was {incorrect_project_name}. Returning current path\n"
    assert out == expected_err_mess


def test_get_project_root_empty_project_name(capfd):
    """
    Test get_project_root utility function with empty project name.
    """
    empty_project_name = ''
    assert get_project_root.get_project_root(empty_project_name) == os.getcwd()

    # Check output warning message
    out, err = capfd.readouterr()
    expected_err_mess = f"Incorrect project name sent to get_project_root function. " \
                        f"Argument given was {empty_project_name}. Returning current path\n"
    assert out == expected_err_mess
