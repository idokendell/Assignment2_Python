def until_middle(word):
    leng = int(len(word))
    if leng % 2 == 0:
         return leng//2
    return leng//2+1

def is_sorted(string,middle):
    return string[:middle] == ''.join(sorted(string[:middle]))

def is_sorted_polyndrom(string):
    middle = until_middle(string)
    return is_sorted(string,middle) and is_sorted(string[::-1],middle)
