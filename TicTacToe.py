import sys, os, random, getopt


def makeMove(move):
    if move > 9 or move < 1:
        print "Please choose a valid number"
        sys.exit()
    move = move - 1
    if board[move] is not " ":
        print "place already taken"
        sys.exit()
    board[move] = "X"
    pcRoll = random.randrange(0,8)
    while " " in board and board[pcRoll] is not " ":
        pcRoll =  random.randrange(0,8)

    board[pcRoll] = "O"
    print board[0] +  "|" + board[1] + "|" + board[2]
    print board[3] +  "|" + board[4] + "|" + board[5]
    print board[6] +  "|" + board[7] + "|" + board[8]

    checkWin(board,"X")
    checkWin(board,"O")

def checkWin(b,i):
    if i is "X":
        text = "You won!"
    else:
        text = "You lost!"
    if b[0] is  b[1] is b[2] is i:
        print text
        sys.exit()
    if b[3] is  b[4] is b[5] is i:
        print text
        sys.ext()
    if b[6] is  b[7] is b[8] is i:
        print text
        sys.exit()
    if b[0] is  b[3] is b[6] is i:
        print text
        sys.exit()
    if b[1] is  b[4] is b[7] is i:
        print text
        sys.exit()
    if b[2] is  b[5] is b[8] is i:
        print text
        sys.exit()
    if b[0] is  b[4] is b[8] is i:
        print text
        sys.exit()
    if b[2] is  b[4] is b[6] is i:
        print text
        sys.exit()
    if not " " in b:
        print "Its a tie!"
        sys.exit()

try:
    opts, args = getopt.getopt(sys.argv[1:],"h2",["help",""])
except getopt.GetoptError:
    print 'Error with input'
    sys.exit(2)

for opt, arg in opts:
    if opt in "-h":
        print"1|2|3"
        print"4|5|6"
        print"7|8|9"
        print"start with -2 for 2 players"
        sys.exit()
    if opt in "-2":
        print"2 player modus is not yet implemented"
        sys.exit()

board = [" "," "," "," "," "," "," "," "," "]
userMove = ''
while userMove is not 'quit':
    userMove = int(raw_input("Move:"))
    makeMove(userMove)

