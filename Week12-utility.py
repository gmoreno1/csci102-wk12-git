# Gabriella Moreno
# CSCI 102 - Section A
# Week 12 - Part A

def PrintOutput(x):
    print('OUTPUT',x)
    
def LoadFile(file):
    f = open(file)
    contents = f.readlines()
    print('OUTPUT', contents)

# this code has bugs

def UpdateString(string_1, a, num):
    s_1_list = []
    
    for i in len(string_1):
        s_1_list.append(string_1[i])
    

    s_1_list[num] = a
    final_string = s_1_list.join()
    print('OUTPUT', final_string)


