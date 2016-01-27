employees = ['Silva','Melonie','Marvin','Simon','Sascha','Simi','Sylvain','Peter','Jamyang','Joao','Joel','Andrea','Angela','Stefan','Tibor','Jess','Ines','Florian','Ilona','Irene']

shift = 11
for i in range(4):
    buddies = []
    for j in range(len(employees)):
        buddies.append([employees[j],employees[(j+i+shift)%len(employees)]])
    print buddies
