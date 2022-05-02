import csv

class lcsvreader:
    def __init__(self, csvfile): # The initial function of the class, which reads in a CSV file
        try:
            # Try to open the CSV file
            with open(csvfile, 'r') as csv: # Opens a file
                self.csvlines = csv.readlines() # Reads the lines from the imported file
                self.headeritems = [] # Creates a new list to store the items in the header of the CSV
                for item in self.csvlines[0].split(","):
                    # For each item in the first row of the CSV, split by commas (to seperate items)
                    self.headeritems.append(item) # Add the header item to a new header list

                self.headeritems[-1] = self.headeritems[-1].rstrip("\n") # Removes the newline from the last item in the list (as python automatically adds this, but we dont want it)
                self.csvlines.pop(0) # Pop the top row off of the CSV file as we have now stored it in a seperate list

        except FileNotFoundError:
            # Throw an error and print an error message if the file was not found
            print("File not Found")
            return 1



    def get_header(self): # A function to return the header items from the CSV file
        return(self.headeritems)



    def get_dimension(self): # returns the dimensions of the CSV file
        rows = [] # new list
        rowcount = 0
        colcount = 0
        for row in self.csvlines:
            # For each row in the csv file, increase the counter
            rowcount += 1
        for col in self.headeritems:
            # Same for each column (headeritems is the total number of columns)
            colcount += 1
        dimension = [rowcount, colcount]
        return dimension
    


    def count_instances(self, column_heading, value): # A function to count the number of occurences of a particular value, under a given heading
        counter = 0
        tempitemstore = [] # A temporary item list
        items = [] # The items to store
        for item in self.headeritems:
            # For each header item
            if item == column_heading:
                # If that header item is the one we want to count within
                index = self.headeritems.index(column_heading) # Set the index we're checking to this value
                for line in self.csvlines:
                    # For each line in the CSV file
                    tempitemstore.append(line.split(",")) # Append the entire line to a list, split by commas
                    items = tempitemstore[0]
                    if items[index] == value:
                        # If the value at the index we are checking = the value we are checking for
                        counter += 1 # Increase the counter
                    tempitemstore = [] # And reset tempitemstore for the next run
        return counter
    


    def total_missing(self): # Check the number of missing elements under a particular heading
        # This function is very similar to the above...
        tempitemstore = []
        items = []
        count = 0
        for line in self.csvlines:
            tempitemstore.append(line.split(","))
            items = tempitemstore[0]
            for thing in items:
                if thing == "NA" or thing == "?" or thing == "":
                    count += 1
                    break
            tempitemstore = []
        return count



# TEST ITEMS
csvreader = lcsvreader("python-csv-manipulation/diabetes_data.csv")
if csvreader == 1:
    print("Closing Program")
    exit

print("\nHeader Items:")
print(csvreader.get_header())

print("\nInstance Count for: Age, 40")
print(csvreader.count_instances("Age", "40"))

print("\nThe total number of missing values in the CSV file is:")
print(csvreader.total_missing())

print("\nThe dimensions of the CSV file are:")
print(csvreader.get_dimension())