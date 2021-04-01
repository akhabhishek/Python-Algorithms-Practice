def number2words(s):
    """
    Function to convert a string of digits into number in words
    Eg: "1234" -> one thousand two hundred and thirty four

    Range of input: "0" to "99999"
    """

    if s == '0':
        return "zero"
    elif len(s) == 0:
        return "Empty input"
    elif len(s) > 5:
        return "Range of input supported '0' to '99999'"

    # Reverse input and store digit strings in a list to have highest place digit at end of list
    # This will help in using list.pop() and step down places with each pop (thousands -> hundreds -> tens -> units)
    num_rev = list(reversed(s))

    units = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':''}
    tens_place = {'2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety', '0':''}
    nums_11_19 = {'10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', \
    '17':'seventeen', '18':'eighteen', '19':'nineteen'}

    # Highest place based on number of digits
    highest_place = {3:'hundred', 4:'thousand', 5:'thousand'}

    # Length of input number
    length = len(s)

    output = []

    while num_rev:

        if len(num_rev) == 1:
            output.append(units[num_rev.pop()])

        elif len(num_rev) == 2:

            # For numbers where tens place is 1, i.e. numbers between 10 to 19
            if num_rev[-1] == '1':
                last2digits = num_rev.pop() + num_rev.pop()
                output.append(nums_11_19[last2digits])
                break

            tens_num = num_rev.pop()
            output.append(tens_place[tens_num])

            units_num = num_rev.pop()
            output.append(units[units_num])

        else:

            while length > 2:
                if length == 5:
                    num1 = num_rev.pop()
                    num2 = num_rev.pop()
                    place = highest_place[length]
                    output.append(str(tens_place[num1]) + ' ' + str(units[num2]) + ' ' + place)

                    length -= 2

                number = num_rev.pop()
                place = highest_place[length]
                output.append(str(units[number]) + ' ' + place)

                length -= 1

    return (' '.join(output))


print(number2words("0"))
print(number2words("4"))
print(number2words("12"))
print(number2words("95"))
print(number2words("115"))
print(number2words("3425"))
print(number2words("1210"))
print(number2words("1200"))
print(number2words("99999"))
