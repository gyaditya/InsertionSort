#Insertion

nums = [10, 70, 30, 100, 40, 45, 90, 80, 85]
words = ["dog","at", "good", "eye", "cat", "ball", "fish"]

def insertionSort(anArray):
    for i in range(1, len(anArray)):
        insertion = anArray[i]
        n = i -1
        while n >= 0 and insertion < anArray[n]:
            anArray[n + 1] = anArray[n]
            n = n - 1
        anArray[n + 1] = insertion

insertionSort(nums)
print(nums)

insertionSort(words)
print(words)
    