def countAffordablePairs(prices, budget):

    n = len(prices)

    if n < 2:
        return 0

    left = 0
    right = n - 1
    count = 0

    while left < right:

        current_sum = prices[left] + prices[right]

        if current_sum <= budget:

            count += (right - left)
            left += 1

        else:
            right -= 1

    return count
