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

def main():
    start = "0000000000000001000000000000000"
    num = 30 
    number = dec_to_bin(30)
    rules = make_rules(number)
    boundary_condition = reflection_boundary 
    rows = draw_rules(num, start, rules, boundary_condition)
    draw_wolfram(rows)
    turtle.mainloop()
 
if __name__ == "__main__":
    main()
