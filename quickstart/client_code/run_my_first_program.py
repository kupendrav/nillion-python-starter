from nada_dsl import *

def nada_binomial_coefficient():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    n = SecretInteger(Input(name="N", party=party1))
    k = SecretInteger(Input(name="K", party=party2))

    # Calculate n factorial
    n_factorial = SecretInteger(1, party=party1)
    for i in range(1, n + 1):
        i_secret = SecretInteger(i, party=party1)
        n_factorial *= i_secret
    
    # Calculate k factorial
    k_factorial = SecretInteger(1, party=party2)
    for j in range(1, k + 1):
        j_secret = SecretInteger(j, party=party2)
        k_factorial *= j_secret
    
    # Calculate (n - k) factorial
    nk_factorial = SecretInteger(1, party=party1)
    nk = n - k
    for m in range(1, nk + 1):
        m_secret = SecretInteger(m, party=party1)
        nk_factorial *= m_secret

    # Calculate binomial coefficient (n choose k) = n! / (k! * (n - k)!)
    numerator = n_factorial
    denominator = k_factorial * nk_factorial
    result = numerator / denominator

    return [Output(result, "binomial_coefficient_output", party3)]
