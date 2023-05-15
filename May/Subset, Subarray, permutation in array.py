#SUBSET :

arr=[1,2,3,4]
def sub(arr):
   if arr==[]:
      return [[]]
   else:
      a = sub(arr[1:])
      return a + [[arr[0]]+ b for b in a]
print(" ")
print(sub(arr))

#SUBARRAY :
arr1=[]
arr=[1,2,3,4]
for i in range(0,len(arr)):
   for j in range (i+1,len(arr)+1):
      arr1.append(arr[i:j])
print(" ")
print(arr1)


#PERMUTATION : 
nums=[1,2,3,4]
def perm(start, end=[],arr=[]):
   if(len(start) == 0):
         arr.append(end)
   else:
         for i in range(len(start)):
            perm(start[:i] + start[i+1:], end + start[i:i+1])
   return arr
print(" ")
print(perm(nums))
