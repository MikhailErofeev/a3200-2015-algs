def digit(num, pos):
     if pos < len(str(num)):
          return int(str(num)[len(str(num)) - pos - 1])
     else:
          return 0

def radixsort(arr):
     if arr == []:
          return []
     for i in range(len(str(max(arr)))):
          cntarr = [0 for i in range(10)]                                
          for j in range(len(arr)):
               d = digit(arr[j], i)
               cntarr[d] += 1
          count = 0
          for j in range(10):
               cntarr[j], count = count, count + cntarr[j]
          tarr = [0 for i in range(len(arr))] 
          for j in range(len(arr)):
               d = digit(arr[j], i)                             
               tarr[cntarr[d]] = arr[j]            
               cntarr[d] += 1
          arr = tarr
     return arr

def sort(arr):
     neg = []
     pos = []
     for j in arr:
          if j < 0:
               neg.append(j)
          else:
               pos.append(j)
     for j in range(len(neg)):
          neg[j] = abs(neg[j])
     neg = radixsort(neg)
     pos = radixsort(pos)
     for j in range(len(neg)):
          neg[j] = -neg[j]
     res = neg[::-1] + pos
     return res
