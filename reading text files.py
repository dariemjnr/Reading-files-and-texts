openfile = open("./story.txt", "r")
read_file= openfile.read()
print(read_file)

def readfile(filename):
    with open ("./story.txt", "r") as openfile:
      read_file = openfile.read()
    return read_file

def countwords():
    text= readfile("./story.txt", "r")  
    split_text= text.split()
    
    count={}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] =1

    return count

print (countwords())

   







