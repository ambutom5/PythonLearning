def file_analysis(filename="Demo.txt",outputfile="output.txt"):
    try:
        count_line = 0
        longestw = ""
        with open(filename) as file:
            for line in file:
                count_line += 1
                words = line.strip().split()
                for word in words:
                    word = word.strip('.?!')
                    if len(word) > len(longestw):
                        longestw = word

        with open(outputfile,"w") as out:
            out.write(f"Count of Lines : {count_line}\n")
            out.write(f"Longest Word : {longestw}")

    except FileNotFoundError:
        print("File Not Found!")

result = file_analysis("Demo.txt")
