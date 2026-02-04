#MergeSort
#Haley Gray
#02/03/2026

#merges 2 sub arrays together
#Left subarr indexes == [start, mid]
#right subarr indexes == [mid+1, end]
#when finished merging,
#merged subarr indexes == [start, end]
def merge(arr, start, mid, end):
    #lengths of each subarray
    lLength = mid - start + 1
    rLength = end - mid
    #temp arrays
    L = [0] * lLength
    R = [0] * rLength
    #copy into temp arrays from main arr
    for i in range(lLength):
        L[i] = arr[start + i]
    for j in range(rLength):
        R[j] = arr[mid+1+j]
    #merge L&R arrays to main arr
    i = 0
    j = 0
    k = start
    while (i < lLength and j < rLength):
        if (L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    #finish copying remaining items
    #in-order from either L or R
    while (i < lLength):
        arr[k] = L[i]
        i += 1
        k += 1
    while (j < rLength):
        arr[k] = R[j]
        j += 1
        k += 1

#mergeSort - splits arr into 2 halves recursively
#then merges the subarrays back into main arr
#uses temp L&R arrays when merging
#to prevent loss of elements
def mergeSort(arr, start, end):
    #start == end -> only one element -> sorted
    if (start < end):
        mid = (start + end) // 2
        mergeSort(arr, start, mid) #sort left
        mergeSort(arr, mid+1, end) #sort right
        merge(arr, start, mid, end)

xs = [3,7,1,6,2,5,1]
mergeSort(xs,0,len(xs)-1)
print(xs)

