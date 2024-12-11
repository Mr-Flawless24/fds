Mark = []
n = int(input("Enter the number of Students :"))
for i in range(n):
    mark = int(input(" Enter the Marks : "))
    Mark.append(mark)
    
print("List of fds Marks",(Mark))

# Average marks of students

def average_marks(Mark):
    total_marks = 0
    total_students = 0

    for j in range(len(Mark)):
        if (Mark[j] != -1):
            total_students += 1
    
    for i in range(len(Mark)):
        if (Mark[i] != -1):
            total_marks += Mark[i]
    
    avg = total_marks/total_students
    
    return(avg)
    
print("Average Marks : ",average_marks(Mark))

# highest marks of students 

def highest_marks(Mark):
    max = 0
    for i in range(len(Mark)):
        if max < Mark[i]:
           max = Mark[i]
    return max

print(" Highest marks of students : ",highest_marks(Mark))

# lowest Marks of students

def lowest_marks(Mark):
    min = Mark[0]
    for i in range(len(Mark)):
        if min > Mark[i] and Mark[i] != -1:
           min = Mark[i]
    return min

print(" lowest marks of students : ",lowest_marks(Mark))

#count of absent students

def absent_students(Mark):
    count = 0
    for i in range(len(Mark)):
         if Mark[i]== -1:
            count+=1
    return count
    
print("Absent Student Marks :",absent_students(Mark))

#highest frequency of marks

def highest_frequency(Mark):
    count = 0
    check = highest_marks(Mark)
    for i in range(len(Mark)):
        if check == Mark[i]:
           count += 1
    return count

print("highest frequency of marks : ",highest_frequency(Mark))         