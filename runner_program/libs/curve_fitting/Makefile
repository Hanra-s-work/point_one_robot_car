##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

SRC	=	./main.cpp	\

CC	=	g++

OBJ	=	$(SRC:.cpp=.o)

RM	=	rm -f

CP	=	cp -f

CXXFLAGS := -Wall -Wextra

CPPFLAGS	:=	-iquote ../../include

INCLUDE_FILE	:=	curve_fitting.hpp

NAME	=	libcurve_fitting.a

all:	update_include_files $(NAME) update_library_path

$(NAME):	$(OBJ)
		ar rc $(NAME) $(OBJ) 

update_include_files:
	$(CP) $(INCLUDE_FILE) ../../include/

update_library_path:
	$(CP) $(NAME) ../$(NAME)
	$(CP) $(NAME) ../../$(NAME)

clean:
		$(RM) $(OBJ)

fclean: clean
		$(RM) $(NAME)
		$(RM) ../$(NAME)
		$(RM) ../../$(NAME)

tests_run:
	@exit 0

coverage:
	@exit 0

debug:
	@exit 0

re:	fclean all

.PHONY:	all update_include_files update_library_path clean fclean re \
		tests_run coverage debug
