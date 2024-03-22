##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

# The source fies

SRC	=	./src/main.cpp

# The object files

OBJ	=	$(SRC:.cpp=.o)

# The compiler users

CC	=	g++

# The flags that are to be applied during the compilation

CFLAGS	=	-Wall -Wextra

# The location of the header files

CXXFLAGS	=	-iquote./include

# Library directory

LIB_DIR = -L./libs

# Libraries

LIBS = # -llib1 -llib2

# The final name of the binary

NAME	=	runner

# Silence the outputs we wish not to listen to
SILENT	=	@

# Colour codes
C_BACKGROUND	=	\033[48;5;16m
C_RED	=	\033[38;5;9m$(C_BACKGROUND)
C_PINK	=	\033[38;5;206m$(C_BACKGROUND)
C_CYAN	=	\033[38;5;87m$(C_BACKGROUND)
C_BLUE	=	\033[38;5;45m$(C_BACKGROUND)
C_WHITE	=	\033[38;5;15m$(C_BACKGROUND)
C_GREEN	=	\033[38;5;46m$(C_BACKGROUND)
C_RESET	=	\033[0m$(C_BACKGROUND)
C_YELLOW	=	\033[38;5;226m$(C_BACKGROUND)

# Compile the project
all:	update_libraries $(NAME) update_binary_location

$(NAME):	$(OBJ)
	@echo -e "$(C_BLUE)Building binary '$(C_YELLOW)$(NAME)$(C_BLUE)'$(C_RESET)"
	$(SILENT) $(CC) -o $(NAME) $(OBJ) $(CFLAGS) $(CXXFLAGS) $(LIB_DIR) $(LIBS)
	@echo -ne "$(C_BLUE)Binary '$(C_YELLOW)$(NAME)$(C_BLUE)' "
	@echo -e  "$(C_GREEN)built$(C_RESET)"

update_libraries:
	@echo -e "$(C_BLUE)Building libraries$(C_RESET)"
	$(SILENT) make SILENT=$(SILENT) -C ./libs
	@echo -e "$(C_BLUE)Libraries $(C_GREEN)built$(C_RESET)"

update_binary_location:
	@echo -e "$(C_PINK)Updating binary locations$(C_RESET)"
	$(SILENT) cp -vf $(NAME) ../
	@echo -e "$(C_PINK)Binary locations $(C_GREEN)updated$(C_RESET)":

clean:
	$(SILENT) make SILENT=$(SILENT) -C ./libs clean
	$(SILENT) rm -f $(OBJ)

clean_binary_location:
	$(SILENT) rm -vf ../$(NAME)

fclean: clean clean_binary_location
	$(SILENT) make SILENT=$(SILENT) -C ./libs fclean
	$(SILENT) rm -f $(NAME)

tests_run:
	$(SILENT) make SILENT=$(SILENT) -C ./libs tests_run
	$(SILENT) exit 0

coverage:
	$(SILENT) make SILENT=$(SILENT) -C ./libs coverage
	$(SILENT) exit 0

build_library_as_debug:
	$(SILENT) make SILENT=$(SILENT) -C ./libs debug

debug: CFLAGS += -g3
debug: build_library_as_debug all

re: fclean all

noisy:
	@echo -e "$(C_PINK)Silent mode is $(C_RED)inactive$(C_RESET)"
	$(eval SILENT=)

noop:
	@echo -e "$(C_PINK)Silent mode is $(C_GREEN)active$(C_RESET)"
	$(eval SILENT=@)

silent: noop

.PHONY: fclean all clean re tests_run coverage debug noisy noop silent \
		update_binary_location clean_binary_location update_libraries	\
		build_library_as_debug

