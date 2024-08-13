def productExceptSelf(self, nums):

    """

    :type nums: List[int]

    :rtype: List[int]

    """

    n = len(nums)

    answer = [1] * n

    

    prefix_product = 1

    for i in range(n):

        answer[i] = prefix_product

        prefix_product *= nums[i]
