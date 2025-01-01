def combo_operand(reg, op):
    if op == 4:
        op = reg["A"]
    elif op == 5:
        op = reg["B"]
    elif op == 6:
        op = reg["C"]
    return op
def parse_program(arr):
    reg = {}
    prog = []
    for line in arr:
        if "Register" in line:
            args = line[9:].split(":")
            reg[args[0]] = int(args[1].strip())
        if "Program" in line:
            prog = line[8:].split(",")
            prog = [int(x) for x in prog]

    return reg, prog
def run(reg, prog, match=None):
    ip = 0

    out = ""
    while ip < len(prog):
        opc = prog[ip]
        op = prog[ip + 1]
        
        if opc == 0:
            reg["A"] //= 2 ** combo_operand(reg, op)
        elif opc == 1:
            reg["B"] ^= op
        elif opc == 2:
            reg["B"] = combo_operand(reg, op) % 8
        elif opc == 3:
            if reg["A"] != 0:
                ip = op
                continue
        elif opc == 4:
            reg["B"] ^= reg["C"]
        elif opc == 5:
            out += str(combo_operand(reg, op) % 8) + ","
            if match and out != match[:len(out)]:
                return None, None
        elif opc == 6:
            reg["B"] = reg["A"] // 2 ** combo_operand(reg, op)

        elif opc == 7:
            reg["C"] = reg["A"] // 2 ** combo_operand(reg, op)
        ip += 2

    return out

def pt1(arr):
    reg, prog = parse_program(arr)    
    print(reg, prog)
    # removes last comma
    return run(reg, prog)[:-1]


def pt2(arr):
    reg, prog = parse_program(arr)
    found = [0]
    for digit in range(1, len(prog)+1):
        program_str = ",".join([str(x) for x in prog[-digit:]]) + ","
        # The next program will be the last + one place value in octal (* 8)
        for i in range(found[-1]*8, 10**17):
            reg["A"] = i
            output = run(reg, prog, program_str)
            if output == program_str:
                found.append(i)
                break

    return found[-1]

arr = open('input/temp').read().splitlines()
# arr = open('input/d17').read().splitlines()
# print(arr)
print("Part 1", pt1(arr))
# 2,1,0,4,6,2,4,2,0,
print("Part 2", pt2(arr))
# 109685330781408