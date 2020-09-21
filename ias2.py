#IMT2019525 - VIJAY JAISANKAR
# THIS IS FOR PROGRAM - 2

# To view the high level program, please see program2.py


# Indicates instruction absent here
VOID_INSTRUCTION = '00000000'

# Opcodes to Instruction name decoder
INSTRUCTION_DICTIONARY = {
    '00001010': 'LOAD MQ',
    '00001001': 'LOAD MQ,M(X)',
    '00100001': 'STOR M(X)',
    '00000001': 'LOAD M(X)',
    '00000010': 'LOAD -M(X)',
    '00000011': 'LOAD |M(X)|',
    '00000100': 'LOAD -|M(X)|',
    '00001101': 'JUMP M(X,0:19)',
    '00001110': 'JUMP M(X,20:39)',
    '00001111': 'JUMP + M(X,0:19)',
    '00010000': 'JUMP + M(X,20:39)',
    '00000101': 'ADD M(X)',
    '00000111': 'ADD |M(X)|',
    '00000110': 'SUB M(X)',
    '00001000': 'SUB |M(X)|',
    '00001011': 'MUL M(X)',
    '00001100': 'DIV M(X)',
    '00010100': 'LSH',
    '00010101': 'RSH',
    '00010010': 'STOR M(X,8:19)',
    '00010011': 'STOR M(X,28:39)',
    '11110000': 'HALT'
}

# Sizes of instruction memory and data memory
SIZE_INS = 300
SIZE_DATA = 700



# Converts regular decimal number into binary
def convert_binary_into_regularDecimal(n):
    x = int(n,2)
    return x


# Gets modulus of a decimal number
def getMod(n):
    if n>=0:
        return n
    else:
        return -n

# Pads a positive decimal to k digits in binary
def pad_to_k(positiveN,k):
    s = bin(positiveN).replace("0b","")
    l = len(s)
    s2=''
    for i in range(k-l):
        s2+='0'
    s2+=s
    return s2

# Sign Magnitude to Decimal Conveter
def convert_signMagBinary_to_decimal(s):
    if(s[0]=='0'):
        mult = 1
    else:
        mult = -1
    s2 = s[1:]
    return mult * int(s2,2)

# Decimal to Sign Magnitude Converter
def convert_decimal_to_signMagBinary(n):
    if n>=0:
        first = '0'
    else:
        first = '1'
    x = getMod(n)
    s = bin(n).replace("0b","")
    s2 = pad_to_k(x,39)
    return first + s2

# Check if ALU is non-negative
def isALU_Non_Negative(ALU_content):
    n = convert_signMagBinary_to_decimal(ALU_content)
    if n<0:
        return False
    else:
        return True

# Adds ALU content with that of MBR
def AddTwo_dec_SignMag(ALU_content,MBR_content):
    n1 = convert_signMagBinary_to_decimal(ALU_content)
    n2 = convert_signMagBinary_to_decimal(MBR_content)
    x = n1+n2
    l=[]
    l.append(x)
    s = convert_decimal_to_signMagBinary(x)
    l.append(x)
    return l
    # print(l)

# Subtracts ALU content from that of MBR
def SubtractTwo_dec_SignMag(ALU_content,MBR_content):
    n1 = convert_signMagBinary_to_decimal(ALU_content)
    n2 = convert_signMagBinary_to_decimal(MBR_content)
    x = n1-n2
    l=[]
    l.append(x)
    s = convert_signMagBinary_to_decimal(x)
    l.append(x)
    return l

# Shifts ALU content left once
def leftShift_dec_SignMag(ALU_content):
    n1 = convert_signMagBinary_to_decimal(ALU_content)
    n1 = n1*2
    l=[]
    l.append(n1)
    s = convert_decimal_to_signMagBinary(n1)
    l.append(s)
    return l

# Shifts ALU content right once
def rightShift_dec_SignMag(ALU_content):
    n1 = convert_signMagBinary_to_decimal(ALU_content)
    n1 = n1//2
    l=[]
    l.append(n1)
    s = convert_decimal_to_signMagBinary(n1)
    l.append(s)
    return l

# Gets left instruction from MBR
def getLeftInstruction_opcode_address_instructionName(complete_Instruction):
    l=[]
    l.append(complete_Instruction[0:8])
    l.append(complete_Instruction[8:20])
    return l

# Gets right instruction from MBR
def getRightInstruction_opcode_address_instructionName(complete_Instruction):
    l=[]
    l.append(complete_Instruction[20:28])
    l.append(complete_Instruction[28:40])
    return l

