if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]

    # Finding the average marks 
    average = sum(marks)/len(marks)
    
    #rounding the average to 2 decimal places 
    average_round = round(average, 2)

    print("{:.2f}".format(average_round))
