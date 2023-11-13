def roman_numerals_to_int(roman_numeral):
    roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_num = 0

    if not isinstance(roman_numeral, str):
        return None

    for i in range(len(roman_numeral)):
        if roman_numeral[i] not in roman_to_int:
            return None
        if i > 0 and roman_to_int[roman_numeral[i]] > roman_to_int[roman_numeral[i - 1]]:
            int_num += roman_to_int[roman_numeral[i]] - 2 * roman_to_int[roman_numeral[i - 1]]
        else:
            int_num += roman_to_int[roman_numeral[i]]

    return int_num
print(roman_numerals_to_int('V'))