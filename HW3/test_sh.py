import sys
import re

if __name__ == "__main__":
    file_name_list = sys.argv[1:]                                           #taking input files from command line

    for file_name in file_name_list:                                        #iterating over all the files
        with open(file_name, "r", encoding="utf8") as f:
            lines = f.read()
            lines = re.sub(u'[\u201c\u201d]', '"', lines)
            #lines = re.sub(r'(?=(\n.?"[^"]+\n\n))',r'\1"',lines)           #this is not working for some reason
            haha = re.findall(r'(?=(\n.?"[^"]+\n\n))',lines)
            print(haha)
            out1 = re.findall(r'(".*?")', lines, re.DOTALL)                 #extracting each dialogue
            for k in range(len(out1)):
                out1[k] = re.sub(r'\n\s*', ' ', out1[k])                    #removing unnecessary new lines and spaces
        f.close()
        #print(out1)
        with open(file_name.strip('.txt') + "_dialogues.txt", "w") as f2:
            temp = [x for x in out1]
            for k in range(len(temp)):                                      #writing dialogues into new file
                f2.write(temp[k])
                f2.write('\n')
        f2.close()
