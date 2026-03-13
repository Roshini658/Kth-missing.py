def kth_missing(arr,k):#find kth missing positive number using binary search
    low=0#start index
    high=len(arr)-1#last index
    while low<=high:#binary search loop
        mid=(low+high)//2#find middle index
        missing=arr[mid]-(mid+1)#count missing numbers before arr[mid]
        if missing<k:#if missing numbers less than k
            low=mid+1#search right side
        else:#if missing numbers greater or equal to k
            high=mid-1#search left side
    return low+k#final kth missing number

#example
arr=[2,3,4,7,11]#given sorted array
k=5#find 5th missing number
print(kth_missing(arr,k))#print answer
