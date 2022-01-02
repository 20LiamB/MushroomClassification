# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('liam')


def minCut(A):
    if isPalindrome(A):
        return 0

    count = 0
    substring = A
    partition = 0
    while partition != len(A) - 1:
        for i in range(len(substring), 0, -1):
            if isPalindrome(substring[0: i]):
                partition += i
                substring = substring[i + 1:]
                count += 1
                break
    return count


def find_max_sum_sub_array(A):
    m = -1000000
    for i in range(0, len(A)):
        s = 0
        for j in range(i, len(A)):
            s = s + A[j]
            if s + A[j] <= s:
                break
        if s > m:
            m = s
    return m


def isPalindrome(s: str) -> bool:
    n = len(s)
    if n <= 1:
        return True
    n = n - 1
    for i in range(len(s)):
        if s[i] != s[n - i]:
            return False
    return True


def surroundingLand(grid, i, j):
    surroundingLands = []
    if i > 0 and grid[i - 1][j] == "1":
        surroundingLands.append([i - 1, j])
    if i < len(grid) - 1 and grid[i + 1][j] == "1":
        surroundingLands.append([i + 1, j])
    if j > 0 and grid[i][j - 1] == "1":
        surroundingLands.append([i, j - 1])
    if j < len(grid[i]) - 1 and grid[i][j + 1] == "1":
        surroundingLands.append([i, j + 1])
    return surroundingLands


def bfs(grid, i, j):
    connected = []
    q = []
    q.append([i, j])
    while q:
        curr = q.pop(0)
        for x in surroundingLand(grid, curr[0], curr[1]):
            if x not in connected:
                q.append(x)
                connected.append(x)
    return connected


def dfs(grid, i, j):
    connected = []
    stack = []
    stack.append([i, j])
    while stack:
        curr = stack.pop()
        sl = surroundingLand(grid, curr[0], curr[1])
        if sl[0] not in connected:
            stack.append(sl[0])
            connected.append(sl[0])
        # for x in sl:
        #     if x not in connected:
        #         stack.append(x)
        #         connected.append(x)

    return connected


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "1":
                count += 1
                grid[i][j] = "0"
                for x in bfs(grid, i, j):
                    grid[x[0]][x[1]] = "0"

    return count


'''
reverse an arbitrary string without allocating any memory
'''


def rec_reverse(s):
    if len(s) <= 1:
        return s
    else:
        return s[len(s) - 1] + reverse(s[1:len(s) - 1]) + s[0]


def reverse(s):
    n = len(s)
    for i in range(len(s) - 1, -1, -1):
        s += s[i]
    return s[n:]


def tensDigit(num):
    ret = ''
    if num >= 90:
        ret += 'XC'
        num -= 90
    elif num >= 50:
        ret += 'L'
        num -= 50
    elif num >= 40:
        ret += 'XL'
        num -= 40
    while num >= 10:
        ret += 'X'
        num -= 10
    return [ret, num]


def onesDigit(num):
    ret = ''
    if num == 9:
        ret += 'IX'
        num -= 9
    elif num >= 5:
        ret += 'V'
        num -= 5
    elif num == 4:
        ret += 'IV'
        num -= 4
    while num >= 1:
        ret += 'I'
        num -= 1
    return [ret, num]


def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    answer = ''
    m = num
    while m >= 1000:
        answer += 'M'
        m -= 1000
    if m >= 900:
        answer += 'CM'
        m -= 900
    elif m >= 500:
        answer += 'D'
        m -= 500
    elif m >= 400:
        answer += 'CD'
        m -= 400
    while m >= 100:
        answer += 'C'
        m -= 100
    tens = tensDigit(m)
    answer += tens[0]
    m = tens[1]
    ones = onesDigit(m)
    answer += ones[0]
    m = ones[1]

    return answer


