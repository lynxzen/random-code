import turtle
SQUARE_SIZE = 30 

'''
Quick implementation of the rule of (NUMBER) in cellular automata
'''

# simple decimal to binary converting function
def dec_to_bin(dec):
    binary = bin(dec)
    binary = binary[2:]
    binary = fill_zeros(binary)
    return binary

# helper function for dec_to_bin to ensure binary is 8-bit
def fill_zeros(binary):
    num_zeros = 8 - len(binary)
    return ("0" * num_zeros) + binary

# returns a dictionary of the rule of (number) rules
def make_rules(number):
    patterns = ["111", "110", "101", "100", "011", "010", "001", "000"]
    rules = {}
    for idx, i in enumerate(number):
        if i == "1":
            rules[patterns[idx]] = 1
        else:
            rules[patterns[idx]] = 0
    return rules

# returns a string representing the 3-bit block where the adiabatic boundary condition is applied
def adiabatic_boundary(row, isStart):
    if (isStart):
        return row[0] + row[0] + row[1]
    else:
        return row[-2] + row[-1] + row[-1]

# returns a string representing the 3-bit block where reflection boundary condition is applied
def reflection_boundary(row, isStart):
    if (isStart):
        return row[1] + row[0] + row[1]
    else:
        return row[-2] + row[-1] + row[-2]

# displays the wolfram number and chart with the generated rules
def draw_rules(number, start_row, rules, boundary_condition):
    print(start_row)
    rows = len(start_row)
    row_list = [list(start_row)]

    for _ in range(rows):
        new_row = ""
        for idx, _ in enumerate(start_row):
            # apply boundary condition at start
            if idx == 0:
                curr_block = boundary_condition(start_row, 1)
                rule_output = rules[curr_block]
                new_row += str(rule_output) 
            # apply boundary condition at end
            elif idx == len(start_row) - 1:
                curr_block = boundary_condition(start_row, 0)
                rule_output = rules[curr_block]
                new_row += str(rule_output) 
                break 
            # general case
            else:
                curr_block = start_row[idx-1] + start_row[idx] + start_row[idx+1]
                rule_output = rules[curr_block]
                new_row += str(rule_output) 
        start_row = new_row
        row_list.append(list(start_row))
        print(new_row)
    print(f"Wolfram number {number}")
    return row_list 

# draws hollow square
def draw_zero():
    turtle.down()
    turtle.end_fill()
    turtle.fd(SQUARE_SIZE)
    turtle.rt(90)
    turtle.fd(SQUARE_SIZE)
    turtle.rt(90)
    turtle.fd(SQUARE_SIZE)
    turtle.rt(90)
    turtle.fd(SQUARE_SIZE)
    turtle.rt(90)
    turtle.fd(SQUARE_SIZE)
    turtle.up()

# draws filled in square
def draw_one():
    turtle.down()
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.fd(SQUARE_SIZE)
    turtle.rt(90)
    turtle.fd(SQUARE_SIZE)
    turtle.rt(90)
    turtle.fd(SQUARE_SIZE)
    turtle.rt(90)
    turtle.fd(SQUARE_SIZE)
    turtle.rt(90)
    turtle.fd(SQUARE_SIZE)
    turtle.end_fill()
    turtle.up()

# draw the row
def draw_row(row):
    for i in row:
        if i == str(0):
            draw_zero()
        else:
            draw_one()

# iterate through rows and pass into draw_row
def draw_wolfram(rows):
    # turtle initializing 
    turtle.hideturtle()
    x_0, y_0 = turtle.position()
    x_0 = -500
    y_0 = 500
    turtle.up()
    turtle.goto(x_0, y_0)
    turtle.speed(1000)
    
    # iterate through rows and draw them 
    for i in rows:
        draw_row(i)
        y_0 -= SQUARE_SIZE # shift down to next row
        turtle.goto(x_0, y_0) # reset position

# runs the default scenario that i setup
def default_case():
    start = "0000000000000001000000000000000"
    num = 30 
    number = dec_to_bin(30)
    rules = make_rules(number)
    boundary_condition = adiabatic_boundary 
    rows = draw_rules(num, start, rules, boundary_condition)
    draw_wolfram(rows)
    turtle.mainloop()

# helper function for custom case, collects input for the starting row
def get_start_input():
    while True:
        print("Please enter the starting row with only 0s and 1s: ")
        try:
            start = input()
        except:
            continue

        # check if string is a binary number
        is_binary = all(c in '01' for c in start)
        if is_binary:
            return start
        else:
            print("Invalid starting row!")

# helper function for custom case, collects input for wolfram number
def get_num_input():
    while True:
        print("Please enter a number between 0 and 255")
        try:
            num = int(input())
        except:
            continue

        if num < 0 or num > 255:
            print("Invalid number!")
        else:
            return num

# helper function for custom case, collects input for the boundary condition 
def get_boundary_condition_input():
    while True:
        print("Please select a boundary condition")
        print("1) Reflection 2) Adiabatic")
        
        try:
            selection = int(input())
        except:
            continue
        
        if selection == 1:
            return reflection_boundary
        elif selection == 2:
            return adiabatic_boundary
        else:
            print("Invalid Option!")

# let user select parameters for wolfram number program
def custom_case():
    start = get_start_input()
    num = get_num_input()
    number = dec_to_bin(num)
    rules = make_rules(number)
    boundary_condition = get_boundary_condition_input()
    rows = draw_rules(num, start, rules, boundary_condition)
    draw_wolfram(rows)
    turtle.mainloop()

def main():
    # prompt user for default case or custom case
    while True:
        print("Use default case (0) or custom case (1)?")
        try:
            case = int(input())
        except:
            continue
        if case < 0 or case > 1:
            print("Invalid Option!")
        else:
            break

    # prompt user for live drawing or instant display
    while True:
        print("Draw wolfram number(0) or display(1)?")
        try:
            draw_mode = int(input())
        except:
            continue
        if draw_mode == 0:
            turtle.tracer()
            break
        elif draw_mode == 1:
            turtle.tracer(0)
            break
        else:
            print("Invalid option!")

    # perform default or custom cases
    match case:
        case 0:
            default_case()
        case 1:
            custom_case()
        case _:
            print("Invalid Option!")

if __name__ == "__main__":
    main()
