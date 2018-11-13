#!/bash/bin/python

import sys

def read_header(first_line, descriptors=''):
    """
    Parse the first line of the input file 
    and identify which columns correspond to 
    the variable names containing the descriptors.
    """
    #line = in_file.readline()
    tokens = first_line.split(';')

    # Initialize
    STATE_ind = None
    labels = tokens
    # Determine which columns contain the variables of interest.
    for i1,tok in enumerate(tokens):
        # Two work states might be listed -- I'll use the first.
        if 'work' in tok.lower() and 'state' in tok.lower() and not STATE_ind:
            STATE_ind = i1
        if 'soc_name' in tok.lower():
            SOC_ind = i1
        if 'status' in tok.lower():
            STATUS_ind = i1
    return (STATE_ind, SOC_ind, STATUS_ind)

def count_vars(in_file, STATE_ind, SOC_ind, STATUS_ind):
    # Read through lines in input file and increment appropriate counters.
    # Return a dictionary of counts for each state, job, and total certified.

    # Initialize counter variables.
    TotalCert = 0
    STATE_dict = {}
    SOC_dict = {}

    for line in in_file:
        tokens = line.split(';');

        soc_name = tokens[ SOC_ind ]
        state = tokens[ STATE_ind ]
        status_tok = tokens[ STATUS_ind ] 
        status_flag = 0
    
        # Here I might normally use a Counter() object from the containers module
        # but a regular dictionary can be used. It is slightly faster to try to 
        # increment and catch the key error than to first check the key-list.

        if status_tok.lower()=='certified':
            status_flag = 1
            TotalCert += 1

            try:
                STATE_dict[ state] += 1
            except KeyError as e:
                STATE_dict[ state] = 1

            try:
                SOC_dict[ soc_name] += 1
            except KeyError as e:
                SOC_dict[ soc_name ] = 1
    # Return two dictionaries of counts by state and job.
    return STATE_dict, SOC_dict, TotalCert 

def sort_dict(dCount):
    # Convert dictionary of { item :counts} to list of item, count 
    # sorted by decreasing number counted.
    # Sort keys alphabetically, then by count.
    #var_count = [ (k, dCount[k]) for k in sorted(dCount, key=dCount.get, reverse=True)]
    var_count = [ (k, VarCount[k]) for k in sorted(VarCount, key=lambda x: (x[1],x[0]), reverse=True)]
    return var_count

def main():
    if True:
        in_filename = sys.argv[1]
        #outfile_jobs = './output/top_10_occupations.txt'
        #outfile_states = './output/top_10_states.txt'
        outfile_jobs = sys.argv[2]
        outfile_states = sys.argv[3]

        # Set of strings that suffice to identify the variables
        # we're interested in.
        var_descriptors = [['work','state'],['poc_code'],['status']]

        # Open the input file for reading,
        with open(in_filename,'r') as f:
            # Identify columns containing the desired variables.
            (STATE_ind, SOC_ind, STATUS_ind) = read_header(f, var_descriptors)

            # Count successful certifications by state and by job POC_name.
            (byState, bySOC, TotCert) = count_vars( f, STATE_ind, SOC_ind, STATUS_ind)

        # Sort by count first, then alphabetically.
        states_sorted = sort_dict( byState )
        soc_sorted = sort_dict( bySOC)

        # Write out the output files.
        with open(outfile_jobs,'w') as f2:
            f2.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
            for i1 in range( min(10,len(soc_sorted))):
                job = soc_sorted[i1][0]
                numCert = soc_sorted[i1][1]
                percentCert = soc_sorted[i1][1] / TotCert
                f2.write( '{};{};{:2.1%}\n'.format(job.upper(), numCert, percentCert) )

        with open(outfile_states,'w') as f3:
            f3.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')    
            for i1 in range( min(10,len(states_sorted))):
                state = states_sorted[i1][0]
                numCert = states_sorted[i1][1]
                percentCert = states_sorted[i1][1] / TotCert
                f3.write( '{};{};{:2.1%}\n'.format(state.upper(), numCert, percentCert) )

if __name__=='__main__':
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv) )
    if len(sys.argv) < 4:
        print('Need one input and two output file names, e.g.: ')
        print('h1b_thing infile outfile_jobs outfile_states')
    else:
        main()
