from fractions import Fraction
"""
from math import log
from math import gcd
from math import sqrt


# got code for finding Highly Composite Numbers From https://gist.github.com/dario2994/fb4713f252ca86c1254d
def make_prime_list(max_number):
    prime_list = []
    product_of_primes = 1
    test_number = 2
    while True:
        n_prime = True
        for div in range(2, test_number):
            if test_number % div == 0:
                n_prime = False
        if n_prime:
            prime_list.append(test_number)
            product_of_primes *= test_number
        if product_of_primes > max_number:
            break
        test_number += 1
    return prime_list


def gen_hcn(primes, number):
    hcn = [(1, 1, [])]
    for i in range(len(primes)):
        new_hcn = []
        for el in hcn:
            new_hcn.append(el)
            if len(el[2]) < i: continue
            e_max = el[2][i-1] if i >= 1 else int(log(number, 2))
            n = el[0]
            for e in range(1, e_max+1):
                n *= primes[i]
                if n > number: break
                div = el[1] * (e+1)
                exponents = el[2] + [e]
                new_hcn.append((n, div, exponents))
        new_hcn.sort()
        hcn = [(1, 1, [])]
        for el in new_hcn:
            if el[1] > hcn[-1][1]: hcn.append(el)
    return hcn

# got code for phi fuction from https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-120.php
def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)


def main():
    n = int(input())
    primes = make_prime_list(n)
    hcn = gen_hcn(primes, n)
    hcn = hcn[-1][0]
    numerator = hcn-phi_func(hcn)
    denom = hcn
    divsor = gcd(numerator, denom)
    print("{}/{}".format(numerator//divsor, denom//divsor))



if __name__ == "__main__":
    main()

"""

n = int(input())
'''
possible_numbers = []
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
num = 1
for prime in primes:
    num *= prime
    if num > 1000000000000000000:
        break
    possible_numbers.append(num)
'''
possible_numbers = [2, 6, 30, 210, 2310, 30030, 510510, 9699690,
                    223092870, 6469693230, 200560490130, 7420738134810,
                    304250263527210, 13082761331670030, 614889782588491410, 32589158477190044730]
toitent = [1, 4, 22, 162, 1830, 24270, 418350, 8040810, 186597510, 5447823150,
           169904387730, 6317118448410, 260105476071210, 11228680258518030, 529602053223499410, 28154196550210460730]
for i in range(len(possible_numbers)-1):
    if possible_numbers[i+1] > n:
        break
print(Fraction(toitent[i],possible_numbers[i]))
