def solution(height):
    water = 0

    left = 0
    right = len(height) - 1

    while left < right:
        water_level = min(height[left], height[right])
        # print(left, right, "\t", "height is ", water_level)
        # print(height)
        # input()

        if height[left] <= height[right]:
            for j in range(left, right + 2):
                if j == right + 1:
                    left = right
                    break

                if height[j] > height[left]:
                    left = j
                    break
                elif height[j] < water_level:
                    water += water_level - height[j]
                    height[j] = water_level

        elif height[right] < height[left]:
            for j in range(right, left - 1, -1):
                if height[j] > height[right]:
                    right = j
                    break
                elif height[j] < water_level:
                    water += water_level - height[j]
                    height[j] = water_level
    return water


def solution_bis(height):
    water = 0
    for i in range(1, len(height) - 1):
        print(i)
        water_level = min(max(height[:i]), max(height[i:]))
        if height[i] < water_level:
            water += water_level - height[i]
    return water
