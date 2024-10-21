# COPY RIGHT Amir mohammad Rouhani
print("This program gives you FCFS , SRTF , SJF , RR time computation")
NOC = int(input("please enter your number of computation : "))
C_table = []
C_table_2 = []
explosion_time = 0
enter_time = 0
quantomic_time = 0
FCFS_table = []
SJF_table = []
SRTF_table = []
RR_table = []

for i in range(NOC):
    temp_table = []
    explosion_time = int(input("please enter explosion time of " + "p"+str(i) + " : "))
    enter_time = int(input("please enter enter time of " + "p"+str(i) + " : "))
    temp_table.append("p"+str(i))
    temp_table.append(explosion_time)
    temp_table.append(enter_time)
    C_table.append(temp_table)

quantomic_time = int(input("if you have quantomic time please enter it , else enter -1 :"))

print("Your entered table is : ",C_table,"\n")


def table_sort_enterTime(table):
    def swap(i, j):
        table[i], table[j] = table[j], table[i]

    n = len (table)
    swapped = True
    
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if table[i - 1][2] > table[i][2]:
                swap(i - 1, i)
                swapped = True
                    
    return table


def FCFS(table):
    waiting_time = 0
    return_time = 0
    c_start_time = 0
    c_end_time = 0
    for i in range(NOC):
        c_start_time = c_end_time
        c_end_time = c_start_time + table[i][1]
        waiting_time = c_start_time - table[i][2]
        return_time = c_end_time - table[i][2]
        FCFS_table_temp = []
        FCFS_table_temp.append(table[i][0])
        FCFS_table_temp.append(waiting_time)
        FCFS_table_temp.append(return_time)
        FCFS_table.append(FCFS_table_temp.copy())
        FCFS_table_temp.clear()
    
    FCFS_lengh = len(FCFS_table)
    waiting_sum = 0
    for i in range(FCFS_lengh):
        waiting_sum = FCFS_table[i][1] + waiting_sum
    
    return_sum = 0
    for i in range(FCFS_lengh):
        return_sum = FCFS_table[i][2] + return_sum
    
    waiting_avr = waiting_sum/FCFS_lengh
    return_avr = return_sum/FCFS_lengh

    print("FCFS table = ",FCFS_table,"\n")
    print("average waiting time in FCFS = ",waiting_avr,"\n")
    print("average return time in FCFS = ",return_avr,"\n")
    return

    
def SJF (table):
    waiting_time = 0
    return_time = 0
    c_start_time = 0
    c_end_time = 0

    def mini_SJF(Number,end_time):
        end_temp_time = []
        end_temp_name = []
        end_sjf_temp = []
        x = -1
        for i in range(len(SJF_table)):
            end_sjf_temp.append(SJF_table[i][0])
        for i in range(0, Number):
            if (table[i][2] <= end_time) and (table[i][0] not in end_sjf_temp):
                end_temp_time.append(table[i][1])
                end_temp_name.append(table[i][0])
        z = min(end_temp_time)
        for i,j in zip(end_temp_time,end_temp_name):
            if i == z :
                x = j
        return x

    for i in range(NOC):
        x_2 = mini_SJF(len(table),c_end_time)
        for m in range(len(table)):
            if x_2 in table[m]:
                x_2 = m
                break
        c_start_time = c_end_time
        c_end_time = c_start_time + table[x_2][1]
        waiting_time = c_start_time - table[x_2][2]
        return_time = c_end_time - table[x_2][2]
        SJF_table_temp = []
        SJF_table_temp.append(table[x_2][0])
        SJF_table_temp.append(waiting_time)
        SJF_table_temp.append(return_time)
        SJF_table.append(SJF_table_temp.copy())
        SJF_table_temp.clear()
    
    SJF_lengh = len(SJF_table)
    waiting_sum = 0
    for i in range(SJF_lengh):
        waiting_sum = SJF_table[i][1] + waiting_sum
    
    return_sum = 0
    for i in range(SJF_lengh):
        return_sum = SJF_table[i][2] + return_sum
    
    waiting_avr = waiting_sum/SJF_lengh
    return_avr = return_sum/SJF_lengh
    print("SJF_table : ",SJF_table,"\n")
    print("average waiting time in SJF = ",waiting_avr,"\n")
    print("average return time in SJF = ",return_avr,"\n")
    return


