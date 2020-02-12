import sys
import re

if __name__ == "__main__":
    file_name_list = sys.argv[1:]
    for file_name in file_name_list:
        file_read=open(r'HW3/'+file_name, "r", encoding="utf8")
        lines = file_read.read()
        line_split=re.split('[\r\n]{2}',lines)
        file_read.close()
        pattern = (r'^CHAPTER\sM{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})')
        patter_2 = (r'^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\.\s.*[^0-9]*')
        new_file = []
        count = 0
        sub_string = input("Enter dialogue:")
        new_line = " "
        line_2=""
        flag=False
        flag2=False
        for i in range(len(line_split)):
            line=line_split[i].split("\n")
            line_split[i]=line_split[i].replace("\n"," ")
            for k in range(len(line)):
                match = re.search(pattern, line[k])
                match2 = re.search(patter_2, line[k])
                if match:
                    new_line = line[k]
                    line_2=line_split[i+1]
                elif match2:
                    new_line=line[k]
                    line_2=""
            if(line_split[i].find(sub_string) != -1):
                line_split[i] = re.sub(u'[\u201c\u201d]', '"', line_split[i])
                dialogue=re.findall(r'("[^"]*["]*)', line_split[i], re.DOTALL)
                #print(line_split[i])
                #print(dialogue)
                for m in range(len(dialogue)):
                    dialogue[m]=dialogue[m].replace('\n',' ')
                    if(sub_string in dialogue[m]):
                            print('pattern exists at' + ' ' + new_line + ' ' + line_2+ ' and is a part of dialogue '+ dialogue[m])
                            count = count + 1
                            flag2=True
                if(flag2==False):
                    print('pattern exists at ' + ' ' + new_line + ' ' + line_2+ ' but is not a dialogue')
                flag=True

    if(flag==False):
        print("pattern does not exist")
    print("count is "+ str(count))




