import os

input1 = input("Which 'dir' would you like to scan?\nEnter here: ")

failed = []
with os.scandir(input1 + '/') as entries1:
    for count, entry1 in enumerate(entries1, 1):

        with open(entry1, 'r') as f:

            contents = f.readlines()
            #print(contents) # in case all of the searches equal False print content to make sure that "string_search" has the correct syntax
            string_search = '*    1 12    WS-C3560CX-8PC-S          15.2(4)E6             C3560CX-UNIVERSALK9-M    \n' #This string can be replaced in case a IOS change occurs; retrieve it from show version
            oP1 = list(filter(lambda a: string_search in a, contents))
            #print(oP1) # this line will test and see if the lambda method is searching for the correct string
            if string_search in oP1:
                print(f"{count} <> {entry1.name} correct IOS installed$$$$$")
            else:
                print(f"{count} <> {entry1.name} does not have correct IOS installed!!!!!!")
                failed.append(entry1)
n = 0
for i in failed:
    print( i)
    n += 1


print(f"Total files that failed QC check: {n}")




