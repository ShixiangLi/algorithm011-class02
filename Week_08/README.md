学习笔记
# 位运算

左移<<，右移>>，按位或|，按位与&，取反~，异或^

## 异或的特殊操作

1. x ^ 0 = x
2. x ^ 1s = ~x //注意1s=~0，全1
3. x ^ (~x) = 1s
4. x ^ x = 0
5. c = a ^ b => a ^ c = b, b ^ c = a //交换两个事
6. a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c //associate
7. 将x最右边的n位清零：x & (~0 << n)
8. 获取x的第n位值（0或者1）：(x >> n) & 1
9. 获取x的第n位的幂值：x & (1 << n)
10. 仅将第n位置为1：x | (1 << n)
11. 仅将第n为置为0：x & (~(1 << n))
12. 将x最高位至第n位（含）清零：x & ((1 << n) - 1)
13. 判断奇偶：x & 1 == 1（奇数）；x & 1 == 0（偶数）
14. x >> 1 -> x // 2
15. x = x & (x - 1)清零最低位的1
16. x & -x得到最低位的1
17. x & ~x => 0

# 排序
	nums = [1,5,-8,0,2,11,5,8]
	
	def bubblesort(nums):
	    if len(nums) <= 1:
	        return nums
	    for i in range(len(nums)):
	        flag = False
	        for j in range(len(nums) - i - 1):
	            if nums[j] > nums[j+1]:
	                nums[j], nums[j+1] = nums[j+1],nums[j]
	                flag = True
	        if not flag:
	            break
	    return nums
	
	print(bubblesort(nums))
	
	def insertsort(nums):
	    if len(nums) <= 1:
	        return nums
	    for i in range(1,len(nums)):
	        value = nums[i]
	        for j in range(i-1,-1,-1):
	            if nums[j] > nums[j+1]:
	                nums[j+1] = nums[j]
	            else:
	                j += 1
	                break
	        nums[j] = value
	    return nums
	
	print(insertsort(nums))
	
	def shellsort(nums):
	    if len(nums) <= 1:
	        return nums
	    n = len(nums)
	    gap = n // 2
	    while gap:
	        for i in range(gap, n):
	            value = nums[i]
	            for j in range(i-gap, -1, -gap):
	                if nums[j] > value:
	                    nums[j+gap] = nums[j]
	                else:
	                    j += gap
	                    break
	            nums[j] = value
	        gap //= 2
	    return nums
	
	print(shellsort(nums))
	
	
	def selectsort(nums):
	    if len(nums) <= 1:
	        return nums
	    for i in range(len(nums)-1):
	        index = i
	        for j in range(i,len(nums)):
	            if nums[j] < nums[index]:
	                index = j
	        nums[i],nums[index] = nums[index], nums[i]
	    return nums
	
	print(selectsort(nums))
	
	def mergesort(nums):
	    if len(nums) <= 1:
	        return nums
	    mid = len(nums) >> 1
	    left = mergesort(nums[:mid])
	    right = mergesort(nums[mid:])
	    return merge(left, right)
	
	def merge(left, right):
	    temp = []
	    l = r = 0
	    while l < len(left) and r < len(right):
	        if left[l] < right[r]:
	            temp.append(left[l])
	            l += 1
	        else:
	            temp.append(right[r])
	            r += 1
	    if l == len(left):
	        temp += right[r:]
	    else:
	        temp += left[l:]
	    return temp
	
	# 哨兵
	'''def merge(left, right):
	    len_left = len(left)
	    len_right = len(right)
	    left += [float('inf')]
	    right += [float('inf')]
	    temp = []
	    l = r = 0
	    while l <= len_left and r <= len_right:
	        if l == len_left and r == len_right:
	            break
	        if left[l] < right[r]:
	            temp.append(left[l])
	            l += 1
	        else:
	            temp.append(right[r])
	            r += 1
	    return temp'''
	
	print(mergesort(nums))
	
	import random
	def quicksort(nums):
	    quick_sort(nums, 0, len(nums)-1)
	    return nums
	
	def quick_sort(nums,low,high):
	    if low >= high:
	        return nums
	    pivot_index = partitions(nums, low, high)
	    quick_sort(nums, low, pivot_index-1)
	    quick_sort(nums, pivot_index+1, high)
	
	def partitions(nums, low, high):
	    pivot_index = random.randint(low, high)
	    pivot = nums[pivot_index]
	    nums[high], nums[pivot_index] = nums[pivot_index], nums[high]
	    i = low
	    for j in range(low, high):
	        if nums[j] < pivot:
	            nums[i], nums[j] = nums[j], nums[i]
	            i += 1
	    nums[i], nums[high] = nums[high], nums[i]
	    return i
	
	print(quicksort(nums))
