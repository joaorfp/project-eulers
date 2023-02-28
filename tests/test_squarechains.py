from project.squarechains import square_sum

def test_square_chain():
    """Testa se o número dado termina em 89 ou em 1 (89 significa true)"""
    assert square_sum(85) is True
    assert square_sum(44) is False