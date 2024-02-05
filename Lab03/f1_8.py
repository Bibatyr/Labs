def spy_game(nums):
    zero_count = 0

    for num in nums:
        if num == 0:
            zero_count += 1
        elif num == 7 and zero_count >= 2:
            return True
        return False