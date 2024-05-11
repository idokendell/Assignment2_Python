#a+b+c=sum
#a^2+b^2=c^2

def pythagorean_triplet_by_sum(sum):
    for a in range(1,sum):
        for b in range(a+1,sum):
            c = sum-a-b
            if c>b:#יתר ארוך מניצב
                if a**2 + b**2 == c**2:
                    print(f"{a},{b}, {c}")

