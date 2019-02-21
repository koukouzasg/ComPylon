import sys

# CHARACTERS
SPACES = 0
LETTER = 1
DIGIT = 2
ADD = 3
SUB = 4
MUL = 5
DIV = 6
LESS = 7
MORE = 8
EQUAL = 9
COLON = 10
SEMICOLON = 11
COMMA = 12
LEFTBRAC = 13
RIGHTBRAC = 14
LEFPAR = 15
RIGHTPAR = 16
EOF = 19
NEWLINE = 17
other = 20

# STATES

STATE0 = 0
STATE1 = 1
STATE2 = 2
STATE3 = 3
STATE4 = 4
STATE5 = 5
STATE6 = 6
STATE7 = 7
STATE8 = 8
STATE9 = 9

# RETURNING TOKENS

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
assignTK = 33
semicolonTK = 34
commaTK = 35
leftBracketTK = 36
rightBracketTK = 37
leftParenthesisTK = 38
rightParenthesisTK = 39
colonTK = 40
openCommentTK = 42
closeCommentTK = 43

# RESERVED WORDS TOKEN IDS
PROGTK = 1001
ENDPROGTK = 1002
DECLTK = 1003
ENDDECLTK = 1004
IFTK = 1005
THENTK = 1006
ELSETK = 1007
ENDIFTK = 1008
WHILETK = 1009
ENDWHILETK = 1010
REPEATTK = 1011
ENDREPEATTK = 1012
EXITTK = 1013
SWITCHTK = 1014
CASETK = 1015
ENDSWITCHTK = 1016
FORCASETK = 1017
ENDFORTK = 1018
PROCTK = 1019
ENDPROCTK = 1020
FUNCTK = 1021
ENDFUNCTK = 1022
CALLTK = 1023
RETURNTK = 1024
INTK = 1025
INOUTTK = 1026
ANDTK = 1027
ORTK = 1028
NOTTK = 1029
INPUTTK = 1030
PRINTTK = 1031
WHENTK = 1032

# BOOLEANS
TRUETK = 300
FALSETK = -300

# ERRORS

ERRORTK = -1
EOFTK = -2
NOENDCOMMENTSTK = -3
NUMFIRST = -12

# USING STATE ARRAY FOR THE DIFFERENT STATES

# INSTANTIATE STATE ARRAY
stateArray = [[0 for x in range(21)] for y in range(10)]

# CHANGES OF STATE ARRAY

stateArray[STATE0][SPACES] = STATE0  # IGNORE SPACES
stateArray[STATE0][LETTER] = STATE1  # ALPHANUM STATE
stateArray[STATE0][DIGIT] = STATE2  # DIGIT STATE
stateArray[STATE0][ADD] = plusTK  # RETURN +
stateArray[STATE0][SUB] = minusTK  # RETURN -
stateArray[STATE0][MUL] = multiplyTK  # RETURN *
stateArray[STATE0][DIV] = STATE3  # FIRST APPEARANCE OF /
stateArray[STATE0][LESS] = STATE6  # FIRST APPEARANCE OF <
stateArray[STATE0][MORE] = STATE7  # FIRST APPEARANCE OF >
stateArray[STATE0][EQUAL] = equalTK  # RETURN =
stateArray[STATE0][COLON] = STATE8  # FIRST APPEARANCE OF :
stateArray[STATE0][SEMICOLON] = semicolonTK  # RETURN ;
stateArray[STATE0][COMMA] = commaTK  # RETURN ,
stateArray[STATE0][LEFTBRAC] = leftBracketTK  # RETURN [
stateArray[STATE0][RIGHTBRAC] = rightBracketTK  # RETURN ]
stateArray[STATE0][LEFPAR] = leftParenthesisTK  # RETURN (
stateArray[STATE0][RIGHTPAR] = rightParenthesisTK  # RETURN )
stateArray[STATE0][EOF] = EOFTK  # END OF FILE TOKEN

for i in range(21):  # ALPHANUMS
    stateArray[STATE1][i] = identifierTK

stateArray[STATE1][LETTER] = STATE1
stateArray[STATE1][DIGIT] = STATE1

for i in range(21):  # CONSTANTS
    stateArray[STATE2][i] = constantTK
stateArray[STATE2][DIGIT] = STATE2

for i in range(21):  # COMMENTS
    stateArray[STATE3][i] = divideTK
stateArray[STATE3][DIV] = STATE9
stateArray[STATE3][MUL] = STATE4