def SRTF (table_copy):
    table = []
    for i in range(len(table_copy)):
        table.append(table_copy[i].copy())
    c_range = 0
    waiting_time = 0
    return_time = 0
    c_start_time = 0
    c_end_time = 0
    x_2 = []

    for i in range(NOC):
        c_range = c_range + table[i][1]

    def mini_SRTF(Number,end_time):
        end_temp_time = []
        end_temp_name = []
        x = -1
        for i in range(0, Number):
            if (table[i][2] <= end_time):
                end_temp_time.append(table[i][1])
                end_temp_name.append(table[i][0])

        z = min(end_temp_time)
        for i,j in zip(end_temp_time,end_temp_name):
            if i == z :
                x = j
        return x

    last_poin_checker = []
    for i in range(c_range):
        SRTF_table_temp = []
        x = -1
        x_2 = mini_SRTF(len(table),c_end_time)
        for m in range(len(table)):
            if x_2 in table[m]:
                x = m
                break
        
        c_start_time = c_end_time
        c_end_time = c_start_time + 1
        table[x][1] = table[x][1] -1
        breaker = False

        if len(SRTF_table) == 0:
            waiting_time = c_start_time - table[x][2]
            return_time = c_end_time - table[x][2]
            SRTF_table_temp.append(table[x][0])
            SRTF_table_temp.append(waiting_time)
            SRTF_table_temp.append(return_time)
            SRTF_table.append(SRTF_table_temp.copy())
            SRTF_table_temp.clear()
            last_poin_checker.append(x)
        else:
            for q,j in zip(range(len(SRTF_table)),SRTF_table):
                if x_2 in j:
                    waiting_time = c_start_time - SRTF_table[q][2]
                    return_time = c_end_time - table[x][2]
                    if x not in last_poin_checker : 
                        SRTF_table[q][1] = SRTF_table[q][1] + waiting_time
                    SRTF_table[q][2] = return_time
                    breaker = True
                    last_poin_checker.pop()
                    last_poin_checker.append(x)
                    break
            if breaker == False:
                waiting_time = c_start_time - table[x][2]
                return_time = c_end_time - table[x][2]
                SRTF_table_temp.append(table[x][0])
                SRTF_table_temp.append(waiting_time)
                SRTF_table_temp.append(return_time)
                SRTF_table.append(SRTF_table_temp.copy())
                SRTF_table_temp.clear()
                last_poin_checker.pop()
                last_poin_checker.append(x)   
        
        if table[x][1] == 0:
            del table[x]

    SRTF_lengh = len(SRTF_table)
    waiting_sum = 0
    for i in range(SRTF_lengh):
        waiting_sum = SRTF_table[i][1] + waiting_sum
    
    return_sum = 0
    for i in range(SRTF_lengh):
        return_sum = SRTF_table[i][2] + return_sum
    
    waiting_avr = waiting_sum/SRTF_lengh
    return_avr = return_sum/SRTF_lengh


   

    print("SRTF Table = ",SRTF_table,"\n")
    print("average waiting time in SRTF = ",waiting_avr,"\n")
    print("average return time in SRTF = ",return_avr,"\n")
    return


def RR (table_copy):
    table = []
    RR_fifo_check = False
    for i in range(len(table_copy)):
        table.append(table_copy[i].copy())
    if quantomic_time == -1 :
        print(" this computation can't Run round rubin algorithim because you dont have quantomic time.")
        print(" your entered number for quantomic time is : ",quantomic_time)
        return
    RR_fifo_list = []
    RR_table_temp = []
    c_range = 0
    waiting_time = 0
    return_time = 0
    c_start_time = 0
    c_end_time = 0

    for i in range(NOC):
        c_range = c_range + table[i][1]
    c_range = ((c_range//quantomic_time)*quantomic_time)+(c_range % quantomic_time)

    def mini_RR(Number,end_time):
        x = -1
        for i in range(0, Number):
            if (table[i][2] <= end_time) and (table[i][0] not in RR_fifo_list):
                RR_fifo_list.append(table[i][0])
        if RR_fifo_check == False:
            RR_fifo_list.append(RR_fifo_list[0])
            del RR_fifo_list[0]
        x = RR_fifo_list[0]
        return x


    last_poin_checker = []
    for i in range(c_range):
        RR_table_temp = []
        x = -1
        x_2 = mini_RR(len(table),c_end_time)
        for m in range(len(table)):
            if x_2 in table[m]:
                x = m
                break
        
        c_start_time = c_end_time
        c_end_time = c_start_time + min(table[x][1],quantomic_time)
        table[x][1] = table[x][1] - min(table[x][1],quantomic_time)
        breaker = False

        if len(RR_table) == 0:
            waiting_time = c_start_time - table[x][2]
            return_time = c_end_time - table[x][2]
            RR_table_temp.append(table[x][0])
            RR_table_temp.append(waiting_time)
            RR_table_temp.append(return_time)
            RR_table.append(RR_table_temp.copy())
            RR_table_temp.clear()
            last_poin_checker.append(x_2)
        else:
            for q,j in zip(range(len(RR_table)),RR_table):
                if x_2 in j:
                    waiting_time = c_start_time - RR_table[q][2] - table[x][2]
                    return_time = c_end_time - table[x][2]
                    if x_2 not in last_poin_checker : 
                        RR_table[q][1] = waiting_time + RR_table[q][1]
                    RR_table[q][2] = return_time
                    breaker = True
                    last_poin_checker.pop()
                    last_poin_checker.append(x_2)
                    break
            if breaker == False:
                waiting_time = c_start_time - table[x][2]
                return_time = c_end_time - table[x][2]
                RR_table_temp.append(table[x][0])
                RR_table_temp.append(waiting_time)
                RR_table_temp.append(return_time)
                RR_table.append(RR_table_temp.copy())
                RR_table_temp.clear()
                last_poin_checker.pop()
                last_poin_checker.append(x_2)  
        if table[x][1] == 0:
            if table[x][0] in RR_fifo_list:
                RR_fifo_list.remove(table[x][0])
                RR_fifo_check = True
            del table[x]
        else:
            RR_fifo_check = False
        if len(table)==0:
            break

    RR_lengh = len(RR_table)
    waiting_sum = 0
    for i in range(RR_lengh):
        waiting_sum = RR_table[i][1] + waiting_sum
    
    return_sum = 0
    for i in range(RR_lengh):
        return_sum = RR_table[i][2] + return_sum
    
    waiting_avr = waiting_sum/RR_lengh
    return_avr = return_sum/RR_lengh

    print("RR Table = ",RR_table,"\n")
    print("average waiting time in RR = ",waiting_avr,"\n")
    print("average return time in RR = ",return_avr,"\n")
    return

for i in range(len(C_table)):
    C_table_2.append(C_table[i].copy())

C_table_3 = table_sort_enterTime(C_table_2)
FCFS(C_table_3)
SJF(C_table_3)
SRTF(C_table_3)
RR(C_table_3)

print(" THANKS FOR USING MY PROGRAM ")

# COPY RIGHT Amir mohammad Rouhani
