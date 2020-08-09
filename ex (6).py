''' Exercise #6. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def reverse_string(s):
    if(len(s) == 1):
        return s[0]
    return s[-1] + reverse_string(s[:-1])


#########################################
# Question 2 - do not delete this comment
#########################################
def find_maximum(lst):
    if(lst == []):
        return -1
    if(len(lst) == 1):
        return lst[0]
    if(lst[0] > find_maximum(lst[1:])):
        return lst[0]
    else:
        return find_maximum(lst[1:])

    


#########################################
# Question 3 - do not delete this comment
#########################################
def is_palindrome(s):
    if(len(s) == 0):
        return True
    if (len(s) == 1):
        return True
    if(s[0] != s[-1]):
        return False
    return is_palindrome(s[1:-1])


#########################################
# Question 4 - do not delete this comment
#########################################
def climb_combinations(n):
    if(n == 1):
        return 1

    if(n == 2):
        return 2

    return climb_combinations(n - 1) + climb_combinations(n - 2)


#########################################
# Question 5 - do not delete this comment
#########################################
def is_valid_paren(s, cnt=0):
    if(s == '' and cnt == 0):
        return True
    elif(s == '' and cnt != 0):
        return False
    elif(cnt < 0):
        return False
    if(s[0] == '('):
        cnt += 1
        return is_valid_paren(s[1:], cnt)
    if(s[0] == ')'):
        cnt -=1
        return is_valid_paren(s[1:], cnt)
    return is_valid_paren(s[1:], cnt)
            

 


#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == "__main__":
    #you can add tests for your code here.
    
    assert(reverse_string("abc") == 'cba')
    assert(reverse_string("Hello!") == '!olleH')

    assert(find_maximum([9,3,0,10]) == 10)
    assert(find_maximum([9,3,0]) == 9)
    assert(find_maximum([]) == -1)

    assert(is_palindrome("aa") == True)
    assert(is_palindrome("aa ") == False)
    assert(is_palindrome("caca") == False)
    assert(is_palindrome("abcbbcba") == True)

    assert(climb_combinations(3) == 3)
    assert(climb_combinations(10) == 89)

    assert(is_valid_paren("(.(a)") == False)
    assert(is_valid_paren("p(()r((0)))") == True)
    assert(is_valid_paren("") == True)

# ============================== END OF FILE =================================
