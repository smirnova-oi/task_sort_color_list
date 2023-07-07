import pytest
from sort_list import sort_list


@pytest.fixture
def rules():
    return ('З', 'С', 'К')


def test_sort_list(rules):
    assert sort_list(rules, ['С', 'З', 'С', 'З', 'К', 'З']) == ['З', 'З', 'З', 'С', 'С', 'К']
    assert sort_list(rules, ['К', 'С']) == ['С', 'К']
    assert sort_list(rules, ['К']) == ['К']
    assert sort_list(rules, []) == []

    # Невалидный тип правила
    with pytest.raises(TypeError):
        sort_list(rules="wrong_rules_type", color_lst=['К'])

    # Невалидный тип входного списка
    with pytest.raises(TypeError):
        sort_list(rules=('К'), color_lst="wrong_color_list_type")

    # Пустое правило. Предполагаем, что это недопустимо
    with pytest.raises(Exception):
        sort_list(rules=(), color_lst=['К'])

    # Регистр важен, т.к. в задании иного не указаного
    with pytest.raises(KeyError):
        sort_list(rules=rules, color_lst=['к'])

    # K - другой раскладки
    with pytest.raises(KeyError):
        sort_list(rules=rules, color_lst=['З', 'K'])

    # None как объекты, в том числе и на границе
    with pytest.raises(KeyError):
        sort_list(rules=rules, color_lst=[None])
    with pytest.raises(KeyError):
        sort_list(rules=rules, color_lst=['С', None])

    # итерируемый объект как элемент списка
    with pytest.raises(KeyError):
        sort_list(rules=rules, color_lst=[('С', 'К'), 'С'])

    # Повторяющиеся элементы правила
    with pytest.raises(Exception):
        sort_list(rules=('С', 'К', 'С'), color_lst=['С', 'К'])
