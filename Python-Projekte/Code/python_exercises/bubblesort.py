def bubbleSort(arr):
    n = len(arr)

    print ("n", n)
 
    # Traverse through all array elements
    for i in range(n):
        print ("i", i)
        # Last i elements are already in place
        for j in range(0, n-i-1):
            print ("j", j)
            print ("arrj vorher", arr[j])
            print ("arrj+1 vorher", arr[j+1])
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
            print ("arrj nachher", arr[j])
            print ("arrj+1 nachher", arr[j+1])
 
# Driver code to test above
arr = [35,15,1]
 
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]), 