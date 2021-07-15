def given_dictionary_value(a,b,oper):
    if oper == "or" :
        if a in dict_a:
            result = dict_a[a]
        else:
            result = dict_a[b]
    elif oper == "and":
        result = dict_a[a] + dict_a[b]
    return result    


# read the given expression
expression = input().split()
#print(expression)
#read the given dictionary
dict_a = eval(input())  #eval() converts string to dictionary
#print(dict_a)

operators=[]
other_index = []
indexs = []
val = []
for i in expression:
    if i == "and" or i == "or":
        operators.append(i)
    elif len(i) >1 :
        index = expression.index(i)
        indexs.append(index)
        
        for j in i:
            if j != "(" and j != ")":
                val.append(j)
           
    else:
        val.append(i)
        other_index.append(expression.index(i))
#print(val)  
#print(operators)
#print(indexs)
#print(other_index)
result =""

result1 = ""
if len(indexs) >0:
    result1+= given_dictionary_value(val[indexs[0]-1], val[indexs[1]-2],operators[indexs[0]-1])
    #print(result1)
    
l = 0    
if len(expression)==3 :
    if expression[1] == "or":
        if expression[0] in dict_a and ord(expression[0]) < ord(expression[2]):
            result = dict_a[expression[0]]
        else:
            result = dict_a[expression[2]]
        print(result)
    else:
        result = dict_a[expression[0]] + dict_a[expression[2]] 
        print(result) 
    
elif len(expression) >3:
    
    if len(other_index) == 1:
        result = dict_a[expression[other_index[0]]] + result1
        print(result)
    elif len(other_index)>1 and len(indexs)>0:
        result = dict_a[expression[other_index[0]]] + result1 + dict_a[expression[other_index[1]]] 
        print(result) 
    else:
        while l < len(expression):
            result += dict_a[expression[l]]
            l += 2 
        print(result)