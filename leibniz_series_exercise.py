
def approximate_pi(n):
    total = 0
    for i in range(n):
        total += ((-1) ** i) / (2 * i + 1)
    leibniz_series = total *4    
    return leibniz_series
