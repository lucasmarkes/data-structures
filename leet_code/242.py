def isAnagram(s: str, t: str) -> bool:
    sdic = {}
    tdic = {}
    for i in range(len(s)):
        if s[i] not in sdic:
            sdic[s[i]] = 1
        else:
            sdic[s[i]] += 1

    for i in range(len(t)):
        if t[i] not in tdic:
            tdic[t[i]] = 1
        else:
            tdic[t[i]] += 1

    return sdic == tdic

    #     if t[i] not in s:
    #         return False
    #     else:
    #         c += 1

    # if c > 1:
    #     return True
    # else:
    #     return False


print(isAnagram(s="ab", t="a"))
