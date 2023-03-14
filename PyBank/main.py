import os
import csv

rindex = 0
months_arr = []
profloss_arr = []
diff_list = []
#in the resources subfolder we will read all data save the header from budget_data.csv
csvpath = os.path.join('./','Resources','budget_data.csv')

#open and read csv
with open(csvpath,'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csv_reader)

    for row in csv_reader:
# I am loading from each row of the spreadsheet an element to each arr months and profloss
        months_arr.append(row[0])
        profloss_arr.append(int(row[1]))
        rindex +=1

#I define a function to compare neighbouring elements within an array 
def elements_difference(nums):
    result = [j-i for i, j in zip(nums[:-1], nums[1:])]
    return result


print("Financial Analysis")
print("-------------------------------------")

num_mths = len(months_arr)
print("Total Months: " + str(len(months_arr)))

#I calculate a grand sum of each element in the profloss array
l_hold = sum(int(i) for i in profloss_arr)
print("Total $" + str(l_hold))

 
# Calculating difference list
diff_list = elements_difference(profloss_arr)
#The diff_list contains one less element than the profloss_arr
#It contains the difference between each neighbouring element of profloss_arr
#We step through and sum each element in this array
m_hold = sum(int(j) for j in diff_list)
l_avchg = m_hold / (len(diff_list))
print("Average Change: $" + str(round(l_avchg,2)))
int_len = int(len(diff_list))
#Having a diff_list means we can walk through the list to see max and min value
#First we set the max and min as that of the first element in the list
max = diff_list[0]
min = diff_list[0]

#We now loop through the diff list to see if we get a larger value 
# than the largest seen so far and for a value smaller than that seen before
#Remember that the diff list has one less element than the month list 
# so they are out of phase by one element
for x in range(int_len):
    if diff_list[x] > max:
        max = diff_list[x]
        l_month = months_arr[x + 1]
    if diff_list[x] < min:
        min = diff_list[x]
        ll_month = months_arr[x + 1]    
print("Greatest Increase in Profits: " + str(l_month) +  " (" + str(max) + ")")
print("Greatest Decrease in Profits: " + str(ll_month) + " (" + str(min) + ")")
#We will now mirror the output to the terminal with output to a txt file
output_path = os.path.join('./','analysis','FinAnalRes.txt')
with open(output_path,"w") as f:
    f.write("Financial Analysis\n")
    f.write("-------------------------------------\n")
    f.write("Total Months: " + str(len(months_arr)) + "\n")
    f.write("Total $" + str(l_hold) + "\n")
    f.write("Average Change: $" + str(round(l_avchg,2)) + "\n")
    f.write("Greatest Increase in Profits: " + str(l_month) +  " (" + str(max) + ")" + "\n")
    f.write("Greatest Decrease in Profits: " + str(ll_month) + " (" + str(min) + ")" + "\n")
