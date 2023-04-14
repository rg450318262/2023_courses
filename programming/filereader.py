def readfile(filepath, separator):
    file = open(filepath)
    #create dictionary
    columns_data = {}
    
    #read the first line
    header = file.readline()
    #strip spaces etc from start and end
    header = header .strip()

    #separate the column names in the first line to a list
    columns = header.split(separator)
    
    #add column names to the dictionary and associate them with (empty) lists
    for column in columns:
        columns_data[column] = []
        
    #take all the other lines and read them to a list
    lines = file.readlines()
    #loop through the files
    for line in lines:
        #separate the values on a line to a list
        values = line.split(separator)
        #loop through the column indices
        for i in range(len(columns)):
            column = columns[i] #we get the relevant columns name, e.g one of Year, Helsinki, Sodankyla at each loop
            #try to take value from the corresponding column as float, but if it causes an error then take as string
            try:
                value = float(values[i])
            except:
                value = values[i]
            #append value to the list associated list using the column as the key
            columns_data[column].append(value)
            
    return columns_data
