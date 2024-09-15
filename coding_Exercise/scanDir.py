import os
import re

# try:
#     entries = os.listdir(input("Which 'dir' would you like to scan?\nEnter here: ") + '/')
#
#     print(entries)
#     for entry in entries:
#         print(entry)
# except:
#     print("could not be found, try again")
input1 = input("Which 'dir' would you like to scan?\nEnter here: ")

with os.scandir(input1 + '/') as entries:

    for count, entry in enumerate(entries, 1):
        print(count, entry.name)

with os.scandir(input1 + '/') as entries1:
    for count, entry1 in enumerate(entries1, 1):
        with open(entry1, 'rt') as f:
            contents = f.readlines()
            #print(contents)
            string_search = 'System image file is "flash:c3560cx-universalk9-mz.152-4.E6.bin"\n' #This string can be replaced in case a IOS change occurs; retrieve it from show version
            oP1 = list(filter(lambda a: string_search in a, contents))
            #print(oP1)
            if string_search in oP1:
                print(f"{count} <> {entry1.name} correct IOS installed$$$$$")
            else:
                print(f"{count} <> {entry1.name} does not have correct IOS installed!!!!!!")




            # pattern = re.compile(r'^System image file is "flash:c3560cx-universalk9-mz.152-4.E6.bin"')
            # matches = pattern.finditer(contents)
            # for match in matches:
            #     print(match.group(0))
            #     if 'System image file is "flash:c3560cx-universalk9-mz.152-4.E6.bin"' in match.group(0):
            #         print(f"{entry1.name} correct IOS installed$$$$$")
            #         pass
            #     else:
            #         print(f"{entry1.name} does not have correct IOS installed!!!!!!")
