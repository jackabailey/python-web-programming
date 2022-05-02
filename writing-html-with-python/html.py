import csv
# create a new file called index.html
with open("requiredfiles/index.html","w") as html:
	# write the boilerplate html stuff
	html.write("<html>\n")
	html.write("<head>\n")
	html.write("<meta charset=\"UTF-8\">\n")
	html.write("<style>\n")
	html.write("table, th, td {\n")
	html.write("border: 1px solid black;\n")
	html.write("border-collapse: collapse;\n")
	html.write("}\n")
	html.write("</style>\n")
	html.write("<title>Student grades</title>\n")
	html.write("</head>\n")
	html.write("<body>\n")
	html.write("<h2>Test scores</h2>\n")
	html.write("<table>\n")
	
	# open a csv file to read data from
	with open("requiredfiles/scores.csv","r") as students:
		students.readline()
		# format the table header 
		html.write("<tr>\n")
		html.write("<th> First name</th>\n")	
		html.write("<th> Surname</th>\n")
		html.write("<th> Maths score</th>\n")
		html.write("<th> English score</th>\n")
		html.write("<th>Average</th>\n")
		html.write("</tr>\n")
 
		reader = csv.reader(students)
		
		# iterate over the lines in the file printing out formatted html
		for row in reader:
			html.write("<tr>\n")
			for elm in row:
				html.write("<td>"+ elm + "</td>\n")
			math_score = int(row[2])
			english_score = int(row[3])
			html.write("<td>"+ str((math_score + english_score)/2) + "</td>\n")
			html.write("</tr>\n")
	
	# close all the opened html tags
	html.write("</table>\n")
	html.write("</body>\n")
	html.write("</html>\n")