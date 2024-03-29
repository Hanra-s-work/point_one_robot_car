##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

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
all:
	$(SILENT) make SILENT=$(SILENT) -C ./curve_fitting

clean:
	$(SILENT) make SILENT=$(SILENT) -C ./curve_fitting clean

fclean: clean
	$(SILENT) make SILENT=$(SILENT) -C ./curve_fitting fclean

tests_run:
	$(SILENT) make SILENT=$(SILENT) -C ./curve_fitting tests_run

coverage:
	$(SILENT) make SILENT=$(SILENT) -C ./curve_fitting coverage

debug: 
	$(SILENT) make SILENT=$(SILENT) -C ./curve_fitting debug

re: fclean all

.PHONY: fclean all clean re tests_run coverage debug