'''
A frog is crossing a river. The river is divided into x units and at each unit
there may or may not exist a stone. The frog can jump on a stone, but it must 
not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order,
determine if the frog is able to cross the river by landing on the last stone.
Initially, the frog is on the first stone and assume the first jump must be 1 
unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k,
or k + 1 units. Note that the frog can only jump in the forward direction.
'''


def frogJump(arr) -> bool:
    for i in range(3, len(arr)):
        if arr[i] > arr[i - 1] * 2:
            return False
    stone_positions = set()
    for i in arr:
        stone_positions.add(i)
    lastStone = arr[-1]
    positions_stack = []
    jumps_stack = []
    positions_stack.append(0)
    jumps_stack.append(0)
    while positions_stack:
        position = positions_stack.pop()
        jump = jumps_stack.pop()
        for i in range(jump - 1, jump + 1):
            if i <= 0:
                continue
            nextPosition = position + i
            if nextPosition == lastStone:
                return True
            elif nextPosition in stone_positions:
                positions_stack.append(nextPosition)
                jumps_stack.append(i)
    return False


def merge(arr, L, R):
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        elif R[j] <= L[i]:
            arr[k] = R[j]
            j += 1
            k += 1
    if i < len(L):
        while i < len(L):
            arr[k] = L[i]
            k += 1
            i += 1
    elif j < len(R):
        while j < len(R):
            arr[k] = R[j]
            k += 1
            j += 1
    return arr


def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        L = arr[:m]
        R = arr[m:]
        mergeSort(L)
        mergeSort(R)
        merge(arr, L, R)
    return arr


def call_binsearch(arr, x):
    return binarySearch(x, arr, 0, len(arr) - 1)


def binarySearch(x, arr, b, e):
    if b > e:
        return -1
    m = (b + e) // 2
    if arr[m] == x:
        return m
    elif arr[m] > x:
        return binarySearch(x, arr, b, m - 1)
    else:
        return binarySearch(x, arr, m + 1, e)


def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    count1 = 0
    i = 0
    j = 0
    while i < len(text1) and j < len(text2):
        c = text1[i]
        if c in text2[j:]:
            i += 1
            j = text2[j:].find(c) + j
            count1 += 1
        else:
            i += 1
    count2 = 0
    i = 0
    j = 0
    while j < len(text1) and i < len(text2):
        c = text2[i]
        if c in text1[j:]:
            i += 1
            j = text1[j:].find(c) + j
            count2 += 1
        else:
            i += 1
    return max(count2, count1)

def convertChar(c):
    if c == '0':
        return 0
    elif c == '1':
        return 1
    elif c == '2':
        return 2
    elif c == '3':
        return 3
    elif c == '4':
        return 4
    elif c == '5':
        return 5
    elif c == '6':
        return 6
    elif c == '7':
        return 7
    elif c == '8':
        return 8
    elif c == '9':
        return 9

def convert(s):
    i = 0
    ans = 0
    negative = False
    while i < len(s):
        if i == 0:
            if s[i] == '-':
                negative = True
                i += 1
                continue
            if s[i] == '+':
                negative = False
                i += 1
                continue
        ans *= 10
        ans += convertChar(s[i])
        i += 1
    if negative:
        ans *= -1
    return ans


def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    accepted = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
    n = len(s)
    i = 0
    while i < n and s[i] not in accepted:
        i += 1
    temp = s[i:]
    i = 0
    while i < len(temp) and temp[i] in accepted:
        i += 1
    temp = temp[:i]
    answer = convert(temp)
    return answer


if __name__ == '__main__':
    # grid = [
    #     ["1", "1", "1", "1", "0"],
    #     ["1", "1", "0", "1", "0"],
    #     ["1", "1", "0", "0", "0"],
    #     ["0", "0", "0", "0", "0"]
    # ]
    # arr = [5, 7, 1, 4, 8, 2, 3, 9, 0, 6]
    # merged = mergeSort(arr)
    # print(merged)
    # print(call_binsearch(merged, 0))


    print(myAtoi('words and 987'))
