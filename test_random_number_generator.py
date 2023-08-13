from random_number_generator import random_number_generate


def test_random_number_generator():
    for _ in range(10000):
        assert 0 <= random_number_generate() <= 1000
