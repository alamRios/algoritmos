def busquedabin(arr, bajo, alto):
	
	mid = (bajo + alto)//2
	
	if mid is arr[mid]:
		return mid
	
	if mid > arr[mid]:
		return busquedabin(arr, (mid + 1), alto)
	else:
		return busquedabin(arr, bajo, (mid -1))
	return -1 # Regresa -1 si no encuentra un valor
	
arr = [-10, -1, 2, 100]
n = len(arr)
print(str(busquedabin(arr, 0, n-1)))