N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
nume = 0.0
deno = 0
for i in range(N):
    nume += X[i] * W[i]
    deno += W[i]
print(round((nume/deno),1))
