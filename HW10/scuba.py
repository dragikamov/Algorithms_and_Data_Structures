import numpy as np
scuba_diver = np.zeros((1000,22,80))
container_ox = [0]*1000
container_ni = [0]*1000
container_weight = [0]*1000

def find_equipment(cylinder, oxigen, nitrogen):
    if oxigen == 0 and nitrogen == 0:
        scuba_diver[cylinder,oxigen,nitrogen] = 0
    elif cylinder == 0:
        scuba_diver[cylinder,oxigen,nitrogen] = 123456789
    else:
        scuba_diver[cylinder,oxigen,nitrogen] = min(
            find_equipment(cylinder-1,oxigen,nitrogen),
            find_equipment(cylinder-1,
                           max(oxigen-container_ox[cylinder-1],0),
                           max(nitrogen-container_ni[cylinder-1],0))+
            container_weight[cylinder-1])
    return scuba_diver[cylinder,oxigen,nitrogen]

def main():
    cases = int(input())
    while (cases>0):
        oxigen = int(input())
        nitrogen = int(input())
        cylinder = int(input())

        for i in range(cylinder):
            container_ox[i] = int(input())
            container_ni[i] = int(input())
            container_weight[i] = int(input())

        for i in range(cylinder+1):
            for j in range(oxigen+1):
                for k in range(nitrogen+1):
                    scuba_diver[1,j,k]=-1

        print(find_equipment(cylinder,oxigen,nitrogen))

        i = cylinder-1
        temp_oxigen = oxigen
        temp_nitrogen = nitrogen
        seq = []
        while (i>0) and (temp_oxigen>=0) and (temp_nitrogen>=0):
            if(scuba_diver[i,temp_oxigen,temp_nitrogen] != scuba_diver[i-1,temp_oxigen,temp_nitrogen]):
                temp_oxigen = temp_oxigen-container_ox[i]
                temp_nitrogen = temp_nitrogen-container_ni[i]
                seq.append(i+1)
                i-=1
            else:
                i-=1
        seq.reverse()
        for i in seq:
            print(i,end=" ")
        cases-=1

main()
