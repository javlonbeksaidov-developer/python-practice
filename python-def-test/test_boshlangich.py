from boshlangich import reverse, count_vowel

def test_reverse():
    assert reverse('') == ''
    assert reverse(' ') == ' '
    assert reverse('hello') == 'olleh'
    assert reverse('Hi, my name is Javlon') == 'nolvaJ si eman ym ,iH'
    assert reverse('123456789') == '987654321'


def test_count_vowel():
    assert count_vowel('') == 0
    assert count_vowel(' ') == 0
    assert count_vowel('Javlonbek') == 3
    assert count_vowel('AAaaOOooIIiiUUuuEEee') == 20
    assert count_vowel('aeuioAEUIO') == 10