def is_devide_by_three(a):
    return a%3==0
nums=[1,2,3]
result=list(map(is_devide_by_three, nums))
def multiply(a,b):
    return a*b
nums=[1,2]
nums2=[2,4]
multipliednums=list(map(multiply,nums,nums2))