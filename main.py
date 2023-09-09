import random
from os import system
def main():
    while True:
        print("""
 ████████╗ ██████╗ ██████╗ ██╗████████╗ ██████╗ 
 ╚══██╔══╝██╔═══██╗██╔══██╗██║╚══██╔══╝██╔═══██╗
    ██║   ██║   ██║██║  ██║██║   ██║   ██║   ██║
    ██║   ██║   ██║██║  ██║██║   ██║   ██║   ██║
    ██║   ╚██████╔╝██████╔╝██║   ██║   ╚██████╔""")
        x = int(random.randint(1, 6))
        lt = list(['T','O','D','I','T','O'])
        print(str(x)+' -> '+str(lt[x-1]))
        inp = input('[+]')
        if(inp!='q'):
            system('clear')
        else:
            exit()
if __name__=="__main__":
    main()