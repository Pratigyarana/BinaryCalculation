import addition
import conversion
import user_input


def list_to_string(li):
    """Converts a list li into a string"""
    
    string = ""
    for i in li:
        i = str(i)
        string = string + i
    return string 

check = "yes"

while check != "no":
    if check == "yes":
        li = user_input.user_input()
        
        first_binary = conversion.decimal_to_binary(li[0])
        
        second_binary = conversion.decimal_to_binary(li[1])
       
        bit_addition = addition.bit_addition(first_binary, second_binary)

        bitwise_add = addition.bitwise_addition(li[0],li[1])

        print("The first number converted to binary is ", list_to_string(first_binary))
        print("The second number converted to binary is ", list_to_string(second_binary))
        print("The sum of these two numbers in binary is ", list_to_string(bit_addition))
        print("The sum of these two number in decimal notation is ",bitwise_add)

    else:
        print("Enter either yes or no only.")
    check = input("Do you want to do another addition? Enter yes for another addition or Enter no to end the program : ")
    check = check.lower()    


if check == "no":
    print("Have a good day.")
        
        
