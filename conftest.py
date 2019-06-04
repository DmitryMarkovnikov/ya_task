import pytest
import re
import inspect

from solutions.student_A import incorrect_solution, correct_solution


@pytest.fixture()
def student_vars(student_code):
    """
    Returns variables created by student, takes student_code fixture as an input
    Notice: if student code parametrized as a string this fixture will raise an error.
    :return: list with variables defined by user
    """
    if isinstance(student_code, str):
        raise NotImplementedError('Student code is not as expected, should be list, not string.')
    rv = []
    str_pattern = '\w*\s*='
    pattern = re.compile(str_pattern)
    for line in student_code:
        matched = pattern.match(line)
        if matched:
            rv.append(matched.group().replace('=', '').rstrip())
    return rv


@pytest.fixture()
def student_code(request, solution_type):
    """
    Returns the code created by student, can be correct and incorrect, based on solution type fixture value
    takes solution_type fixture as an inout to inspect correct or incorrect solution.

    :return: If parametrized `as_string` will return code as a string,
     if parametrized `as_list` will return code as a list
    """

    if solution_type == 'correct':
        solution = correct_solution
    elif solution_type == 'incorrect':
        solution = incorrect_solution

    if 'as_list' in request.param:
        return inspect.getsourcelines(solution)[0]
    elif 'as_string' in request.param:
        return inspect.getsource(solution)

    else:
        raise NotImplementedError('Cannot return code in such format')


@pytest.fixture(scope='session')
def student_output():
    """
    Fixture returns a student output as a string
    :return: string with student output
    """
    output = open('user_output.txt', 'r').read()
    return output


@pytest.fixture(scope='session')
def correct_output():
    """
    Fixture returns correct output solution as a string
    :return: string with correct output
    """
    output = open('correct_output.txt', 'r').read()
    return output


@pytest.fixture(autouse=True, scope='session')
def erase_user_output():
    """
    Helper fixture, erases all user output from file, to disable make autouse=False
    :return: None
    """
    yield
    open('user_output.txt', 'w').close()


def pytest_addoption(parser):
    """
    Just add new option to pytest executor
    """
    parser.addoption(
        "--solution-type", action="store", default="correct", help="which solution to test, correct or incorrect"
    )


@pytest.fixture
def solution_type(request):
    """
    FIxture that parses flag of pytest executor
    """
    return request.config.getoption("--solution-type")
