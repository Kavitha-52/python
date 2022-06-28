nums=[1,2,3,4]
'''print(nums[0])
print(nums[1])
for i in nums:
    print(i)'''

it=iter(nums)
print(it)#print format
print(it.__next__())
#print(it)#format
for i in nums:
    print(i)
