import re
import pytest
from test_data import pregenerated_vars


@pytest.mark.parametrize('student_code', ['as_string'], indirect=True)
def test_pregenerated_vars_unchanged(student_code):
    for var, var_value in pregenerated_vars.items():
        if var in student_code:
            assert str(var_value) in student_code, 'Проверьте изначальное значение переменоой {}'.format(var)


@pytest.mark.run(order=1)
@pytest.mark.parametrize('student_code', ['as_list'], indirect=True)
def test_pregenerated_vars_exist(student_code, student_vars):
    assert all(var in student_vars for var in pregenerated_vars), 'Похоже вы удалили изначальные переменные, ' \
                                                                  'верните их или нажмите кнопку "Заново"'


@pytest.mark.run(order=2)
def test_output_appearence(student_output, correct_output):
    if student_output[0] == '\n':
        raise AssertionError('Возможно вы забыли убрать пустую строку в начале вашего вывода')
    student_output_formatted = student_output.strip().split('\n')
    assignment_output_formatted = correct_output.strip().split('\n')

    assert student_output_formatted[0] == assignment_output_formatted[0], 'Проверьте заголовок вашего вывода'
    assert student_output_formatted[1] == assignment_output_formatted[1],\
        'Проверьте разделительную строку вашего вывода'


@pytest.mark.parametrize('student_code', ['as_list'], indirect=True)
def test_student_use_for_loop(student_code):
    student_code_formatted = list(map(lambda s: s.strip(), student_code))

    regex_idx_pattern = re.compile('for\s\w+\sin\srange')
    for line in student_code_formatted:
        matched_idx_iterator = regex_idx_pattern.match(line)
        if matched_idx_iterator:
            raise AssertionError("В этом задании не нужно использовать range")


@pytest.mark.run(order=3)
def test_output_value(student_output, correct_output):
    task_limit = 10
    student_output_formatted = student_output.strip().split('\n')
    output_len = len(student_output_formatted[2:])
    assert not output_len < task_limit, 'Ваш вывод меньше ожидаемого,' \
                                        ' проверьте границы выборки, вам нужны первые {} элементов'.format(task_limit)
    assert not output_len > task_limit, 'Ваш вывод больше ожидаемого, ' \
                                        'проверьте не забыли ли вы использовать срезы или проверьте границы выборки,' \
                                        ' вам нужны первые {} элементов'.format(task_limit)
    assignment_output_formatted = correct_output.strip().split('\n')
    assert student_output_formatted[2:] == assignment_output_formatted[2:], 'Проверьте значения вашей выборки'
