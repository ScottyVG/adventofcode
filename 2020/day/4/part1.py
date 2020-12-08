import re

def main():
    with open("test-input.txt", "r") as input_file:
        test_input_data = input_file.read()
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    # li = list(test_input_data.split("\n\n"))
    li = list(input_data.split("\n\n"))

    count = 0

    for i in range(len(li)): 
        # byr (Birth Year) regex
        byr_passport_regex = re.compile(r'(byr):')
        byr_regex_match = byr_passport_regex.search(li[i])
        # iyr (Issue Year) regex
        iyr_passport_regex = re.compile(r'(iyr):')
        iyr_regex_match = iyr_passport_regex.search(li[i])
        # eyr (Expiration Year) regex
        eyr_passport_regex = re.compile(r'(eyr):')
        eyr_regex_match = eyr_passport_regex.search(li[i])
        # hgt (Height) regex
        hgt_passport_regex = re.compile(r'(hgt):')
        hgt_regex_match = hgt_passport_regex.search(li[i])
        # hcl (Hair Color) regex
        hcl_passport_regex = re.compile(r'(hcl):')
        hcl_regex_match = hcl_passport_regex.search(li[i])
        # ecl (Eye Color) regex
        ecl_passport_regex = re.compile(r'(ecl):')
        ecl_regex_match = ecl_passport_regex.search(li[i])
        # pid (Passport ID) regex
        pid_passport_regex = re.compile(r'(pid):')
        pid_regex_match = pid_passport_regex.search(li[i])
        # cid (Country ID) regex
        # cid_passport_regex = re.compile(r'(cid):')
        # cid_regex_match = cid_passport_regex.search(li[i])
        
        if byr_regex_match == None:
            pass
        elif iyr_regex_match == None:
            pass
        elif eyr_regex_match == None:
            pass
        elif hgt_regex_match == None:
            pass
        elif hcl_regex_match == None:
            pass
        elif ecl_regex_match == None:
            pass
        elif pid_regex_match == None:
            pass
        else:
            count += 1

    print (count)

if __name__ == "__main__":
    main()

