from project.lychrel import is_lychrel_number

def test_is_lychrel_number():
    """Um número lychrel deve retornar True. Um número palíndromo deve retornar False"""
    assert is_lychrel_number(196) is True
    assert is_lychrel_number(11) is False