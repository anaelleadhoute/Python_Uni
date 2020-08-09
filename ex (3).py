''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_divisible_by_k(lst, k):
    s = 0
    for elem in lst:
        if elem%k == 0:
            s += elem
    return s




#########################################
# Question 2 - do not delete this comment
#########################################
def mult_odd_digits(n):
    d = 0
    s = 1
    for i in range(len(str(n))):
        d = n%10
        if(d%2 != 0):
            s *= d
        n = n//10

    return int(s)

#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):
    count = 0
    maxc = 0
    for string in s:
        if string == c:
            count += 1
            if(count > maxc):
                maxc = count
        else:
            count = 0
            

    return maxc



#########################################
# Question 4 - do not delete this comment
#########################################
def upper_strings(lst):
    if(isinstance(lst, list) == False):
        return -1 
    for i, elem in enumerate(lst):
        if(isinstance(elem, str)):
            lst[i] = lst[i].upper()
    return lst



#########################################
# Question 5 - do not delete this comment
#########################################
def div_mat_by_scalar(mat, alpha):
    nmat = [[0]*len(mat[0]) for i in range(len(mat))]
    for i in range(len(nmat)):
        for y in range(len(nmat[0])):
            nmat[i][y] = mat[i][y]//alpha
    return nmat

mat1 = [[2, 4], [6, 8]]
mat2 = div_mat_by_scalar(mat1, 2)




#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    nmat = [[0]*len(mat) for i in range(len(mat[0]))]
    for i in range(len(mat)):
        for y in range(len(mat[0])):
            nmat[y][i] = mat[i][y]
    return nmat


    
#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

print(sum_divisible_by_k([3, 6, 4, 10, 9], 3) == 18)
print(sum_divisible_by_k([45.5, 60, 73, 48], 4) == 108)


print(mult_odd_digits(5638) == 15)
print(mult_odd_digits(2048) == 1)
print(mult_odd_digits(54984127) == 315)


print(count_longest_repetition('eabbaaaacccaaddd', 'a') == 4)
print(count_longest_repetition ('cccccc','c') == 6)
print(count_longest_repetition ('abcde', 'z') == 0)


vals = [11, 'TeSt', 3.14, 'cAsE']
upper_strings(vals)
print(vals == [11, 'TEST', 3.14, 'CASE'])

vals = [-5, None, True, [1, 'dont change me', 3]]
upper_strings(vals)
print(vals == [-5, None, True, [1, 'dont change me', 3]])

print(upper_strings(42) == -1)
print(upper_strings('im not a list') == -1)
print(upper_strings(False) == -1)


mat1 = [[2, 4], [6, 8]]
mat2 = div_mat_by_scalar(mat1, 2)
print(mat1 == [[2, 4], [6, 8]])
print(mat2 == [[1, 2], [3, 4]])
print(div_mat_by_scalar([[10,15], [-3,6]], -5) == [[-2, -3], [0, -2]])


mat = [[1,2],[3,4],[5,6]]
mat_T = mat_transpose(mat)
print(mat == [[1, 2], [3, 4], [5, 6]])
print(mat_T == [[1, 3, 5], [2, 4, 6]])

mat2 = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
mat2_T = mat_transpose(mat2)
print(mat2_T == [[0, 10, 20], [1, 11, 21], [2, 12, 22]])


# ============================== END OF FILE =================================
