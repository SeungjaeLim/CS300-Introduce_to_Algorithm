def solution(A) -> int:
    """
    Find the maximum score

    Parameter
    ----------
    A : list of N+2 numbers with A[0]=A[N+1]=1
    """
    length = len(A)
    dp = [[0 for j in range(length)] for i in range(length)]
    if length < 2:
        return 0
    return solution_dp(A, dp, 0, length - 1)

def solution_dp(A, dp, i, j)->int:
    if j-i < 2:
        dp[i][j] = 0
        return 0
    elif j-i == 2:
        dp[i][j] = A[i]*A[i+1]*A[j]
        return dp[i][j]
    elif dp[i][j] != 0:
        return dp[i][j]
    else:
        maxScore = 0
        for k in range(i+1,j):
            tmpScore =  solution_dp(A, dp, i, k) + solution_dp(A, dp, k, j) + A[i]*A[k]*A[j]
            if tmpScore > maxScore:
                maxScore = tmpScore
        dp[i][j] = maxScore
        return dp[i][j]
    return 0

if __name__ == "__main__":
    # sample 1
    A = [1,2,1,2,1]
    answer = solution(A)
    print(answer)  # 36
