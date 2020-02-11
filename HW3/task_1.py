import sys
import re

if __name__ == "__main__":
    file_name_list = sys.argv[1:]                                           #taking input files from command line

    for file_name in file_name_list:                                        #iterating over all the files
        f2 = open(file_name.strip('.txt') + "_dialogues.txt", "w")
        file_read=open("HW3/"+file_name, "r", encoding="utf8")
        lines = file_read.read()
        line_split=re.split('[?\r\n][\r\n]',lines)
        #print(line_split)
        k=0
        out1={}
        for line in line_split:
            line_loop = re.sub(u'[\u201c\u201d]', '"', line)
            out1[k]={}
            out1[k]=re.findall(r'("[^"]*["\r\n]*)',line_loop,re.DOTALL)
            #print(out1[k])
            if(len(out1[k])!=0):
                #print(out1[k])

                #print(len(out1[k]))
                for i in range(len(out1[k])):
                    f2.write(out1[k][i])
                    f2.write('\n')
                k = k + 1
        '''for line in line_split:
            print("**************")
            print(line)'''

        #print(line_split)
        file_read.close()
        f2.close()
        '''with open(file_name.strip('.txt') + "_dialogues.txt", "w") as f2:
            #temp = [x for x in out1]
            for temp in out1:  # writing dialogues into new file
                f2.write(temp)
                f2.write('\n')
        f2.close()'''
        '''lines = re.sub(u'[\u201c\u201d]', '"', lines)
            out1 = re.findall(r'(".*?["\r\n])', lines, re.DOTALL)                 #extracting each dialogue
            for k in range(len(out1)):
                out1[k] = re.sub(r'\n\s*', ' ', out1[k])                    #removing unnecessary new lines and spaces
        print(out1)
        f.close()
        with open(file_name.strip('.txt') + "_dialogues.txt", "w") as f2:
            temp = [x for x in out1]
            for k in range(len(temp)):                                      #writing dialogues into new file
                f2.write(temp[k])
                f2.write('\n')
        f2.close()'''

