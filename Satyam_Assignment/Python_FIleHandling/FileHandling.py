import glob

read_files = glob.glob("*.csv")

with open("result.csv", "wb") as outfile:
    try: 
     for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
    except FileNotFoundError:
       print("File is not there")


