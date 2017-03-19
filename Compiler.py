#Names: Koukouzas Georgios-Gkoutzios Nikolaos
#AM   :         2468      -     2044

import sys
#print("Expected factor and received " ,state, "at line:",line,"\n")

white = 0
character = 1
digit = 2
plus = 3
minus = 4
multiply = 5
divide = 6
less = 7
more = 8
equals = 9
colon = 10
semicolon = 11
comma = 12
leftBracket = 13
rightBracket = 14
leftParenthesis = 15
rightParenthesis = 16
leftCaret = 17
rightCaret = 18
EOF = 19
other = 20

STATE0 = 0
STATE1 = 1
STATE2 = 2
STATE3 = 3
STATE4 = 4
STATE5 = 5
STATE6 = 6
STATE7 = 7
STATE8 = 8
identifierTK = 21
constantTK = 22
plusTK = 23
minusTK = 24
multiplyTK = 25
divideTK = 26
lessTK = 27
moreTK = 28
equalTK = 29
lessEQTK = 30
moreEQTK = 31
differentTK = 32
defineTk = 33
semicolonTK = 34
commaTK = 35
leftBracketTk = 36
rightBracketTK = 37
leftParenthesisTK = 38
rightParenthesisTK = 39
leftCaretTK = 40
rightCaretTK = 41
openCommentTK = 42
closeCommentTK = 43
andTK = 44
exitTK = 45
ifTK = 46
programTK = 47
declareTK = 48
procedureTK = 49
inTK = 50
orTK = 51
doTK = 52
functionTK = 53
inoutTK = 54
returnTK = 55
elseTK = 56
printTK = 57
notTK = 58
whileTK = 59
enddeclareTK = 60
callTK = 61
selectTK = 62
defaultTK = 63
errorTK = -1
EOFTK = -2
colonTK = 64

# Read file
file = sys.argv[1]
f = open(file, 'r')

# Initialize State Array

stateArray = [[0 for x in range(21)] for y in range(9)]
stateArray[STATE0][white] = STATE0
stateArray[STATE0][character] = STATE1
stateArray[STATE0][digit] = STATE2
stateArray[STATE0][plus] = plusTK
stateArray[STATE0][minus] = minusTK
stateArray[STATE0][multiply] = multiplyTK
stateArray[STATE0][divide] = STATE3
stateArray[STATE0][less] = STATE6
stateArray[STATE0][more] = STATE7
stateArray[STATE0][equals] = equalTK
stateArray[STATE0][colon] = STATE8
stateArray[STATE0][semicolon] = semicolonTK
stateArray[STATE0][comma] = commaTK
stateArray[STATE0][leftBracket] = leftBracketTk
stateArray[STATE0][rightBracket] = rightBracketTK
stateArray[STATE0][leftParenthesis] = leftParenthesisTK
stateArray[STATE0][rightParenthesis] = rightParenthesisTK
stateArray[STATE0][leftCaret] = leftCaretTK
stateArray[STATE0][rightCaret] = rightCaretTK
stateArray[STATE0][EOF] = EOFTK

for i in range(21):  # IDENTIFIERS
    stateArray[STATE1][i] = identifierTK
stateArray[STATE1][character] = STATE1
stateArray[STATE1][digit] = STATE1

for i in range(21):  # CONSTANTS
    stateArray[STATE2][i] = constantTK
stateArray[STATE2][digit] = STATE2

for i in range(21):  # COMMENTS
    stateArray[STATE3][i] = divideTK
stateArray[STATE3][multiply] = STATE4

for i in range(21):  # INSIDE COMMENTS
    stateArray[STATE4][i] = STATE4
stateArray[STATE4][multiply] = STATE5

for i in range(21):  # CLOSE COMMENTS
    stateArray[STATE5][i] = STATE4
stateArray[STATE5][multiply] = STATE5
stateArray[STATE5][divide] = STATE0

for i in range(21):  # LESS
    stateArray[STATE6][i] = lessTK
stateArray[STATE6][equals] = lessEQTK
stateArray[STATE6][more] = differentTK

for i in range(21):  # MORE
    stateArray[STATE7][i] = moreTK
stateArray[STATE7][equals] = moreEQTK

for i in range(21):  # DECLARE
    stateArray[STATE8][i] = errorTK
stateArray[STATE8][equals] = declareTK


global line
line = 1


