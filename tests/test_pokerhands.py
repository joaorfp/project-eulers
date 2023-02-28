from project.pokerhands import rank_hand, compare_hands

def test_poker_hands():
    """Testa os cenários de mãos em uma partida de poker entre 2 jogadores"""
    assert rank_hand(['6H', '6C', 'JC', '3D', '3S']) is 3 
    assert compare_hands(['QC', 'KC', '3S', 'JC', 'KD'], ['2C', '8D', 'AH', 'QS', 'TS']) is True
    assert compare_hands(['9C', 'JD', '7C', '6D', 'TC'], ['6H', '6C', 'JC', '3D', '3S']) is False

    