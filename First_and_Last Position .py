'''You have been given a sorted array/list ARR consisting of 'N' elements. 
You are also given an integer 'K'. Now, your task is to find the first and last 
occurrence of 'K' in ARR.

Note:
1 . If 'K' is not present in the array, then the first and the last occurrence will be -1 .
2. ARR may contain duplicate elements.
	For example, if ARR = [0, 1, 1, 5] and K = 1, then the first and 
    last occurrence of 1 will be 	- indexed) and 2.
    
Input Format
The first line of each test case contains two single-space separated integers 'N' and 'K', respectively.
The second line of each test case contains 'N' single space-separated integers denoting the elements of the array/list ARR.

Sample Input O
6 3
0 5 5 6 6 6
Sample Output O
-1 -1

Explanation O
For this test case, 3 is not present in the array. 
Hence the first and last occurence of 3 is -1 and -1 .

Sample Input 1
 8 2
 0 0 1 1 2 2 2 2
Sample Output 1
4 7

Explanation 1
For this test case, the first occurrence of 2 in at index 4 and last occurrence is at index 7.

'''

def search_range(arr , k):
    ans = [-1,-1]
    # First occurrence in ans
    start ,end = 0 , len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if k == arr[mid]:
            ans[0] = mid
            end = mid - 1
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    # Last occurrence in ans
    start ,end = 0 , len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if k == arr[mid]:
            ans[1] = mid
            start = mid + 1
        elif k < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return ans    

n,k = list(map(int,input().split(" ")))
arr = list(map(int,input().split(" ")))[:n]

x = search_range(arr , k)
print(*x)