def readCharacter():
    global line
    output = 19
    if c == ' ' or c == '\t' or c == '\n':
        output = 0
        if c == '\n':
           line = line + 1
    elif c.isalpha():
        output = 1
    elif c.isdigit():
        output = 2
    elif c == '+':
        output = 3
    elif c == '-':
        output = 4
    elif c == '*':
        output = 5
    elif c == '/':
        output = 6
    elif c == '<':
        output = 7
    elif c == '>':
        output = 8
    elif c == '=':
        output = 9
    elif c == ':':
        output = 10
    elif c == ';':
        output = 11
    elif c == ',':
        output = 12
    elif c == '{':
        output = 13
    elif c == '}':
        output = 14
    elif c == '(':
        output = 15
    elif c == ')':
        output = 16
    elif c == '[':
        output = 17
    elif c == ']':
        output = 18
    elif c == 'EOF':
        output = 19
    #else:
       # output = 19
    return output


def isBooked(word):
    global state
    if word == "and":
        output = 44
    elif word == "exit":
        output = 45
    elif word == "if":
        output = 46
    elif word == "program":
        output = 47
    elif word == "declare":
        output = 48
    elif word == "procedure":
        output = 49
    elif word == "in":
        output = 50
    elif word == "or":
        output = 51
    elif word == "do":
        output = 52
    elif word == "function":
        output = 53
    elif word == "inout":
        output = 54
    elif word == "return":
        output = 55
    elif word == "else":
        output = 56
    elif word == "print":
        output = 57
    elif word == "not":
        output = 58
    elif word == "while":
        output = 59
    elif word == "enddeclare":
        output = 60
    elif word == "call":
        output = 61
    elif word == "select":
        output = 62
    elif word == "default":
        output = 63
    else:
        output = state
    return output


buffer = ""
state = None
col = None
c = None


def lexicalAnalyser():
    global col
    global buffer
    global state
    global c
    global line
    col = 0
    buffer = ""
    state = STATE0
    while state >= 0 and state <= 8:
        c = f.read(1)
        if len(buffer) < 31:
            buffer += c
        col = readCharacter()
        state = stateArray[state][col]
        if state == 0:
            col = 0
            buffer = ""
    if state == identifierTK or state == constantTK or state == lessTK or state == moreTK or state == divideTK:
        currentPos = f.tell()
        f.seek(currentPos-1, 0)
        if buffer[-1] == '\n':
            line-= 1
        buffer = buffer[:-1]
        if state == constantTK:
            number = int(buffer)
            if -32768 >= number or number > 32768:
                print("Numbers exceeding supporting format at line:",line,"\n")
                exit(1)
    if state == identifierTK:
        state = isBooked(buffer)
    print("State is ", state,buffer)

def program():
    global state
    lexicalAnalyser()
    if state == programTK:
        lexicalAnalyser()
        if state == identifierTK:
            block()
            print("be4 unx",state,buffer)
            if state != EOFTK and state!= functionTK and state!= procedureTK:
                print("Unexpected text after code Block")
                exit(1)
        else:
            print("Expected program name at line:",line,"\n")
            exit(1)
    else:
        print("Expected program keyword at line:",line,"\n")
        exit(1)


def block():
    global state
    lexicalAnalyser()
    if state == leftBracketTk:
        lexicalAnalyser()
        if state == declareTK:
            declarations()
        subprograms()
        sequence()
        print("after seq",state,buffer)
        if state == rightBracketTK:
            print("317",state,buffer)
            lexicalAnalyser()
        elif state == identifierTK or (state >= 44 and state <= 63):
            print("at block",state,buffer)
            print("Expected semicolon between statements at line",line,"\n")
            exit(1)
        else:
            print(" '}' was expected at line:",line,"\n")
            exit(1)


def declarations():  #do
    global state
    lexicalAnalyser()
    if state == identifierTK:
        varlist()
    if state == enddeclareTK:
        lexicalAnalyser()
    else:
        print("Expected 'enddeclare' at line:",line,"\n")
        exit(1)


def varlist():
    global state
    lexicalAnalyser()
    while state == commaTK:
        lexicalAnalyser()
        if state == identifierTK:
            lexicalAnalyser()
        else:
            print("Expected identifier after ',' at  line:",line,"\n")
            exit(1)


def subprograms():
    global state
    while state == procedureTK or state == functionTK:
        func()


def func():
    global state
    print("func call", state)
    lexicalAnalyser()
    if state == identifierTK:
        funcbody()
    else:
        print("Expected function or procedure name at line:",line,"\n")
        exit(1)


def funcbody():
    print("be4 formalpars", state)
    formalpars()
    block()


def formalpars():  #
    global state
    print("be4,",state)
    lexicalAnalyser()
    print("after,",state)
    if state == leftParenthesisTK:
        lexicalAnalyser()
        if state != rightParenthesisTK:
            formalparlist()
    else:
        print("Expected '(' at line:",line,"\n")
        exit(1)
    if state == rightParenthesisTK:
        lexicalAnalyser()
    else:
        print("Expected ')' at line:",line,"\n")
        exit(1)


def formalparlist():
    global state
    formalparitem()
    while state == commaTK:
        lexicalAnalyser()
        formalparitem()


