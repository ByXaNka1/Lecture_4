#Завдання 1
def replace_quotes(string):
    result = ""
    for char in string:
        if char == '"':
            result += "'"
        elif char == "'":
            result += '"'
        else:
            result += char
    return result
#Завдання 2
def is_palindrome(string):
    if not isinstance(string,str):
        raise ValueError("Вхід повинен бути рядком")
    cleaned_string = "".join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]
#Завдання 3
def custom_split(string):
    if not isinstance(string,str):
        raise ValueError("Вхід повинен бути рядком")
    result = []
    word = ""
    for char in string:
        if char != " ":
            word += char
        else:
            result.append(word)
            word = ""
    if word != "":
        result.append(word)
    return result
#Завдання 4
from typing import List
def split_by_index(string: str,indexes: List[int]) -> List[str]:
    result = []
    prev_index = 0
    for index in indexes:
        if isinstance(index,int) and index > prev_index:
            result.append(string[prev_index:index])
            prev_index = index
    if prev_index < len(string):
        result.append(string[prev_index:])
    return result
#Завдання 5
from typing import Tuple
def get_digits(*args) -> Tuple[int]:
    digits = []
    for num in args:
        if isinstance(num,int):
            digits.extend(int(digit) for digit in str(num) if digit.isdigit())
        else:
            raise ValueError("Усі аргументи мають бути цілими числами")
    return tuple(digits)
#Завдання 6
def get_longest_word(s: str) -> str:
    if not isinstance(s,str):
        raise ValueError("Вхід повинен бути рядком")
    words = s.split()
    longest_word = ""
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)
    return longest_word
#Завдання 7
from typing import List
def foo(numbers: List[int]) -> List[int]:
    product = 1
    zero_count = 0
    for num in numbers:
        if num != 0:
            product *= num
        else:
            zero_count += 1
    result = []
    for num in numbers:
        if zero_count > 1:
            result.append(0)
        elif num == 0:
            result.append(product)
        else:
            result.append(product // num)
    return result
#Завдання 8
from typing import List,Union
def get_pairs(items: List[Union[int,str]]) -> List[Union[tuple,None]]:
    if len(items) == 1:
        return None
    pairs = []
    for i in range(len(items) - 1):
        pairs.append((items[i],items[i + 1]))
    return pairs
#Завдання 9
def sum_odd_digits(n):
    if not isinstance(n,int) or n < 0:
        raise TypeError("Вхідні дані повинні бути додатнім цілим числом")
    odd_sum = 0
    for digit in str(n):
        if int(digit) % 2 != 0:
            odd_sum += int(digit)
    return odd_sum
#Завдання 10
def sum_binary_1(n):
    if not isinstance(n,int) or n < 0:
        raise TypeError("Вхідні дані повинні бути додатнім цілим числом")
    binary = bin(n)[2:]
    return binary.count("1")
#Завдання 11
def fibonacci_loop(seq):
    result = ""
    for num in seq:
        if isinstance(num,float):
            continue
        elif isinstance(num,str):
            break
        else:
            result += str(num) + " "
    return result.strip()