def Binary_search(arr, start_index, last_index, element):
	mid = float(start_index+last_index)/2
	arr = [2, 14, 19, 21, 99, 210, 512, 1028, 4443, 5110]
	element = 210
	start_index = 0
	last_index = len(arr)-1


if (start_index > last_index):
	print("Element not found")

elif (element > arr[mid]):
	start_index = mid+1
	Binary_search(arr, start_index, last_index, element)
elif (element < arr[mid]):
	last_index = mid-1
	Binary_search(arr, start_index, last_index, element)

else:
	print("element is present at index ") + str(mid)
	Binary_search(arr, start_index, last_index, element)