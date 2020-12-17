from collections import Counter

#Initializing the process for Shanon-Fano Coding

#We will also use the test message to determine the correctness of the program.
#AAAAAAAAABBBBBBBBCCCCCCDDDDDEEEEFF
message="AAAAAAAAABBBBBBBBCCCCCCDDDDDEEEEFF"
print("Original message:",message)
bin_msg=str()
for i in message:bin_msg+=bin(ord(i))[2:]

#Counting all symbols and thier occurences using Counter and storing them in descending order in the dictionary.
print('')
message_values=Counter(message)
sorted_message_values=dict(sorted(message_values.items(), key =lambda kv:(kv[1], kv[0]),reverse=True))
print("Printing number of occurences of each symbolin the given message:")
print('')
for i,j in sorted_message_values.items():print(str(i) +" | " +str(j))

enc_code={key: None for key in sorted_message_values.keys()}
count_vals=list(sorted_message_values.values())    



#Now we will form the groups for binary 0's and 1's assignment.
def SeperationIndex(count_values):
    eval_values=dict()
    for marker in range(len(count_values)):
        #print(marker)
        diff=sum(count_values[:marker])-sum(count_values[marker:])
        eval_values[marker]=diff
    global upper_grp
    global lower_grp
    for marker,j in eval_values.items():
        if j==min(a for a in eval_values.values() if a>=0):
            #print("marker:",marker)
            upper_grp=count_values[:marker]
            lower_grp=count_values[marker:]
            
    
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
    
        
            
    #print(enc_code)



SeperationIndex(count_vals)
Bit_Encoder(upper_grp,lower_grp)





if len(upper_grp)>1:
    #print(upper_grp)
    SeperationIndex(upper_grp)
    Bit_Encoder(upper_grp,lower_grp)




SeperationIndex(count_vals)
low1=lower_grp.copy()
if len(lower_grp)>1:
    #print(lower_grp)
    SeperationIndex(lower_grp)
    Bit_Encoder(upper_grp,lower_grp)

SeperationIndex(low1)

if len(low1)>1:
    #print(lower_grp)
    SeperationIndex(upper_grp)
    Bit_Encoder(upper_grp,lower_grp)



SeperationIndex(low1)    
if len(low1)>1:
    #print(lower_grp)
    SeperationIndex(lower_grp)
    Bit_Encoder(upper_grp,lower_grp)


print('---------------------------------------------------------------')
print('---------------------------------------------------------------')
print('---------------------------------------------------------------')

print('Printing the Shanon Fano codes:')
for i,j in enc_code.items():
    print(i,"|",j)

shrt_msg=str()
print('')    
print('We will now compare the encoded binary length and the original message binary length and see compression effeciency')    

#We will now compare the encoded binary length and the original message binary length and see compression effeciency

print('')   
for i in message:shrt_msg+=enc_code[i]
enc_str=str()
for i in message:
    enc_str+=enc_code[i]
    enc_str+=" "

print('Compressed message binary length:',len(shrt_msg))
print('Original message binary length:',len(bin_msg))

effeciency=round(((len(bin_msg)-len(shrt_msg))/len(bin_msg))*100,2)

print('Compression effeciency is:',effeciency,'%')
print('')

#Decoding our shortened message
print("Recovering our message.....")
print('')
recv_msg=str()
enc_arr=enc_str.split(' ')
for i in enc_arr:
	for a,b in enc_code.items():
		if (i==b):recv_msg+=a


print("Recovered message:",recv_msg)
print('')
if(recv_msg==message):print("Both messages match perfectly")    



















    

