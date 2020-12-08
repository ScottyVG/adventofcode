import re

def main():
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    li = list(input_data.split("\n"))

    def Convert(string): 
        list1=[] 
        list1[:0]=string 
        return list1 

    turns = -3
    count = 0

    for i in range(len(li)):
        
        slist = Convert(li[i])
        turns += 3

        if turns >= 31:
            turns = turns - 31

        if i == 0:
            pass
        else:
            if slist[turns] == '#':
                count += 1
    
    print (count)

if __name__ == "__main__":
    main()

