def approximate_pi(n_terms):
    leibniz_series = []
    for i in range(n_terms):
        term = ((-1) ** i) / (2 * i + 1)
        leibniz_series.append(term)
    pi_approximation = sum(leibniz_series) * 4
    return pi_approximation
