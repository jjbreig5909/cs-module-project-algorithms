'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here    
    for i in range(len(arr)):
        dupe = False
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                dupe = True
        if not dupe:
            return arr[i]
    
    return -1

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")