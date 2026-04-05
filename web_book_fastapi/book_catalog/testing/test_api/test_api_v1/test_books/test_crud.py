from unittest import TestCase
import random


def total(num_a,num_b):
    return num_a + num_b


class TotalTestcase(TestCase):

    def test_total(self) -> None:
        num_a = random.randint(1,100)
        num_b = random.randint(1,100)
        result = total(num_a,num_b)
        expected_result = num_a + num_b
        self.assertEqual(expected_result, result)