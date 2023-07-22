import numpy as np

mn = np.zeros((8,8), dtype=int)
mn[7] = np.array([9,8,7,6,5,4,3,2])
mn[:,7] = np.array(list(reversed([2,8,7,6,5,4,3,2])))

mx = mn.copy()

# je mozne tahnout i diagonalne?
kral = True

# pole nad hlavni diagonalou a na ni
for k in reversed(range(7)):
    tot = 7-k
    for i in range(tot):
        if kral:
            mn[k+i,6-i] = min(mx[k+i+1,6-i], mx[k+i,6-i+1], mx[k+i+1,6-i+1])
            mx[k+i,6-i] = max(mn[k+i+1,6-i], mn[k+i,6-i+1], mn[k+i+1,6-i+1])
        else:
            mn[k+i,6-i] = min(mx[k+i+1,6-i], mx[k+i,6-i+1])
            mx[k+i,6-i] = max(mn[k+i+1,6-i], mn[k+i,6-i+1])

# pole pod hlavni diagonalou
for k in reversed(range(6)):
    tot = k + 1
    for i in range(tot):
        if kral:
            mn[i,k-i] = min(mx[i+1,k-i], mx[i,k-i+1], mx[i+1,k-i+1])
            mx[i,k-i] = max(mn[i+1,k-i], mn[i,k-i+1], mn[i+1,k-i+1])
        else:
            mn[i,k-i] = min(mx[i+1,k-i], mx[i,k-i+1])
            mx[i,k-i] = max(mn[i+1,k-i], mn[i,k-i+1])


print(np.flipud(mn))
print(np.flipud(mx))