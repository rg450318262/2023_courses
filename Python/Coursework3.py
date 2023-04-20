# %% [markdown]
# 1. Weighted sum (2 points)
# Write a function that calculates the weighted sum of two lists. The function should receive two lists as arguments, one that contains the values and other one that contains their weights. It should return the sum of the weighted values (weight*value).
# 
# I.e. the weighted sum of values [5, 2, 4] and weights [2, 1, 2] would be 5*2 + 2*1 + 4*2 = 20

# %%
def wsum(value_list, weight_list):
    weighted_sum = 0
    for i in range(len(value_list)):
        weighted_sum += value_list[i] * weight_list[i]
    return weighted_sum

# check if the function works
list1 = [1,2,3]
list2 = [2,3,4]
wsum(list1, list2)

# %% [markdown]
# 2. Rescaling values (2 points)
# Write a function, that rescales a list of values so that their total sum is 1.
# 
# Hint: Divide each value with the total sum of all values. You can either do it with a for-loop or with the help of numpy.
# 
# For example, if your function is called "rescale_values",  it should work like below:

# %%
# numpy solution
import numpy as np
def rescale_to_one(mylist):
    array = np.array(mylist)
    total_sum = np.sum(mylist)
    rescale_value = array/total_sum
    return rescale_value

#check if it works
mylist = [1,1,1,2]
rescale_to_one(mylist)

# %%
# loop solution
def rescale_to_one_v2(mylist):
    rescale_value_list = list()
    sum_list = 0
    for i in range(len(mylist)):
        sum_list += mylist[i]
    for j in range(len(mylist)):
        rescale_value = mylist[j]/sum_list
        rescale_value_list.append(rescale_value)
    return rescale_value_list

#check if it works
mylist = [1,1,1,2]
rescale_to_one_v2(mylist)
    

# %% [markdown]
# 3. Weighted mean (2 points)
# Write a function that calculates the weighted arithmetic mean of two lists. Weighted arithmetic mean is a weighted sum, where the sum of the weights is 1. Use the functions in exercise 1 and 2 in your solution.
# 
# Check. http://en.wikipedia.org/wiki/Weighted_arithmetic_mean

# %%
def wmean(list1, list2):
    average_list = [np.average(list1), np.average(list2)]
    count_list = [len(list1), len(list2)]
    weight_list = rescale_to_one_v2(count_list)
    weighted_sum = wsum(average_list, weight_list)
    print("The weighted mean of", list1, "and", list2, "is", weighted_sum)
    
    
#check if it works
#This is the example from wikipedia (the correct answer should be 86)
Morning_class = [62, 67, 71, 74, 76, 77, 78, 79, 79, 80, 80, 81, 81, 82, 83, 84, 86, 89, 93, 98]
Afternoon_class = [81, 82, 83, 84, 85, 86, 87, 87, 88, 88, 89, 89, 89, 90, 90, 90, 90, 91, 91, 91, 92, 92, 93, 93, 94, 95, 96, 97, 98, 99]

wmean(Morning_class, Afternoon_class)

# %% [markdown]
# 4. Calculating sample standard deviation (2 points)
# Write a function, that calculates the sample standard deviation of a list of values.
# 
# Hint: Remember that in Python the operator for exponentiation is **, so for example 2**2 == 4 and so on. Square root is the same as raising a number to one-half power, so 4**0.5==2.0. In case your not familiar with it, the required formula can be found here, and also you can ask for help during the exercise group.

# %%
def sample_sd(mylist):
    array = np.array(mylist)
    mean = np.average(array)
    squared_diff = np.subtract(mean, array)**2
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/(len(mylist)-1)
    sd = variance**0.5
    values = [str(x) for x in mylist]
    print("The sample standard deviation of", ','.join(values), "is", sd)

#Check if it works(the sample sd of 1,2,3 is 1)
mylist = [1,2,3]
sample_sd(mylist)

