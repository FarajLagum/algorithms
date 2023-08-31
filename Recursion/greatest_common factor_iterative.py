def get_factors(number):
    factors = set()
    for index in range(1, number+1):
        # print(index, number % index)
        if number % index == 0:
            factors.add(index)
    return factors


def greatest_common_factor(n, m):
    n_factors = get_factors(n)
    m_factors = get_factors(m)

    gcf = max(n_factors.intersection(m_factors))

    return  gcf



if __name__ == "__main__":
    n = 12
    m = 8
    print(greatest_common_factor(n, m))
