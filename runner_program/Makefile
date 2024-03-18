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

tests_run:
	exit 0

coverage:
	exit 0

debug: CFLAGS += -g3
debug: all

re: fclean all

.PHONY: fclean all clean re tests_run coverage debug \
		update_binary_location clean_binary_location

