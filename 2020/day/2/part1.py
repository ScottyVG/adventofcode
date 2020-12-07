import re

def main():
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    li = list(input_data.split("\n"))

    count = 0

    for i in range(len(li)):
        password_regex = re.compile(r'(\d+)-(\d+)\s([a-z]):\s(.*)')
        regex_match = password_regex.search(li[i])
        a = int(regex_match.group(1))
        b = int(regex_match.group(2))
        c = int(regex_match.group(4).count(regex_match.group(3)))
        
        if c >= a and c <= b:
            count += 1

    print (count)

if __name__ == "__main__":
    main()