# %% [markdown]
# 5. Student debt (2 points)
# Download a time-series of the number of student debtors and the total amount of student debt between years 2002–2014. Plot the amounts of student debtors as a line plot, so that the x-axis will display the year and y-axis will display the number of debtors. Do a separate plot with the total amount of student debt on the y-axis. Finally, do a a third plot where you have the average amount of debt per debtor for each year.
# 
# Hint: If you are using the split function, you can use "\t" as the separator to split by tab (you can also just leave the separator empty to split by any whitespace, i.e. "1 2 3".split() → ['1', '2', '3']). You can use the code from the lectures to read the file. 

# %%
import pandas as pd
data_debator = pd.read_csv("data/student_debtors.txt", sep="	")
data_debt = pd.read_csv("data/student_debt.txt", sep="	")
mydata = pd.merge(data_debator, data_debt)
print(mydata)

# %%
import matplotlib.pyplot as plt
plt.plot(
    "Year", 
    "StudentDebtors", 
    data = mydata
    )
plt.title("Figure 1. Amounts of student debtors, 2002 to 2014")
plt.xlabel('Year')
plt.ylabel('Number of debtors')

# %%
plt.plot("Year", "StudentDebt", data = mydata)
plt.title("Figure 2. Amount of student debt, 2002 to 2014")
plt.xlabel('Year')
plt.ylabel('Amount of student debt (billion)')

# %%
mydata["Average"] = mydata["StudentDebt"]/mydata["StudentDebtors"]
plt.plot(
    "Year", 
    "Average", 
    data = mydata
    )
plt.title("Figure 3. Average amount of student debt per debtor, 2002 to 2014")
plt.xlabel('Year')
plt.ylabel('Average amount of student debt')

# %% [markdown]
# 6. Frequency of characters (3 points)
# Write a program that reads all text from a file into a string and counts how many times each character appears in the file. Include only lower-case characters (hint: str.islower()).
# 
# Investigate, how many times the letters a, b and c appear in hamlet. Draw a bar chart (you can look for examples here) of the letter frequencies (ie. how many times the letters appear). 
# 
# Hint: Implement the program using a dictionary with the letters as keys and their number of occurrences as values. You can loop through the letters in a string/text with a normal for loop. Instead of just a,b,c, you can alternatively also plot the frequencies of all the alphabet letters for an extra challenge (not required for full 3 points however). 

# %%
def count_lowercase_characters(filename):
    character_counts = {}  
    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                if char.islower():
                    if char in character_counts:
                        character_counts[char] += 1
                    else:
                        character_counts[char] = 1
    
    return character_counts

# counts how many times each character appears in hamlet
mydict = count_lowercase_characters("data/hamlet.txt")
for char, count in mydict.items():
    print(f"Character '{char}' appears {count} times.")

# %%
#Investigate, how many times the letters a, b and c appear in hamlet
mydict = count_lowercase_characters("data/hamlet.txt")
keys = ["a", "b", "c"]

for key in keys:
    print(f"Character '{key}' has an occurence of {mydict.get(key)}")

# %%
# frequency of a, b, c
values = list(mydict.get(k) for k in ('a', 'b', 'c'))
plt.bar(keys, values)
plt.title("Figure 4. Frequency of Characters 'a', 'b' and 'c' in Hamlet" )
plt.xlabel("Characters")
plt.ylabel("Frequency")

# %%
#frequncy of all letters
mydict_sort = sorted(
    mydict.items(), 
    key=lambda x:x[1], 
    reverse=True
    )

mydict_sort = dict(mydict_sort)
keys = list(mydict_sort)
values = list(mydict_sort.values())

plt.bar(keys, values)
plt.title("Figure 5. Frequency of All Characters in Hamlet" )
plt.xlabel("Characters")
plt.ylabel("Frequency")

# %% [markdown]
# 7. Visualizing volumes and densities (2 points)
# Once again, we meet the physical functions that we used in the last exercises. This time, your task is to inspect their behavior with by plotting their results. Visualize how the cube volume and density changes when the mass of the cube is 5 and the length of its side increases linearly from 1 to a 100. Plot the volume and density values to separate figures. What does the data look like? Is the change linear with respect to the length?
# 
# Hint: First create a variable to describe the mass of our cube and a list containing integers from 1 to 100. Run the functions with these values and save the results. 

# %%
def volume(length):
    return length ** 3
  
