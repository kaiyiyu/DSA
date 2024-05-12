# Purpose: Makefile for C array implementation

CC = gcc
CFLAGS = -Wall -Werror -g 
OBJ = array.o
EXEC = array

$(EXEC): $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

array.o: array.c 
	$(CC) $(CFLAGS) -c array.c

clean:
	rm -f $(EXEC) $(OBJ)