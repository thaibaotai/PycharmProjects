with open('input.txt', 'r') as my_file:
    # Some action performed with the file, the read() method explained later.
    print(my_file.read(), '\n')


with open('input1.txt', 'r') as file:  # Open the file input1.txt in read mode using the with statement
    print(file.read())


outfile = open('outfile.txt', 'w')  # Opening the file in write mode (using `w` argument)
outfile.write('Hello World')  # Writing to the file, the write() method is explained later.
outfile.close()  # Close the output file!
