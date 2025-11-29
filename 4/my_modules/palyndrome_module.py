def is_palyndrome(s):
    for i in range(len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True
