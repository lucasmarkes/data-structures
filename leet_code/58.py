def lengthOfLastWord(s: str) -> int:
    x = s.split()

    return len(x[-1])
