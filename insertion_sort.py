def insertion_sort(inordinate_array):
    A = inordinate_array[:]
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


inordinate_array = []
n = int(input("Size of array: "))

print("Array elements: ", end="")
linha = input().split(" ")
for j in range(n):
    inordinate_array.append(int(linha[j]))

B = insertion_sort(inordinate_array)

print(inordinate_array)
print(B)