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

## Results

Analysis of the election show:

– There were 369,711 total votes cast   

Three candidates:     
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Charles Casper Stockham  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Diana DeGette\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Raymon Anthony Doane  
    
Three counties:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jefferson\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Denver\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Arapahoe
    
The results were:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Stockham received 23% of the vote with 85,213 votes\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DeGette received 73.8% of the vote with 272,892 votes\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Doane received 3.1% of the vote with 11, 606 votes
  

Making Diana DeGette the landslide victor with 73.8% of the vote (272,892 of 369,711)
  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Jefferson county had 10.5% of the total voter turnout with 38,855 voters\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Denver county had 82.8% of the total voter turnout with 306,055 voters\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Arapahoe county had 6.7% of the total voter turnout with 24,801 voters
  
Making Denver county the largest representation out of the participating counties.

## Summary

Given that the algorithm is able to process over a million data points (Ballot ID, County info, and Candidate info) in fractions of a second, I am confident this program can handle future elections within the state of Colorado and beyond.  With just a few adjustments in the code, I know that this algorithm can handle scale.  

With files containing comma separated values, such as the list provided with the election data, my algorithm can grab information from any column on a spreadsheet and tally up quantity. 
