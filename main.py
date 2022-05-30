"""Maximum profit in single transaction"""
def maxprofit(arr):
  mi = min(arr)
  profit = 0
  for i , v in enumerate(arr):
    if arr.index(mi) < i and v - mi > profit:
      profit = v - mi
  print(profit)




arr = [9,11,8,25,7,10,30,60]
maxprofit(arr)