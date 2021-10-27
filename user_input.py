def check_for_integer(number):
    """A function to catch exception handeling of integer datatype error."""
    
    try:
        int(number)    
        return True
    except ValueError:
        return False
    
def user_input():
    """A function for taking input from users."""

    first_check = "no"
    second_check = "no"
    final_check = "no"
    

    while final_check == "no" :
        while first_check == "no" :
            first_input = input("Enter the first number:")
            if check_for_integer(first_input) == False:    
                print("Please enter an integer only.")
            else:
                first_number = int(first_input)
                if first_number > -1 and first_number < 256 :
                    first_check = "yes"
                else:
                    print("Please enter a number between 0 and 255. Only numbers ranging 0 to 255 can be represented in 8-bit binary.")


        while second_check == "no" :
            second_input = input("Enter the second number:")
            if check_for_integer(second_input) == False:
                print("Please enter an integer only.")
            else:
                second_number = int(second_input)
                if second_number > -1 and second_number < 256 :
                    second_check = "yes"
                else:
                    print("Enter a number between  0 and 255. Only numbers ranging 0 to 255 can be represented in 8-bit binary.")

        if (first_number + second_number) > 255 :
            print("The sum of these numbers cannot be more than 255. Only numbers ranging 0 to 255 can be represented in 8-bit binary.")
            first_check = "no"
            second_check = "no"

        else:
            final_check = "yes"
            return[first_number,second_number]    # Returns a list containing two numbers taken from user


                
            
            