def density(mass, length):
    v = volume(length)
    d = 1.0 * mass / v
    return d

# %%
#create a variable to describe the mass of our cube and a list containing integers from 1 to 100. 
cube_mass = 5
cube_len = list(range(1,101))
#run the functions with these values and save the results. 
vol_dict = dict((k, volume(k)) for k in cube_len)
den_dict = dict((k, density(5, k)) for k in cube_len)
lengths = list(vol_dict.keys())
volumes = list(vol_dict.values())
densities = list(den_dict.values())

# %%
#change of volumes with length increasing from 1 to 100
plt.plot(
    lengths, 
    volumes
    )

plt.title(
    "Figure 6. Changes of volumes with length increasing from 1 to 100", 
    pad = "20.0"
    )
plt.xlabel("Lengths")
plt.ylabel("Volumes")

# %%
#change of densities with length increasing from 1 to 100
plt.plot(
    lengths, 
    densities
    )

plt.title(
    "Figure 7. Changes of densities with length increasing from 1 to 100", 
    pad = "5.0"
    )
plt.xlabel("Lengths")
plt.ylabel("densities")

# %%
# What does the data look like? Is the change linear with respect to the length?
# The relationship between length and volume is not linear, but exponential. See figure 6
# The relationship between length and density is not liner, but is close to Michaelis-Menten equation. See figure 7.


# %% [markdown]
# 8. Numpy-arrays (2 points)
# Make a numpy-array out of the list [4, 0, 0, 4, 2.5]
# 
# Do all of the following without any loops:
# 
# a) Multiply all elements of the array by two and attach this new array to a new variable.
# 
# b) Print out the last four elements of this new array.
# 
# c) Scale the values of the array, so that their sum is 1.

# %%
#create a numpy array
mylist = [4,0,0,4,2.5]
array = np.array(mylist)
#tasks
## Multiply all elements of the array by two and attach this new array to a new variable.
new_array = array *2
## Print out the last four elements of this new array.
alist = list(new_array[-4:])
newlist = map(str, alist)
print(f"The last four elements are: {', '.join(newlist)}")
# Scale the values of the array, so that their sum is 1.
scaled = map(str,list(np.around(new_array/np.sum(new_array), 3)))
print(f"The scaled values of the array are {', '.join(scaled)}")

# %% [markdown]
# 9. Visualizing gaze data (3 points)
# In order to study the gaze behavior of moving subjects, we have decided to visualize drivers' eye movement. To do this, save a data file that contains driving and eye-movement data from two test subjects. The data has been collected while driving on a section of about fifty meters on a steady curve. Your task is to draw a figure where the horizontal eye movements of each driver are plotted in respect to the distance traveled.
# 
# If you open the file using a spreadsheet program for example, you will notice that there are quite a few columns (gps, speed etc). However, in our program, we need only three of them:
# 
# g_heading: Driver's horizontal gaze positions (in radians).
# 
# dist: Traveled total distance in meters.
# 
# session_id: Subjet's ID number.
# 
# First read the data into a form you can process and find the columns that we need. Separate the two subjects by their ID-numbers (hint: the id numbers are 2011080101 and 2011080302) and draw a figure where you have the traveled distance on x-axis and horizontal eye-movements on the y-axis.  The end result should look something like this.

# %%
#read the data
gaze = pd.read_csv("data/driving_data.csv", sep = ";")
gaze

# %%
#separate the two subjects by ID
gaze1 = gaze.loc[gaze['session_id'] == 2011080101]
gaze2 = gaze.loc[gaze['session_id'] == 2011080302]


# %%
# draw the figure
plt.figure(figsize=(16,6))
plt.plot(gaze1["dist"], gaze1["g_heading"], label = "ID: 2011080101")
plt.plot(gaze2["dist"], gaze2["g_heading"], label = "ID: 2011080302")
plt.legend()
plt.title("Figure 8. Change of horizontal eye movements with the distance traveled for two participants")
plt.xlabel("Distance (meters)")
plt.ylabel("Horizontal gaze positions (radians)")

