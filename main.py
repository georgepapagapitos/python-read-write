import simplejson as json
import os

new_file = open("new-file.txt", "w+")

string = "This is the content that will be written to the text file."

new_file.write(string)

# if there is an existing file, open in read / write mode
if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
    old_file = open("./ages.json", "r+")
    # load data from file
    data = json.loads(old_file.read())
    print("current age is", data["age"], "--- adding a year")
    # increase age by 1
    data["age"] = data["age"] + 1
    print("new age is", data["age"])
# if no file is found, create a file
else:
    old_file = open("./ages.json", "w+")
    data = {"name": "George", "age": 30}
    print("no file found, setting default age to", data["age"])

old_file.seek(0)
old_file.write(json.dumps(data))

