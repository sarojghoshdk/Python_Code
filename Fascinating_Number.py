'''When a number N( 3 digits or more ) is multiplied by 2 and 3, and when both these 
products are concatenated with the original number, then it results in all digits 
from 1 to 9 present exactly once. There could be any number of zeros and are ignored.

Input Format
First line contains the number N.

Output Format
Print whether 'Fascinating Number' or 'Not Fascinating Number'.

Sample Input O
192                                                   192 + 384 + 576 = 192384576

Sample Output O
Fascinating Number

Sample Input 1
501                                             501 + 1002 + 1503=50110021503

Sample Output 1
Not Fascinating Number
'''

def check_fascinating(num):

    concat = str(num) + str(num*2) + str(num*3)

    if "0" in concat:
        return "Not Fascinating Number"
    if len(concat) > 9:
        return "Not Fascinating Number"
    for i in range(1,10):
        if str(i) not in concat:
            return "Not Fascinating Number"
        
    return "Fascinating Number"
    

num = int(input())
x = check_fascinating(num)
print(x)
