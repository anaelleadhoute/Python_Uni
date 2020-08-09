''' Exercise #5. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def sum_nums(file):

    f = open(file, 'r')
    lst = f.readlines()[0].split(' ')
    num = 0
    for n in lst:
        num += int(n)
    return num

#########################################
# Question 2 - do not delete this comment
#########################################
def count_lines(in_file, out_file):
    f_in = open(in_file, 'r')
    lst = f_in.readlines()
    f_in.close()
    f_out = open(out_file, 'w')
    f_out.write(str(len(lst)))
    f_out.close()


#########################################
# Question 3 - do not delete this comment
#########################################
def simple_sent_analysis(in_file):
    f = None
    try:
        f = open(in_file, 'r')
        d = {'happy':0, 'sad':0}
        words = []
        for line in f:
            words = line.split()
            for word in words:
                if (word.lower().strip('!?, -;$%') == 'happy'):
                    d['happy'] += 1
                if (word.lower().strip('!?, -;$%') == 'sad'):
                    d['sad'] += 1
        return d
    except IOError:
        dd = {}
        print('Cannot encode ' + in_file + ' due to IOError')
        return dd
    finally:
        if(f != None):
            f.close()

        
            
        


#########################################
# Question 4 - do not delete this comment
#########################################
def calc_profit_per_group(in_file):
    f = None
    try:
        hcounter = 0
        scounter = 0
        ncounter = 0
        series = []
        d = {'sad':0, 'happy':0, 'neutral':0}
        f = open(in_file, 'r')
        for line in f:
            line = line.strip()
            lst = line.split(',')
            try:
                if(lst[0] not in series):
                    series.append(lst[0])
                else:
                    raise ValueError()
            except ValueError:
                print('The series ' + lst[0] + ' appears more than once')
                return {}



            if(len(lst) != 3):
                raise ValueError('Invalid Input.')
            if(lst[2] != 'happy' and lst[2] != 'neutral' and lst[2] != 'sad'):
                raise ValueError('Invalid Input.')
            try:
                float(lst[1])
            except ValueError:
                raise ValueError('Invalid Input.') from None



                

            if(lst[2] == 'happy'):
                    hcounter += 1
                    d['happy'] +=  float(lst[1])
            if(lst[2] == 'sad'):
                scounter += 1
                d['sad'] +=  float(lst[1])
            if(lst[2] == 'neutral'):
                ncounter += 1
                d['neutral'] +=  float(lst[1])


        
        if(scounter != 0):
            d['sad'] = d['sad']/scounter
        else:
            d['sad'] = 'NA'
        if(hcounter != 0):
            d['happy'] = d['happy']/hcounter
        else:
            d['happy'] = 'NA'
        if(ncounter != 0):
            d['neutral'] = d['neutral']/ncounter
        else:
            d['neutral'] = 'NA'
        return d
    except IOError:
        print("Can't load " + in_file + " due to IOError")

    finally:
        if (f != None):
            f.close()

    
            

            
        
    
  


#########################################
# Question 5 - do not delete this comment
#########################################

def listofcharsToString(s):  
    
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new

    

def letter_change(lst):
    abc = list('abcdefghijklmnopqrstuvwxyz')
    ABC = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for y, letter in enumerate(lst):
        if(letter in abc):
            if(letter == 'a'):
                lst[y] = 'z'
            i = abc.index(letter)
            lst[y] = abc[i - 1]
        if(letter in ABC):
            if(letter == 'A'):
                lst[y] = 'Z'
            i = ABC.index(letter)
            lst[y] = ABC[i - 1]
    return lst


def decode(in_file, out_file):
    f = None
    f_out = None
    try:
        f = open(in_file, 'r')
        f_out = open(out_file, 'w')

        
        for line in f:
            lst = []
            l = line.split()
            for word in l:
                lst.append(listofcharsToString(letter_change(list(word))))

            s = ' '.join(word for word in lst)


            f_out.write(s + '\n')

    except IOError:
        print('Cannot decipher' + in_file + 'due to IOError')
    finally:
        if(f != None):
            f.close()
        if(f_out != None):
            f.close()
        

print(decode('q5.txt', 'q5_deciphered.txt'))
            
        
        



            
            
            
    
    



#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################

	
# ============================== END OF FILE =================================