def formalparitem():
    global state
    if state == inTK or state == inoutTK:
        lexicalAnalyser()
        if state == identifierTK:
            lexicalAnalyser()
        else:
            print("Expected parameter name at line:",line,"\n")
            exit(1)
    else:
        print("Expected 'in' or 'inout' at line:",line,"\n")
        exit(1)


def sequence():  #
    global state
    statement()
    while state == semicolonTK:
        lexicalAnalyser()
        statement()


def brackets_seq():
    global state
    lexicalAnalyser()
    sequence()
    if state == rightBracketTK:
        lexicalAnalyser()
    else:
        print("Expected '}' at line:",line,"\n")
        exit(1)


def brack_or_stat():
    global state
    if state == leftBracketTk:
        print("brackts",state,buffer)
        brackets_seq()
    else:
        statement()


def statement():
    global state
    if state == identifierTK:
        assignment_stat()
    elif state == ifTK:
        if_stat()
    elif state == whileTK:
        while_stat()
    elif state == doTK:
        do_while_stat()
    elif state == selectTK:
        select_stat()
    elif state == exitTK:
        exit_stat()
    elif state == returnTK:
        return_stat()
    elif state == printTK:
        print_stat()
    elif state == callTK:
        call_stat()


def assignment_stat():
    global state
    lexicalAnalyser()
    if state == declareTK:
        lexicalAnalyser()
        expression()
    else:
        print("Expected ':' at line:",line,"\n")
        exit(1)


def if_stat():
    global state
    lexicalAnalyser()
    if state == leftParenthesisTK:
        lexicalAnalyser()
        condition()
        if state == rightParenthesisTK:
            lexicalAnalyser()
            print("state at if " ,state, buffer)
            brack_or_stat()
            elsepart()
        else:
            print("Expected ')' at line:",line,"\n")
            exit(1)
    else:
        print("Expected '('  at line:",line,"\n")
        exit(1)


def elsepart():
    global state
    if state == leftCaretTK:
        lexicalAnalyser()
        if state == elseTK:
            lexicalAnalyser()
            brack_or_stat()
            if state == rightCaretTK:
                lexicalAnalyser()
            else:
                print("Expected ']' and got ", state, "at line :", line, "\n")
        else:
            print("Expected else and got ", state, "at line :", line, "\n")
    else:
        print("Expected '[' and got ",state,"at line :",line,"\n")
        exit(1)


def while_stat():
    global state
    lexicalAnalyser()
    if state == leftParenthesisTK:
        lexicalAnalyser()
        condition()
        if state == rightParenthesisTK:
            lexicalAnalyser()
            brack_or_stat()
        else:
            print("Expected ')' at line:",line,"\n")
            exit(1)
    else:
        print("Expected '(' at line:",line,"\n")
        exit(1)


def select_stat():
    global state
    number = 0
    lexicalAnalyser()
    if state == leftParenthesisTK:
        lexicalAnalyser()
        if state == identifierTK:
            lexicalAnalyser()
            if state == rightParenthesisTK:
                lexicalAnalyser()
            else:
                print("Expected ')' at line:",line,"\n")
                exit(1)
        else:
            print("Expected identifier at line:",line,"\n")
            exit(1)
    else:
        print("Expected '(' at line:",line,"\n")
        exit(1)
    while state == constantTK:
        number += 1
        if number != int(buffer):
            print("Statements need to be sorted at line",line,"\n")
            exit(1)
        lexicalAnalyser()
        state = colonTK
        if state == colonTK:
            lexicalAnalyser()
            brack_or_stat()
        else:
            print("Expected ':' at line:",line,"\n")
            exit(1)
    if state == defaultTK:
        lexicalAnalyser()
        state = colonTK
        if state == colonTK:
            lexicalAnalyser()
            brack_or_stat()
        else:
            print ("Expected ':' after default at line:",line,"\n")
            exit(1)
    else:
        print("Expected default at line:",line,"\n")
        exit(1)


def do_while_stat():
    global state
    lexicalAnalyser()
    brack_or_stat()
    if state == whileTK:
        lexicalAnalyser()
        if state == leftParenthesisTK:
            lexicalAnalyser()
            condition()
            if state == rightParenthesisTK:
                lexicalAnalyser()
            else:
                print("Expected ')' at line:",line,"\n")
                exit(1)
        else:
            print("Expected '(' at line:",line,"\n")
            exit(1)
    else:
        print("Expected 'while' keyword at line:",line,"\n")
        exit(1)


def exit_stat():
    global state
    if state == exitTK:
       print("Exit command was issued, terminating ...")
       exit(0)


def return_stat():
    global state
    lexicalAnalyser()
    if state == returnTK:
        lexicalAnalyser()
        if state == leftParenthesisTK:
            lexicalAnalyser()
            expression()
            if state == rightParenthesisTK:
                lexicalAnalyser()
            else:
                print("Expected ')' at line:",line,"\n")
                exit(1)
        else:
            print("Expected '(' at line:",line,"\n")
            exit(1)
    else:
        print("Expected return keyword at line:",line,"\n")
        exit(1)


