import re

def main():
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    li = list(input_data.split("\n"))

    count = 0

    def Convert(string): 
        list1=[] 
        list1[:0]=string 
        return list1 

    for i in range(len(li)):
        plist = ""
        password_regex = re.compile(r'(\d+)-(\d+)\s([a-z]):\s(.*)')
        regex_match = password_regex.search(li[i])
        a = int(regex_match.group(1))
        b = int(regex_match.group(2))
        c = regex_match.group(3)
        d = regex_match.group(4)
        plist = Convert(d)
        if plist[a-1] == c and plist[b-1] == c:
            pass
        elif plist[a-1] == c:
            count += 1
        elif plist[b-1] == c:
            count += 1
    print (count)

if __name__ == "__main__":
    main()

