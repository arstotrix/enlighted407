def openfile(file):
    ff = 0
    with open (file, encoding = 'utf-8') as f:
        text = f.read()
        #print(text[:100])
return ff

def create(start_path):
    i = 0
    for root, dirs, files in os.walk(start_path):
        print(files)
        for file in files:
            fname = start_path + '/' + file
            openfile(fname)
    return i
