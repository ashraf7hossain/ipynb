

n,m = map(int,input().split())
g = [[] for _ in range(n)]

for i in range(m):
  x,y = map(int,input().split())
  x-=1;y-=1
  g[x].append((y,i))
  g[y].append((x,i))
  
s,path = [0],[]
visit = [False for _ in range(m)]

for i in range(n):
  if len(g[i])&1:
    print("IMPOSSIBLE");
    exit(0)

while len(s) > 0:
  u = s[-1]
 # s.pop(0)
  f = False
  while len(g[u])>0:
    (v,i) = g[u].pop()
   # print((v,i))
    if not visit[i]:
      visit[i] = True
      s.append(v)
      f = True
      break
  if not f :
    path.append(u)
    s.pop()

if m + 1 != len(path):
  print("IMPOSSIBLE")
  exit(0)
    
for i in path:
  print(i+1, end=' ')
    
    
    