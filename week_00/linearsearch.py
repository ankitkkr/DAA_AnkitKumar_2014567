
tc = int(input('enter the number of test cases'))
while tc != 0:
    size = int(input('Enter the size'))
    arr = list(map(int, input('enter the elements of array').split()))
    key = int(input('enter the key element'))
    i=0
    count = 0
    flag = 0

    while True:

        if size==i:
            break

        elif arr[i] == key:
            # print('true')
            flag=1
            break

        else:
            # print('false')
            count +=1
            # print(count)
            i+=1


    if flag == 1:
        print('yes your key is present', '-', count)
    else:
        print("Key Not Present")

    tc -= 1
