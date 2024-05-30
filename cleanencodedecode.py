# required modules imported
# random modules helping us with the operations to generate much stronger and random characters
# string module to work with different methods of the string

import random    
import string
# this helps with the generating of the random strings we'll need later on the program

def pref(length): 
    result = ''.join((random.choice(string.ascii_lowercase) for x in range(length)))
    return result
# this userdefined function helps with the genneration of the encrypted form of the strings entered by the user

def encode():
    userin=input("ENTER THE STRING TO ENCODE  : ")
    if(len(userin)<10):
        nuserin=userin[::-1]
        nuserin=(pref(len(userin)) + str(nuserin) + str(len(userin)))
        print("the encoded version of the string is",nuserin,"\n")
        print("the Un-Encoded version of the input is",userin)
        final=str(input("press Undo to reverse the Encoding process!!"))
        if(final.capitalize()=="Undo"):
            nuserin=userin
            print("the Encoding of the string is Undone sucesfully")
        else:
            print("wrong input!!")
            print("assuming the user does not want to Undo the operation>>>")    
        re=str(input("Press RE to perform the operation again"))
        if(re=='RE'):
            main_menu()
        else:
            print("not transferring into the main menu")
        decoder_again=input("Press Decode_agn to decode the encoded version")
        if(decoder_again.capitalize()=='Decode_agn'):
            decode()
    else:
        print("THE INPUT PARAMETERS TOO HIGH")
        print("input the string less than 10")
        to_Re=input("Enter Again to re perform: \n")
        if(to_Re.capitalize()=='Again'):
            encode()
    
# decode function with the purpose of decoding the code encoded by the funciton above

def decode():
    user_in=input("ENTER THE ENCODED STRING TO FURTHER DECODE:\n ")
    finding_length=int(user_in[-1])
    new_userin=user_in[finding_length:]
    new_userin=new_userin[::-1]
    decoded_versn=new_userin[1:]
    print(f"THE DECODED VERSION OF {user_in} is {decoded_versn}")

#  all the controls and the menu of the program to be accessed as well as monitored by the main_menu funciton

def main_menu():
    print("what do you expect to do with this programm??")
    print("ENCODE || DECODE")
    print("Enter the response in all CAPS")
    act=input("Enter the action to be performed: ")
    if(act.capitalize()=='Encode'):
        encode()
    elif(act.capitalize()=='Decode'):
        decode()

# main menu function call to inititate the program on command.
main_menu()
