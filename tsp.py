dist_type = input()
no_of_city = int(input())
city_cords = []
dist = []

for _ in range(no_of_city):
    c = list(map(float,input().split()))
    city_cords.append(c)

for i in range(no_of_city):
    d = list(map(float,input().split()))
    dist.append(d)

sol = []
sm = float("inf")    

for k in range(no_of_city):
    start = k
    count = 1
    vis = [False for j in range(no_of_city)]
    vis[0] = True
    path = [0,]
    cost = 0
    while count < no_of_city:
        mi,mn = -1, float("inf")
        for j in range(no_of_city):
            if vis[j]:
                continue
            if mi != -1:
                if dist[start][j]>0 and mn < dist[start][j]:
                    mi,mn = j,dist[start][j]
            else:
                if dist[start][j] > 0:
                    mi,mn = j,dist[start][j]
        path.append(mi)
        cost += mn
        count +=1
        vis[mi] = True

    if sm>cost:
        sol = path
        sm = cost

for i in range(len(sol)):
    if i<len(sol)-1:
        print(sol[i], end=" ")
    else:
        print(sol[i])
 