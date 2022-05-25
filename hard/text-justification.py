# a TERRIBLE answer. I was bored and tired


from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def fill(number_char, current):
            if len(current) > 1:
                less_than_max = True
                while less_than_max:
                    for i in range(len(current) - 1):
                        if number_char > maxWidth:
                            less_than_max = False
                            break
                        current[i] += " "
                        number_char += 1
            else:
                current[0] += " " * ((maxWidth + 1) - number_char)
            return " ".join(current)

        result = []
        current = []
        number_char = 0
        for word in words:
            if number_char + len(word) < (maxWidth + 1):
                current.append(word)
                number_char += 1 + len(word)
            else:
                result.append(fill(number_char, current))
                current = [word]
                number_char = len(word) + 1

        if current:
            left = " ".join(current)
            left += " " * ((maxWidth + 1) - number_char)
            result.append(left)

        return result
