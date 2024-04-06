'''
Quick implementation of the rule of (NUMBER) in cellular automata
'''

def dec_to_bin(dec):
    binary = bin(dec)
    binary = binary[2:]
    binary = fill_zeros(binary)
    return binary

def fill_zeros(binary):
    num_zeros = 8 - len(binary)
    return ("0" * num_zeros) + binary

def make_rules(number):
    patterns = ["111", "110", "101", "100", "011", "010", "001", "000"]
    rules = {}
    for idx, i in enumerate(number):
        if i == "1":
            rules[patterns[idx]] = 1
        else:
            rules[patterns[idx]] = 0
    return rules

def adiabatic_boundary(row, isStart):
    if (isStart):
        return row[0] + row[0] + row[1]
    else:
        return row[-2] + row[-1] + row[-1]

def reflection_boundary(row, isStart):
    if (isStart):
        return row[1] + row[0] + row[1]
    else:
        return row[-2] + row[-1] + row[-2]

def draw_rules(start_row, rules, boundary_condition):
    print(start_row)
    cols = len(start_row)
    rows = cols

    for _ in range(rows):
        new_row = ""
        for idx, i in enumerate(start_row):
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
