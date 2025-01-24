from collections import deque

def max_score(arr, k):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]
    
    dq = deque([0])  #deque to maintain index of dp in decreasing order
    
    for i in range(1, n):
        #remove index out of the current window
        if dq[0] < i - k:
            dq.popleft()
        
        #compute dp[i] as arr[i] + max in window
        dp[i] = arr[i] + dp[dq[0]]
        
        #maintain deque order: remove locations with smaller dp values
        while dq and dp[dq[-1]] <= dp[i]:
            dq.pop()
        
        #add current index
        dq.append(i)
    
    return dp[-1]

t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    k = int(input().strip())
    results.append(max_score(arr, k))

print("\n".join(map(str, results)))
