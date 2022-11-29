def solution(m, n, board):
    answer = 0
    newBoard = ["" for _ in board[0]]
    for i in range(len(board)):
        for j in range(len(board[i])):
            newBoard[j] += board[i][j]
    newBoard = [list(i) for i in newBoard]
    copyBoard = [i[:] for i in newBoard]

    # print(newBoard)
    arr = [[1 for _ in range(m)] for _ in range(n)]

    isTrue = True
    while isTrue:
        isTrue = False
        for i in range(len(newBoard)):
            for j in range(len(newBoard[i])):
                if i == len(newBoard) - 1 or j == len(newBoard[0]) - 1:
                    break
                tempValue = newBoard[i][j]
                if tempValue == newBoard[i + 1][j + 1] and tempValue != "0":
                    if tempValue == newBoard[i][j + 1] and tempValue == newBoard[i + 1][j]:
                        copyBoard[i][j] = copyBoard[i + 1][j] = copyBoard[i][j + 1] = copyBoard[i + 1][j + 1] = ""
            if "" in copyBoard[i]:
                num = copyBoard[i].count("")
                copyBoard[i] = list("0" * num + "".join(copyBoard[i]))
                isTrue = True
        newBoard = [i[:] for i in copyBoard]
        copyBoard = [i[:] for i in newBoard]

    # print(copyBoard)
    for i in newBoard:
        answer += i.count("0")
    return answer