for i in range(21):  # INSIDE COMMENTS
    stateArray[STATE4][i] = STATE4
stateArray[STATE4][EOF] = NOENDCOMMENTSTK
stateArray[STATE4][MUL] = STATE5

for i in range(21):  # CLOSE COMMENTS
    stateArray[STATE5][i] = STATE4
stateArray[STATE5][MUL] = STATE5
stateArray[STATE5][DIV] = STATE0

for i in range(21):  # LESS
    stateArray[STATE6][i] = lessTK
stateArray[STATE6][EQUAL] = lessEQTK
stateArray[STATE6][MORE] = differentTK

for i in range(21):  # MORE
    stateArray[STATE7][i] = moreTK
stateArray[STATE7][EQUAL] = moreEQTK

for i in range(21):  # COLON
    stateArray[STATE8][i] = colonTK
stateArray[STATE8][EQUAL] = assignTK

for i in range(21):  # CLOSE SINGLE LINE COMMENTS
    stateArray[STATE9][i] = STATE9
stateArray[STATE9][NEWLINE] = STATE0

# DICTIONAIRIES
reserved = {'program': PROGTK, 'endprogram': ENDPROGTK,
            'declare': DECLTK, 'enddeclare': ENDDECLTK, 'if': IFTK,
            'then': THENTK, 'else': ELSETK,
            'endif': ENDIFTK, 'while': WHILETK,
            'endwhile': ENDWHILETK,
            'repeat': REPEATTK, 'endrepeat': ENDREPEATTK,
            'exit': EXITTK, 'switch': SWITCHTK,
            'case': CASETK, 'endswitch': ENDSWITCHTK,
            'forcase': FORCASETK, 'when': WHENTK,
            'endforcase': ENDFORTK, 'procedure': PROCTK,
            'endprocedure': ENDPROCTK, 'function': FUNCTK,
            'endfunction': ENDFUNCTK, 'call': CALLTK, 'return': RETURNTK,
            'in': INTK, 'inout': INOUTTK, 'and': ANDTK,
            'or': ORTK, 'not': NOTTK, 'true': TRUETK,
            'false': FALSETK, 'input': INPUTTK, 'print': PRINTTK}

symbols = {'<': LESS, '>': MORE, '<>': differentTK, '+': ADD, '/': DIV, '-': SUB, '=': EQUAL, '*': MUL, '(': LEFPAR,
           ')': RIGHTPAR, '[': LEFTBRAC, ']': RIGHTBRAC, ',': COMMA, ':': COLON, ';': SEMICOLON}

errors = {ERRORTK: 'ERRORTK', 'EOFTK': EOFTK, 'NOENDCOMMENTSTK': NOENDCOMMENTSTK, 'NUMFIRST': NUMFIRST}

bufferWord = ""
state = None
col = 0
c = None
lines = 1
flagEOF = False
myFile = sys.argv[1]
try:
    inputFile = open(myFile, "r")  # open file with read rights

except IOError:
    print "FILE NOT FOUND"


# LEX
def readNext():
    global lines, flagEOF
    if c == ' ' or c == '\t' or c == '\n':

        if c == '\n':
            lines = lines + 1
            return NEWLINE
        else:
            output = STATE0

    elif c.isalpha():
        output = LETTER
        if state == STATE2:
            print "ERROR %d NUMBER BEFORE LETTER IN ALPHANUM AT LINE : %d" % (NUMFIRST, lines)
            sys.exit(NUMFIRST)
    elif c.isdigit():
        output = DIGIT
    elif c in symbols:
        output = symbols[c]
    elif c == '':
        flagEOF = True
        output = EOF
    else:
        print "ERROR %d UNRECOGNIZED SYMBOL AT LINE : %d" % (ERRORTK, lines)
        sys.exit(ERRORTK)
    return output

# CHECK IF ALPHANUM IS IN RESERVED WORDS
def isRsrvd(word):
    global state
    if word in reserved:
        output = reserved[word]
    else:
        output = identifierTK
    return output


