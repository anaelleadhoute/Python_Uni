""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 4  # Replace the assignment with a positive integer to test your code.
A = [1, 2, 3, 4]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 1 below here.

for i,elem in enumerate(A):
    if(elem%a == 0):
        print(i)
        break
    if(i == len(A) - 1):
        print("-1")


# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
B = ['aaaaa','aaaaaa','aaaaaa','aaaaaa','a']
# Replace the assignment with other lists of strings (str) to test your code.


# Write the code for question 2 using a for loop below here.
oreh = 0
for word in B:
    oreh+= len(word)

ave = oreh/len(B)
counter = 0
for word in B:
    if(len(word)> ave):
        counter += 1
print("The number of strings longer than the average is: " + str(counter))
        

# Write the code for question 2 using a while loop below here.
ore = 0
while i < len(B):
    print(B[i])
    ore += len(B[i])
    i += 1
av = ore/len(B)
counte = 0
while i < len(B):
    if(len(B[i]) > av):
        counte += 1

print("The number of strings longer than the average is: " + str(counter))


# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

C = [2]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.

summ = 0
for i in range(len(C) - 1):
    summ += C[i]*C[i + 1]
print(summ)


# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

D = [1, 2, 3, 4, 7]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.

        
i = 0
c = 0
l = [D[0]]
for i,elem in enumerate(D):
    if(abs(elem - l[-1]) > c):
        c = abs(elem - l[-1])
        l.append(elem)
    else:
        continue


  
print(l)
    
    

# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefggggg'  # Replace the assignment with other strings to test your code.
k = 5  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.

for i,letter in enumerate(my_string):
    if i > len(my_string) - k:
        print("Didn't find a substring of length "  + str(k))
        break
    if(my_string[i:k + i] == k*letter):
        print('For length ' + str(k) + ',' ' found the substring ' + k*letter + '!')
        break








# End of code for question 5
