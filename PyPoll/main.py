import os
import csv
#Create an array for each candidate, in which we place each voter id that supported them
Charles_arr = []
Diana_arr = []
Rayman_arr = []
#In the resources subfolder we will read all data save the header from election_data.csv
csvpath = os.path.join('./','Resources','election_data.csv')

#open and read csv
with open(csvpath,'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    #we will skip reading the header
    csv_header = next(csv_reader)
    #we will check by candidate name which array will receive the current records ballot id
    for row in csv_reader:
        if row[2] == "Charles Casper Stockham":
            Charles_arr.append(row[0])
        elif row[2] == "Diana DeGette":
            Diana_arr.append(row[0])
        else:
            Rayman_arr.append(row[0])
#We count the number of supporters for each candidate within their own array

l_count_Charles = int(len(Charles_arr))
l_count_Diana = int(len(Diana_arr))
l_count_Raymon = int(len(Rayman_arr))
l_tot_count = (l_count_Charles + l_count_Diana + l_count_Raymon)
l_pct_Charles = round(((100 * l_count_Charles) / l_tot_count),3)
l_pct_Diana = round(((100 * l_count_Diana) / l_tot_count),3)
l_pct_Raymon = round(((100 * l_count_Raymon) / l_tot_count),3)
#Make a Data Dictionary of candidates paired with their votes
results_dic = {'Charles':l_count_Charles, 'Diana':l_count_Diana, 'Raymon':l_count_Raymon}
max_key = max(results_dic, key = results_dic.get)

#We write to the terminal all polling information
print("Winner! " + max_key)

print("Election Results")
print("-----------------")
print("Total Votes: " + str(l_tot_count) )
print("-----------------")
print("Charles Casper Stockham: "  + str(l_pct_Charles) + "% ("+ str(l_count_Charles) + ")" )
print("Diana DeGette: "  + str(l_pct_Diana) + "% ("+ str(l_count_Diana) + ")" )
print("Raymon Anthony Doane: "  + str(l_pct_Raymon) + "% ("+ str(l_count_Raymon) + ")" )
print("-----------------\n")

#We will now mirror the output to the terminal with output to a txt file
output_path = os.path.join('./','analysis','FinAnalRes.txt')
with open(output_path,"w") as f:
    f.write("Election Results\n")
    f.write("-------------------------------------\n")
    f.write("Total Votes: " + str(l_tot_count) + "\n")
    f.write("-------------------------------------\n")
    f.write("Charles Casper Stockham: "  + str(l_pct_Charles) + "% ("+ str(l_count_Charles) + ")" + "\n")
    f.write("Diana DeGette: "  + str(l_pct_Diana) + "% ("+ str(l_count_Diana) + ")"  + "\n")
    f.write("Raymon Anthony Doane: "  + str(l_pct_Raymon) + "% ("+ str(l_count_Raymon) + ")" + "\n")
    f.write("-------------------------------------\n")
    f.write("Winner! " + max_key)