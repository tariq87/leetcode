"""Maximum profit in single transaction"""
def maxprofit(arr):
  left = 0
  right = 1
  mxprofit = 0
  while right < len(arr):
    curr_prof = arr[right] - arr[left]
    if arr[left] < arr[right]: 
      mxprofit = max(curr_prof,mxprofit)
    else:
      left = right
    right+=1
  print(mxprofit)
