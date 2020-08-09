''' Exercise #4. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def most_popular_character(my_string):
    d = {}
    for s in my_string:
        d[s] = d.get(s, 0) + 1
    sorted_values = sorted(d.keys(), key=d.get, reverse = True)

    letters = [sorted_values[0]]
    
    for i in range(1, len(sorted_values)):
        if(d[sorted_values[i]] == d[sorted_values[0]]):
            letters.append(sorted_values[i])

    sorted_letters = sorted(letters)
    return sorted_letters[0]            
    

#########################################
# Question 2 - do not delete this comment
#########################################
def diff_sparse_matrices(lst):
    
    sparse = {}
    final = {}
    for dic in lst:
        for key in dic:
            if((key not in sparse)):
                sparse[key] = dic[key]
            else:
                sparse[key] -= dic[key]
    for key in sparse:
        if (sparse[key] != 0):
            final[key] = sparse[key]
    return final

#########################################
# Question 3 - do not delete this comment
#########################################
def find_substring_locations(s, k):
    d = {}
    for i in range(len(s) - k + 1):
        if(s[i: i + k] in d.keys()):
            d[s[i: i + k]].append(i)
        else:
            d[s[i: i + k]] = [i]
    return d



#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):
    d = {}
    for t in tuples_lst:
        if(t[0].lower() not in d):
            l = t[1].lower()
            d[t[0].lower()] = [l]
        else:
            l = t[1].lower()
            d[t[0].lower()].append(l)

    return d


    


def students_per_course(tuples_lst):
    d_courses  = courses_per_student(tuples_lst)    
    d_new = {}
    for t in d_courses:
        d_new[t] = len(d_courses.get(t))
    return d_new



if __name__ == '__main__':
    # Q1
    assert most_popular_character('aabbAA') == 'A'

    # Q2
    assert diff_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): -4, (2, 7): 1}

    # Q3
    assert find_substring_locations('TTAATTAGGGGCGC', 2) == {'TT': [0, 4], 'TA': [1, 5], 'AA': [2], 'AT': [3],
                                                             'AG': [6], 'GG': [7, 8, 9], 'GC': [10, 12], 'CG': [11]}

    # Q4
    assert courses_per_student([('Rina', 'Math'), ('Yossi', 'Chemistry'),
                                ('Riki', 'python'), ('Rina', 'pYthon'), ('Yossi', 'biology')]) == \
           {'rina': ['math', 'python'], 'yossi': ['chemistry', 'biology'], 'riki': ['python']}

    assert students_per_course([('Rina', 'Math'), ('Yossi', 'Chemistry'),
                               ('Riki', 'python'), ('Rina', 'pYthon'), ('Yossi', 'biology')]) == \
           {'rina': 2, 'yossi': 2, 'riki': 1}

# ============================== END OF FILE =================================