# Instruction Memory Preprocessing
memory_instruction = []
for i in range(SIZE_INS):
    memory_instruction.append(VOID_INSTRUCTION+pad_to_k(300,20)+VOID_INSTRUCTION+pad_to_k(300,20))

# Data memory Preprocessing
data_memory = []
for i in range(SIZE_DATA):
    data_memory.append(pad_to_k(0,40))

# Programming the instructions
memory_instruction[0] = '00000001' + pad_to_k(500,12) + '00000101' + pad_to_k(501,12)
memory_instruction[1] = '00001111' + pad_to_k(100,12) + '00001000' + pad_to_k(502,12)
memory_instruction[2] = '00010101' + pad_to_k(1000,12) + '00010101' + pad_to_k(1000,12)
memory_instruction[3] = '00100001' + pad_to_k(504,12) + '11110000' + pad_to_k(1000,12)

memory_instruction[100] = '00000110' + pad_to_k(502,12) + '00000111' + pad_to_k(503,12)
memory_instruction[101] = '00010100' + pad_to_k(1000,12) + '11110000' + pad_to_k(1000,12)

# Taking Input from user
print("Please enter the value of a.")
a = int(input())
print("Please enter the value of b.")
b = int(input())
print("Please enter the value of c.")
c = int(input())
print("Please enter the value of d.")
d = int(input())


# Programming the memory
data_memory[500] = convert_decimal_to_signMagBinary(a)
data_memory[501] = convert_decimal_to_signMagBinary(b)
data_memory[502] = convert_decimal_to_signMagBinary(c)
data_memory[503] = convert_decimal_to_signMagBinary(d)
data_memory[504] = convert_decimal_to_signMagBinary(0)


# Defining the registers

# Program Counter
Pc = pad_to_k(0,12)

# Accumulator - Sign Magnitude
Ac = pad_to_k(0,40)

# Memory Address Register
Mar = pad_to_k(0,12)

# Instruction Register
Ir = pad_to_k(0,8)

# Instruction Buffer Register
Ibr = pad_to_k(0,20)

# Memory Buffer Register - Can be sign Magnitude
Mbr = pad_to_k(0,40)

# Multiplicative Quotient - Sign Magnitude
Mq = pad_to_k(0,40)

# String that says which instruction is to be processed
Instruction_Set = 'Left'