# %% [markdown]
# Bonus
# B1. Preliminary cryptanalysis (2 points)
# We have received a hint that an encrypted text found from the possession of the radical neobehavioristic resistance movement is in fact an article by B.F. Skinner.  Demonstrate this, by showing that the frequency distribution of lower case letters are the same in both texts (i.e. the number of all letters is the same in both texts ). Use the program you wrote in exercise 6 to inspect the frequency of the letters.
# 
# Check http://en.wikipedia.org/wiki/Frequency_analysis

# %%
encr_txt_dict = count_lowercase_characters("data/crypttext1.txt")
article_dict = count_lowercase_characters("data/superstition_in_the_pigeon.txt")

# %%
# plot them side by side in alphabetical order
plt.figure(figsize=(10,5))
#frequncy of all letters fot the encrypted text
encr_txt_dict_sort = sorted(
    encr_txt_dict.items(), 
    key=lambda x:x[0], 
    reverse=True
    )

encr_txt_dict_sort = dict(encr_txt_dict_sort)
keys_txt = list(encr_txt_dict_sort)
values_txt = list(encr_txt_dict_sort.values())

#frequncy of all letters fot the article text
article_dict_sort = sorted(
    article_dict.items(), 
    key=lambda x:x[0], 
    reverse=True
    )

article_dict_sort = dict(article_dict_sort)
keys_article = list(article_dict_sort)
values_article = list(article_dict_sort.values())

# plot 
fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle('Figure 9. Comparing number of characters betwen encrypted text and the article')
ax1.barh(keys_txt, values_txt)
ax1.set_title("(a)Encrypted text")
bar1 = ax1.barh(keys_txt, values_txt)
ax1.bar_label(bar1)
ax1.set_xlim(0,1800)

ax2.barh(keys_article, values_article, color = "blue")
ax2.set_title("(b)Article text")
bar2 = ax2.barh(keys_article, values_article)
ax2.bar_label(bar2)
ax2.set_xlim(0,1800)
fig.tight_layout()

# %%
# Yes, each character has same frequency across two texts. They are the same.

# %% [markdown]
# B2. More advanced cryptanalysis (2 points)
# The same radical terrorist organization has been found to posses another encrypted text . It is suspected of being the same B.F. Skinner's article, but with better encryption! Encryption is suspected to be based on character replacement. Demonstrate this by printing the number of occurrences in both texts for both of the three most popular and the three rarest characters.
# 
# Hint: To get the values of a dictionary as a list, use the dict.values() method.

# %%
# read new encrypted text
encr_txt_dict = count_lowercase_characters("data/ciphertext2.txt")

# %%
# plot them side by side in descending order of the value
plt.figure(figsize=(10,5))
#frequncy of all letters fot the encrypted text
encr_txt_dict_sort = sorted(
    encr_txt_dict.items(), 
    key=lambda x:x[1], 
    #reverse=True
    )

encr_txt_dict_sort = dict(encr_txt_dict_sort)
keys_txt = [list(encr_txt_dict_sort)[k] for k in [0,1,2,-1,-2,-3]]
values_txt = [list(encr_txt_dict_sort.values())[k]  for k in [0,1,2,-1,-2,-3]]

#frequncy of all letters fot the article text
article_dict_sort = sorted(
    article_dict.items(), 
    key=lambda x:x[1], 
    #reverse=True
    )

article_dict_sort = dict(article_dict_sort)
keys_article = [list(article_dict_sort)[k] for k in [0,1,2,-1,-2,-3]]
values_article = [list(article_dict_sort.values())[k] for k in [0,1,2,-1,-2,-3]]

# plot 
fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle('Figure 9. Comparing number of characters betwen encrypted text and the article')
ax1.barh(keys_txt, values_txt)
ax1.set_title("(a)Encrypted text to decipher")
bar1 = ax1.barh(keys_txt, values_txt)
ax1.bar_label(bar1)
ax1.set_xlim(0,1800)

ax2.barh(keys_article, values_article, color = "blue")
ax2.set_title("(b)Article text")
bar2 = ax2.barh(keys_article, values_article)
ax2.bar_label(bar2)
ax2.set_xlim(0,1800)
fig.tight_layout()

# %%
# Yes, each character in encrypted text can find a corresponding character in the article with exact same frequency

# %%


# %%


# %%



