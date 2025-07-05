# Mario Bros for RISC OS
A remake of the NES version of Mario Bros for RISC OS, programmed in C using OSLib.
 
## How to run
1. Go on a RISC OS machine or emulator (I used RPCEmu RISC OS Direct (5.27) Easy Start Bundle: https://www.marutan.net/rpcemu/easystart.html)
2. Navigate to the root folder (MarioBrosRiscOS)
3. Double click !MarioBros
4. Press ENTER to start and pause whilst playing. The controls are the left and right arrow keys, and X to jump

## How to compile
### The program is already compiled with an executable, but to compile the program:
1. Go on a RISC OS machine or emulator (I used RPCEmu RISC OS Direct (5.27) Easy Start Bundle: https://www.marutan.net/rpcemu/easystart.html)
2. Make sure GCC, OSLib and SharedCLibrary are installed and running
3. Open a Task Window with at least 16000K of memory
4. Set the directory to the root folder (MarioBrosRiscOS)
5. Type 'make' in the Task Window and wait for the program to compile
