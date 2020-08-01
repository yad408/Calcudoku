#Yad n Lev



from func_calcudoku import *

def main():
    cagE=cageInfo()
    oz=[0 for x in range(5)]
    puzzle=[oz for x in range(5)]

    
    cellValue = 0
    #function for cage input
    
    while cellValue < 25:
        row = cellValue // 5
        col = cellValue % 5
      # print(row,col,cellValue)
        puzzle[row][col]+=1
        if puzzle[row][col] > 5 or val_cages(puzzle,cagE)==False:
           print(row,col,cellValue)
           puzzle[row][col]=0
           cellValue -= 1 
           continue
        if validate_all(puzzle,cagE)==False:
           continue
        cellValue+=1
    print(cubeup(puzzle))
if __name__=='__main__':
  main()

