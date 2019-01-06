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
```
def oracle0(qci,n,q1,q2):

    for i in range(n):    
    
      qci.s(q[i])     
      
    qci.cz(q[q1],q[q2]) 
    
    for i in range(n):  
    
        qci.s(q[i])    
 ```  
 
