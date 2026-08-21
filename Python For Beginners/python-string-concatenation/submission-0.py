def concatenate(s1: str, s2: str) -> str:
    w = s1+s2
    if len(w) > 10:
        return 'Too long!'
    else:
        return w




# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
