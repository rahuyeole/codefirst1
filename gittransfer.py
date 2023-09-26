with open("read.txt", "r") as input:

   

    with open("write.txt", "w") as output:

       

        for line in input:

            output.write(line)