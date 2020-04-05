# note: this is a quick and dirty program written to extrapolate from official coronavirus numbers to actual infection rates, assuming a 14 to 16 day delay from infection to symptoms showing, getting serious, and getting to the hospital to be tested (plus testing delays)

# import modules
import csv

# define function
def extrapolate_cases(file):
    # open and read the files, create Header Row for export .csv
    import_file = open(file)
    entry = csv.reader(import_file)

    export_file_name = "extrapolated.csv"
    export_file = open(export_file_name, 'a+')
    export_file.write('state,day 0,population,official cases,current doubling,extrapolated cases,extrapolated + possible asymptomatic cases,percent infected\n')

    i = 0

    # import entities_str column
    for line in entry:
        # ignore header row
        if i == 0:
            print("ignoring header row")
            i = i+1
            continue
        else:
            #print(i)
            # read line and write values back to export file 
            state = line[0]
            date = line[1]
            population = line[2]
            official_today = 0
        
            j = 1
            line_length = len(line)
            #print(line_length)
            while j < line_length:
                #print(line[line_length - j])
                try:
                    if int(line[line_length - j]) > 0:
                        official_today = line[line_length-j]
                        break
                except:
                    j = j + 1
                    #print(j)            
    
            export_file.write(state + "," + date + "," + population + "," + str(official_today) + ",")
    
            # calculate current doubling rate
            current_doubling = 0
            k = 0
    
            while j < line_length:
                #print("official today: " + str(official_today))
                #print("earlier rate: " + str(line[line_length-j]))
                #print("j = " + str(j))
                #print("k = " + str(k))
                if int(official_today) / int(line[line_length-j]) > 1.9:
                    current_doubling = k
                    print(state + " has a current doubling of " + str(k))
                    break
                else:
                    j = j + 1
                    k = k + 1
    
            export_file.write(str(current_doubling) + ",")
    
            # use current doubling rate to estimate actual infections
            extrapolated_today = official_today
    
            if current_doubling == 1:
                extrapolated_today = int(official_today)*(2^14)
            elif current_doubling == 2:
                extrapolated_today = int(official_today)*(2^7)
            elif current_doubling == 3:
                extrapolated_today = int(official_today)*(2*5)
            elif current_doubling == 4:
                extrapolated_today = int(official_today)*(2^4)
            elif current_doubling == 5:
                extrapolated_today = int(official_today)*(2*3)
            else:
                extrapolated_today = int(official_today)*2
    
            export_file.write(str(extrapolated_today) + "," + str(extrapolated_today*1.25) + "," + str((extrapolated_today*1.25*100)/int(population)) + "\n")   

    # close files
    import_file.close()
    export_file.close()
    
# end function definition

#begin program
file_name = input("What is the name of the CSV file (including .csv)? ")
extrapolate_cases(file_name)

# end program