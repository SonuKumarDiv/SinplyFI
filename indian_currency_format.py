def indian_currency_format(number):
    if not type(number)==int:
        print("Input must be an integer")

    if number < 0:
        print('Currency Must be greater than Zero')

    number_str = str(number)
    length = len(number_str)

    if length > 12:
        print('Currency shoult not  be greater than 12 digits')

    result = ""
    count = 0
    reversed_number_str = number_str[::-1]
    print('rev',reversed_number_str)
    for digit in reversed_number_str:
        print('digit',digit)
        result = digit + result
        print('result',result)
        count += 1


        if count == 3 and digit != number_str[0]:
            print('count',count)
            print('number_str[0]',number_str[0])
            result = ',' + result
            print("result",result)
            count = 0

    return result



input_number = 12436
output_currency_notation = indian_currency_format(input_number)
print(f"Input: {input_number}")
print(f"Output: {output_currency_notation}")




### Algo Steps::::

# 1 Take Currency as a Input 
# 2 : Check Input Type and input lenght 
    # if type(userInput)== int
    # if userinput<0:
# 3 : will convert userinput in to string
# 4 : I will reverse hole input
# 5 : for the currency notations main logics like 
      # if count == 3 and digit != number_str[0]:     
    # i will add format with ',' after above condiction




