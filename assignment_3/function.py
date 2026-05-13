def iteration_function(c, max_iterations=500):
    """
    Determines the iteration count at which a point diverges.
    Parameters:
    -----------
    c: complex number (x + iy)
    max_iteration: maximum number of iterations to make sure the code is not in an infinite loop
    Returns: 
    --------
    iteration count if it diverges, or max_iter if it stays bounded.
    """
    z = 0 
    
    for i in range(1,max_iterations+1):
        z = z**2 + c
        value_squared = z.real**2 + z.imag**2
        if value_squared > 4:
            return i
    return max_iterations
  