while Ir != '11110000' and convert_binary_into_regularDecimal(Pc) <= SIZE_INS:
    if Instruction_Set == 'Left':
        Mar = Pc
        Mbr = memory_instruction[convert_binary_into_regularDecimal(Mar)]
        l_right = getRightInstruction_opcode_address_instructionName(Mbr)
        l_left = getLeftInstruction_opcode_address_instructionName(Mbr)
        Ibr = l_right[0]+l_right[1]

        # Void Instruction
        if l_left[1] == VOID_INSTRUCTION:
            Instruction_Set = 'Right'
            toBeProcessed = False
            Ir = l_right[0]
            Mar = l_right[1]
        else:
            Ibr = l_right[0]+l_right[1]
            Ir = l_left[0]
            Mar = l_left[1]
            toBeProcessed = True

        # Decode and Execute Cycle
        if toBeProcessed == True:
            code = INSTRUCTION_DICTIONARY[Ir]

            # Transfer M(X) to the accumulator
            if code == 'LOAD M(X)':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                Ac = Mbr
                print('Loading '+str(convert_signMagBinary_to_decimal(Ac))+' into the Accumulator ...')
                Instruction_Set = 'Right'

            # Transfer –M(X) to the accumulator
            elif code == 'LOAD -M(X)':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                if Mbr[0]=='0':
                    x = '1' + Mbr[1:]
                    Mbr = x
                else:
                    x = '0' + Mbr[1:]
                    Mbr = x
                Ac = Mbr
                print('Loading '+str(convert_signMagBinary_to_decimal(Ac))+' into the Accumulator ...')
                Instruction_Set = 'Right'

            # Transfer absolute value of M(X) to the accumulator
            elif code == 'LOAD |M(X)|':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                x = '0' + Mbr[1:]
                Mbr = x
                Ac = Mbr
                print('Loading '+str(convert_signMagBinary_to_decimal(Ac))+' into the Accumulator ...')
                Instruction_Set = 'Right'

            # Transfer –|M(X)| to the accumulator
            elif code == 'LOAD -|M(X)|':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                x = '1' + Mbr[1:]
                Mbr = x
                Ac = Mbr
                print('Loading '+str(convert_signMagBinary_to_decimal(Ac))+' into the Accumulator ...')
                Instruction_Set = 'Right'

            # Add M(X) to AC; put the result in AC
            elif code == 'ADD M(X)':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                x = convert_signMagBinary_to_decimal(Ac) + convert_signMagBinary_to_decimal(Mbr)
                Ac = convert_decimal_to_signMagBinary(x)
                print('Accumulator now contains '+str(convert_signMagBinary_to_decimal(Ac))+' ...')
                Instruction_Set = 'Right'

            # Add |M(X)| to AC; put the result in AC
            elif code == 'ADD |M(X)|':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                x1 = '0' + Mbr[1:]
                Mbr = x1
                x = convert_signMagBinary_to_decimal(Ac) + convert_signMagBinary_to_decimal(Mbr)
                Ac = convert_decimal_to_signMagBinary(x)
                print('Accumulator now contains '+str(convert_signMagBinary_to_decimal(Ac))+' ...')
                Instruction_Set = 'Right'

            # Subtract M(X) from AC; put the result in AC
            elif code == 'SUB M(X)':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                x = convert_signMagBinary_to_decimal(Ac) - convert_signMagBinary_to_decimal(Mbr)
                Ac = convert_decimal_to_signMagBinary(x)
                print('Accumulator now contains '+str(convert_signMagBinary_to_decimal(Ac))+' ...')
                Instruction_Set = 'Right'

            # Subtract |M(X)| from AC; put the remainder in AC
            elif code == 'SUB |M(X)|':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                x1 = '0' + Mbr[1:]
                Mbr = x1
                x = convert_signMagBinary_to_decimal(Ac) - convert_signMagBinary_to_decimal(Mbr)
                Ac = convert_decimal_to_signMagBinary(x)
                print('Accumulator now contains '+str(convert_signMagBinary_to_decimal(Ac))+' ...')
                Instruction_Set = 'Right'


            # Multiply accumulator by 2; that is, shift left one bit position
            elif code == 'LSH':
                l = leftShift_dec_SignMag(Ac)
                Ac = l[1]
                print('Ac now contains '+str(l[0])+' ...')
                Instruction_Set = 'Right'

            # Transfer contents of accumulator to memory location X
            elif code == 'STOR M(X)':
                Mbr = Ac
                data_memory[convert_binary_into_regularDecimal(Mar)] = Mbr
                print('Storing '+str(convert_signMagBinary_to_decimal(Mbr))+'...')
                Instruction_Set = 'Right'

            # Divide accumulator by 2; that is, shift right one position
            elif code == 'RSH':
                l = rightShift_dec_SignMag(Ac)
                Ac = l[1]
                print('Ac now contains '+str(l[0])+' ...')
                Instruction_Set = 'Right'

            # If number in the accumulator is nonnegative, take next instruction from left half of M(X)
            elif code == 'JUMP + M(X,0:19)':
                if isALU_Non_Negative(Ac) == False:
                    Instruction_Set = 'Right'
                else:
                    print('Accumulator is non negative')
                    Pc = Mar
                    Instruction_Set = 'Left'

            # Take next instruction from left half of M(X)
            elif code == 'JUMP M(X,0:19)':
                Pc = Mar
                Instruction_Set = 'Left'

            # If number in the accumulator is nonnegative, take next instruction from right half of M(X)
            elif code == 'JUMP + M(X,20:39)':
                if isALU_Non_Negative(Ac) == False:
                    Instruction_Set = 'Right'
                else:
                    print('Accumulator is non negative')
                    Pc = Mar
                    Instruction_Set = 'Left'
                    toBeProcessed = False

            # Take next instruction from right half of M(X)
            elif code == 'JUMP M(X,20:39)':
                Pc = Mar
                Instruction_Set = 'Left'
                toBeProcessed = False

            # Transfer contents of register MQ to the accumulator AC
            elif code == 'LOAD MQ':
                Ac = Mq
                Instruction_Set = 'Right'

            # Transfer contents of memory location X to MQ
            elif code == 'LOAD MQ,M(X)':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                Mq = Mbr
                Instruction_Set = 'Right'

            # Halt Instruction
            elif code == 'HALT':
                Ir = '11110000'
                print('Halting!!!')
                break
    else:
        Ir = Ibr[0:8]
        Mar = Ibr[8:20]
        code = INSTRUCTION_DICTIONARY[Ir]

        # Transfer M(X) to the accumulator
        if code == 'LOAD M(X)':
            Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
            Ac = Mbr
            print('Loading '+str(convert_signMagBinary_to_decimal(Ac))+' into the Accumulator ...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Transfer –M(X) to the accumulator
        elif code == 'LOAD -M(X)':
                Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
                if Mbr[0]=='0':
                    Mbr[0] = '1'
                else:
                    Mbr[0] = '0'
                Ac = Mbr
                print('Loading '+str(convert_signMagBinary_to_decimal(Ac))+' into the Accumulator ...')
                Instruction_Set = 'Right'

        # Transfer absolute value of M(X) to the accumulator
        elif code == 'LOAD |M(X)|':
            Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
            Mbr[0] = '0'
            Ac = Mbr
            print('Loading '+str(convert_signMagBinary_to_decimal(Ac))+' into the Accumulator ...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Transfer –|M(X)| to the accumulator
        elif code == 'LOAD -|M(X)|':
            Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
            Mbr[0] = '1'
            Ac = Mbr
            print('Loading '+str(convert_signMagBinary_to_decimal(Ac))+' into the Accumulator ...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Add |M(X)| to AC; put the result in AC
        elif code == 'ADD |M(X)|':
            Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
            x = '0' + Mbr[1:]
            Mbr = x
            x = convert_signMagBinary_to_decimal(Ac) + convert_signMagBinary_to_decimal(Mbr)
            Ac = convert_decimal_to_signMagBinary(x)
            print('Accumulator now contains '+str(x)+' ...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Subtract |M(X)| from AC; put the remainder in AC
        elif code == 'SUB |M(X)|':
            Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
            x = '0' + Mbr[1:]
            Mbr = x
            x1 = convert_signMagBinary_to_decimal(Ac) - convert_signMagBinary_to_decimal(Mbr)
            Ac = convert_decimal_to_signMagBinary(x1)
            print('Accumulator now contains '+str(x1)+' ...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Subtract M(X) from AC; put the remainder in AC
        elif code == 'SUB M(X)':
            Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
            x1 = convert_signMagBinary_to_decimal(Ac) - convert_signMagBinary_to_decimal(Mbr)
            Ac = convert_decimal_to_signMagBinary(x1)
            print('Accumulator now contains '+str(x1)+' ...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Add M(X) to AC; put the result in AC
        elif code == 'ADD M(X)':
            Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
            x = convert_signMagBinary_to_decimal(Ac) + convert_signMagBinary_to_decimal(Mbr)
            Ac = convert_decimal_to_signMagBinary(x)
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Multiply accumulator by 2; that is, shift left one bit position
        elif code == 'LSH':
            l = leftShift_dec_SignMag(Ac)
            Ac = l[1]
            print('Ac now contains '+str(l[0])+' ...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Transfer contents of accumulator to memory location X
        elif code == 'STOR M(X)':
            Mbr = Ac
            data_memory[convert_binary_into_regularDecimal(Mar)] = Mbr
            print('Storing '+str(convert_signMagBinary_to_decimal(Mbr))+'...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # Divide accumulator by 2; that is, shift right one position
        elif code == 'RSH':
            l = rightShift_dec_SignMag(Ac)
            Ac = l[1]
            print('Ac now contains '+str(l[0])+' ...')
            Instruction_Set = 'Left'
            Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

        # If number in the accumulator is nonnegative, take next instruction from left half of M(X)
        elif code == 'JUMP + M(X,0:19)':
            if isALU_Non_Negative(Ac) == False:
                Instruction_Set = 'Left'
                Pc = pad_to_k(convert_binary_into_regularDecimal(Pc) + 1,12)

            else:
                print('Accumulator is non negative')
                Pc = Mar
                Instruction_Set = 'Left'

        # Take next instruction from left half of M(X)
        elif code == 'JUMP M(X,0:19)':
            Pc = Mar
            Instruction_Set = 'Left'

        # If number in the accumulator is nonnegative, take next instruction from right half of M(X)
        elif code == 'JUMP + M(X,20:39)':
            if isALU_Non_Negative(Ac) == False:
                Instruction_Set = 'Right'
            else:
                print('Accumulator is non negative')
                Pc = Mar
                Instruction_Set = 'Left'
                toBeProcessed = False

        # Take next instruction from right half of M(X)
        elif code == 'JUMP M(X,20:39)':
            Pc = Mar
            Instruction_Set = 'Left'
            toBeProcessed = False

        # Transfer contents of register MQ to the accumulator AC
        elif code == 'LOAD MQ':
            Ac = Mq
            Instruction_Set = 'Left'

        # Transfer contents of memory location X to MQ
        elif code == 'LOAD MQ,M(X)':
            Mbr = data_memory[convert_binary_into_regularDecimal(Mar)]
            Mq = Mbr
            Instruction_Set = 'Left'

        # Halt Instruction
        elif code == 'HALT':
            Ir = '11110000'
            print('Halting!!!')
            break
