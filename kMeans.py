
def assign_to_clusters(data,clusters,centroids,old_points_assign):
    l=list(centroids.values( ))
    for i in range(len(data)):
        p = [(abs(data[i] - l[j])) for j in range(len(l))]
        min=p[0]
        for j in p:
            if min>j:
                min=j
        for k in range(len(p)):
            if min == p[k]:
                old_points_assign[k].append(data[i])
                break
    return old_points_assign
def recompute_centroid(data,clusters,centroids):
    new_centroid_assign = { }
    total=[0 for i in range(k)]
    for i in range(len(temp)):
        total[i]=sum(temp[i])
        new_centroid_assign[i]=total[i]/len(temp[i])
    centroids=new_centroid_assign.copy()
    return centroids
try:
    data = [float(x.rstrip()) for x in open('C:\\Users\\Admin\\Desktop\\prog2-input-data.txt','r')]
    k = int(input("enter number of clusters:", ))
    centroids = dict(zip(range(k), data[0:k]))
    clusters = dict(zip(range(k), [[] for i in range(k)]))
    iteration = 0
    while 1:
        iteration = iteration + 1
        print("Iteration ", iteration)
        old_points_assign = dict(zip(range(k), [[] for i in range(k)]))
        new_clusters_assign = assign_to_clusters(data, clusters, centroids, old_points_assign)
        clusters = new_clusters_assign.copy()
        for i in clusters:
            print(i, clusters[i])
        temp = list(new_clusters_assign.values())
        new_centroids=recompute_centroid(data, clusters, centroids)
        if centroids==new_centroids:
            break
        else:
            for i in range(k):
                centroids[i] = new_centroids[i]

    print()
    output_file = open("prog2-output-data.txt", "w")
    for point in data:
        for k in range(len(clusters)):
            if point in clusters[k]:
                output_file.write("Point " +str(point)+" in cluster "+str(k)+ " \n")

    output_file.close()
    m=open("prog2-output-data.txt","r")
    o=m.read()
    print(o)
    m.close()
except FileNotFoundError:
    print("\nNo file found")
except ValueError:
    print("\nInvalid input, needs to be a interger!!!")









