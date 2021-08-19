def numToWords(num):
    length_of_string = len(num);
    if (length_of_string == 0):
        print("String is Empty");
        return;
    if (length_of_string > 4):
        print("Please enter the string with supported length");
        return;
    ones_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
    tens_digits = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen","nineteen"];
    multiple_of_ten = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"];
    power_of_ten = ["hundred", "thousand"];
    print(num, ":", end = " ");
    if (length_of_string == 1):
        print(ones_digits[ord(num[0]) - '0']);
        return;
    x = 0;
    while (x < len(num)):
        if (length_of_string >= 3):
            if (ord(num[x]) - 48 != 0):
                print(ones_digits[ord(num[x]) - 48], end = " ");
                print(power_of_ten[length_of_string - 3], end = " ");
            length_of_string -= 1;
        else:
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 + ord(num[x]) - 48);
                print(tens_digits[sum]);
                return;
            elif (ord(num[x]) - 48 == 2 and ord(num[x + 1]) - 48 == 0):
                print("twenty");
                return;
            else:
                i = ord(num[x]) - 48;
                if(i > 0):
                    print(multiple_of_ten[i], end = " ");
                else:
                    print("", end = "");
                x += 1;
                if(ord(num[x]) - 48 != 0):
                    print(ones_digits[ord(num[x]) - 48]);
        x += 1;
numToWords("1055")
