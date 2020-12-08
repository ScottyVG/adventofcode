import re

def main():
    with open("test-input.txt", "r") as input_file:
        test_input_data = input_file.read()
    with open("test-invalid-input.txt", "r") as input_file:
        invalid_input_data = input_file.read()
    with open("test-valid-input.txt", "r") as input_file:
        valid_input_data = input_file.read()
    with open("input.txt", "r") as input_file:
        input_data = input_file.read()

    # li = list(test_input_data.split("\n\n"))
    # li = list(invalid_input_data.split("\n\n"))
    li = list(valid_input_data.split("\n\n"))
    # li = list(input_data.split("\n\n"))

    print(li)

    count = 0

    for i in range(len(li)):
        print("########################################")
        print("New i")
        print("########################################")
        # byr (Birth Year) regex
        byr_passport_regex = re.compile(r'(byr):(\s|\n)')
        byr_regex_match = byr_passport_regex.search(li[i])
        print(byr_regex_match)
        print(byr_regex_match.group(1))
        # iyr (Issue Year) regex
        iyr_passport_regex = re.compile(r'(iyr):(\s|\n)')
        iyr_regex_match = iyr_passport_regex.search(li[i])
        print(iyr_regex_match)
        print(iyr_regex_match.group(1))
        # eyr (Expiration Year) regex
        eyr_passport_regex = re.compile(r'(eyr):(\s|\n)')
        eyr_regex_match = eyr_passport_regex.search(li[i])
        print(eyr_regex_match)
        print(eyr_regex_match.group(1))
        # hgt (Height) regex
        hgt_passport_regex = re.compile(r'(hgt):(\s|\n)')
        hgt_regex_match = hgt_passport_regex.search(li[i])
        print(hgt_regex_match)
        print(hgt_regex_match.group(1))
        # hcl (Hair Color) regex
        hcl_passport_regex = re.compile(r'(hcl):(\s|\n)')
        hcl_regex_match = hcl_passport_regex.search(li[i])
        print(hcl_regex_match)
        print(hcl_regex_match.group(1))
        # ecl (Eye Color) regex
        ecl_passport_regex = re.compile(r'(ecl):(\s|\n)')
        ecl_regex_match = ecl_passport_regex.search(li[i])
        print(ecl_regex_match)
        print(ecl_regex_match.group(1))
        # pid (Passport ID) regex
        pid_passport_regex = re.compile(r'(pid):(\s|\n)')
        pid_regex_match = pid_passport_regex.search(li[i])
        print(pid_regex_match)
        print(pid_regex_match.group(1))
        # cid (Country ID) regex
        # cid_passport_regex = re.compile(r'(cid):(\s|\n)')
        # cid_regex_match = cid_passport_regex.search(li[i])

        # if byr_regex_match == None:
        #     pass
        # elif iyr_regex_match == None:
        #     pass
        # elif eyr_regex_match == None:
        #     pass
        # elif hgt_regex_match == None:
        #     pass
        # elif hcl_regex_match == None:
        #     pass
        # elif ecl_regex_match == None:
        #     pass
        # elif pid_regex_match == None:
        #     pass
        # else:
        #     count += 1

    print (count)

if __name__ == "__main__":
    main()

