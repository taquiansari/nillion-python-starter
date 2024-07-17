from nada_dsl import *


def nada_main():
    """
    This program computes the average of secret integers provided by two parties.

    In this example, Party1 and Party2 each provide 5 secret integers.
    """

    num_parties = 2
    num_integers_per_party = 5
    total_integers = num_parties * num_integers_per_party

    parties = [Party(name=f"Party{i}") for i in range(num_parties)]
    outparty = Party(name="OutParty")

    secret_integers = []
    for i, party in enumerate(parties):
        for j in range(num_integers_per_party):
            secret_integers.append(SecretInteger(Input(name=f"int_{i}_{j}", party=party)))

    total_sum = secret_integers[0]
    for secret_integer in secret_integers[1:]:
        total_sum += secret_integer

    total_count = Integer(total_integers)
    average = total_sum / total_count

    return [Output(average, "average", outparty)]

