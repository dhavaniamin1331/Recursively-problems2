def ways(stairs):
    # Check corner case 
    if stairs < 0:
        return 0
    # If no stair left, just return one as we reach the top 
    if stairs == 0:
        return 1
    
    twoSteps = 0
    oneStep = 0

    # We can jump 2 only if 2 or more stairs are left 
    if stairs >=2:
        twoSteps = ways(stairs - 1)
    # Jump 1 if 1 or more stairs remain 
    oneStep = ways(stairs - 1)

    # Return total ways 
    return twoSteps + oneStep

stairs = int(input("Enter number of steps: "))
print("Number of ways to climb:", ways(stairs))
