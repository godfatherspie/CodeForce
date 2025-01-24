def can_construct_special_triangle(h, numbers):
    #sorting the numbers
    numbers.sort()
    
    #determining the start and end numbers for rows in the triangle
    start = 0
    for row in range(1, h + 1):
        current_row = numbers[start:start + row]
        start += row
        
        #skipping the last row as it doesn't need to satisfy the condition
        if row == h:
            break
        
        #satisfying the condition for the current row
        next_row = numbers[start:start + row + 1]
        for i in range(row):
            if not (current_row[i] < next_row[i] and current_row[i] < next_row[i + 1]):
                return "NO"
    
    return "YES"


h = int(input().strip())
numbers = list(map(int, input().strip().split()))

print(can_construct_special_triangle(h, numbers))
