truth_table = {
    ( 1, 1) : 1,
    ( 1,-1) : 1,
    (-1, 1) : 1,
    (-1,-1) :-1 
}

#split into input and output lists
inputs = list(truth_table.keys())
targets = list(truth_table.values())

#EPOCHES
epochs = 2 #will run for itne iteration for now

#STARTING WEIGHTS AND BIAS
w1 = 0.1
w2 = 0.1
bias = 0.1

#learning rate
alpha = 0.1


#calculate Y
def agregation_fxn(w1,x1,w2,x2,bias):
    return w1*x1 + w2*x2 + bias

#best case
Best_w1 = 0
Best_w2 = 0
Best_bias = 0
min_error = 10000


for epoch in range(epochs):
    #total error
    Total_error = 0
    #Training
    print("X1 | X2 | T | Ynet | T-Ynet | squared | ")
    for i in range(len(targets)):
        #x1,x2,target
        x1,x2 = inputs[i]
        t = targets[i]

        #ynet calculate kiya
        y = agregation_fxn(w1,x1,w2,x2,bias)

        #error for each input
        error = t-y
        #Total error add kro
        Total_error+=error**2

        #error ke hisab sai change
        if error!=0:
            Change_w1 = alpha*error*x1
            Change_w2 = alpha*error*x2
            Change_bias = alpha*error
        else:
            Change_w1 = 0
            Change_w2 = 0
            Change_bias = 0
        
        #new weights values
        w1 = w1 + Change_w1
        w2 = w2 + Change_w2
        bias = bias + Change_bias

        #printing values
        print(f" {x1} | {x2} | {t} | {y:.4f} | {error:.4f} | {error**2:.4f} | ")
        

    #Total error
    print("Total error = ",Total_error)
    print()
    if(Total_error<min_error):
        min_error = Total_error
        Best_bias = bias
        Best_w1 = w1
        Best_w2 = w2
print("Training Finished Minimum Error = ",min_error)
print(f"w1 = {Best_w1:.4f} w2 = {Best_w2:.4f} bias = {Best_bias:.4f}")
    

