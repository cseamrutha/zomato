def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        swap= False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
            if swap==False:
                break
if __name__ =="__main__":
    arr=[64,34,25,12,2,11,90]
    bubblesort(arr)
    print("the sorted array is:")
    for i in range(len(arr)):
        print(arr[i],end=" ") 
                    
