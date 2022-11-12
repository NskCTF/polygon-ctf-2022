from bitfields import Bits

registers = {"r0": "000", "r1": "001", "r2": "010", "r3": "011", "r4": "100", "r5": "101", "r6": "110", "r7": "111"}
cond_reg = {"pos": 1 << 0, "zro": 1 << 1, "neg": 1 << 2}
instructions = {"com": "pass", "label": "pass", "addr": "pass", "trap": "0000", "lea": "0001", "res": "0010", "jmp": "0011", "sti": "0100", "ldi": "0101", "sub": "0110", "xor": "0111", "str": "1000", "ldr": "1001", "mult": "1010", "jsr": "1011", "st": "1100", "ld": "1101", "add": "1110", "br": "1111", "jsrr": "1011"}
memory_register = {"kbsr": 0xfe00, "kbdr": 0xfe02}
trap_signals = {"getc": b'\x20', "out": b'\x21', "puts": b'\x22', "in": b'\x23', "putsp": b'\x24', "halt": b'\x25'}


curr_offset = 0
labels = {}


instruction_cnt = 0
all_lines = 0
with open("/home/spile/share_folder/virtual_mashine/source.asm") as source:
    incode = 1
    for line in source.readlines():
        all_lines += 1
        if line.strip() == "SRINGS:":
            incode = 0
        if line.strip() == "" or line.strip().split()[0] == "com":
            continue
        if "label" in line.strip():
            labels[line.strip().split()[1]] = instruction_cnt
            continue
        if incode:
            instruction_cnt += 1

def two_components(binq, n):
    print(binq)
    if binq[0] == "-":
        binq = binq[3:]
        new_bin = ""
        for i in range(len(binq)):
            if binq[i] == "1":
                new_bin += "0"
            else:
                new_bin += "1"
        new_bin = new_bin.rjust(n, "1")
        # print(bin(int(new_bin, 2) + 1)[2:])
        return bin(int(new_bin, 2) + 1)[2:]
    else:
        # print(binq[2:].rjust(n, "0"))
        return binq[2:].rjust(n, "0")

def arithmetic_instructions(ins_binary, cur_instruction, instruction_cnt):
    ins_binary += registers[cur_instruction[1]]
    ins_binary += registers[cur_instruction[2]]
    if cur_instruction[3][0] == "#":
        ins_binary += "1"
        number1 = int(cur_instruction[3][1:])
        # print(number1)
        if number1 > 15:
            print(f"Instruction on {instruction_cnt}. Number biiger than 15.")
            exit(1)
        number1 = two_components(bin(number1), 5)
        ins_binary += number1
    else:
        ins_binary += "000"
        ins_binary += registers[cur_instruction[3]]
    output = bytes(Bits.from_binary(ins_binary))
    return output


def load_instructions(ins_binary, cur_instruction, instruction_cnt):
    ins_binary += registers[cur_instruction[1]]
    # print(cur_instruction)
    number2 = 0
    if cur_instruction[2][0] == "#":
        number2 = int(cur_instruction[2][1:])
    if number2 > (1 << 10) - 1:
        print(f"Instruction on {instruction_cnt}. Number biiger than {(1 << 10) - 1}.")
        exit(1)
    number2 = bin(number2)
    number2 = two_components(number2, 9)
    ins_binary += number2
    output = bytes(Bits.from_binary(ins_binary))
    return output

def ldr(ins_binary, cur_instruction, instruction_cnt):
    ins_binary += registers[cur_instruction[1]]
    ins_binary += registers[cur_instruction[2]]
    number2 = int(cur_instruction[3][1:])
    if number2 > (1 << 7) - 1:
        print(f"Instruction on {instruction_cnt}. Number biiger than {(1 << 7) - 1}.")
        exit(1)
    number2 = bin(number2)[2:].rjust(6, "0")
    ins_binary += number2
    output = bytes(Bits.from_binary(ins_binary))
    return output

