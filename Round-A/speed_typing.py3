def speed_typing():
    I = input().strip()
    P = input().strip()
    result = j = 0
    for i in range(len(P)):
        if j < len(I) and I[j] == P[i]:
            j += 1
        else:
            result += 1
    return result if j == len(I) else "IMPOSSIBLE"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, speed_typing()))
