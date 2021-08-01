def cat_dog(str):
    '''
    Return True if the string "cat" and "dog" appear the same
    number of times in the given string.


    cat_dog('catdog') → True
    cat_dog('catcat') → False
    cat_dog('1cat1cadodog') → True
    '''

    if str.count("cat") == str.count("dog"):
        return True
    return False

def close_far(a, b, c):
    '''
    (int,int,int)-> bool
    Return True if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    >>> close_far(1, 2, 10)
    True
    >>> close_far(1, 2, 3)a
    False
    >>> close_far(4, 1, 3)
    True

    '''
    if abs(a-b)<=1 and abs(a-c)>=2 and abs(b-c)>=2:
        return True
    elif abs(a-c)<=1 and abs(a-b)>=2 and abs(b-c)>=2:
        return True
    else:
        return False


def count_hi(str):
    '''

    Return the number of times that the string "hi" appears
    anywhere in the given string.


    >>> count_hi('abc hi ho')
    1
    >>> count_hi('ABChi hi')
    2
    >>> count_hi('hihi')
    2
    '''
    h = 0
    for i in range(0, len(str) - 1):
        if str[i] == 'h' and str[i + 1] == 'i':
            h = h + 1
    return h


def double_char(str):
    '''

    Given a string, return a string where for every char in the original,
    there are two chars.


    >>> double_char('The')
    'TThhee'
    >>> double_char('AAbb')
    'AAAAbbbb'
    >>> double_char('Hi-There')
    'HHii--TThheerree'
    '''

    double = ''
    for i in str:
        double = double + i * 2
    return double


def first_last6(nums):
    '''

    Given an array of ints, return True if 6 appears as either
    the first or last element in the array.
    The array willbe length 1 or more.


    >>> first_last6([1, 2, 6])
    True
    >>> first_last6([6, 1, 2, 3])
    True
    >>> first_last6([13, 6, 1, 2, 3])
    False
    '''

    if nums[0] == 6 or nums[-1] == 6:
        return True
    return False


def front_back(str):
    '''Given a string, return a new string where the first and last
    chars have been exchanged.


    >>>front_back('code')
    'eodc'
    >>>front_back('a')
    'a'
    >>>front_back('ab')
    'ba'
    '''
    if len(str) >= 2:
        return str[-1] + str[1:-1] + str[0]
    else:
        return str

def lone_sum(a, b, c):
    '''
    (int,int,int)->int
    Given 3 int values, a b c, return their sum.
    However, if one of the values is the same as another of the values,
    it does not count towards the sum.

    >>> lone_sum(1, 2, 3)
    6
    >>> lone_sum(3, 2, 3)
    2
    >>> lone_sum(3, 3, 3)
    0
    '''

    if a == b == c:
        return 0
    elif a == b:
        return c
    elif b == c:
        return a
    elif c == a:
        return b
    else:
        return a + b + c

