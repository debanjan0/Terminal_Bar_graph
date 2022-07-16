
"""
A simple function for displaying a bar graph in the terminal.
"""

def bar_graph(height,x,space=2):
    for i in range(height+1):
        print("|", end=" ")
        for j in x:
            if i > height-j:
                print("HH", end=(space*" "))
            else:
                print("  ", end=(space*" "))
        print()
    print("-"*(len(x)*(space+2)+2))

bar_graph(10,[1,3,2,7,4,5,6,2,8,9],space=1)
