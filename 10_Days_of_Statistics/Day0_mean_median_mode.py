import statistics as st
from scipy import stats

N = int(input())
X = list(map(int, input().split()))
print(st.mean(X))
print(st.median(X))
print(int(stats.mode(X)[0]))
