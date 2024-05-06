# divide: divide the problem into a number of subproblems of smaller instance than the original problem
# conquer: conquer the subproblems by solving them recursively. Small problem -> easy solution
# combine: combine the solutions of each subproblem into one solution, wich is the solution for the original subproblem

# how does a merge sort works?
# first we divide our problem in half, so if there is an array of n element we will divide it into two arrays of size n/2.
# Then, we sort these 2 subproblems in a recursively way.
# Finaly, we merge our two solutions into on.

def merge_sort(A):
    if len(A) > 1:
        q = len(A)//2
        L = A[:q] #o python eh um lixo pq ele modifica diretamente na memoria a array e n uma copia dela, por isso crio antes os vetores a serem usados
        R = A[q:]
        merge_sort(L)
        merge_sort(R)
        merge(A, L, R)
    return A
        
def merge(A, L, R):

    i = j = k = 0    
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
        
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    
array = [16, 31, 41, 39, 24, 7, 30, 11]


inordinate_array = []
n = int(input("Size of array: "))

print("Array elements: ", end="")
linha = input().split(" ")
for j in range(n):
    inordinate_array.append(int(linha[j]))

print(inordinate_array)    
merge_sort(inordinate_array)
print(inordinate_array)
