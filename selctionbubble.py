percentage = []
n = int(input("Enter the number of students in class: "))
for i in range(n):
    k = float(input(f"Enter the percentage of student {i + 1}: "))
    percentage.append(k)

# Selection sort
def selectionsort(percentage):
    for i in range(len(percentage)):
        min_index = i
        for j in range(i + 1, len(percentage)):
            if percentage[j] < percentage[min_index]:
                min_index = j
        percentage[i], percentage[min_index] = percentage[min_index], percentage[i]
    return percentage

print("Selection sorted array:", selectionsort(percentage))

# Bubble sort
def bubblesort(percentage):
    for i in range(len(percentage)):
        for j in range(0, len(percentage) - i - 1):
            if percentage[j] > percentage[j + 1]:
                percentage[j], percentage[j + 1] = percentage[j + 1], percentage[j]
    return percentage

print("Bubble sorted array:", bubblesort(percentage))
