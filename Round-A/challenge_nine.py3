def challenge_nine():
    N = int(input().strip())
    s = list(map(int, str(N)))
    x = -sum(s)%9
    s.insert(next((i for i in range(int(x == 0), len(s)) if s[i] > x), len(s)), x)
    return "".join(map(str, s))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, challenge_nine()))
