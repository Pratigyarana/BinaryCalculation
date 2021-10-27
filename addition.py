def full_adder(carry_in, a , b):  #takes three input 
    """A function that simulates full adder circuit."""
    
    added = (a ^ b) ^ carry_in
    carry_out = (carry_in & a) | (carry_in & b) | (a & b)
    return [carry_out,added] # returns a list having carry out and added as its element


def bit_addition(a, b):
    """Function for 8-bit binary addition which takes two list as input and returns a added list."""
    
    addition_list = [0,0,0,0,0,0,0,0] # a lsit for storing the added binary number  
    carry = 0
    for i in range (7 , -1 ,-1):
        addition_list[i] = full_adder(carry, a[i], b[i])[1]
        carry = full_adder(carry, a[i], b[i])[0]
        
   
    return(addition_list) #returns a list
  


def bitwise_addition(a,b):
    """A function for bitwise addition of two numbers."""
    
    carry = a & b   
    added = a ^ b
    while carry > 0:
        shift_left = carry << 1
        carry = added & (carry << 1)
        added = added ^ shift_left   
    return added  #returns a integer number.
