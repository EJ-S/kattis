while True:
    n = int(input())
    if n == 0:
        break
    points_list = []
    for _ in range(n):
        point = tuple(map(int, input().split()))
        points_list.append(point)
    
    area = 0
    for i in range(len(points_list)-1):
        product1 = points_list[i][0] * points_list[i+1][1]
        product2 = points_list[i][1] * points_list[i+1][0]
        area += (product1 - product2)
    product1 = points_list[-1][0] * points_list[0][1]
    product2 = points_list[-1][1] * points_list[0][0]
    area += (product1 - product2)
    area /= 2
    if area < 0:
        print("CW {:.1f}".format(abs(area)))
    else:
        print("CCW {}".format(area))
        
