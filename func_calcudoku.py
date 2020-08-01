# Lev Gamaley & Yadvir Singh
# S. Einakian
# Project 4


#none-> list
def cageInfo():
    cageNum = int(input("Cage Number"))
    cages = []
    cage = []
    for n in range(cageNum):
        cages = input("Cage Data(sum locations)").split()
        cageVal = []
        for n in cages:
            cageVal.append(int(n))
        cage.append(cageVal)
    return cage


'''
'''
#
#
#list->bool
def validate_rows(grid):
    for lst in grid:
       for n in lst:
          if lst.count(n) >1 and n != 0:
             return False
    return True
'''    
'''
#
#
#list->bool
def val_cols(grid):
    gridd = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    return validate_rows(gridd)

'''
'''
#

#list list -> bool
def val_cages(grid, cage):
    for cages in cage:
       total = 0
       for num in range(1, len(cages)):
           row = cages[num] // 5
           col = cages[num] % 5
           total += grid[row][col]
       if total > cages[0] or total< cages[0]:
          return False
    return True
'''
'''
#
#
#list list->bool
def validate_all(grid, cage):
   if validate_rows(grid) and val_cols(grid) and val_cages(grid, cage) == True:
     return True
   else:
     return False


'''
'''
#
#
#list->string
def cubeup(grid):
   for i in grid:
      return(''.join(map(str, i)))


