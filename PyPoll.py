# - The data we need to retrieve
# - 1.  The total number of votes cast
# - 2.  A complete list of candidates who received votes
# - 3.  The percentage of votes each candidate won
# - 4.  The total number of votes each candidate won
# - 5.  The winner of the election based on the popular vote

import csv

import os

# file to load
file_to_load = os.path.join('Resources', 'election_results.csv')

# file to save 
election_analysis = os.path.join('Analysis', 'election_analysis.txt')


# 1. initialize accumulator variable (or total vote counter)

total_votes = 0

# declaring  a list to retrieve candidate info 

candidate_options = []

# declare an empty dictionary in order to tie {key: value} for candidates and their respective votes

candidate_votes = {}

# Winning Candidate and Count Tracker

    # 1. declare a variable that holds an empty string value for the winning cadidate:

winning_candidate = ""

    # 2. declare a variable for the "winning count" equal to zero:

winning_count = 0

    # 3. declare a variable for the "winning_percentage" equal to zero:

winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:

# To do: read and analyze the data here  (to add later: ----- , delimiter=',' ------)
        election_reader = csv.reader(election_data)

    # Print the header row.

        headers = next(election_reader)
        # print(headers)

# Print each row in the CSV file:

        for row in election_reader:

            # 2. Add the total vote count:

            total_votes += 1 

            # print(row)
            # #  print(row[0]) would give just the first item


            # Print the candidate name from each row:

            candidate_name = row[2]

            # If the candidate does not match any existing candidate...
            if candidate_name not in candidate_options:

                #  1.   Then add the unique candidate name to the candidate list:

                candidate_options.append(candidate_name)

                #  2.   Begin tracking that candidate's vote count by initializing to 0:

                candidate_votes[candidate_name] = 0

                # 3.    Begin tallying votes:

            candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts
# 1.    Iterate through the candidate list

for candidate_name in candidate_votes:

    # 2.    Retrieve vote count of a candidate

    votes = candidate_votes[candidate_name]

    # 3.    Calculate the percentage of the vote count:

    vote_percentage = float(votes)/float(total_votes)*100

    # 4.    Print the candidate name , vote count, and % of votes:

    print(f'\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

# 5.    Determine winning count and candidate:

    # a)    Determine if the votes is greater than the winning count:

    if (votes > winning_count) and (vote_percentage > winning_percentage):

        #  If true, then set winning_count = votes and Winning % = vote %

        winning_count = votes

        winning_percentage = vote_percentage

        #  And, set the winning_candidate = candidate's name

        winning_candidate = candidate_name

#  Print the winning candidate, vote count and percentage
winning_candidate_summary = (
    f"----------------------------\n\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n\n"
    f"----------------------------\n")

print(winning_candidate_summary)




# # Print candidate list: (next bullet)
# print(candidate_options)

# # Update to print candidate vote dictionary
# print(candidate_votes)

# # 3. Print the total votes.

# print(total_votes)

# To do: perform analysis.
    #  print(election_reader)

# election_analysis = os.path.join('Analysis', 'election_analysis.txt')
# outfile = open(election_data, "w")
# outfile.write("Hello World")
# outfile.close()

with open(election_analysis, "w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
   