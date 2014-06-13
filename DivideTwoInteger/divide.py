#! /usr/bin/python

max=0
i_max=0
j_max=0
k_max=0
for i in range(101):
   for j in range(101):
     for k in range(101):
        if i*j+j*k+k*i-2*i-2*j-2*k-46==0:
           if  i*j*k>=max:
               max=i*j*k
	       i_max=i
               j_max=j
               k_max=k
	       print max, (i_max,j_max,k_max)

