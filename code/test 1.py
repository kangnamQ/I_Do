#비어 있는 칸을 찾아서 리스트로 반환한다.
def empty_cells(board):
    cells = []
    for x, cell in enumerate(board):
        if cell == '':
            cells.append(x)
    return cells

#비어있는 칸에 놓을 수 있게 만드는 함수
def valid_move(x):
    return x in empty_cells(game_board)

#위치 X에 놓는 경우
def move(x,player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

#보드를 그리기 위한 함수
def draw(board):
    for i, cell in enumerate(board):
        if i%3 == 0:
            print("\n------------------------")
        print("|",cell,"|",end ="")
    print("\n------------------------")

#보드의 상태 평가 함수
def evaluate(board):
    if check_win(board,"X"):
        score = 1
    elif check_win(board,"O"):
        score = -1
    else:
        score = 0
    return score

#1차원 리스트에서 동일한 문자가 수직선이나 수평선,대각선으로 나타나면 승리
def check_win(board, player):

    win_conf = [
    [board[0],board[1],board[2]],
    [board[3],board[4],board[5]],
    [board[6],board[7],board[8]],
    [board[0],board[3],board[6]],
    [board[1],board[4],board[7]],
    [board[2],board[5],board[8]],
    [board[0],board[4],board[8]],
    [board[2],board[4],board[6]],
    ]
    return [player,player,player] in win_conf

#1차원 리스트에서 동일한 문자가 수직선이나 수평선,대각선으로 나타나면 승리
def game_over(board):
    return check_win(board,"X") or check_win(board,"O")

#위치를 탐색하기 위한 미니맥스 알고리즘 함수
def minimax(board, depth, maxPlayer):
    #최대값의 위치 초기화
    pos = -1
    #게임이끝나는 조건문을 작성 후 강제 종료후 evaluate함수를 호출
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)
    #플레이어가 X일 경우(사람)
    if maxPlayer == True:
        value = -10000 #음의 무한대
        #보드에 값을 입력
        user_input = int(input("input number ( 0 ~ 8 )"))

        #올바르지 않은 값에 대해 재설정
        while user_input > 8 or user_input < 0:
                print("invalid number!")
                user_input = int(input("input number ( 0 ~ 8 )"))

        board[user_input] = "X"
        board[user_input] = ""

        pos = user_input  #최대값의 위치를 기억한다.

    #플레이어가 O일경우(컴퓨터)
    else:
        value = +10000 #양의 무한대
        #자식 노드를 하나씩 평가하여서 최선의 수를 찾는다.
        for p in empty_cells(board):
            board[p] = "O"  #보드의 p위치에  "O"를 놓는다.

            #경기자를 교체하여서 minimax()를 순환호출한다.
            x,score = minimax(board, depth-1,False)
            board[p] = ""   #보드는 원상태로 돌린다.
            if score < value:
                value = score   #최대값을 취한다.
                pos = p     #최대값의 위치를 기억한다.

    return pos, value #위치와 값을 반환한다.

#1차원 리스트의 보드 구현
game_board = ['', '', '',
            '', '', '',
            '', '', '']

player = "X"
while True:
    #현재의 보드를 그린다.
    draw(game_board)
    #게임보드의 빈칸의 길이가 0이거나 게임오버가 되었을때 멈추는 if문
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break;
    #빈칸에 들어갈 값을 구하기 위한 미니맥스 함수 호출
    i, v = minimax(game_board, 9, player=="X")
    #리스트에 빈칸에 i값을 삽입한다.
    move(i,player)
    #차례를 넘기는 if문
    if player == "X":
        player = "O"
    else:
        player = "X"
#승리를 검사하는 if
if check_win(game_board,"X"):
    print("X win!")
elif check_win(game_board,"O"):
    print("O win!")
else:
    print("draw!")