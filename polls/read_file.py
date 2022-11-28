def read_file():
    with open('work.txt') as f:
        data = f.read()
        print(data)

print(read_file())