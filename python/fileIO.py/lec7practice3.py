word = "learning"
with open("python/practice.txt", "r")as f:
    data = f.read()
    if(data.find("word") != -1):
        print("found")
    else:
        print("not found")