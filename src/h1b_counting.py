import sys

from get_var_indices import get_var_indices
from count_vars import  count_vars
from sort_dict import sort_dict

def main():
    in_filename = sys.argv[1]
    outfile_jobs = sys.argv[2]
    outfile_states = sys.argv[3]

    # Set of strings (case-insensitive) that identify the 
    # variables we want in the input-file column headers.
    var_descriptors = [['work','state'],['soc_name'],['status']]

    # Open the input file for reading.
    with open(in_filename,'r') as f:
        header = f.readline()

        # Identify columns containing the desired variables.
        (state_ind, soc_ind, status_ind) = get_var_indices(header, var_descriptors)

        # Count certifications by state and by job soc_name.
        [byState, bySOC], TotCert = count_vars( f, [state_ind, soc_ind], status_ind,'certified')

    # Sort by count and alphabetically.
    states_sorted = sort_dict( byState )
    soc_sorted = sort_dict( bySOC )

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
    if len(sys.argv) < 4:
        print('Too few arguments:')
        print('h1b_counting <input_filepath> <output_jobs_filepath> <output_states_filepath>')
    else:
        main()
