from project.prime import prime

def test_is_prime():
    """Testa se o número dado no parâmetro é  primo"""
    assert prime(4) is False
    assert prime(7) is True
