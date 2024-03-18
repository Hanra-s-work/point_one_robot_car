##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

SRC	=	./main.cpp

OBJ	=	$(SRC:.cpp=.o)

CC	=	g++

CFLAGS	=	-Wall -Wextra -str=gnu17

CPPFLAGS	=	-iquote./include

NAME	=	runner

all:	$(NAME)

$(NAME):	$(OBJ)
	$(CC) -o $(NAME) $(OBJ) $(CFLAGS) $(CPPFLAGS)

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all clean

.PHONY: fclean all clean re

