def sort_dict( dCount ):
    """
    Returns a sorted list of the most popular keys in the dict dCount.
    list [var, count] is sorted numerically by counts (largest to smallest) 
    and alphabetically by key where the count is the same.
    """
    # Sort by count (largest to smallest), then alphabetically..
    var_count = [ item for item in sorted( dCount.items(), key=lambda x: [-x[1], x[0]] )]
    return var_count
