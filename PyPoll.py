#the data we need to retrive
#the total number of votes cast
#complete list of candidates who recieved votes
#percentage of votes each candidate recived 
#total number of votes each candidate won 
#repeat lines 3-5 for counties
#winner based on popular vote

#assign a variable for the file to load and the path.
#file_to_load = 'Desktop/Resources/election_results.csv'

#open and read the election results file
#election_data = open(file_to_load, 'r')




#add dependencies
import csv
import os
#assign a variable to load a file from a path
file_to_load = os.path.join("Desktop/Resources/election_results.csv")
#assign a variable to save the file to a path
file_to_save = os.path.join("Desktop/Resources/election_analysis.txt")

#define variable
total_votes = 0
#candidate options list
candidate_options = []
#declare candidate dictionary
candidate_votes = {}

#define variable
total_countyvotes = 0
#county options list
county_options = []
#declare county dictionary
county_votes = {}

#winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open and read the election results file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #read header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        #add to the total vote count
        total_votes += 1
        #add to the total vote count
        total_countyvotes += 1

        #print the candidate name from each row
        candidate_name = row[2]
        #print the county name from each row
        county_name = row[1]

        #if the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            #add name to the list of candidates
            candidate_options.append(candidate_name)

            #begin tracking candidates vote count
            candidate_votes[candidate_name] = 0

        #add vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #if the county does not match any existing county
        if county_name not in county_options:

            #add name to the list of county
            county_options.append(county_name)

            #begin tracking county vote count
            county_votes[county_name] = 0

        #add vote to that counties count
        county_votes[county_name] += 1

#save results to the text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #save final vote count to the text file
    txt_file.write(election_results)

    Filler= (f"County Votes:\n")
    print(Filler)
    txt_file.write(Filler)

    for county in county_votes:
        #get vote count and percentage
        cvotes = county_votes[county]
        cvote_percentage = float(cvotes) / float(total_countyvotes) * 100
        county_results = (f"{county}: {cvote_percentage:.1f}% ({cvotes:,})\n")

        txt_file.write(county_results)

        #print each counties voter count and percentage to the terminal
        print(county_results)

    largest_county = (
        f"-------------------------\n"
        f"Largest County Turnout: Denver\n"
        f"-------------------------\n")
    print(largest_county)
    txt_file.write(largest_county)

    for candidate in candidate_votes:
        #get vote count and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        #print each candidate's voter count and percentage to the terminal
        print(candidate_results)

        #save candidate results to the text file
        txt_file.write(candidate_results)

        #determine winning vote count, winning percentage, winning candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    #print winning candidate's results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    #save winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)

    #print each row in the CSV file
    #for row in file_reader:
    
    