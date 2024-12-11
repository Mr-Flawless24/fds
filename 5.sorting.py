percentage = []
n = int(input(" enter the number of students in class : "))
for i in range(n):
    k = float(input(" enter the percentage of students : "))
    percentage.append(k)


# selection sort

def selectionsort(percentage):
    for i in range(len(percentage)):
        min_index = i
        for j in range(i+1, len(percentage)):
            if percentage[j] < percentage[min_index]:
                min_index = j
        percentage[i], percentage[min_index] = percentage[min_index], percentage[i]
    return percentage


print("selection sorted array :", selectionsort(percentage))


# bubble sort

def bubblesort(percentage):
    for i in range(len(percentage)):
        for j in range(0, len(percentage)-i-1):
            if percentage[j] > percentage[j+1]:
                percentage[j], percentage[j+1] = percentage[j+1], percentage[j]
    return percentage


print("bubble sorted array :", bubblesort(percentage))


# insertion sort

def insertionsort(percentage):
    for i in range(1, len(percentage)):
        key = percentage[i]

        j = i-1

        while j >= 0 and key < percentage[j]:
            percentage[j+1] = percentage[j]
            j == 1
        percentage[j+1] = key

    return percentage


print(" Insertion sorted array : ", insertionsort(percentage))


# shell sort

def shellsort(percentage):
    gap = len(percentage)//2

    while gap > 0:
        j = gap
        while j < len(percentage):
            i = j - gap

            while i >= 0:
                if percentage[i+gap] > percentage[i]:
                    break

                else:
                    percentage[i+gap], percentage[i] = percentage[i], percentage[i+gap]

                i = i-gap

            j += 1
        gap = gap//2

    return percentage


print(" Shell sorted array :", shellsort(percentage))
