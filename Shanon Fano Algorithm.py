from collections import Counter

#Initializing the process for Shanon-Fano Coding
#Counting all symbols and thier occurences using Counter and storing them in descending order in the dictionary.
#We will also use the test message to determine the correctness of the program.
#AAABBBBCCCCCCDD
#AAAAAAAAABBBBBBBBCCCCCCDDDDDEEEEFF
#FFFFFFFFFGGYYYYNNNNNNN
message="AAAAAAAAABBBBBBBBCCCCCCDDDDDEEEEFF"
message_values=Counter(message)
msg_keys=dict()
#print(message_values)
#print(sorted(list(message_values.values()),reverse=True))
#print(message_values.items())
sorted_message_values=dict(sorted(message_values.items(), key =lambda kv:(kv[1], kv[0]),reverse=True))
#print(type(sorted_message_values))
#print(sorted_message_values)
for i,j in sorted_message_values.items():
##    j=j/sum(list(sorted_message_values.values()))
##    sorted_message_values[i]=j
    print(str(i) +" | " +str(j))
enc_code={key: None for key in sorted_message_values.keys()}
count_vals=list(sorted_message_values.values())    
sum_length=sum(count_vals)
print('count_values:',count_vals)




#Now we will form the groups for binary 0's and 1's assignment.
def SeperationIndex(count_values):
    eval_values=dict()
    for marker in range(len(count_values)):
        #print(marker)
        diff=sum(count_values[:marker])-sum(count_values[marker:])
        #print(sum(count_values[:marker]),sum(count_values[marker:]),diff)
        eval_values[marker]=diff
    print("Eval values:",eval_values)
    global upper_grp
    global length
    global lower_grp
    #print(min(i for i in eval_values.values() if i>=0))
    for marker,j in eval_values.items():
        if j==min(a for a in eval_values.values() if a>=0):
            print("marker:",marker)
            upper_grp=count_values[:marker]
            lower_grp=count_values[marker:]
            print("cnt vals:",count_values)
            length=len(count_values)
    return upper_grp,lower_grp





#Now we will assign binary 0 to the upper group and binary 1 to the lower group#
def Bit_Encoder(upper_grp,lower_grp):
    for i in list(sorted_message_values.keys()):
        if sorted_message_values[i] in upper_grp:
            if enc_code[i]==None:enc_code[i]='0'
            else:enc_code[i]+=''.join('0')


    for i in list(sorted_message_values.keys()):
        if sorted_message_values[i] in lower_grp:
            if enc_code[i]==None:enc_code[i]='1'
            else:enc_code[i]+=''.join('1')
    
        
            
    print(enc_code)



print(SeperationIndex(count_vals))
Bit_Encoder(upper_grp,lower_grp)



print('-----------------------------')

if len(upper_grp)>=1:
    print(upper_grp)
    print(SeperationIndex(upper_grp))
    Bit_Encoder(upper_grp,lower_grp)

print('-----------------------------')


print(SeperationIndex(count_vals))
low1=lower_grp.copy()
if len(lower_grp)>=1:
    print(lower_grp)
    print(SeperationIndex(lower_grp))
    Bit_Encoder(upper_grp,lower_grp)
    



print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')

for i,j in enc_code.items():
    print(i,j)
    #time.sleep(1)
    

























    

