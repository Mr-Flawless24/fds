def remove_duplicates(lst):
    """Remove duplicate entries from a list."""
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


def intersect(lst1, lst2):
    """Find the intersection of two lists."""
    result = []
    for item in lst1:
        if item in lst2 and item not in result:
            result.append(item)
    return result


def union(lst1, lst2):
    """Find the union of two lists."""
    result = remove_duplicates(lst1 + lst2)
    return result


def difference(lst1, lst2):
    """Find the difference of two lists."""
    result = []
    for item in lst1:
        if item not in lst2:
            result.append(item)
    return result


def symmetric_difference(lst1, lst2):
    """Find the symmetric difference of two lists."""
    return difference(lst1, lst2) + difference(lst2, lst1)

# Define groups of students
cricket = []
badminton = []
football = []

cricket_count = int(input('Enter how many students play cricket: '))
for i in range(1, cricket_count+1):
    element = input(f"Enter {i} student name: ")
    cricket.append(element)

badminton_count = int(input('Enter how many students play badminton: '))
for i in range(1, badminton_count+1):
    element = input(f"Enter {i} student name: ")
    badminton.append(element)

football_count = int(input('Enter how many students play football: '))
for i in range(1, football_count+1):
    element = input(f"Enter {i} student name: ")
    football.append(element)

# Remove duplicates from each group
cricket = remove_duplicates(cricket)
badminton = remove_duplicates(badminton)
football = remove_duplicates(football)


# a) Students who play both cricket and badminton
both_cricket_badminton = intersect(cricket, badminton)
print("a) Students who play both cricket and badminton:",
      both_cricket_badminton)


# b) Students who play either cricket or badminton but not both
either_but_not_both = symmetric_difference(cricket, badminton)
print("b) Students who play either cricket or badminton but not both:",
      either_but_not_both)


# c) Number of students who play neither cricket nor badminton
all_students = union(union(cricket, badminton), football)
cricket_badminton = union(cricket, badminton)
neither_cricket_nor_badminton = difference(all_students, cricket_badminton)
print("c) Number of students who play neither cricket nor badminton:",
      len(neither_cricket_nor_badminton))


# d) Students who play cricket and football but not badminton
cricket_and_football = intersect(cricket, football)
result_d = difference(cricket_and_football, badminton)
print("d) Students who play cricket and football but not badminton:", result_d)
