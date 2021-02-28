def SupportFunction(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct

def MainFunction(array_val,n,k,l):
    result = +2147483647 
    final_output.clear()
    array_val.sort() 
    for i in range(n-k+1): 
        result = int(min(result, array_val[i+k-1] - array_val[i])) 
    for j in range(0,l):
        for name1,value in input_item.items():
            if(int(value)==array_val[k+j]):
                val = SupportFunction([name1,value])
                final_output.update(val)
    return result



input_file = open("input.txt",'r')
global input_items, final_output 
input_item = {}
final_output = {}

for line in input_file:
    lines = line.split(":")
    val = SupportFunction(lines)
    input_items.update(val)

val = (input_item.values())
actual = []
for n in val:
    actual.append(int(n))

arr= actual 
n =len(arr) 
input_file.close()
while(True):
    f1 = open("output.txt", "a")
    k = int(input("Number of employees : ")) 
    f1.write("Number of employees : "+str(k))
    f1.write("\n")
    f1.write("Here the input_items that are selected for distribution are:")
    f1.write("\n")
    result = MainFunction(arr, n, k,k)
    for name1,value in final_output.items():
        f.write(name1+" : "+value)
    f1.write("\n")
    print("Output File Written")
    f1.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(result))
    f1.write("\n")
    f1.close()

