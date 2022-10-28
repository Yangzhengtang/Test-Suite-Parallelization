
projects = dict()
with open("LOC.txt", "r") as file:
    for line in file.readlines():
        name = line.split(" - ")[0]
        num = line.split(" - ")[1]
        projects[name] = int(num)

sorted_projects = [k for k, v in sorted(projects.items(), key=lambda item : item[1])]
for project in sorted_projects:
    cnt = projects[project]
    print(f'{project} : {cnt}')
