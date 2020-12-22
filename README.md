# File-System-Emulation
## The main working code

------------

- First the number of threads are initialized. For x threads  x objects will be created of the class "**threading_class**"
- Then those threads are started and each thread read the *"input<x>.txt"* file. Here x is the numbers of threads. 
- Each thread read a line from the file and analyze it. That thread performs that function. Every thread functions this in this way. 
- Each thread is treated as a seperate program. In the "*output<x>.txt*" file , the output is stored in a way if that how the data will be stored in "*sample.dat*" file if there are no threads and the system is working just normal.
- Also, threads store data in "*smaple.dat*" file. But, before and after storing data, a function is applied which sync the file regarding in view the all threads.
- After the threads are completely executed, a memory map is displayed on the console just for any verification.

------------

## Changes made

------------

- Firstly, the "**fileHandling"** class functions were changed a bit. The arguments passing in them are optional. For example: example(self, *args). It certainly helps.
- Secondly, a new class is created named "**threading_class**".  
- Each object of "**threading_class**" class is considered as a thread. A thread is created in the class constructor.
- Different functions are implemented in this class. Some of them are :
	- Reading  the input file.
	- Calling "**fileHandling**" class functions dynamically.
	- Syncing the "*sample.dat*" file.

------------

