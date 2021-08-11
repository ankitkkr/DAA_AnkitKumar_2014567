t=int(input('enter number of test cases : '))

while(t):
	size = int(input('Enter the size : '))
	arr = list(map(int, input('enter the elements of array : ').split()))
	key = int(input('enter the key element : '))
	low=0
	high=size-1
	flag=0
	while low<=high:

		mid=int((high+low)/2)

		if key>arr[mid]:
			low=mid+1
		elif key<arr[mid]:
			high=mid-1
		elif key==arr[mid]:
			print('key is present')
			flag=1
			break


	if flag==0:
		print('key not present')

	t=t-1