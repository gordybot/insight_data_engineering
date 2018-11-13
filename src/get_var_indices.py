def get_var_indices( first_line, descriptors = '', delimiter=';'):
    """
    Inputs: 
      first_line: a string of column headers separated by 'delimiter'
      descriptors: a list containing a list of strings describing each variable
                   whose index is sought.
      delimiter: a single character used to separate columns
        
    Returns: an array of the indices of variables whose
             headers include the strings in descriptors.
    
    Example: if descriptors = [['work','state'], ['status']] 
             returns array [index of column where 'work' and 'state' appear,
                            index of column where 'status' appears]

    If there are multiple matching entries, return only the first occurrence.
    """
    tokens = first_line.split(delimiter)
    var_indices = [None for i2 in range(len(descriptors))]

    for i1,tok in enumerate(tokens):
        # Check to see if a header-token matches any description.
        for i2, description in enumerate(descriptors):
            # If a match has already been found, don't check again.
            if not var_indices[i2]:
                matches = True
                for word in description:
                    if not word in tok.lower():
                        matches = False
                if matches:
                    var_indices[i2] = i1
    return var_indices
