# Enter your code here. Read input from STDIN. Print output to STDOUT

n=int(input())
rooms=map(int,input().split(" "))
rooms=sorted(rooms)
for i in range(1,len(rooms)):
    if i!=len(rooms)-1:
        if rooms[i]!=rooms[i-1] and rooms[i]!=rooms[i+1]:
            print (rooms[i])
            break
    else:
        print (rooms[i])
