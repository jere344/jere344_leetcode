def solution(s, words):
    result = []
    size = len(words[0])
    combined_size = len(words) * size
    for i in range(len(s) - combined_size + 1):
        leftover = [e for e in words]
        starting_indice = i

        while True:
            if leftover == []:
                result.append(i)
                break
            elif s[starting_indice : starting_indice + size] in leftover:
                leftover.remove(s[starting_indice : starting_indice + size])
                starting_indice += size
            else:
                break

    return result


if __name__ == "__main__":
    print(solution("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
