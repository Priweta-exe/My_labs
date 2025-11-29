def average_ariphmetic(l):
    return sum(l)/len(l)
def average_geometric(l):
    comp = 1
    for i in l:
        comp *= i
    return comp**(1/len(l))
def average_harmonic(l):
    new_l = [1/i for i in l]
    avg_new_l = sum(new_l)/len(l)
    return 1/avg_new_l
def average_exponentional(l, power):
    new_l = [i**power for i in l]
    avg_new_l = sum(new_l)/len(l)
    return avg_new_l**(1/power)
