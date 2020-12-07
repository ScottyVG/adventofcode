import re

def main():
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    li = list(input_data.split("\n"))

    def Convert(string): 
        list1=[] 
        list1[:0]=string 
        return list1 

    turns = 0

    for i in range(len(li)):
        # slist = Convert(li[i])
        # print(slist)
        print(turns)
        if turns >= 31:
            turns = 0
        else:
            turns += 3
        
        # if i == 0:
        #     pass
        # else:
        #     print(slist[turns+1])
            # print("")
            # print("###################################")
            # print(li[i])
            # print(li[i].index(turns))
            # print(li[i])




    #     password_regex = re.compile(r'(\d+)-(\d+)\s([a-z]):\s(.*)')
    #     regex_match = password_regex.search(li[i])
    #     a = int(regex_match.group(1))
    #     b = int(regex_match.group(2))
    #     c = int(regex_match.group(4).count(regex_match.group(3)))
        
    #     if c >= a and c <= b:
    #         count += 1

if __name__ == "__main__":
    main()

