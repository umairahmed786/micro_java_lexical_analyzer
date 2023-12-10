# Importing some libraries
import threading
from redblack import *
from transitionTable import *
from lexeme import *
import os




# Initialization of all the variables
bufferSize = 10
exitStatement = 'q'
response=[]
tokens=[]
buffer_1 = [''] * bufferLength
buffer_2 = [''] * bufferLength
raw=''
line_no=0
col_no=0
incomplete_token=""
col_no=0
tem_col=0
comment_started=False
chr_started=False

# Initialize a flag to control program termination
exit_flag = False

# Function to fill the buffer


dictionary = {
    r"int": "datatype",  
    r"float": "datatype",
    r"if|main|else|for|while|function|return": "keyword",
    r"\+|-|\*|/|==|!=|<|>": "operator",
    r"=|{|}|;|\(|\)": "delimiter",
    r"[a-zA-Z_][a-zA-Z_0-9]*": "identifier",
    r"\d+\.\d+|\d+\.\d*|\.\d+": "float",
    r"\d+": "int",
    r'"([^"\\]*(\\.[^"\\]*)*)"': "string",
}


tree =RBTree()



def process_data(buffer):
    global incomplete_token
    global col_no
    global line_no
    global tem_col
    global response
    global comment_started
    temp_word=incomplete_token
    global chr_started
    i=0
    while i<len(buffer):
        col_no+=1
        if buffer[i]!='':
            if buffer[i] =="/":
                # print(buffer[buffer.index(i)+1])
                if buffer[i+1]=="/":
                    comment_started=True
            if buffer[i]=='\n':
                comment_started=False
                col_no=0
                line_no+=1
            if not(comment_started):
                if buffer[i] in ("><=!"):
                    if buffer[i+1]=="=":
                        if temp_word!="":
                            # response.append(temp_word)
                            response.append(lexicalsymbol(line_no,col_no-len(temp_word),temp_word))

                            temp_word=""
                        # response.append(buffer[i]+buffer[i+1])
                        response.append(lexicalsymbol(line_no,col_no-len(buffer[i]),buffer[i]+buffer[i+1]))
                        i+=1
                        col_no+1
                        # break
                    elif temp_word!="":
                        # response.append(temp_word)
                        response.append(lexicalsymbol(line_no,col_no-len(temp_word),temp_word))
                        # response.append(buffer[i])
                        response.append(lexicalsymbol(line_no,col_no-len(buffer[i]),buffer[i]))
                    else:
                        # response.append(buffer[i])
                        response.append(lexicalsymbol(line_no,col_no-len(buffer[i]),buffer[i]))
                elif (ord(buffer[i])==34 or ord(buffer[i])==39 ) :
                    chr_started=not(chr_started)
                    temp_word+=buffer[i]
                elif buffer[i] in ("+-*.,?(}[)]{/")  and not(chr_started):
                    if temp_word!="":
                        # response.append(temp_word)
                        response.append(lexicalsymbol(line_no,col_no-len(temp_word),temp_word))
                        # response.append(buffer[i]) 
                        response.append(lexicalsymbol(line_no,col_no-len(buffer[i]),buffer[i]))
                        temp_word=""
                    else:
                        # response.append(buffer[i])
                        response.append(lexicalsymbol(line_no,col_no-len(buffer[i]),buffer[i]))
                elif (buffer[i]==" " or buffer[i]==";" or buffer[i]=='\r' or buffer[i]=='\n')  and not(chr_started):
                    if temp_word!="":
                        # response.append(temp_word)
                        response.append(lexicalsymbol(line_no,col_no-len(temp_word),temp_word))
                        temp_word=""
                    if buffer[i]=="\n":
                        col_no=0
                    tem_col=col_no
                else:
                    temp_word+=buffer[i]
            i+=1    
        else:
            i+=1    
    
    if temp_word!="":
        incomplete_token=temp_word
    else:
        incomplete_token=""


# Clearing the buffer
    for i in range(0,len(buffer)):
        buffer[i]=''
 




def fill_buffer(buffer):
    # useing global variables
    global exit_flag
    global incomplete_token
    global line_no
    global tem_col
    active_buffer = buffer_1 if buffer is buffer_1 else buffer_2
    activeIndex = 0

    f = open("code.txt", "r")
    for x in f:
        for i in x:
            input_data=i


            
            # If user press Enter button than move to the next line
            if input_data=='\n':
                # print("")
                print("")
                active_buffer[activeIndex] =input_data
                activeIndex = (activeIndex + 1) % bufferLength
            else:    
                print(str(input_data),end='',flush=True)
            
                # Check for exit command and process the buffer
                if input_data == exitStatement:
                    exit_flag = True

                    # If the previous buffer is half filled than process it before break
                    # if activeIndex!=0:
                    consumer_thread = threading.Thread(target=process_data, args=(active_buffer,))
                    consumer_thread.start()
                    consumer_thread.join()
                    if incomplete_token!="":
                        # for key in dictionary:
                        #     if re.match(key,incomplete_token):
                        #         token_type=dictionary[key]
                        #         break
                        # response.append({"token":incomplete_token,"line_no":line_no,"column_no":tem_col,"type":token_type})
                        # response.append(incomplete_token)
                        response.append(lexicalsymbol(line_no,col_no,incomplete_token))

                        # tokens.append(get_next_token(incomplete_token))


                        # if(tree.exists(response[len(response)-1]).val['token']==None):
                        #     tree.insert(response[len(response)-1])

                    break

                # adding chr into buffer
                active_buffer[activeIndex] = input_data
                activeIndex = (activeIndex + 1) % bufferLength

            # If buffer is full, put it for processing
            if activeIndex == 0:
                consumer_thread = threading.Thread(target=process_data, args=(active_buffer,))
                consumer_thread.start()

                # Shuffle the buffer for more input
                active_buffer = buffer_1 if active_buffer is buffer_2 else buffer_2
    
    
    consumer_thread = threading.Thread(target=process_data, args=(active_buffer,))
    consumer_thread.start()



# Create producer and consumer threads
producer_thread = threading.Thread(target=fill_buffer, args=(buffer_1,))

# Initializa first thread
producer_thread.start()

# Wait for the threads to finish
producer_thread.join()


# Printing all the tokenization
# print("\n***Tokenization of the source code.***")
# for i in range(0,len(response)):
#     print("Token "+str(i+1)+"= "+str(response[i]['token'])+" Line No:"+str(response[i]['line_no'])+" Column No:"+str(response[i]['column_no'])+" Type:"+str(response[i]['type']))


# print(response)

with open(os.path.dirname(os.path.abspath(__file__))+"\\output.txt",'w') as file:
        
        for token in response:
            file.write(f"Lexeme: {token.lexeme}\n")
            file.write(f"Row Number: {token.rowNum}\n")
            file.write(f"Column Number: {token.colNum}\n")
            file.write(f"Token Type: {token.tokenType}\n")
            file.write('-------------------------------\n')
            
            # print(tree.exists(token).val)
            
            if tree.exists(token).val==0:
                tree.insert(token)
file.close()



# print(tree)



# for i in range(0,len(response)):


# print(tree)