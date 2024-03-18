##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

SRC	=	./main.cpp

OBJ	=	$(SRC:.cpp=.o)

CC	=	g++

CFLAGS	=	-Wall -Wextra -std=gnu17

CPPFLAGS	=	-iquote./include

NAME	=	runner

all:	$(NAME) update_binary_location

$(NAME):	$(OBJ)
	$(CC) -o $(NAME) $(OBJ) $(CFLAGS) $(CPPFLAGS)

update_binary_location:
	cp -vf $(NAME) ../

clean:
	rm -f $(OBJ)

clean_binary_location:
	rm -vf ../$(NAME)

fclean: clean clean_binary_location
	rm -f $(NAME)

re: fclean all clean

.PHONY: fclean all clean re \
		update_binary_location clean_binary_location

