#FIRST NN
#OR gate TT
truth_table = {
    ( 1, 1) : 1,
    ( 0, 1) : 1,
    ( 1, 0) : 1,
    ( 0, 0) : -1
}
#EPOCHES
epochs = 8 #will run for itne iteration for now

#split into input and output lists
inputs = list(truth_table.keys())
targets = list(truth_table.values())

#STARTING WEIGHTS AND BIAS
W1 = 0
W2 = 0
bias = 0

#CHANGE IN WEIGHTS AND BIAS
Change_W1 = 0
Change_W2 = 0
Change_bias = 0

#Activation fxn 
# z to linear output 1,0,-1
def linear_fxn(z):
    if z>0.2:
        return 1
    elif -0.2 <= z <= 0.2:
        return 0
    else:
        return -1


for epoch in range(0,epochs):

    for i in range(0,len(inputs)):

        #inputs
        X1,X2 = inputs[i]
        #target
        t = targets[i]

        #aggregator fxn
        z = W1*X1 + W2*X2 + bias

        #get linear output
        y = linear_fxn(z) #get 1,0-1

        #NOw calculate changes and new weights by comparing y and t
        if(y != t):
            Change_W1 = X1*t
            Change_W2 = X2*t
            Change_bias = t
        else:
            Change_bias = 0
            Change_W1 = 0
            Change_W2 = 0

        #Change the value to new 
        W1 = W1 + Change_W1
        W2 = W2 + Change_W2
        bias = bias + Change_bias



print(f"w1 = {W1} and w2 = {W2} and bias = {bias}")