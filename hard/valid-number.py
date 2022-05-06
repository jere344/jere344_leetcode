def solution(s: str):
    s = s.lower().split("e")
    if len(s) > 2:
        return False
    for i in range(len(s)):
        if not s[i]:
            return False
        if s[i][0] == "+" or s[i][0] == "-":
            s[i] = s[i][1:]

    s[0] = s[0].replace(".", "", 1)

    return s[0].isnumeric() and (s[1].isnumeric() if len(s) == 2 else True)


valid = [
    "2",
    "0089",
    "-0.1",
    "+3.14",
    "4.",
    "-.9",
    "2e10",
    "-90E3",
    "3e+7",
    "+6e-1",
    "53.5e93",
    "-123.456e789",
]
invalid = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
for e in valid:
    print(solution(e))
print()
for e in invalid:
    print(solution(e))
