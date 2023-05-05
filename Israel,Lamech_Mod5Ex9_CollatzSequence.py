###############################################
# CS 1110A - Programming in Python            #
# Module 5 - Exercise 9 - Collatz Sequence    #
# Author: Lamech Israel                       #
#                                             #
###############################################





# The Collatz Sequence
# The seq3np1() function comes from Section 7.5 in our textbook
def seq3np1(n, find_hundred):
    """ Print the 3n+1 sequence from n,
        terminating when it reaches 1.
    """
    # Create a list
    array = [n]
    # Get a new sequence number, since 'n' changes
    sequence_number = n
    
    
    # The calculation portion
    
    while n > 1:
        if n % 2 == 0:      # n is even
            n = n // 2
        else:               # n is odd
            n = n * 3 + 1
        # Add number to array
        array.append(n)
        
    # Get values to print
    length = len(array)
    
    
    # Prints the sequence 1-8
    if sequence_number < 9:
        print('{0}  :  '.format(sequence_number), end='')
        print('lth = {l}  :  {a}'.format(a = array, l = length), end="\n")
        return find_hundred
    # Prints the first sequence with a length greater than 100
    elif length >= 100 and find_hundred == 'one':
        print('\n{0}  :  '.format(sequence_number), end='')
        print('lth = {l}  :  {a}'.format(a = array, l = length), end="\n")
        return 'two'
    # Prints the first sequence with a length greater than 200
    elif length >= 200 and find_hundred == 'two':
        print('\n{0}  :  '.format(sequence_number), end='')
        print('lth = {l}  :  {a}'.format(a = array, l = length), end="\n")
        return False
    else:
        #print(sequence_number, find_hundred)
        return find_hundred
 
    
# Start Program!    
print('\nDisplay the first several Collatz sequences')
print('and the first of lengths greater than 100 and 200\n')
print('\n#  : Length  : Sequence\n')


# Will track whether we look for 100, 200, or to finish
find_hundred = 'one'
c = 1

while find_hundred != False:
    
    find_hundred = seq3np1(c, find_hundred)
    c+=1
 
print('\nDone!')
