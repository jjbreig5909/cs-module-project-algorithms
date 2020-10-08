'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = None):
    # Your code here
    if n == 0 or n==1:
       return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    pass

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 25

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
