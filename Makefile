##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

# The folders of the trainer and runners

TRAINER_DIR	=	./trainer_program

RUNNER_DIR	=	./runner_program

SILENT	=	@

NOISY_BUILD	=	noop

# Compile the projects

# Colour codes
C_BACKGROUND	=	\033[48;5;16m
C_PINK	=	\033[38;5;206m$(C_BACKGROUND)
C_RESET	=	\033[0m$(C_BACKGROUND)
C_GREEN	=	\033[38;5;46m$(C_BACKGROUND)
C_RED	=	\033[38;5;9m$(C_BACKGROUND)

all: runner trainer

runner:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) all

trainer:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) all

# Clean the cache projects

clean: runner_clean trainer_clean 

runner_clean:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) clean

trainer_clean:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) clean

# Clean the binaries produced

fclean: runner_fclean trainer_fclean 

runner_fclean:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) fclean

trainer_fclean:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) fclean

# Run the tests for the programs

tests_run: runner_tests_run trainer_tests_run 

runner_tests_run:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) tests_run

trainer_tests_run:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) tests_run

# Check the coverage for the programs

coverage: runner_coverage trainer_coverage 

runner_coverage:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) coverage

trainer_coverage:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) coverage

# Create the debug versions for the program

debug: runner_debug trainer_debug 

runner_debug:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) debug

trainer_debug:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) debug

# Create the re function
re: fclean all

# Show all
noisy:
	@echo -e "$(C_PINK)Silent mode is $(C_RED)inactive$(C_RESET)"
	$(eval SILENT=)
	$(eval NOISY_BUILD:=noisy)

# Only show the warnings and errors
noop:
	@echo -e "$(C_PINK)Silent mode is $(C_GREEN)active$(C_RESET)"
	$(eval SILENT=@)
	$(eval NOISY_BUILD:=noop)

silent: noop

# The .PHONY to to avoid functions being overriden

.PHONY: all clean fclean tests_run coverage debug re noisy noop silent	\
		runner runner_clean runner_fclean runner_tests_run runner_coverage \
		runner_debug \
		trainer trainer_clean trainer_fclean trainer_tests_run \
		trainer_coverage trainer_debug \