def lex():
    global col, bufferWord, state, c, lines, flagEOF
    col = 0
    bufferWord = ""
    state = STATE0
    while STATE0 <= state <= STATE9:
        c = inputFile.read(1)
        if len(bufferWord) < 31:
            bufferWord += c
        col = readNext()
        state = stateArray[state][col]
        if state == STATE0:
            col = 0
            bufferWord = ""
        if state == NOENDCOMMENTSTK:
            print "ERROR %d COMMENTS NOT CLOSED AT LINE  : %d" % (NOENDCOMMENTSTK, lines)
            sys.exit(NOENDCOMMENTSTK)

    if state == identifierTK or state == constantTK or state == lessTK or state == moreTK or state == divideTK or state == colonTK:
        if not flagEOF:
            index = inputFile.tell() - 1
            inputFile.seek(index, 0)
            if bufferWord[-1] == '\n':
                lines -= 1
            bufferWord = bufferWord[:-1]
        if state == constantTK:
            if bufferWord != '':
                number = int(bufferWord)
                if -32768 >= number or number > 32768:
                    print("SUPPORTING NUMBER FORMAT EXCEEDED AT LINE : %d" % lines + "\n")
                    sys.exit(ERRORTK)
    if state == identifierTK:
        state = isRsrvd(bufferWord)
    print [state, bufferWord]


# SYNT

def program():
    global state, bufferWord
    lex()
    if state == PROGTK:
        lex()
        if state == identifierTK:
            block()
            # lex()

            if state != ENDPROGTK:
                print "ERROR AT LINE : %d" % lines
                print "ENDPROGRAM WAS NOT FOUND"
                sys.exit(ERRORTK)
        else:
            print "ERROR AT LINE : %d" % lines
            print "INVALID ALPHANUM FOR PROGRAM ID"
            sys.exit(ERRORTK)
    else:
        print "ERROR AT LINE : %d" % lines
        print "ALPHANUM PROGRAM WAS NOT FOUND"
        sys.exit(ERRORTK)


def block():
    global state, bufferWord
    lex()
    if state == DECLTK:
        declarations()
    subprograms()

    statements()


def declarations():
    global state, bufferWord
    lex()
    if state == identifierTK:
        varlist()
    if state == ENDDECLTK:
        lex()
    else:
        print "ERROR AT LINE : %d" % lines
        print "ALPHANUM ENDDECLARE WAS NOT FOUND"
        sys.exit(ERRORTK)


def varlist():
    global state, bufferWord
    lex()
    while state == commaTK:
        lex()
        if state == identifierTK:
            lex()
        else:
            print "ERROR AT LINE : %d" % lines
            print "EXPECTED IDENTIFIER NOT FOUND AFTER COMMA ',' "
            sys.exit(ERRORTK)


def subprograms():
    global state, bufferWord
    while state == FUNCTK or state == PROCTK:
        procorfunc()


def procorfunc():
    global state, bufferWord
    if state == PROCTK:
        lex()
        if state == identifierTK:
            lex()

            procorfuncbody()

            if state == ENDPROCTK:
                lex()
            else:
                print "ERROR AT LINE : %d" % lines
                print "ALPHANUM ENDPROCEDURE WAS NOT FOUND"
                sys.exit(ERRORTK)
        else:
            print "ERROR AT LINE : %d" % lines
            print "INVALID ALPHANUM FOR PROCEDURE ID"
            sys.exit(ERRORTK)
    elif state == FUNCTK:
        lex()
        if state == identifierTK:
            lex()
            procorfuncbody()
            if state == ENDFUNCTK:
                lex()
            else:
                print "ERROR AT LINE : %d" % lines
                print "ALPHANUM ENDFUNCTION WAS NOT FOUND"
                sys.exit(ERRORTK)
        else:
            print "ERROR AT LINE : %d" % lines
            print "INVALID ALPHANUM FOR FUNCTION ID"
            sys.exit(ERRORTK)


def procorfuncbody():
    global state, bufferWord

    formalpars()
    block()


