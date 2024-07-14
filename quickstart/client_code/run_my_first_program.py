from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Inputs from Party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Input from Party2
    my_int3 = SecretInteger(Input(name="my_int3", party=party2))

    # Perform operations
    sum_result = my_int1 + my_int2
    product_result = sum_result * my_int3
    comparison_result = my_int1 > my_int2

    # Return multiple outputs
    return [
        Output(sum_result, "sum_output", party1),
        Output(product_result, "product_output", party2),
        Output(comparison_result, "comparison_output", party1)
    ]