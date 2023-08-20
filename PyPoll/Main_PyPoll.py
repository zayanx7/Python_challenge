#%%
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
Ap = os.path.join("Analysis","Results.txt")

# Create a dictionary to store candidate votes
candidate_votes = {}

# Read and process the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row

    total_votes = 0

    for row in csvreader:
        voter_id, county, candidate = row

        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


with open(Ap, 'w' )as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")

    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

# %%
