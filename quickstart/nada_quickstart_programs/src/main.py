from nada_dsl import *

def nada_factorial():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    n = SecretInteger(Input(name="N", party=party1))

    result = SecretInteger(1, party=party1)  # Initialize result to 1

    # Loop to calculate factorial
    for i in range(1, n + 1):
        i_secret = SecretInteger(i, party=party1)
        result *= i_secret

    return [Output(result, "factorial_output", party3)]

