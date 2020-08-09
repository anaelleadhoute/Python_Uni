''' Exercise #1 - solution. Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
R = 5 # Replace ??? with a positive float of your choice.
# Write the rest of the code for question 1 below here.

pi = 3.14
d = R*2
c = 2*pi*R
a = pi*(R**2)
print('Diametre is: %s' % str(d))
print('Circumference is: %s' % str(c))
print('Area is: %s' % str(a))


#########################################
# Question 2 - do not delete this comment
#########################################
S = "hello, dear world!" # Replace ??? a string of your choice.
# Write the rest of the code for question 2 below here.
if(len(S) > 10):
    lower = S[0:10].lower()
    upper = S[10:].upper()
    print(lower + upper)
else:
    mid = S[1:len(S)]
    print('$' + mid + '@')
    





#########################################
# Question 3 - do not delete this comment
#########################################
number  = -6 # Replace ??? with a int of your choice.
# Write the rest of the code for question 3 below here.
if(number % 2 == 0):
    print('I am %s and I am even' % str(number))
else:
    print('I am %s and I am odd' % str(number))



#########################################
# Question 4 - do not delete this comment
#########################################
a = 9 # Replace ??? with a positive int of your choice.
b = 5  # Replace ??? with a positive int of your choice.
c = 5  # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 4 below here.
print("%.5f" % (a + b)**(1/c))
print("%.5f" % (a**b)**(1/c))
print("%.5f" % ((a/b) - (b/c)))



#########################################
# Question 5 - do not delete this comment
#########################################
year = 1900 # Replace ??? with a positive int of your choice.
# Write the rest of the code for question 5 below here.

if((year%100!=0 and year%4 == 0) or year%400 == 0):
    print(str(year) + ' is a leap year')

else:
    print(str(year) + ' is not a leap year')



