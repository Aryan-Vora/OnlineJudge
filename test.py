A = [1, 2, 4, 4]


def CheckSorted(A, P, R):
    if P == R:
        return True
    Q = (R+P)//2
    if not CheckSorted(A, P, Q) or not CheckSorted(A, Q+1, R):
        return False

    if A[Q] > A[Q+1]:
        return False
    return True


print(CheckSorted(A, 0, 3))