with open("/home/spile/share_folder/virtual_mashine/source.asm") as source, open("/home/spile/share_folder/virtual_mashine/image.out", "wb") as image:
    bu = b"\x30\x00"
    image.write(bu)
    for i in range(all_lines):
        cur_instruction = source.readline().strip()
        if cur_instruction == "":
            continue
        cur_instruction = cur_instruction.split()
        ins_name = cur_instruction[0]
        if ins_name == "label" or ins_name == "com":
            continue
        curr_offset += 1
        if ins_name[:2] == "br":
            ins_binary = instructions["br"]
        else:
            ins_binary = instructions[ins_name]
        if ins_name == "trap":
            ins_binary += "0000"
            output = b"\x00"
            if cur_instruction[1] == "getc":
                output += trap_signals["getc"]
            elif cur_instruction[1] == "out":
                output += trap_signals["out"]
            elif cur_instruction[1] == "puts":
                output += trap_signals["puts"]
            elif cur_instruction[1] == "in":
                output += trap_signals["in"]
            elif cur_instruction[1] == "putsp":
                output += trap_signals["putsp"]
            elif cur_instruction[1] == "halt":
                output += trap_signals["halt"]
            image.write(output)
        elif ins_name == "lea":
            a = load_instructions(ins_binary, cur_instruction, i)
            image.write(a)
        elif ins_name == "jmp":
            ins_binary += "000"
            ins_binary += registers[cur_instruction[1]]
            ins_binary += "000000"
            output = bytes(Bits.from_binary(ins_binary))
            image.write(output)
        elif ins_name == "sti":
            image.write(load_instructions(ins_binary, cur_instruction, i))
        elif ins_name == "ldi":
            image.write(load_instructions(ins_binary, cur_instruction, i))
        elif ins_name == "sub":
            image.write(arithmetic_instructions(ins_binary, cur_instruction, i))
        elif ins_name == "xor":
            image.write(arithmetic_instructions(ins_binary, cur_instruction, i))
        elif ins_name == "str":
            image.write(ldr(ins_binary, cur_instruction, i))
        elif ins_name == "ldr":
            image.write(ldr(ins_binary, cur_instruction, i))
        elif ins_name == "mult":
            image.write(arithmetic_instructions(ins_binary, cur_instruction, i))
        elif ins_name == "jsr":
            ins_binary += "1"
            if cur_instruction[1][0] == "#":
                number2 = int(cur_instruction[1][1:])
            else:
                number2 = labels[cur_instruction[1]] - curr_offset
            curr_offset += number2
            if number2 > (1 << 12) - 1:
                print(f"Instruction on {instruction_cnt}. Number biiger than {(1 << 12) - 1}.")
                exit(1)
            number2 = bin(number2)
            number2 = two_components(number2, 11)
            ins_binary += number2
            output = bytes(Bits.from_binary(ins_binary))
            image.write(output)
        elif ins_name == "jsrr":
            ins_binary += "000"
            ins_binary += registers[cur_instruction[1]]
            ins_binary += "000000"
            output = bytes(Bits.from_binary(ins_binary))
            image.write(output)
        elif ins_name == "st":
            image.write(load_instructions(ins_binary, cur_instruction, i))
        elif ins_name == "ld":
            image.write(load_instructions(ins_binary, cur_instruction, i))
        elif ins_name == "add":
            image.write(arithmetic_instructions(ins_binary, cur_instruction, i))
        elif "br" in ins_name:
            if "n" in ins_name:
                ins_binary += "1"
            else:
                ins_binary += "0"
            if "z" in ins_name:
                ins_binary += "1"
            else:
                ins_binary += "0"
            if "p" in ins_name:
                ins_binary += "1"
            else:
                ins_binary += "0"
            number2 = 0
            if cur_instruction[1][0] != "#":
                number2 = labels[cur_instruction[1]] - curr_offset
            else:
                number2 = int(cur_instruction[1][1:])
            print(number2)
            curr_offset += number2
            if number2 > (1 << 10) - 1:
                print(f"Instruction on {instruction_cnt}. Number biiger than {(1 << 10) - 1}.")
                exit(1)
            number2 = bin(number2)
            number2 = two_components(number2, 9)
            ins_binary += number2
            output = bytes(Bits.from_binary(ins_binary))
            image.write(output)
        elif ins_name == "addr":
            num = int(cur_instruction[1], 16).to_bytes(2, 'big')
            image.write(num)
        else:
            print(f"nety takoi instrukcii: {i}")