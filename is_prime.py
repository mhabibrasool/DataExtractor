from math import sqrt

def is_prime(n):
    """ Returns True if nonnegetive number integr n is prime;
    otherwise, return False. """
    if n == 2:                          # Two is only even prime.
        return True
    if n < 2 and n % 2 == 0:            # Handle simple cases
        return False

    trial_factor = 3
    root = sqrt(n)
    while trial_factor <= root:
        if n % trial_factor == 0:       # Is trial_factor is a factor.
            return False                # Yes, return right way.
        trial_factor += 2               # Next, potential factor
    return True


def prime_sequence(begin, end):
    """ Generate the sequence of prime number
    between begin and end."""
    for value in range(begin, end + 1):
        if is_prime(value):                          # See if the value is prime
            yield value                               # Produce the prime number.

        
def main():
    """ Make a list from a generator."""
    # Build the list prime number's in the range.
    begin = int(input("Enter the beginning number: "))
    end = int(input("Enter the ending nunbmer: "))
    primes = list(prime_sequence(begin, end))
    print(primes)

if __name__ == "__main__":
    main()                 # Run the program.