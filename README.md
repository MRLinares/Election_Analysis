# Election_Analysis

## Overview

Colorado Board of Elections employee tasked me with completing election audit of recent local congressional election.  

### Data Needed:

- Total number of votes cast
- Complete list of candidates who received votes
- Complete list of counties participating
- Percentage of votes each candidate won
- Percentage of voter turnout for each county
- Total number of votes each candidate won
- Total nuber of votes placed in each county
- Winner of the election based on the popular vote
- Largest county as represented by their respective vote count

## Resources:

– Data Source: election_results.csv

– Software: Python 3.9.12, Visual Studio Code 1.70.0


### Analysis Results:


There were 369,711 total votes cast   

Three candidates:     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Charles Casper Stockham  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Diana DeGette\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Raymon Anthony Doane  
    
Three counties:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Jefferson\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Denver\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Arapahoe
    
The results were:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Stockham received 23% of the vote with 85,213 votes\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – DeGette received 73.8% of the vote with 272,892 votes\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Doane received 3.1% of the vote with 11, 606 votes
  

Making Diana DeGette the landslide victor with 73.8% of the vote (272,892 of 369,711)
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Jefferson county had 10.5% of the total voter turnout with 38,855 voters\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Denver county had 82.8% of the total voter turnout with 306,055 voters\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; – Arapahoe county had 6.7% of the total voter turnout with 24,801 voters
  
Making Denver county the largest representation out of the participating counties.

## Audit Summary

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     Given that the algorithm is able to process over a million data points (Ballot ID, County info, and Candidate info) in fractions of a second, I am confident this program can handle future elections within the state of Colorado and beyond.  With just a few adjustments in the code, I know that this algorithm can handle scale.  With files containing comma separated values (CSV), such as the list provided with the election data, my algorithm can grab information from any column on a spreadsheet and tally up quantity. 

![Screen Shot 2022-08-11 at 11 49 06 PM](https://user-images.githubusercontent.com/108758105/184281702-9cefbbf0-4c1b-4f84-b6ee-83541f1ab9e2.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     The code above, for example, shows how I begin to iterate through rows of data to extract information from a csv file; from a simple digit and variable change, I can extract from an entirely new list of information.  Because the code iterates through each row with values, it can scale up with larger districts, states and even the nation.



![Screen Shot 2022-08-11 at 11 56 05 PM](https://user-images.githubusercontent.com/108758105/184282375-4ee1278f-0efb-437a-8552-0f426525c3b2.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     This code, above, shows how a single formula can be applied to a loop so that a percentage of total votes can be attributeed to a single variable.  This code in particular calculates the percentage of votes for the county.


![Screen Shot 2022-08-12 at 12 18 44 AM](https://user-images.githubusercontent.com/108758105/184284346-2d2375e7-8bc8-41ea-ad9d-b3283dbfd9ef.png)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      Creating empty "dictionaries", or variables that contain key-value relationships (just like standard dictionaries with words and definitions), as indicated by the empty brackets, allows for flexibility in scaling.  If I had designed the program with tuples(lists that cannot be changed) I would limit the program to its current capacity.  Having the empty dictionary, however, allows for added future capacity if need be.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     Also, this code can open a csv file, and with the commands I built in, can write the needed information to any assigned text file using commands such as the one pictured below.  During an election, votes can continue to be processed and added to the csv file and this code can update the text file everytime it you run it.  A future software update will allow this code to update the results file in real-time as votes come in, essentially allowing this program to become both a live vote counter and auditing software.

![Screen Shot 2022-08-11 at 11 59 54 PM](https://user-images.githubusercontent.com/108758105/184282748-91266d98-903a-4459-a3ab-36de0ab00625.png)

