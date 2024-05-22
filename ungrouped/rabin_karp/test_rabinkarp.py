'''
test_rabinkarp.py - Unit tests for the rabin_karp()
Written by Sergey Torshin @torshin5ergey
'''

from rabinkarp import rabin_karp

def test_rabin_karp_smoke():
    assert rabin_karp('Rabin Karp', 'Rabin') == 0
    assert rabin_karp('Rabin Karp', 'Karp') == 6
    assert rabin_karp('Rabin Karp', 'Rabin Karp') == 0

    assert rabin_karp('Rabin Karp', 'foo') == -1
    assert rabin_karp('', 'foo') == -1
    assert rabin_karp('Rabin Karp', '') == 0
    assert rabin_karp('Rabin', 'Rabin Karp') == -1