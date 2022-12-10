import os

def getDependency(filename):
    f = open(filename, encoding="utf-8")
    dict = {}
    label = []
    description = []
    for i in range(10):
        s = f.readline().strip()
        l = s.split(': ')
        label.append(l[0])
        description.append(l[1])
    res = {label[i]: description[i] for i in range(len(label))}
    print(str(res))
    f.close()
    return res

def generateSuites():
    filenames = os.listdir(r'./order-dependency')
    suites = []
    for filename in filenames:
        if (filename[0] == '.'):
            continue
        result = []
        print(filename)
        dict = getDependency('./order-dependency/' + filename)
        polluter = dict['POLLUTER']
        cleaner = dict['CLEANER']
        target = dict['MODIFIED']

        result.append(polluter)
        result.append(cleaner)
        result.append(target)
        suites.append(result)
    with open("file.txt", "w") as output:
        output.write(str(suites))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generateSuites()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
