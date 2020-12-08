import re

def main():
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    li = list(input_data.split("\n"))

    def Convert(string): 
        list1=[] 
        list1[:0]=string 
        return list1 

    def a():
        count = 0
        turns = 0
        for i in range(len(li)):
            if i == 0:
                pass
            else:
                slist = Convert(li[i])
                turns += 1
                if turns >= 31:
                    turns = turns - 31
                if slist[turns] == '#':
                    count += 1
        print (count)
        return count
    
    def b():
        count = 0
        turns = 0
        for i in range(len(li)):
            if i == 0:
                pass
            else:
                slist = Convert(li[i])
                turns += 3
                if turns >= 31:
                    turns = turns - 31
                if slist[turns] == '#':
                    count += 1
        print (count)
        return count

    def c():
        count = 0
        turns = 0
        for i in range(len(li)):
            if i == 0:
                pass
            else:
                slist = Convert(li[i])
                turns += 5
                if turns >= 31:
                    turns = turns - 31
                if slist[turns] == '#':
                    count += 1
        print (count)
        return count

    def d():
        count = 0
        turns = 0
        for i in range(len(li)):
            if i == 0:
                pass
            else:
                slist = Convert(li[i])
                turns += 7
                if turns >= 31:
                    turns = turns - 31
                if slist[turns] == '#':
                    count += 1
        print (count)
        return count

    def e():
        count = 0
        turns = 0
        for i in range(len(li)):
            if (i % 2) == 1 or i == 0:
                pass
            else:
                slist = Convert(li[i])
                turns += 1
                if turns >= 31:
                    turns = turns - 31
                if slist[turns] == '#':
                    count += 1
        print (count)
        return count
    
    # Run Functions:
    print(a()*b()*c()*d()*e())

if __name__ == "__main__":
    main()

