def solution(s: str):
    import re

    for i in range(len(s) // 2):
        s = s.replace(f"({'d' * i})", f"{'d'*(i+1)}")

    compiled = re.compile("(d+d)").findall(s)

    if compiled:
        return len(max(compiled)) * 2
    elif "d" in s:
        return 2
    else:
        return 0
