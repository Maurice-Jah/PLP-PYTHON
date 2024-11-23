
# A program that reads a file and writes a modified version to a new file

def modify_file(input_filename, output_filename):
        with open(input_filename, 'w') as write_to_file:
             write_to_file.write("It is a python assignment")

        with open(input_filename, 'r') as input_file:
            content = input_file.read()
           
        with open(output_filename, 'w') as output_file:
            output_file.write(content)
            
        with open(output_filename, 'a') as append_file:
            append_file.write(" and i will get it right")

        with open(output_filename, 'r') as final_file:
            modified_content = final_file.read()

            print(f"The original content is {content}")
            print(f"The modified file is {modified_content}")


modify_file("input.txt","output.txt")







