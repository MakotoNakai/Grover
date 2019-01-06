# Grover

## The problem this algorithm is trying to aim.  

This algorithm can search the desired choice among unorganized database.

## Process to achive the goal.

I'm going to talk about the case that I want to choose <img src="https://latex.codecogs.com/gif.latex?|00\rangle" title="|00\rangle" />.   

### 1.Create the superposition. 

The first thing you have to do is to put hadamard gates on all the qubits.  In this repository, I prepared 2 qubits. 
So, I got 4 choices.
![screen shot 2019-01-06 at 11 30 44 pm](https://user-images.githubusercontent.com/45162150/50737335-2ff47180-120b-11e9-831d-39d1e545fc19.png) 

### 2. Put the phase oracle,which flips the phase of your desired choice.

After you create the superposition, you have to put something called the phase oracle.  
The following codes is those of the phase oracle for <img src="https://latex.codecogs.com/gif.latex?|00\rangle" title="|00\rangle" />.
  
`  
def oracle0(qci,n,q1,q2):
    for i in range(n):
        qci.s(q[i])
    qci.cz(q[q1],q[q2])
    for i in range(n):
        qci.s(q[i])  
 `  
 In order to make sure that the phase of <img src="https://latex.codecogs.com/gif.latex?|00\rangle" title="|00\rangle" />, you have to write the following code after you measure the quantum states.  
 
 `
backend = BasicAer.get_backend('statevector_simulator')
job = execute(qc,backend)
result = job.result()
outputstate = result.get_statevector(qc, decimals=3)
print(outputstate)
`  
The outcome would be [ -0.5+0.j  0.5+0.j  0.5+0.j 0.5+0.j]  
  
### 3. Subtract probability of the phase from their average, and add it to the average again.  

First, the probability of getting each states are 50% and the one for the desired choice is just flipped, which is -50%.

Then, I substract it from the average of all the probability((50+50+50-50)/4 = 25%), so the outcome would be 75%.  
After that, I should add that value to the average again, which would end up to be 100%.

You can realize this by putting the following codes.  
'bn is the number of qubits, which is 2 in this case.
for j in range(bn):
    qc.h(q[j])
    qc.x(q[j])
oracle0(qc,2,0,1)
for k in range(bn):
    qc.x(q[k])
    qc.h(q[k])
 `  
 
 ### 4. Measure the quantum states.  
 
 This is the result on the QASM simulator.
        


 
