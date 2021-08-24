'''     Richard Elgar
        SDEV220
        Algebra: solve linear 2 X 2 linear equations
        DUE: 31 AUG 21
        
You  can  use  Cramer’s  rule  to  solve  the following 2 X 2 system of linear equation:

        ax + by = e
        cx + dy = f
        x = (ed - bf) / (ad - bc)
        y = (af - ec) / (ad - bc)

Write a program that prompts the user to enter a, b, c, d, e, and f and display the result. 

If ad – bc is 0, report that The equation has no solution.

If X-Y = 0, print out the input numbers used for a,b,c,d,e,f
'''

a, b, c, d, e, f = eval(input("Enter values for a, b, c, d, e and f (separated with commas): "))

if a * d - b * c == 0 : 
        print("Equation has no solution, try a different set of values")
else : 
        y = (a * f - e * c) / (a * d - b * c)           
        x = (e * d - b * f) / (a * d - b * c)

        if x - y == 0 : 
                print("NOTE: x - y = 0")
                print("a = ",a, "\nb = ",b,"\nc = ",c,"\nd = ",d,"\ne = ",e,"\nf = ",f)

        print("x = ", x, "\ny = ", y)
 

        
