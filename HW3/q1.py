import sys
import re

if __name__ == "__main__":
    file_name_list = sys.argv[1:]
    for file_name in file_name_list:
        f2 = open(file_name.strip('.txt') + "_dialogues.txt", "w")
        file_read=open("HW3/"+file_name, "r", encoding="utf8")
        lines = file_read.read()
        line_split=re.split('[\r\n]{2}',lines)
        k=0
        out1={}
        for line in line_split:
            line_loop = re.sub(u'[\u201c\u201d]', '"', line)
            out1[k]={}
            out1[k]=re.findall(r'("[^"]*["]*)',line_loop,re.DOTALL)
            if(len(out1[k])!=0):
                for i in range(len(out1[k])):
                    f2.write(out1[k][i].replace('\n',' '))
                    f2.write('\n')
                k = k + 1
        f2.close()
        file_read.close()