def print_stat():
    global state

    #lexicalAnalyser()

    if state == printTK:
        lexicalAnalyser()
        if state == leftParenthesisTK:
            print("print", state, buffer)
            lexicalAnalyser()
            print("print after", state, buffer)
            expression()
            print("print expre", state, buffer)
            if state == rightParenthesisTK:
                lexicalAnalyser()
            else:
                print("Expected ')' at line:",line,"\n")
                exit(1)
        else:
            print("Expected '(' at line:",line,"\n")
            exit(1)
    else:
        print("Expected print keyword at line:",line,"\n")
        exit(1)


def call_stat():
    global state
    #lexicalAnalyser()
    if state == callTK:
        lexicalAnalyser()
        if state == identifierTK:
            lexicalAnalyser()
            if state == leftParenthesisTK:
                actualpars()
            else:
                print("Expected '(' at line:",line,"\n")
                exit(1)
        else:
            print("Expected identifier at line:",line,"\n")
            exit(1)
    else:
        print("Expected call keyword at line:",line,"\n")
        exit(1)


def actualpars():
    global state
    #lexicalAnalyser()
    if state != rightParenthesisTK:
        actualparlist()
    if state == rightParenthesisTK:
        lexicalAnalyser()
    else:
        print("Expected ')' at line:",line,"\n")
        exit(1)


def actualparlist():
    global state
    actualparitem()
    while state == commaTK:
        lexicalAnalyser()
        actualparitem()


def actualparitem():
    global state
    lexicalAnalyser()
    if state == inTK:
        lexicalAnalyser()
        expression()
    elif state == inoutTK:
        lexicalAnalyser()
        if state == identifierTK:
            lexicalAnalyser()
        else:
            print("Expected identifier at line:",line,"\n")
            exit(1)
    else:
        print("Expected 'in' or 'inout' keyword at line:",line,"\n")
        exit(1)


def condition():
    global state
    boolterm()
    while state == orTK:
        lexicalAnalyser()
        boolterm()


def boolterm():
    global state
    boolfactor()
    while state == andTK:
        lexicalAnalyser()
        boolfactor()


def boolfactor():
    global state
    if state == notTK:
        lexicalAnalyser()
        if state == leftCaretTK:
            lexicalAnalyser()
            condition()
            if state == rightCaretTK:
                lexicalAnalyser()
            else:
                print("Expected ']' at line:",line,"\n")
                exit(1)
        else:
            print("Expected '[' at line:",line,"\n")
            exit(1)
    elif state == leftCaretTK:
        lexicalAnalyser()
        condition()
        if state == rightCaretTK:
            lexicalAnalyser()
        else:
            print("Expected ']' at line:",line,"\n")
            exit(1)
    else:
        expression()
        relational_oper()
        expression()


def expression():
    global state
    #lexicalAnalyser()
    optional_sign()
    term()
    while state == plusTK or state == minusTK:
        lexicalAnalyser()
        term()


def term():
    global state
    factor()
    while state == multiplyTK or state == divideTK:
        lexicalAnalyser()
        factor()


def factor():
    global state
    if state == constantTK:
        lexicalAnalyser()
    elif state == leftParenthesisTK:
        lexicalAnalyser()
        expression()
        if state == rightParenthesisTK:
            lexicalAnalyser()
        else:
            print("Expected ')' at line:",line,"\n")
            exit(1)
    elif state == identifierTK:
        print("factor ", state, buffer)
        lexicalAnalyser()
        print("factor after", state, buffer)
        if state == leftParenthesisTK:
            idtail()
    else:
        print("Expected factor and received " ,state, "at line:",line,"\n")
        exit(1)


def idtail():
    global state
    if state == leftParenthesisTK:
        actualpars()


def relational_oper():
    global state
    if state == equalTK or state == lessTK or state == lessEQTK or state == differentTK or state == moreEQTK or state == moreTK:
        lexicalAnalyser()
    else:
        print("Expected compare operator at line:",line,"\n")
        exit(1)


def add_oper():
    global state
    if state == plusTK or state == minusTK:
        lexicalAnalyser()
    else:
        print("Expected '+' or '-' at line:",line,"\n")
        exit(1)


def mul_oper():
    global state
    if state == multiplyTK or state == divideTK:
        lexicalAnalyser()
    else:
        print("Expected '*' or '/' at line:",line,"\n")
        exit(1)


def optional_sign():
    global state
    #lexicalAnalyser()
    if state == plusTK or state == minusTK:
        add_oper()


program()
#for x in range(40):
    #lexicalAnalyser()
f.close()
