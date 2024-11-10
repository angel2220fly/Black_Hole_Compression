import os  
from time import time
import binascii
import math
import os.path
long_1=0
name=""
add_bits=""
Make_togher=""

print("Quantum computer 1 Billion Qubits or more")
name_input = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
        def cryptograpy_compression4(self):
                          
                def process_files(Number_of_the_file, Hole_Number_information, Add_Numbers, Multiply, counts):
                        Before_X = Number_of_the_file
                        Square_of_ROOT = Hole_Number_information
                        if Square_of_ROOT<=Key:
                               Square_of_ROOT=Key

                                   
                  
                                                                      
                                   
                        
                        Number_of_the_file =((((Number_of_the_file * Square_of_ROOT) + Add_Numbers) // 3) * Multiply)
                        #print(Number_of_the_file)
                        F=0
                        if counts==-1:
                                counts+=1
                                F=1
                        if Number_of_the_file == Before_X:
                            counts=counts
                        
                        else:
                            if F==0:
                                    counts+=1
                    
                
                        return Number_of_the_file, Square_of_ROOT, Add_Numbers, Multiply, counts
                self.name = "Written: Jurijus pacalovas"
                if name_input!="c" and name_input!="e":
                        print("The wrong letter")
                        raise SystemExit
                if name_input=="c" or name_input=="e":        
                    if name_input=="c":
                        i=1
                    if name_input=="e":
                        i=2
                    Clear=""
                    name = input("What is name of file? ")
                    if name_input=="c":
                        X3 = int(input("Strong compress of X3 from 0-69 or more? "))
                       
                    Key = 1
                    level = 2
                    L=40
                    
                    
        
                    
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    x=0
                    C1=1
                    x1=0
                    x2=0
                    x3=0
                    X2=0
                    C1=0
                    C2=0
                    C3=0
                    C4=0
                    C5=0
                    n=0
                    x = time()
                    File_information6_Times2_1=0
                    name_2=name
                    Long_Change=len(name_2)
                    compress_or_not_compress=1
                    File_information6_Times3=0
                    if i==2:
                        C=1
                    Long_Change=len(name_2)
                    s=""
                    File_information5=""
                    File_information5_2=""
                    Clear=""
                    Translate_info_Decimal=""
                    D=0
                    long_name=len(name)
           
                    with open(name, "rb") as binary_file:
                        data = binary_file.read()
                        s=str(data)
                        long_11=len(data)
                        long_17=len(data)
                        if long_17==0:
                        	 raise SystemExit
                        END_working=0
                        File_information6_Times2=0
                        File_information5_23=""
                        INFO18=""
                        File_information5_29=""
                        SpinS=0
                        while END_working<10:
                            File_information6_Times3=File_information6_Times3+1
                            D=1
                            if D==1:
                                if File_information6_Times3==1:
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]#data to binary
                                    long_1=len(INFO)
                                    long_11=len(data)
                                    count_bits=(long_11*8)-long_1
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1
                                    if File_information6_Times3==1:
                                        File_information5_2=INFO
                                    n = int(File_information5_2, 2)
                                    width_bits=len(File_information5_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    data=width_bits3
                                    long_15=len(data)
                                    INFO=bin(int(binascii.hexlify(data),16))[2:]
                                    long_1=len(INFO)
                                    long_11=len(data)
                                    count_bits=(long_11*8)-long_1
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            INFO="0"+INFO
                                            z=z+1
                                    File_information5_2=INFO
                                    Extact=File_information5_2
                                    A=int(Extact,2)                                    
                                
                                        
                                    long_13=len(File_information5_2)
                                long_12=len(File_information5_2)
                                if i==1:
                                    if long_17>=(2**26)-1 and i==1:
                                        print("print file is too big!")
                                        raise SystemExit
                                if i==1:
                                    y=0            
                                    k1=-2
                                    k2=-1
                                    k3=1
                                    X1=1
                                    Extract1=0
                                    Multiply=1
                                    Add_Numbers=-1
                                    Times_12=1
                                    University=-1
                                    Divide=1  
                                    counts=-1
                                    SQUEAR_OF_ROOT=-1
                                    Multiply_Times=0
                                    while Extract1!=1:
                                            k1+=1
                                            k2+=1
                                            k3+=1
                                            University=int(k2)
                                            X2=X1
                                            #print(X1)
                                            C11="0"+str(((8*X2)+L))+"b"
                                         
                                            if X1>(2**255):
                                                
                                                    counts=0
                                                
                                                    
                                                    k3+=1
                                                    
                                            if k3%(2**255)==0:
                                                
                                                    counts=0
                                                    X1+=1
                                                    
                                                    k3=1

                                            
                                           
                                            University_file=format(University,C11)
                                            Divide=int(University_file[0:(X2*8)],2)
                                            Times_12=int(University_file[(X2*8):(X2*8)+8],2)
                                            Multiply=int(University_file[(X2*8)+8:(X2*8)+16],2)
                                            Add_Numbers=int(University_file[(X2*8)+16:(X2*8)+24],2)
                                            SQUEAR_OF_ROOT=int(University_file[(X2*8)+24:(X2*8)+32],2)
                                            Multiply_Times=int(University_file[(X2*8)+32:(X2*8)+40],2)
                              
                                            # Increment X1 by 'i' and reset counts to 0 if Times_12 is greater than 2**i
                                            
                                            if Times_12 > 2**y:
                                                    X1 += 1
                                                    counts = 0 # Reset counts to 0
                                            
                                            
                                            if Times_12>2**21:
                                                Times_12=0
                                               

                                                counts=0
                                                X1+=1
                                                y=0        




                                                                                    

                                            if Divide==0:
                                            	Divide=1
                                            if Times_12==0:
                                                Times_12=1 
                                            if Multiply==0:
                                                Multiply=1 
                                            File_information52=""
                                            File_information53=""
                                            File_information54=""
                                            Add_N=""
                                            File_information52=format(SQUEAR_OF_ROOT,'024b')
                                            File_information53=format(Multiply,'024b')
                                            Add_N=format(Add_Numbers,'024b')
                                            if   File_information6_Times2==0:
                                                File_information54=format(Multiply_Times,'040b')
                                                File_information5_2=File_information54
                                            File_information54=File_information5_2
                                            File_information53=format(Multiply,'024b')                                            
                                            File_information5_2=File_information54
                                            File_information5_17=""
                                            long_16=len(File_information54)
                                            add_bits=""
                                            Clear=""
                                            INFO10=""
                                            Translate_info_Decimal=""
                                            Clear=""
                                            Number_of_the_file=0
                                            C=1
                                            if C==1:
                                                if   File_information6_Times2==0:
                                                        long_16=len(File_information54)
                                                        INFO10=File_information52
                                                        Deep5 = int(INFO10, 2)
                                                        long_16=len(File_information54)
                                                        File_information54=File_information5_2
                                                        Clear=File_information53
                                                        Add_N=Add_N
                                                        T = int(Clear, 2)
                                                        Add= int(Add_N, 2)
                                                        long_16=len(File_information54)
                                                        Times_half_Real=0
                                                if   File_information6_Times2>0:
                                                        Translate_info_Decimal_2=0
                                                if C==1 and Times_12!=0:
                                                        File_information54=File_information54
                                                        long_16=len(File_information54)
                                                        if len (File_information54)!=0:
                                                            Number_of_the_file=int(File_information54, 2)
                                                        else:
                                                            Number_of_the_file=0
                                                        if Deep5<=26*1024*1024:
                                                                Hole_Number_information=(2**Deep5)-1
                                                        else:
                                                                Deep5=26*1024*1024
                                                                Hole_Number_information=(2**Deep5)-1
                                                                
                                                        Square_of_ROOT=Hole_Number_information
                                                        Number_of_the_file, Hole_Number_information, Add_Numbers, Multiply, counts = process_files(Number_of_the_file, Hole_Number_information, Add_Numbers, Multiply, counts)

                                                        Times_half_Real+=1
                                            File_information5_17=bin(Number_of_the_file)[2:]
                                            File_information5_2=File_information5_17
                                            if i==1:
                                                Make_togher=""
                                                Make_togher=Clear
                                                add_bits=""
                                                if C==1 and Times_12!=0:
                                                        File_information6_Times2=File_information6_Times2+1
                                                long_19=len(File_information5_17)
                                                if  File_information6_Times2==Times_12:
                                                        File_information6_Times2_1=File_information6_Times2
                                                        File_information6_Times2=0
                                                        if int(INFO,2)<=Number_of_the_file:  
                                                               if C==1:
                                                                       C=1
                                                if int(INFO,2)<=Number_of_the_file and File_information6_Times2_1==Times_12:
                                                       long_1=len(File_information5_17)
                                                       Time_Real3=bin(long_12)[2:]
                                                       T1=len(Time_Real3)
                                                       Time_Real4=format(T1,'08b')
                                                       long_file=Time_Real4+Time_Real3
                                                       Time_Real3=bin(X1)[2:]
                                                       T1=len(Time_Real3)
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'08b')
                                                       XN=Time_Real4+Time_Real1+Time_Real3
                                                       Time_Real3=bin(counts)[2:]
                                                       T1=len(Time_Real3)
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'08b')
                                                       Counts=Time_Real4+Time_Real1+Time_Real3
                                                       M=Number_of_the_file-int(INFO,2)
                                                       #print(M)
                                                       Time_Real3=bin(M)[2:]
                                                       T1=len(Time_Real3)
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'08b')
                                                       MN=Time_Real4+Time_Real1+Time_Real3
                                                       Time_Real3=bin(k3)[2:]
                                                       T1=len(Time_Real3)
                                                       Time_Real1=bin(T1)[2:]
                                                       T2=len(Time_Real1)
                                                       Time_Real4=format(T2,'08b')
                                                       MN2=Time_Real4+Time_Real1+Time_Real3                                                    
                                                       
                                                       Long_PM=File_information5_17="1"+MN2+MN+XN+Counts+long_file
                                                       Long_PM1=len(Long_PM)
                                                       #print(Long_PM1)
                                                       
                                                       if int(INFO,2)<=Number_of_the_file and Long_PM1+X3<len(data)*8 and File_information6_Times2_1==Times_12 or int(INFO,2)==Number_of_the_file  and File_information6_Times2_1==Times_12:
                                                               File_information5_17="1"+MN2+MN+XN+Counts+long_file
                                                               long_1=len(File_information5_17)
                                                               add_bits=""
                                                               count_bits=8-long_1%8
                                                               z=0
                                                               if count_bits!=0:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1
                                                               File_information5_17=add_bits+File_information5_17
                                                               Extract1=1
                                    if Extract1==1:                
                                            L=len(File_information5_17)
                                            n = int(File_information5_17, 2)
                                            width_bits=len(File_information5_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)
                                            File_information5_2=Clear
                                            name=name+".bin"
                                   
                                    
                                            with open(name, "wb") as f2:
                                                f2.write(width_bits3)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            xs=str(xs)
                                            return xs;

                                if i==2:
                                    if C==1:
                                        if   File_information6_Times2==0:
                                            File_information5=INFO
                                        if   File_information6_Times2==0:
                                                long_16=len(File_information5)

                                                if File_information5[:1]=="0":
                                                    while File_information5[:1]!="1":
                                                        if File_information5[:1]=="0":
                                                            File_information5=File_information5[1:]
                                                            
                                                            
                                                if File_information5[:1]=="1":
                                                    File_information5=File_information5[1:]
                                                    

                                                                                
                                                Random_C=int(File_information5[0:8],2)
                                                File_information5=File_information5[8:]
                                                Random_C1=int(File_information5[:Random_C],2)
                                                File_information5=File_information5[Random_C:]
                                                k4=int(File_information5[:Random_C1],2)
                                                File_information5=File_information5[Random_C1:]
                                                Random_C=int(File_information5[0:8],2)
                                                    
                                                File_information5=File_information5[8:]
                                                Random_C1=int(File_information5[:Random_C],2)
                                                File_information5=File_information5[Random_C:]
                                                MN=int(File_information5[:Random_C1],2)
                                               
                                                File_information5=File_information5[Random_C1:]
                                                                         


                                                Random_C=int(File_information5[0:8],2)
                                                File_information5=File_information5[8:]
                                                Random_C1=int(File_information5[:Random_C],2)
                                                File_information5=File_information5[Random_C:]
                                                XR=int(File_information5[:Random_C1],2)
                                                File_information5=File_information5[Random_C1:]
                                                Random_C=int(File_information5[0:8],2)
                                                File_information5=File_information5[8:]
                                                Random_C1=int(File_information5[:Random_C],2)
                                                File_information5=File_information5[Random_C:]
                                                Extract_info=int(File_information5[:Random_C1],2)
                                                File_information5=File_information5[Random_C1:]
                                                Random_C=int(File_information5[0:8],2)
                                                File_information5=File_information5[8:]
                                                long=int(File_information5[:Random_C],2)
                                                File_information5=File_information5[Random_C:]
                                    
                                    y=0            
                                    k1=-2
                                    k2=-1
                                    k3=1
                                    X1=1
                                    Extract1=0
                                    Multiply=1
                                    Add_Numbers=-1
                                    Times_12=1
                                    University=-1
                                    Divide=1  
                                    counts=-1
                                    SQUEAR_OF_ROOT=-1
                                    Multiply_Times=0
                                    while Extract1!=1:
                                            k1+=1
                                            k2+=1
                                            k3+=1
                                            University=int(k2)
                                            X2=X1
                                            #print(X1)
                                            C11="0"+str(((8*X2)+L))+"b"
                                            if X1>(2**255):
                                                
                                                    counts=0
                                                
                                                    
                                                    k3+=1
                                                    
                                            if k3%(2**255)==0:
                                                
                                                    counts=0
                                                    X1+=1
                                                    
                                                    k3=1                             
                                           
                                            University_file=format(University,C11)
                                            Divide=int(University_file[0:(X2*8)],2)
                                            Times_12=int(University_file[(X2*8):(X2*8)+8],2)
                                            Multiply=int(University_file[(X2*8)+8:(X2*8)+16],2)
                                            Add_Numbers=int(University_file[(X2*8)+16:(X2*8)+24],2)
                                            SQUEAR_OF_ROOT=int(University_file[(X2*8)+24:(X2*8)+32],2)
                                            Multiply_Times=int(University_file[(X2*8)+32:(X2*8)+40],2)
                              
                                            # Increment X1 by 'i' and reset counts to 0 if Times_12 is greater than 2**i
                                            
                                            if Times_12 > 2**y:
                                                    X1 += 1
                                                    counts = 0 # Reset counts to 0
                                            
                                            
                                            if Times_12>2**21:
                                                Times_12=0
                                               

                                                counts=0
                                                X1+=1
                                                y=0        




                                                                                    

                                            if Divide==0:
                                            	Divide=1
                                            if Times_12==0:
                                                Times_12=1 
                                            if Multiply==0:
                                                Multiply=1 
                                            File_information52=""
                                            File_information53=""
                                            File_information54=""
                                            Add_N=""
                                            File_information52=format(SQUEAR_OF_ROOT,'024b')
                                            File_information53=format(Multiply,'024b')
                                            Add_N=format(Add_Numbers,'024b')
                                            if   File_information6_Times2==0:
                                                File_information54=format(Multiply_Times,'040b')
                                                File_information5_2=File_information54
                                            File_information54=File_information5_2
                                            File_information53=format(Multiply,'024b')                                            
                                            File_information5_2=File_information54
                                            File_information5_17=""
                                            long_16=len(File_information54)
                                            add_bits=""
                                            Clear=""
                                            INFO10=""
                                            Translate_info_Decimal=""
                                            Clear=""
                                            Number_of_the_file=0
                                            C=1
                                            if C==1:
                                                if   File_information6_Times2==0:
                                                        long_16=len(File_information54)
                                                        INFO10=File_information52
                                                        Deep5 = int(INFO10, 2)
                                                        long_16=len(File_information54)
                                                        File_information54=File_information5_2
                                                        Clear=File_information53
                                                        Add_N=Add_N
                                                        T = int(Clear, 2)
                                                        Add= int(Add_N, 2)
                                                        long_16=len(File_information54)
                                                        Times_half_Real=0
                                                if   File_information6_Times2>0:
                                                        Translate_info_Decimal_2=0
                                                if C==1 and Times_12!=0:
                                                        File_information54=File_information54
                                                        long_16=len(File_information54)
                                                        if len (File_information54)!=0:
                                                            Number_of_the_file=int(File_information54, 2)
                                                        else:
                                                            Number_of_the_file=0
                                                        Hole_Number_information=(2**Deep5)-1
                                                        Square_of_ROOT=Hole_Number_information
                                                        
                                                        if Deep5<=26*1024*1024:
                                                                Hole_Number_information=(2**Deep5)-1
                                                        else:
                                                                Deep5=26*1024*1024
                                                                Hole_Number_information=(2**Deep5)-1 
                                                        Number_of_the_file, Hole_Number_information, Add_Numbers, Multiply, counts = process_files(Number_of_the_file, Hole_Number_information, Add_Numbers, Multiply, counts)

                                                        Times_half_Real+=1
                                            File_information5_17=bin(Number_of_the_file)[2:]
                                            File_information5_2=File_information5_17
                                            if i==2:
                                                Make_togher=""
                                                Make_togher=Clear
                                                add_bits=""
                                                if C==1 and Times_12!=0:
                                                        File_information6_Times2=File_information6_Times2+1
                                                long_19=len(File_information5_17)
                                                if  File_information6_Times2==Times_12:
                                                        File_information6_Times2_1=File_information6_Times2
                                                        File_information6_Times2=0
                                                        if int(INFO,2)==Number_of_the_file:  
                                                               if C==1:
                                                                       C=1
                                                if Extract_info==counts and File_information6_Times2_1==Times_12 and X1==XR and k4==k3:
                                                       long_1=len(File_information5_17)
                                                       if Extract_info==counts and File_information6_Times2_1==Times_12 and X1==XR:
                                                               CN="0"+str(long)+"b"
                                                               File_information5_17=format(Number_of_the_file-MN,CN)
                                                               Extract1=1
                                    if Extract1==1:                
                                            L=len(File_information5_17)
                                            n = int(File_information5_17, 2)
                                            width_bits=len(File_information5_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)
                                            File_information5_2=Clear
           
                                            long_extract=len(name)
                                            name=name[:long_extract-4]
                                            with open(name, "wb") as f2:
                                                f2.write(width_bits3)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            xs=str(xs)
                                            return xs;
d=compression()
xw1=d.cryptograpy_compression4()
print(xw1)
