def twoSum(nums, target):
    # pivot = 0
    # while pivot < len(nums):
    #     for x in range(pivot + 1, len(nums)):
    #         if nums[pivot] + nums[x] == target:
    #             return [pivot, x]
    #     pivot += 1
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        if remaining in seen:
            return [i, seen[remaining]]
        seen[value] = i


"""
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """


# print(twoSum([1, 4, 3], 4))

# def isPalindrome(x):
#     """
#     :type x: int
#     :rtype: bool
#     """
#     try:
#         if x == int(str(x)[::-1]):
#             return True
#         else:
#             return False
#     except:
#         return False
#
# print(isPalindrome(525))


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)

        # mid = int((left+right)/2)
        print("LEFT: ", left)
        print("MID: ", mid)
        print("RIGHT: ", right)
        # if mid == len(nums):
        #     return -1
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

    # left, right = 0, len(nums) - 1
    # while left <= right:
    #     pivot = left + (right - left) // 2
    #     if nums[pivot] == target:
    #         return pivot
    #     if target < nums[pivot]:
    #         right = pivot - 1
    #     else:
    #         left = pivot + 1
    # return -1


# def main():
#     a = [-1, 0, 3, 5, 9, 12]
#     b = 13
#     print(search(a, b))
#
# main()
#
#
# def firstBadVersion(self, n):
#     """
#     :type n: int
#     :rtype: int
#     """
#     left = 0
#     right = n
#
#     while (left <= right):
#         mid = (left + right) // 2
#         if isBadVersion(mid):
#             if not isBadVersion(mid -1):
#                 return mid
#             else:
#               right = mid - 1
#         else:
#             left = mid + 1

# def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """


# def containsDuplicate(nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     seen = {}
#     if len(nums) == 1:
#         return False
#     else:
#         for i, value in enumerate(nums):
#             print("i: ",i)
#             print("value", value)
#             print("num len: ", len(nums))
#             print("seen: ", seen)
#             if value in seen and i <= len(nums):
#                 return True
#             else:
#                 seen[value] = i
#
#
# print(containsDuplicate([1, 2, 3, 4, 5, 6, 7]))

def insertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        sortedIdx = i - 1

        while sortedIdx >= 0 and nums[sortedIdx] > key:
            nums[sortedIdx + 1] = nums[sortedIdx]
            sortedIdx = sortedIdx - 1
        nums[sortedIdx + 1] = key  # Thêm key vào mảng trị đã được duyệt
    print(nums)


# insertionSort([1, 3, 7, 4, 5, 2, 6,8, 13, 8,3, 9])
# Điểm mấu chốt đó là nếu đối tượng đứng sau mà lớn hơn đối tượng đứng trước thì ta đổi vị trí của chúng nếu thoả điều kiện thì while còn không thì gán index
# của phần từ đã so sánh lên 1, có nghĩa là đã duyệt qua 1 phần tử.
# Tạo ra một vòng lặp để quét từ đầu đến cuối các giá trị trong mảng
# Gán key là đối tượng đang được so sánh, chú ý giá trị sẽ không đổi trong suốt quá trình so sánh ngược về phía trước
# Tạo một vòng while có tác dụng nếu gặp giá trị đang so sánh mà lớn hơn giá trị đứng trước nó thì cứ hoán đổi vị trị về phía trước cho tới phần tử đầu tiên
#


# Given a sorted array of distinct integers and a target value
# return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def searchPosition(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target < nums[0]:
        return 0
    left = 0
    right = len(nums) - 1

    pos = -1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            pos = mid
            return pos
        elif nums[mid] < target:
            left = mid + 1
            pos = left
        else:
            right = mid - 1
            pos = mid
    return pos


print(searchPosition([1, 3, 5, 6], 4))
