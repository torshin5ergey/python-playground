def rabin_karp(string: str, substring:str) -> int:
    """
    Implements the Rabin-Karp algorithm for substring search.
    
    Returns:
        int: Index of the first occurrence of the substring in the string, or -1 if not found.
    """
    n = len(string)
    m = len(substring)
    if m > n:
        return -1
    
    # Prime modulus (big prime number) to minimize collisions
    q = 1000000007
    # Alphabet size, 256 for ASCII
    d = 256

    # Hash calculation
    hash_substring = 0
    hash_string = 0
    # Calculate hash for string and substring
    for c in range(m): # For first m chars
        # Calculating with simplified iterative equation
        hash_substring = (hash_substring * d + ord(substring[c])) % q
        hash_string = (hash_string * d + ord(string[c])) % q
        
    # Check and slide the substring pattern window
    for i in range(n - m + 1): # 
        if hash_string == hash_substring:
            # Additional check
            if string[i:i+m] == substring:
                return i
        # Calculate hash value for the next pattern window
        if i < n - m:
            hash_string = (d * (hash_string - ord(string[i]) * pow(d, m-1)%q) + ord(string[i + m])) % q
    return -1 # Not found
