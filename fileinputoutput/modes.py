with open("python/demo.txt", "r") as f:
    data = f.read()
    print(data)



with open("python/demo.txt", "w") as f:
    f.write("new data") 