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
def draw_rules(start_row, rules, boundary_condition):
    print(start_row)
    rows = len(start_row)

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
        print(new_row)

def main():
    start = "0000000000000001000000000000000"
    number = dec_to_bin(30)
    rules = make_rules(number)
    boundary_condition = adiabatic_boundary 
    draw_rules(start, rules, boundary_condition)


if __name__ == "__main__":
    main()
