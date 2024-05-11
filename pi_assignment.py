from mpmath import mp
def reverse_n_pi_digits(n):
    mp.dps = n
    return str(mp.pi).replace('.','')[::-1]