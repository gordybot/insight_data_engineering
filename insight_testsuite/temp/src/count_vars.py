def count_vars(in_file, var_inds, cond_ind, cond_match, delimiter=';'):
    """
    Count all the occurrences of strings in the columns in var_inds where the string in the cond_ind`th column matches cond_match.

    Inputs: 
         in_file: file handle of an input file with columns delimited by character specified by delimiter.
         delimiter: single character that denotes column break in input data.
         var_inds: list of column indices of variables to count.
         cond_ind: index of the column to check before counting 
         cond_match: string to check before counting -- only increment the counters
                     if the (cond_ind)th column matches cond_match.
                     e.g., if entry corresponding to STATUS == 'certified'
                     The match is case-insensitive.
    Returns:
        [d1,d2,...], NumMatches
        A list of dictionaries containing the count of strings appearing in the columns corresponding to each item in var_inds, and the number of lines that satisfied the conditional match. 
    """

    # Initialize counter variables.
    NumMatches = 0
    Nvars = len(var_inds)
    varCounters = [{} for i1 in range(Nvars)]

    # Read file line-by-line:
    for line in in_file:
        tokens = line.split(delimiter)

        # Test match condition:
        if tokens[cond_ind].lower() == cond_match.lower():
            NumMatches += 1

            # Increment counter for each variable
            for i1 in range(Nvars):
                var_string = tokens[ var_inds[i1] ].replace('"','')
                if var_string in varCounters[i1]:
                    varCounters[i1][ var_string ] += 1
                else:
                    varCounters[i1][ var_string ] = 1

    # Return counts, total matches.
    return varCounters, NumMatches
