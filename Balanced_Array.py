'''
Sample Input O
4
1 2 3 4
Sample Output O
4

Explanation O
Sum of first 2 elements is 1 + 2 = 3
Sum of last 2 elements is 3 +4 
To make the array balanced you can add 4.

Sample Input 1
6
1 2 1 2 1 3
Sample Output 1
2

Explanation 1
Sum of first 3 elements is 1 + 2 + 1 = 4,
Sum of last three elements is 2 + 1 + 3 = 6,
To make the array balanced you can add 2.
'''

n = int(input())

arr = list(map(int,input().split(" ")))[:n]

mid = int(n / 2)

sum1 = 0
for i in range(0,mid):
    sum1 += arr[i]

sum2 = 0
for i in range(mid,n):
    sum2 += arr[i]

x = abs(sum1-sum2)
print(x)