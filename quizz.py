import re
infile = open("Infile.txt","r") #read
outfile = open("Outfile.txt","w") #Write
infilerow = []
tablearray = []
counter = 0
tablevalue = []

for fline in infile:
    #print(fline)
    infilerow = re.split(",|\n", fline) # split the lines in the infile text using regex to split the new line and comma
    tablearray.append(infilerow)
    #print(tablearray)
    counter += 1
    #print(counter)
    #skip table columns
    if counter > 1:
        tablevalue.append(float(infilerow[2])*int(infilerow[3]))
        print(tablevalue)
        
#Writing the results to outFile
outfile.write(tablearray[0][0]+"-"+tablearray[0][1]+"-"+tablearray[0][2]+"-"+tablearray[0][3]+"-"+"Total\n")
for i in range(1,len(tablearray)):
    outfile.write(tablearray[i][0]+"-"+tablearray[i][1]+"-"+tablearray[i][2]+"-"+tablearray[i][3]+"-"+str(tablevalue[i-1])+"\n")
    
outfile.write("Items = "+str(counter-1)+"\n")
outfile.write("Total = "+str(sum(tablevalue))+" EGP\n")
infile.close()
outfile.close()
    
