#changing the learning alpha 
#taking example of ANDNOT gate


#truth table
truth_table = {
    ( 1, 1) :-1,
    ( 1,-1) : 1,
    (-1, 1) :-1,
    (-1,-1) :-1 
}

#selecting learning rate 
#(0.2 for given example)
alpha = 0.2


#selecting epoches (if given)
#train for this many iteration
epochs = 2

#inputs x1 and x2
inputs = list(truth_table.keys())

#respective targets
targets = list(truth_table.values())


#calculate Y
def agregation_fxn(w1,x1,w2,x2,bias):
    return w1*x1 + w2*x2 + bias


#activation fxn
def activation_fxn(y):
    threshold=0
    if(y>=threshold):
        return 1
    else:
        return -1


#start with random or any weights and bias
#in between [1,No.Of.Nuerons]
w1 = 1
w2 = 1
bias = 1

#starting the training
for epoch in range(0,epochs):
    for i in range(len(inputs)):

        x1,x2 = inputs[i]
        t = targets[i]

        #calculating agregation
        y = agregation_fxn(w1,x1,w2,x2,bias)

        #Calculate Error for each input
        error = 
        