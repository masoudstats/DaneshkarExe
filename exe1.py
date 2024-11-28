
from math import sqrt
import statistics
from statistics import mean
from random import randrange, random



# Insert K number from user.
k = input("Please enter k:")
k = int(k)



# Loading file from local dir.
lines = []

with open("points.txt") as f:
    while True:
        line = f.readline()
        lines.append(line)
        if not line:
            break



# calculate euclidean distance.
def dist(x: float, y: float, z: float, x0: float, y0: float, z0: float) -> float:
    dist = sqrt(((x - x0) ** 2 +(y - y0) ** 2 +(z - z0) ** 2 ))
    return dist



# Update cluster.
def new_centroid(list_points: list) -> list :
    xs, ys, zs = [], [], []
    for point in list_points:
        xs.append(point[0])
        ys.append(point[1])
        zs.append(point[2])
    new_centroid =[mean(xs), mean(ys), mean(zs)]

    return new_centroid



# Init K random points.
centroids = []

for num in range(k):
    points = []
    for point in range(3):
        points.append(randrange(-10, 10) + random())
    
    centroids.append(points)
print(f"First centroids are:\n", centroids)




trade_off = 0.02
converge = True
i = 0
while converge:

    clusters = [[] for _ in range(k)]
    for point in lines:

        # Before useing data points, apply naive data cleaning! 
        try:
            x0 = float(point[0])
        except Exception:
            x0 = 0
        try:
            y0 = float(point[1])
        except Exception:
            y0 = 0
        try:
            z0 = float(point[2])
        except Exception:
            z0 = 0

        dist_to_centroids = {}
        for idx, centroid in enumerate(centroids):
            dist_to_centroids[idx] = dist(centroid[0], centroid[1], centroid[2], x0, y0, z0)

        min_val = min(dist_to_centroids.values())
        idx = [k for k,v in dist_to_centroids.items() if v == min_val][0]

        clusters[idx].append([x0, y0, z0])

    new_centroids, diff_list = [], []   
    for cluster, centroid in zip(clusters,centroids):
        try:
            center = new_centroid(cluster)
            new_centroids.append(center)
            diff = dist(centroid[0], centroid[1], centroid[2],
            center[0], center[1], center[2])
            diff_list.append(diff)
        except statistics.StatisticsError:
            print("For better result please enter less k!")
            break

    try: 
        if mean(diff_list) < trade_off:
            break
    except statistics.StatisticsError:
        break

    centroids = new_centroids
    clusters = [[] for _ in range(k)]

    i+=1


print(f"Finall cenroids are:\n", centroids)
print(f"\nNumber of steps:", i)
    