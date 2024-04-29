##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

# The folders of the trainer and runners

TRAINER_DIR	=	./trainer_program

RUNNER_DIR	=	./runner_program

RUNNER_2_DIR	=	./runner_program2

SILENT	=	@

NOISY_BUILD	=	noop

# Compile the projects

# Colour codes
C_BACKGROUND	=	\033[48;5;16m
C_PINK	=	\033[38;5;206m$(C_BACKGROUND)
C_RESET	=	\033[0m$(C_BACKGROUND)
C_GREEN	=	\033[38;5;46m$(C_BACKGROUND)
C_RED	=	\033[38;5;9m$(C_BACKGROUND)

all: runner trainer runner2

runner:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) all

runner2:
	$(SILENT) make -C $(RUNNER_2_DIR) $(NOISY_BUILD) all

trainer:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) all

# Clean the cache projects

clean: runner_clean trainer_clean runner2_clean

runner_clean:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) clean

runner2_clean:
	$(SILENT) make -C $(RUNNER_2_DIR) $(NOISY_BUILD) clean

trainer_clean:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) clean

# Clean the binaries produced

fclean: runner_fclean runner2_fclean trainer_fclean 

runner_fclean:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) fclean

runner2_fclean:
	$(SILENT) make -C $(RUNNER_2_DIR) $(NOISY_BUILD) clean

trainer_fclean:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) fclean

# Run the tests for the programs

tests_run: runner_tests_run runner2_test_run trainer_tests_run 

runner_tests_run:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) tests_run

runner2_test_run:
	$(SILENT) make -C $(RUNNER_2_DIR) $(NOISY_BUILD) tests_run

trainer_tests_run:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) tests_run

# Check the coverage for the programs

coverage: runner_coverage runner2_coverage trainer_coverage 

runner_coverage:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) coverage

runner2_coverage:
	$(SILENT) make -C $(RUNNER_2_DIR) $(NOISY_BUILD) coverage

trainer_coverage:
	$(SILENT) make -C $(TRAINER_DIR) $(NOISY_BUILD) coverage

# Create the debug versions for the program

debug: runner_debug runner2_debug trainer_debug 

runner_debug:
	$(SILENT) make -C $(RUNNER_DIR) $(NOISY_BUILD) debug

runner2_debug:
	$(SILENT) make -C $(RUNNER_2_DIR) $(NOISY_BUILD) debug

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

run:
	$(SILENT) make -C $(RUNNER_2_DIR) $(NOISY_BUILD) run

# The .PHONY to to avoid functions being overriden

.PHONY: all clean fclean tests_run coverage debug re noisy noop silent	\
		runner runner_clean runner_fclean runner_tests_run runner_coverage \
		runner_debug run \
		runner2 runner2_clean runner2_fclean runner2_tests_run \
		runner2_coverage runner2_debug run \
		trainer trainer_clean trainer_fclean trainer_tests_run \
		trainer_coverage trainer_debug \


