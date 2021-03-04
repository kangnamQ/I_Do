## 인공지능_과제_"1-2 과제 틱택토 게임 확장"
## 틱택토 게임이 컴퓨터와 컴퓨터 대결로 작성되어 있습니다.
## 기계공학과_20154523_강남규

## 원래 퀴즈만 있다고 생각하고 있다가 다시 확인해보니 과제가 생겨서 급하게 과제기간 내에 냈지만 완성하지 못 한 것을 제출하였습니다.
## 어떻게 해야 성공할지 이것저것 해보며 성공하여서 다시 재 제출 하겠습니다.
## (갑자기 생긴 과제에 제출 기한이 토요일까지라서 조금 혼란이있었습니다...)


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

    #사람과 컴퓨터의 경기이므로 사람을 인식하여 동작하게 만듬.
    #사람이 두고 컴퓨터가 계산을 하여 그것을 해석하여 놓게끔 만든 것임.
    if maxPlayer == True:
        value = -10000
        where_b = int(input("원하는 위치의 값을 입력해주세요 \n"
                            "[0] [1] [2] \n"
                            "[3] [4] [5] \n"
                            "[6] [7] [8] \n"))


        #이후에 조건들을 if로 주었더니 한번은 뜨지만
        #한번 더 동일한 0~8까지의 숫자가 아닌 숙자 또는 비어있지 않은 구역에 놓으려고 시도를 하면
        #그냥 놓이거나 에러가 떠서 while로 대체 -> 잘 작동하는 것을 확인.


        #0~8까지 판을 보여줫지만 만약 숫자가 두개 눌리거나 0~8이외의 숫자를 눌렀을때 불가능 하다는 것을 알리고 다시 누르라고 함.
        while where_b < 0 or where_b > 8:
            print("불가능한 구역입니다. \n 다시 선택해 주세요. \n")
            where_b = int(input("원하는 위치의 값을 입력해주세요 \n"
                                "[0] [1] [2] \n"
                                "[3] [4] [5] \n"
                                "[6] [7] [8] \n"))


        while  board[where_b] != ' ':
            print("불가능한 구역입니다. \n 다시 선택해 주세요. \n")
            where_b = int(input("원하는 위치의 값을 입력해주세요 \n"
                                "[0] [1] [2] \n"
                                "[3] [4] [5] \n"
                                "[6] [7] [8] \n"))


        #만약 아무런 문제 없이 놓을 수 있다면 누른 자리에 대한 안내문을 띄움
        print(where_b,"번 자리에 돌을 둡니다.")

        board[where_b] = 'X'
        #board[where_b] = ' '       #굳이 없어도 있어도 되는 듯하다.

        pos = where_b


    else:
        value = +10000

        for p in empty_cells(board):

            board[p] = 'O'

            x, score = minimax(board, depth-1, False)
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

예상 시나리오

where_b = input("원하는 위치의 값을 입력해주세요 \n"
                "[0] [1] [2] \n"
                "[3] [4] [5] \n"
                "[6] [7] [8] \n")
p = board[where_b]

1. 플레이어가 선택한다. -> 이때 플레이어는 화면에 뜬 where_b의 화면을 보고 판들의 번호를 보며 정한다.
2. 선택하고 번호를 누르면 해당 번호가 board[where_b]에 들어가며 입력을 시킨다.
3. 그것을 인지하여 컴퓨터가 놓는다.
4. 그다음은 플레이어가 선택한다.
---> 반복
이후 이기거나 지면 동일하게 나온다.

위치를 몰라 해맸지만 if maxPlayer == True: 로변경하고 안의 내용을 바꿈으로써 성공함.

"""

