def f(x, t, k):
    if x == t: return k == 15
    if x > t: return 0
    if x < t: return f(x + 2, t, k+1) + f(x + 5, t, k+1) + f(x + 5, t, k+1)
for a in range(2, 10000):
    if f(1,a,0)==1:
        print(a)