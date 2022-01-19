
# Utilize binary search to complete this problem in O (log n)
def firstBadVersion (n,target):


            
  start = 1
  end = n 
        
  while (start < end) :
    mid = (start + end) //2
    if isBadVersion(mid):
      end = mid
    else:
      start = mid + 1
  return start
     
