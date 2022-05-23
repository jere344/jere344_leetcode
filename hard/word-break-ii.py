from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        queue = []
        for word in wordDict:
            if s == word:
                result.append(word)

            elif s.startswith(word):
                queue.append([word])

        while queue:
            # print(queue)
            current = queue.pop()
            # print(f"\n\t {current}")

            for word in wordDict:
                current_str = "".join(current) + word

                # print(current, word)
                if current_str == s:
                    result.append(" ".join(current + [word]))

                elif s.startswith(current_str):
                    queue.append(current + [word])

        return result
