def arithmetic_arranger(lst, args=False):
    listOne = list()
    listTwo = list()
    listThree = list()
    result = list()    
    gap = 4
    answer = ""
    frstNumPos = list()
    oPos = list()
    nPos = list()

    for operands in lst:
        if len(lst) > 5:
            return "Error: Too many problems."
        ll = operands.split()           
        
        if len(ll) != 3:        # a + b has three elements. if we ecounter more or less element it blows
            return "Error: operands not balanced."
        try:
            if len(ll[0]) > 4:
                return "Error: Numbers cannot be more than four digits."      
            if len(ll[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
        except:
            pass

        try:
            if not ll[0].isdigit():
                return "Error: Numbers must only contain digits."
            if not ll[2].isdigit():
                return "Error: Numbers must only contain digits."

            listOne.append(ll[0])
            listTwo.append(ll[1])
            listThree.append(ll[2])
        except:
            pass
        if not (ll[1].strip() == '+' or ll[1].strip() ==  '-'): 
            return "Error: Operator must be '+' or '-'."        
                 
        result.append(eval(operands))
        
    for i in range (len(listThree)):
        biggerSize = 0
        if len(listOne[i]) < len(listThree[i]):
            biggerSize = len(listThree[i])
        else:
            biggerSize = len(listOne[i])
        if i == 0:
            gap = 0
        else: 
            gap = 4
        space = gap + biggerSize + 2
        opPos = space - biggerSize - 1
        numPos = space - opPos
        frstNumPos.append(space)
        oPos.append(opPos)
        nPos.append(numPos)
   
    for j in range(len(listOne)):
        answer = answer + "%*s" % (frstNumPos[j], listOne[j])
    answer += "\n"

    for i in range (len(listThree)):        
        answer += '%*s' % (oPos[i], listTwo[i])
        answer += '%*s' % (nPos[i], listThree[i])
    answer += "\n"

    for i in range (len(listThree)):
        biggerSize = 0

        if len(listThree[i]) < len(listOne[i]):
            biggerSize = listOne[i]
        else: biggerSize = listThree[i]
        answer += "%*s" % (frstNumPos[i]-len(biggerSize) -2, "" )

        for j in range (len(biggerSize)+2):
            answer += "-"
    if args == True:
      answer += "\n"
      for i in range (len(result)):       
          answer += '%*d' % (frstNumPos[i], result[i])

    return answer
