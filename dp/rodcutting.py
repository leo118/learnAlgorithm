
# 2-D array
#
#
#
tree = []
#max(p, r(1)+r(n-1),...,r(n-1)+r1)
              #0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
PRICE_TABEL = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# N <= len(PRICE_TABEL)

def calP(cuttingtree):
  value = PRICE_TABEL[cuttingtree[-1]-1]
  for i in range(len(cuttingtree)-1, 0, -1):
    value += PRICE_TABEL[cuttingtree[i-1] - cuttingtree[i]-1]
  return value

def cutting(n, subtree):
  subtree.append(n)
  for i in range(n):
    if i==0:
      print 'complete sub-tree'
      print subtree
      tree.append(calP(subtree))

    else:
      cutting(n-i,list(subtree))

def p(i):
    assert i+1 < len(PRICE_TABEL),\
        'rod piece length is undefined in price tabel.'
    return 1

cutting(4, [])
print tree