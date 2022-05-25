from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total_clothes = sum(machines)
        number_of_machine = len(machines)
        if total_clothes % number_of_machine != 0:
            return -1

        clothes_per_machine = int(total_clothes / number_of_machine)

        machines_copy = [e for e in machines]

        to_move = [0 for _ in machines]
        for i in range(1, len(machines)):
            to_move_left = clothes_per_machine - machines[i - 1]
            machines[i - 1] = clothes_per_machine
            machines[i] -= to_move_left
            if to_move_left > 0:
                to_move[i] += to_move_left

        for i in range(len(machines_copy) - 2, -1, -1):
            to_move_right = clothes_per_machine - machines_copy[i + 1]
            machines_copy[i + 1] = clothes_per_machine
            machines_copy[i] -= to_move_right
            if to_move_right > 0:
                to_move[i] += to_move_right

        return max(to_move)


print(Solution().findMinMoves([100, 1, 1]))
