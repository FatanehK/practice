"""Given a list of telephone numbers in the format AAA-BBB-CCCC, 
how would you return them in the two following formats:

BBB-AAA-CCCC
BBB-CCCC-AAA

How would you best return a very large file with all these numbers?"""



# Read telephone numbers from a file and store them in a list
def read_phone_numbers(file_path):

    phone_number =[]
    with open (file_path,"r"):
        for line in file_path:
            phone_number.append(line.strip())
        return phone_number
        

# def format(phone_number):
#     formated=[]
#     for num in phone_number:
#         part = num.split("-")
#         formated.append(f"{part[1]}-{part[0]}-{part[2]}")
#         formated.append(f"{part[1]}-{part[2]}-{part[0]}")
#     return formated
def convert_to_formats(phone_number):
    formatted_numbers = []
    parts = phone_number.split('-')
    print(parts)
        # Format BBB-AAA-CCCC
    formatted_numbers.append(f'{parts[1]}-{parts[0]}-{parts[2]}')
        # Format BBB-CCCC-AAA
    formatted_numbers.append(f'{parts[1]}-{parts[2]}-{parts[0]}')
    return formatted_numbers


print(convert_to_formats("AAA-BBB-CCCC"))
    
