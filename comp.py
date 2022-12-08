A=int(input('Enter lower limit: '))
B=int(input('Enter upper limit: '))
c_count=0
p_count=0
for i in range(A,B+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                print(i,'is composite')
                c_count+=1
                break
        else:
            p_count+=1
            print(i,'is prime')
    else:
        c_count+=1
        print(i,'is composite')
print('There are',p_count,'prime and',c_count,'composite numbers in the range')
