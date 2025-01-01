# https://www.codegrepper.com/code-examples/python/how+to+read+a+file+into+array+in+python
import re

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() # puts the file into an array
    fileObj.close()
    return words


def pt1(arr):
    s = arr[0] # manually converted input to one line
    matches = re.findall(r"mul\([-+]?\d+,[-+]?\d+\)", s)

    total = 0
    for match in matches:
        print(match)
        nums = match[4:-1].split(",")
        print(nums)

        x = int(nums[0])
        y = int(nums[1])

        total += x * y

    return total


def pt2(arr):
    s = arr[0]
    print(s)

    total = 0
    do = True

    # iterate through the string, look for mul(X, Y) and do() and don't()
    for i in range(len(s)):
        if s[i:i+4] == "mul(" and do:
            # find the end of the mul
            j = i + 4

            # while s[j] is a digit or a comma
            while s[j].isdigit() or s[j] == ",":
                j += 1
            if s[j] != ")": # next loop iteration
                continue

            # find the numbers
            nums = s[i+4:j].split(",")
            print("\tnums", nums)

            x = int(nums[0])
            y = int(nums[1])

            total += x * y

        if s[i:i+4] == "do()":
            print("Found do()")
            do = True

        if s[i:i+7] == "don't()":
            print("Found don't()")
            do = False

    # print(s)
    return total


arr = readFile("AoC_Inputs/AoC_2024_d3_input.txt")
print("Part 1", pt1(arr))
print("Part 2", pt2(arr))