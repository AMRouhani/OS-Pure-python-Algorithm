# COPY RIGHT Amir mohammad Rouhani
print("This program gives you Bank Man Algorithim service ")
Need =[]
Allocation = []
Max = []
Available = []
Finish = []




P = int ( input("please enter number of your processing : "))
R = int ( input("please enter number of your resources : "))

for i in range(P):
    temp_table = []
    temp_table.append("P"+str(i))
    for j in range(R):
        m = int(input("please enter "+"P "+str(i)+" Resource "+str(j)+" Allocation number : "))
        temp_table.append(m)
    Allocation.append(temp_table.copy())
    temp_table.clear()
    temp_table.append("P"+str(i))
    for j in range(R):
        m = int(input("please enter "+"P "+str(i)+" Resource "+str(j)+" Max number : "))
        temp_table.append(m)
    Max.append(temp_table.copy())


for i in range(R):
    m = int(input("please enter Available number for Resource "+str(i)+" : "))
    Available.append(m)

def Needer():
    Need.clear()
    for i in range(P):
        temp_table = []
        temp_table.append("P"+str(i))
        for j in range(1,R+1):
            m = Max[i][j]-Allocation[i][j]
            if m <0:
                m=0
            temp_table.append(m)
        Need.append(temp_table.copy())


Needer()

def finisher():
    Finish.clear()
    for i in range(P):
        Finish.append(False)

finisher()

def Safe_algo(p_number):
    internal_finish = []
    if Finish[p_number] == True:
        return True
    else:
        for i in range(R): 
            if Need[p_number][i+1] <= Available[i]:
                internal_finish.append(True)
            else:
                internal_finish.append(False)
        if False not in internal_finish:
            for i in range(R):
                Available[i] = Available[i] + Allocation[p_number][i+1]
                Finish[p_number] = True
        else:
            return False
        return True

def Algo_runner(p_number):
    for i in range(p_number):
        for j in range(p_number):
            m = Safe_algo(j)
        if False not in Finish:
            print("system is in SAFE MODE")
            return
    if False not in Finish:
            print("system is in SAFE MODE")
    else:
        print("Unfortuantly system is NOT in SAFE MODE")



run_in = True
Enter_num = True
while Enter_num == True:
    if run_in == True:
        Algo_runner(P)
        run_in = False
        print("run is : ",run_in)
    user_enter = int(input("do you want to enter more proccessing ? if yes enter 1 else enter 0 : "))
    if user_enter == 0 :
        print("Thanks for using my programm.")
        Enter_num = False
    elif user_enter == 1:
        temp_table = []
        temp_table.append("P"+str(P))
        for j in range(R):
            m = 0
            temp_table.append(m)
        Allocation.append(temp_table.copy())
        temp_table.clear()
        temp_table.append("P"+str(P))
        for j in range(R):
            m = int(input("please enter "+"P "+str(P)+" Resource "+str(j)+" Max number : "))
            temp_table.append(m)
        Max.append(temp_table.copy())
        P+=1
        Needer()
        finisher()
        Algo_runner(P)
    else:
        print("please enter right  number")


# COPY RIGHT Amir mohammad Rouhani
