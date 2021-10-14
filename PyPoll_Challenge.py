# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Create lists of candidates, counties, and total votes
total_votes = 0
candidate_options = []
candidate_votes = {}

countyList = []
countyVotes = {}

# Track the winning candidate/county, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

winningCounty = ""
winning_CountyCount = 0

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        total_votes = total_votes + 1; candidate_name = row[2]; countyName = row[1]

        #Updates candidate names and number of votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name); candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        #Updates county names and number of votes
        if countyName not in countyList:
            countyList.append(countyName); countyVotes[countyName] = 0
        countyVotes[countyName] +=1

with open(file_to_save, "w") as txt_file:
    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    txt_file.write(election_results)

    #prints county votes to terminal, and writes to .txt file
    for county in countyVotes:
        votes = countyVotes.get(county)
        votePercentage = float(votes) / float(total_votes)*100
        countyResults = (
            f"{county}: {votePercentage:.1f}% ({votes:,})\n")
        print(countyResults)
        txt_file.write(countyResults)

        #Determines county with the highest vote turnout
        if (votes > winning_CountyCount) and (votePercentage> winning_percentage):
            winning_CountyCount = votes
            winning_county = county

    winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    print(winning_county_summary)

    # Save winning_county_summary to .txt file
    txt_file.write(winning_county_summary)

    # prints candidate votes to terminal, and writes to .txt file
    for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save winning_candidate_summary to .txt file
    txt_file.write(winning_candidate_summary)
