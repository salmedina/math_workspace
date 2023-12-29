t = [6,2,8,0,4,7,9,None,None,3,5]

def get_path(t, p):
  res = [p]
  while t.index(p) > 0:
    parent_idx = t.index(p) // 2
    print(parent_idx)
    p = t[parent_idx]
    res.append(p)
    return res
  
  path = get_path(t, 3)
  
  print(path)
