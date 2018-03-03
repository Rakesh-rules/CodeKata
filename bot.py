if __name__ == '__main__':
    dir='e'
    x=0
    y=0
    xco={'n':0,'w':-1,'e':1,'s':0}
    yco={'n':-1,'w':0,'e':0,'s':1}
    x1=input('Enter the path')
    for d in x1:
        if d=='n' or d=='w' or d=='e' or d=='s':
            dir=d
        if d=='m':
            if (x+xco[dir])>=0 and (x+xco[dir])<=2 and (y+yco[dir])>=0 and (y+yco[dir])<=2:
                x=x+xco[dir]
                y=y+yco[dir]
    print(x,y,dir)
