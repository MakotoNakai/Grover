
# coding: utf-8

from qiskit import IBMQ, QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer
from qiskit.qasm import pi
from qiskit.tools.visualization import plot_histogram, circuit_drawer
import numpy as np

APItoken = "Replace me"
url = "Replace me"
IBMQ.enable_account(APItoken, url)

IBMQ.backends()

#Oracle to maximize the probability to get |01>
def oracle01(qci,s,q1,q2):
    qci.s(q[s])
    qci.cz(q[q1],q[q2])
    qci.s(q[s])
        
bn = 2
cn = 2

q = QuantumRegister(bn)
c = ClassicalRegister(cn)
qc  = QuantumCircuit(q,c)

for i in range(bn):
    qc.h(q[i])
qc.cz(q[0],q[1])

for j in range(bn):
    qc.h(q[j])
    qc.x(q[j])
    
    
oracle01(qc,0,0,1)

for k in range(bn):
    qc.x(q[k])
    qc.h(q[k])

for l in range(bn):
    qc.measure(q[bn-l-1],c[l])

#Put a real device first and a simulator after that
backends = ['ibmq_20_tokyo', 'qasm_simulator']

#Use this for the actual machine
#backend_sim = IBMQ.get_backend(backends[0])
#{'00': 430, '01': 3464, '10': 77, '11': 125}

#Use this for the simulation
#backend_sim = Aer.get_backend(backends[1])#{'01': 4096}
result = execute(qc, backend_sim, shots=4096).result()

#If you execute the following command, you would get the quantum circuit in Latex form
#circuit_drawer(qc).show()

print(result.get_counts(qc))
plot_histogram(result.get_counts(qc))
