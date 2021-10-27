def decimal_to_binary(number):
    """A function for converting a integer to 8-bit binary."""
    
    x = number
    y = [0,0,0,0,0,0,0,0]  # a list with having length 8 for storing a 8-bit binary
    while x > 0:
        if x > 127:
            y[0] = 1
            x = x - 128
        elif x > 63 and x < 128:
            y[1] = 1
            x = x - 64
        elif x > 31 and x < 64:
            y[2] = 1
            x = x - 32
        elif x > 15 and x < 32:
            y[3] = 1
            x = x - 16
        elif x > 7 and x < 16:
            y[4] = 1
            x = x - 8
        elif x > 3 and x < 8:
            y[5] = 1
            x = x - 4
        elif x > 1 and x < 4:
            y[6] = 1
            x = x - 2
        elif x == 1:
            y[7] = 1
            x = 0
    return y        # Returns a list


    
    


