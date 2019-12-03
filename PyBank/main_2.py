import csv

total_votes = 0
unique_list = []

with open("election_data.csv", "r") as election_data:
    reader = csv.DictReader(election_data)

    
        total_votes = total_votes + 1
    

        
    print(total_votes)
    print(unique_list)

    
    