f = open("Demo.txt","w")                            # Write overwrites exising contents
f.write("Python is simple and easy to use!")
f.close()

f1 = open("Demo.txt","a")                           # Append appends contents to exising contents
f1.write("\nIt is an Interpreted Language.")
f1.close()