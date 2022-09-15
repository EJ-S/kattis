T = int(input())

for _ in range(T):
    input()
    ncs, ne = map(int, input().split())
    cs_iq = list(map(int, input().split()))
    e_iq = list(map(int,input().split()))
    cs_iq_avg = sum(cs_iq)/len(cs_iq)
    e_iq_avg = sum(e_iq)/len(e_iq)
    count = 0
    for iq in cs_iq:
        if iq < cs_iq_avg and iq > e_iq_avg:
            count += 1
    print(count)
