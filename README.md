# insight_data_engineering

Problem

We wish to summarize statistics on successful H1B Visa applications using data from the US Department of Labor and the Office of Foreign Labor Certification Performance Data. In particular, we want to find what occupations have the most success in achieving H1B certification and what states most of the successful H1B applicants go to work in.

The format of the data files changes from year to year, as do the number of columns and the header-strings. Data are published as a .xlsx (Excel) file, but for this problem, we will be using a text file with columns delimited by a semicolon. 

The problem is to write a routine that will extract the appropriate columns (occupations and states for which visas were Certified) from the .csv file, count and return the number and fraction of certified visa applications as a function of occupation (soc_name) and state. 



Approach

I coded in Python 3. I broke the problem into three steps: 
1. Finding the columns containing 'STATUS','WORK_STATE', and 'SOC_NAME'
   The 2014 data tagged 'WORK_STATE' as 'LCA_CASE_WORKLOC1_STATE' -- simply searching for 'WORK_STATE' wouldn't find the correct column,
   so I made a routine (get_var_indices) to parse the header information in the first line of the csv file looking for column headers containing 
   both 'WORK' and 'STATE', or more generally, that finds column headers that contain all of the strings in a list that describe the variable. 
   The function returns the indices of the columns corresponding to the variable_descriptions passed in.
    --- Some years allowed multiple work_states. I only considered the first listed -- this could be changed, but we'd need to decidehow to 
        count one Certified visa that will work in 2 or more states.

2. Counting occurrences of each job (soc_name) and state where an application had STATUS = 'Certified'.
   Normally, I might use a collections.Counter object here; but instead I stored counts in a dictionary.
   For each line in the file, if the application was successful, I incremented the count of total Certified applications 
   and also incremented the count in the dictionary corresponding to soc_name or state. 

3. Sorting the dictionaries by count and alphabetically to get the list of top 10 states and top 10 occupations.
   To get the appropriate order,  I used a lambda function to sort the dictionary items in order of [-1 * count, name of state or occupation].


Run instructions

To run, execute the run.sh script. From the h1b_statistics/ directory: 
$bash ./run.sh

To change the input or output filenames, modify line 3 of run.sh, to fill in the filepaths.
$python3 <input_filepath> <output_jobs_filepath> <output_states_filepath>
