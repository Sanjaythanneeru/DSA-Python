Write a program to do basic string compression. For a character which is consecutively repeated more than once, replace consecutive duplicate occurrences with the count of repetitions.
Example:
If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".

The string is compressed only when the repeated character count is more than 1.
Note:
Consecutive count of every character in the input string is less than or equal to 9.
Input Format:
The first and only line of input contains a string without any leading and trailing spaces.
Output Format:
The output contains the string after compression printed in single line.
Note:
You are not required to print anything. It has already been taken care of. Just implement the given function.
Constraints:
0 <= N <= 10^6

Where 'N' is the length of the input string.

Time Limit: 1 sec
  
  
SOLUTION
=========================================
from sys import stdin

def getCompressedString(input) :
    count, str1=1, ""
    for i in range(len(input)-1):
        if i!=len(input):
            if input[i]==input[i+1]:
                count+=1
            else:
                if count>1:
                    str1=str1+input[i]+str(count)
                else:
                    str1+=input[i]
                    count=1
    return str1

# Main.
string = stdin.readline().strip()
ans = getCompressedString(string)
print(ans)
