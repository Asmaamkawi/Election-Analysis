import csv
import os
#assign variable for the file to load and a path:
file_to_load=os.path.join("Resources","election_results.csv")
#assign a variable to save the file:
file_to_save=os.path.join("Analysis","election_analysis.txt")
# 1. Initialize a total vote counter
total_votes=0
#A complete list of candidates who received votes:
candidate_options=[]
#declare a dictionary to calculate total voes for each candidate:
candidate_votes={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file:
with open(file_to_load) as election_data:
     file_reader=csv.reader(election_data)
#read header row:
     headers=next(file_reader)
# Print each row in the CSV file:
     for row in file_reader:
          total_votes += 1
          candidate_name= row[2]
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
               candidate_votes[candidate_name] = 0
          candidate_votes[candidate_name] += 1
print(candidate_votes)
with open(file_to_save, "w") as txt_file:
#Calculating the Percentage of votes each candidate won:
    for candidate_name in candidate_votes:
      votes = candidate_votes[candidate_name]
      vote_percentage = float(votes) / float(total_votes) * 100
      print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")
      txt_file.write(f"{candidate_name}: received {vote_percentage:.1f}% of the vote")
     
#determine the winner of the election based on popular vote:
# 1. Determine if the votes are greater than the winning count
# Determine the percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list
    for candidate_name in candidate_votes:
     # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
     # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
     #  To do: print out each candidate's name, vote count, and percentage of
     # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
           # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
          # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
#The county with the highest turnout         
    winning_candidate_summary = (
     f"-------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

