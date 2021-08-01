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

def lucky_sum(a, b, c):
    '''
    (int,int,int)->int

    Return sum of the values. However if one of the calues is 13 then it doesn't
    count towards the sum and values to its right do not count.

    >>> lucky_sum(1, 2, 3)
    6
    >>> lucky_sum(1, 2, 13)
    3
    >>> lucky_sum(1, 13, 3)
    1

    '''

    if a == 13:
        return 0
    if b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c

def make_bricks(small, big, goal):
    '''
    (int,int,int)->bool
     We have a number of small bricks (1 inch each) and big bricks (5 inches each).
     Return True if it is possible to make the goal by choosing
     from the given bricks.

    >>> make_bricks(3, 1, 8)
    True
    >>> make_bricks(3, 1, 9)
    False
    >>> make_bricks(3, 2, 10)
    True

    '''
    if big != 0 and goal // 5 <= big and goal % 5 <= small:
        return True
    elif big != 0 and goal // 5 > big and goal - (big * 5) <= small:
        return True
    elif big == 0 and small >= goal:
        return True
    else:
        return False


def make_chocolate(small, big, goal):
    '''
    (int,int,int)->int
    We have small bars (1 kilo each) and big bars (5 kilos each).
    Return the number of small bars to use, assuming we always use big bars
    before small bars. Return -1 if it can't be done.

    >>> make_chocolate(4, 1, 9)
    4
    >>> make_chocolate(4, 1, 10)
    -1
    >>> make_chocolate(4, 1, 7)
    2
    '''

    if big != 0 and goal // 5 <= big and goal % 5 <= small:
        return goal % 5
    elif big != 0 and goal // 5 > big and goal - (big * 5) <= small:
        return goal - big * 5
    elif big == 0 and small >= goal:
        return goal % 5
    else:
        return -1

def missing_char(str, n):
    '''
Given a non-empty string and an int n, return a new string where the char at
index n has been removed. The value of n will be a valid index
of a char in the original string
(i.e. n will be in the range 0..len(str)-1 inclusive).


    >>> missing_char('kitten', 1)
    'ktten'
    >>> missing_char('kitten', 0)
    'itten'
    >>> missing_char('kitten', 4)
    'kittn'
    '''
    if n  <= len(str):
        return str[:n],str[(n+1):]


def near_hundred(n):
    '''
    Given an int n, return True if it is within 10 of 100 or 200.
    Note: abs(num) computes the absolute value of a number.


    >>>near_hundred(93)
    True
    >>>near_hundred(90)
    True
    >>>near_hundred(89)
    False
    '''

    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False

def no_teen_sum(a, b, c):
    '''
    (int,int,int)->int

    Return sum of the values, if any of the values is a teen in the range 13..19
    inclusive then that value counts as 0, except 15 and 16 do not count as a teens.
    >>> no_teen_sum(1, 2, 3)
    6
    >>> no_teen_sum(2, 13, 1)
    3
    >>> no_teen_sum(2, 1, 14)
    3
    '''
    return fix_teen(a)+fix_teen(b)+fix_teen(c)

def fix_teen(n):
    if n != 15 and n != 16 and 13 <= n <= 19:
        return n == 0
    else:
        return n

def not_string(a):
    '''
    Given a string, return a new string where "not " has been added to the front.
    However, if the string already begins with "not", return the string unchanged.

    >>> not_string('candy') → 'not candy'
    >>> not_string('x') → 'not x'
    >>> not_string('not bad') → 'not bad'
    '''
    if a[:3] == 'not':
        return a
    else:
        return 'not ' + a


def pos_neg(a, b, negative):
    '''
    Given 2 int values, return True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return True only if both are negative.


    >>>pos_neg(1, -1, False)
    True
    >>>pos_neg(-1, 1, False)
    True
    >>>pos_neg(-4, -5, True)
    True
    '''

    if a <= 0 and b >= 0 and negative == False:
        return True
    elif a >= 0 and b <= 0 and negative == False:
        return True
    elif a <= 0 and b <= 0 and negative == True:
        return True
    else:
        return False

def round_sum(a, b, c):
    '''
    (int,int,int)-> int

    Return the sum of their rounded values. round an int value up to the next
    multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20.
    Alternately, round down to the previousmultiple of 10 if its rightmost digit
    is less than 5,so 12 rounds down to 10.

    >>> round_sum(16, 17, 18)
    60
    >>> round_sum(12, 13, 14)
    30
    >>> round_sum(6, 4, 4)
    10
    '''
    return round10(a)+round10(b)+round10(c)


def round10(num):
    if num % 10 < 5:
        return num - (num % 10)
    else:
        return num + (10 - num % 10)
