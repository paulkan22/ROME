import unittest

from main import roman_numerals_to_int


class RomanNumeralsConverterTestCase(unittest.TestCase):
    def test_roman_numerals_to_int(self):
        # Набор тестовых данных и ожидаемых результатов
        test_cases = [
            ('I', 1),
            ('IV', 4),
            ('IX', 9),
            ('XII', 12),
            ('XLV', 45),
            ('XCIX', 99),
            ('CXXIX', 129),
            ('CDXLIX', 449),
            ('DCCCXC', 890),
            ('CMXCIX', 999),
            ('MCDXLIV', 1444),
            ('MMCMXCIX', 2999),
        ]

        for input_roman, expected_output in test_cases:
            with self.subTest(input_roman=input_roman, expected_output=expected_output):
                result = roman_numerals_to_int(input_roman)
                self.assertEqual(result, expected_output)


if __name__ == '__main__':
    unittest.main()
