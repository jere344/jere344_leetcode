# def solution_slow(s, p):
#     if isinstance(p, str):
#         p = [c for c in p]

#     for i, e in enumerate(s):
#         # print(s[i:], p)
#         if not p:
#             return False
#         if e == p[0]:
#             p.pop(0)
#         elif p[0] == "?":
#             p.pop(0)
#         elif p[0] == "*":
#             # print(i, len(s[i:]) + 2)
#             for j in range(i, len(s)):
#                 # print("trying ", s[j:], p[1:])
#                 if solution(s[j:], p[1:]):
#                     # print("worked")
#                     return True
#                 # print("didnt' worked")
#         else:
#             return False

#     if not p:
#         return True

#     for c in p:
#         if c != "*":
#             return False
#     return True


# def solution_slow_2(s, p):
#     import re

#     while "**" in p:
#         p = p.replace("**", "*")

#     special = ".+\\$.[]()|-{}"
#     for c in special:
#         p = p.replace(c, "\\" + c)

#     print(p)
#     regx = re.compile(p.replace("*", ".*").replace("?", "."))

#     return bool(regx.fullmatch(s))


def solution(s, p):
    import fnmatch

    return bool(fnmatch.filter([s], p))


print(
    solution(
        "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb",
        "**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb",
    )
)
