## 인공지능_과제_"1-2 과제 틱택토 게임 확장"
## 틱택토 게임이 컴퓨터와 컴퓨터 대결로 작성되어 있습니다.
## 기계공학과_20154523_강남규

#보드 설정
game_board = [ ' ', ' ', ' ',
               ' ', ' ', ' ',
               ' ', ' ', ' ']

#빈 칸을 찾아서 리스트로 만듬
def empty_cells(board):
    cells = []
    for x, cell in enumerate(board):
        if cell == ' ':
            cells.append(x)
    return cells

#빈 보드에만 움직일 수 있게
def valid_move(x):
    return x in empty_cells(game_board)

#x의 위치로 이동
def move(x, player):
    if valid_move(x):
        game_board[x] = player
        return True
    return False

# 현재의 게임보드 표시
def draw(board):
    for i, cell in enumerate(board):
        if i%3 == 0:
            print('\n----------------')
        print(':', cell , ':', end='')
    print('\n----------------')

#보드 상태 평가
def evaluate(board):
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score

#승리 조건
def check_win(board, player):
    win_conf = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conf

#승리자 결정
def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O')


#여기가 미니맥스 함수, 순환적으로 호출된다고함. -> False와 True로 변화하기때문
def minimax(board, depth, maxPlayer):
    pos = -1

    #단말 노드일 경우 보드를 평가하여 위치와 평가값을 반환
    if depth == 0 or len(empty_cells(board)) == 0 or game_over(board):
        return -1, evaluate(board)

    if maxPlayer == True:
        value = -10000
        where_b = input("원하는 위치의 값을 입력해주세요 \n"
                        "[0] [1] [2] \n"
                        "[3] [4] [5] \n"
                        "[6] [7] [8] \n")

        print(where_b)

        if where_b < 0 or where_b > 8:
            print("불가능한 구역입니다. \n 다시 선택해 주세요.")
            where_b = input("원하는 위치의 값을 입력해주세요 \n"
                            "[0] [1] [2] \n"
                            "[3] [4] [5] \n"
                            "[6] [7] [8] \n")


        board[where_b] = 'X'

        pos = where_b


    else:
        value = +10000

        for p in empty_cells(board):

            board[p] = 'O'

            x, score = minimax(board, depth-1, True)
            board[p] = ' '
            if score < value:
                value = score
                pos = p
    return pos, value

player='X'

#여기서부터 메인
while True:
    draw(game_board)
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break
    i, v = minimax(game_board, 9, player=='X')
    move(i, player)
    if player=='X':
        player='O'
    else:
        player='X'

if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')



"""

t = input("원하는 위치의 값을 입력해주세요 \n"
          "[0] [1] [2] \n"
          "[3] [4] [5] \n"
          "[6] [7] [8] \n")
    tb = board[t]
    print(t)

1. 플레이어가 선택한다. -> 이때 플레이어는 화면에 뜬 t의 화면을 보고 판들의 번호를 보며 정한다.
2. 선택하고 번호를 누르면 해당 번호가 board[t]에 들어가며 입력을 시킨다.
3. 그것을 인지하여 max플레이어가 놓는다.
4. 그다음은 플레이어가 선택한다.
---> 반복
이후 이기거나 지면 동일하게 나온다.

"""

