```
# Good Solution
def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        for j in range(i[0], i[1] + 1):
            arr[j - 1] += i[2]
    return max(arr)
```
**We loop over the rows in the query, and then sub-loop over the elements of the array than need summation. 
This approach works, but it will not pass (in an acceptable amount of time) the higher tests in when $n$ is very large 
e.g. the first line is 10000000 100000 ($n=10000000$ and # queries$=100000$).**

```
## Better Solution
def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        arr[i[1]] -= i[2]
    maxval = 0
    itt = 0
    print(arr)
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval
```

**The insight here is that the sum only needs to be calculated for each step or fall in the array rather than every individual element. 
This is easier understand if you draw a picture, 
but ultimately it allows us to do a single loop for calculating the two steps in the array, 
and another for accounting for the maximum step height.**


>**There still remains the edge-case where arr[i[1]] -= i[2] doesn’t work because if i[1] == len(arr), adding ‘fall’ to the ‘step’ is erroneous. So simply add in a conditional before arr[i[1]] -= i[2]**
```
# Best Solution
def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        arr[i[0] - 1] += i[2]
        if i[1] != len(arr):
            arr[i[1]] -= i[2]
    maxval = 0
    itt = 0
    print(arr)
    for q in arr:
        itt += q
        if itt > maxval:
            maxval = itt
    return maxval   
```

[Source](https://sites.northwestern.edu/acids/2018/11/12/solution-hackerrank-array-manipulation/)