def formalpars():
    global state, bufferWord
    if state == leftParenthesisTK:
        formalparlist()
        if state == rightParenthesisTK:
            return
        else:
            print "ERROR AT LINE : %d" % lines
            print "EXPECTED ) WAS NOT FOUND"
            sys.exit(ERRORTK)
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED ( WAS NOT FOUND"
        sys.exit(ERRORTK)


def formalparlist():
    global state, bufferWord
    lex()
    if state == rightParenthesisTK:
        return
    else:
        formalparitem()
        while state == commaTK:
            lex()
            formalparitem()


def formalparitem():
    if state == INTK or state == INOUTTK:
        lex()

        if state == identifierTK:
            lex()

        else:
            print "ERROR AT LINE : %d" % lines
            print "EXPECTED PARAMETER ID WAS NOT FOUND"
            sys.exit(ERRORTK)
    else:
        print "ERROR AT LINE : %d" % lines
        print "INVALID PARAMETRE INPUT"
        sys.exit(ERRORTK)


def statements():
    global state, bufferWord
    statement()
    while state == semicolonTK:
        lex()
        statement()


def statement():
    global state
    if state == identifierTK:
        assignment_stat()
    elif state == IFTK:
        if_stat()
    elif state == WHILETK:
        while_stat()
    elif state == REPEATTK:
        repeat_stat()
    elif state == EXITTK:
        exit_stat()
    elif state == SWITCHTK:
        switch_stat()
    elif state == FORCASETK:
        forcase_stat()
    elif state == CALLTK:
        call_stat()
    elif state == RETURNTK:
        return_stat()
    elif state == INPUTTK:
        input_stat()
    elif state == PRINTTK:
        print_stat()


def assignment_stat():
    global state, bufferWord
    lex()
    if state == assignTK:
        lex()
        expression()
    else:
        print "ERROR AT LINE : %d" % lines
        print "NO ASSIGNMENT SYMBOL := WAS FOUND AFTER ASSIGNMENT STATE"
        sys.exit(ERRORTK)


def if_stat():
    global state, bufferWord
    lex()
    condition()
    if state == THENTK:
        lex()
        statements()
        elsepart()
        if state == ENDIFTK:
            lex()
        else:
            print "ERROR AT LINE : %d" % lines
            print "NO ENDIF ALPHANUM FOUND "
            sys.exit(ERRORTK)
    else:
        print "ERROR AT LINE : %d" % lines
        print "NO THEN ALPHANUM FOUND AFTER IF STATEMENT"
        sys.exit(ERRORTK)


def elsepart():
    global state, bufferWord
    if state == ELSETK:
        lex()
        statements()
    else:
        return


def repeat_stat():
    global state, bufferWord
    lex()
    statements()
    if state == ENDREPEATTK:
        lex()
    else:
        print "ERROR AT LINE : %d" % lines
        print "NO ENDREAPEAT ALPHANUM AFTER REPEAT STATEMENT"
        sys.exit(ERRORTK)


def exit_stat():
    global state
    if state == EXITTK:
        lex()
    else:
        print "EXIT ERROR"


def while_stat():
    global state, bufferWord
    lex()
    condition()
    statements()
    if state == ENDWHILETK:
        lex()
    else:
        print "ERROR AT LINE : %d" % lines
        print "NO ENDWHILE ALPHANUM AFTER WHILE STATEMENT"
        sys.exit(ERRORTK)


def switch_stat():
    global state, bufferWord
    lex()
    expression()
    if state == CASETK:
        lex()
        expression()
        if state == colonTK:
            lex()
            statements()
        else:
            print "ERROR AT LINE : %d" % lines
            print "NO COLON SYMBOL AFTER CASE EXPRESSION"
            sys.exit(ERRORTK)
        while state == CASETK:
            lex()
            expression()
            if state == colonTK:
                lex()
                statements()
            else:
                print "ERROR AT LINE : %d" % lines
                print "NO COLON SYMBOL AFTER CASE EXPRESSION"
                sys.exit(ERRORTK)
        if state == ENDSWITCHTK:
            lex()
        else:
            print "ERROR AT LINE : %d" % lines
            print "ENDSWITCH ALPHANUM WAS EXPECTED"
            sys.exit(ERRORTK)

    else:
        print "ERROR AT LINE : %d" % lines
        print "AT LEAST ONE CASE IS EXPECTED"
        sys.exit(ERRORTK)


def forcase_stat():
    global state, bufferWord
    lex()
    if state == WHENTK:
        lex()
        condition()
        if state == colonTK:
            lex()
            statements()
        else:
            print "ERROR AT LINE : %d" % lines
            print "NO COLON SYMBOL AFTER WHEN EXPRESSION"
            sys.exit(ERRORTK)
        while state == WHENTK:
            lex()
            condition()
            if state == colonTK:
                lex()
                statements()
            else:
                print "ERROR AT LINE : %d" % lines
                print "NO COLON SYMBOL AFTER CASE EXPRESSION"
                sys.exit(ERRORTK)
        if state == ENDFORTK:
            lex()
        else:
            print "ERROR AT LINE : %d" % lines
            print "ENDFORCASE ALPHANUM WAS EXPECTED"
            sys.exit(ERRORTK)

    else:
        print "ERROR AT LINE : %d" % lines
        print "AT LEAST ONE WHEN CONDITION IS EXPECTED"
        sys.exit(ERRORTK)


def call_stat():
    global state, bufferWord
    if state == CALLTK:
        lex()
        print [state, bufferWord, "CALL1"]
        if state == identifierTK:
            lex()
            print [state, bufferWord, "CALL2"]
            if state == leftParenthesisTK:
                actualpars()
            else:
                print "ERROR AT LINE : %d" % lines
                print "EXPECTED '(' NOT FOUND"
                sys.exit(ERRORTK)
        else:
            print "ERROR AT LINE : %d" % lines
            print "EXPECTED IDENTIFIER NOT FOUND"
            sys.exit(ERRORTK)
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED CALL KEYWORD NOT FOUND"
        sys.exit(ERRORTK)


def return_stat():
    global state, bufferWord
    lex()
    expression()


def print_stat():
    global state
    lex()
    expression()


def input_stat():
    global state, bufferWord

    lex()
    if state == identifierTK:
        lex()
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED IDENTIFIER IN INPUT STAT NOT FOUND"
        sys.exit(ERRORTK)


def actualpars():
    global state, bufferWord
    if state != rightParenthesisTK:
        actualparlist()
    if state == rightParenthesisTK:
        lex()
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED ')' NOT FOUND"
        sys.exit(ERRORTK)


def actualparlist():
    global state
    actualparitem()
    while state == commaTK:
        actualparitem()


def actualparitem():
    lex()
    if state == INTK:
        lex()
        expression()
    elif state == INOUTTK:
        lex()
        if state == identifierTK:
            lex()
        else:
            print "ERROR AT LINE : %d" % lines
            print "EXPECTED IDENTIFIER NOT FOUND AFTER INOUT"
            sys.exit(ERRORTK)
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED IN OR INOUT KEYWORD NOT FOUND"
        sys.exit(ERRORTK)


def condition():
    global state
    boolterm()
    while state == ORTK:
        lex()
        boolterm()


def boolterm():
    global state
    boolfactor()
    while state == ANDTK:
        lex()
        boolfactor()


def boolfactor():
    global state
    if state == NOTTK:
        lex()
        print [state, bufferWord, "000"]
        if state == leftBracketTK:
            lex()
            condition()
            if state == rightBracketTK:
                lex()
            else:
                print "ERROR AT LINE : %d" % lines
                print "EXPECTED ']' NOT FOUND"
                sys.exit(ERRORTK)
        else:
            print "ERROR AT LINE : %d" % lines
            print "EXPECTED '[' NOT FOUND"
            sys.exit(ERRORTK)
    elif state == leftBracketTK:
        lex()
        condition()
        if state == rightBracketTK:
            lex()
        else:
            print "ERROR AT LINE : %d" % lines
            print "EXPECTED ']' NOT FOUND"
            sys.exit(ERRORTK)
    elif state == TRUETK:
        lex()
    elif state == FALSETK:
        lex()

    else:
        expression()
        relational_oper()
        expression()


def expression():
    global state
    optional_sign()
    term()
    while state == plusTK or state == minusTK:
        add_oper()
        term()


def term():
    global state, bufferWord
    factor()
    while state == multiplyTK or state == divideTK:
        mul_oper()
        factor()


def factor():
    global state, bufferWord
    if state == constantTK:
        lex()
    elif state == leftParenthesisTK:
        lex()
        expression()
        if state == rightParenthesisTK:
            lex()
        else:
            print "ERROR AT LINE : %d" % lines
            print "EXPECTED ')' NOT FOUND"
            sys.exit(ERRORTK)
    elif state == identifierTK:
        lex()
        if state == leftParenthesisTK:
            idtail()
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED FACTOR NOT FOUND"
        sys.exit(ERRORTK)


def idtail():
    global state
    if state == leftParenthesisTK:
        actualpars()


def relational_oper():
    global state
    if state == equalTK or state == lessEQTK or state == moreEQTK or state == lessTK or state == differentTK or state == moreTK:
        lex()
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED COMPARE OPERATOR NOT FOUND"
        sys.exit(ERRORTK)


def add_oper():
    global state
    if state == plusTK or state == minusTK:
        lex()
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED ADD OPERATOR NOT FOUND"
        sys.exit(ERRORTK)


def mul_oper():
    global state
    if state == multiplyTK or state == divideTK:
        lex()
    else:
        print "ERROR AT LINE : %d" % lines
        print "EXPECTED MULTIPLICATION OPERATOR NOT FOUND"
        sys.exit(ERRORTK)


def optional_sign():
    global state
    if state == plusTK or state == minusTK:
        add_oper()
    else:
        return


program()


inputFile.close()
