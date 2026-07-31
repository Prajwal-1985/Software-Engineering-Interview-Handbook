# Two Sum Problem

nums = [2, 7, 11, 15]
target = 9

# Dictionary to store number and its index
mp = {}

for i in range(len(nums)):

    # Find the required complement
    need = target - nums[i]

    # Check if complement already exists
    if need in mp:
        print("Indices:", mp[need], i)
        break

    # Store current number and its index
    mp[nums[i]] = i