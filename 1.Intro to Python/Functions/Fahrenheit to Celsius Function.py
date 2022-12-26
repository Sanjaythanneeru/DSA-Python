Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.
Input Format :
3 integers - S, E and W respectively
Output Format :
Fahrenheit to Celsius conversion table. One line for every Fahrenheit and Celsius Fahrenheit value. Fahrenheit value and its corresponding Celsius value should be separate by tab ("\t")
Constraints :
0 <= S <= 1000
0 <= E <= 1000
0 <= W <= 1000

SOLUTION
======================
def printTable(start,end,step):
    for i in range(start, end+1, step):
        c= int((5/9) * (i-32))
        print(i, end="\t")
        print(c)
        

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)
