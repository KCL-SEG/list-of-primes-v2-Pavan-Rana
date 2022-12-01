"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
        return
    list = []
    guess = 2
    while(len(list)<number_of_primes):
        flag = True
        for i in range (2,guess):
            if guess % i == 0:
                flag = False
                break
        if flag:
            list.append(guess)
        guess +=1
    return list
