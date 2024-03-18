##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

# The folders of the trainer and runners

TRAINER_DIR	=	./trainer

RUNNER_DIR	=	./runner

# Compile the projects

all: runner trainer

runner:
	make -C $(RUNNER_DIR)

trainer:
	make -C $(TRAINER_DIR)

# Clean the cache projects

clean: runner_clean trainer_clean 

runner_clean:
	make -C $(RUNNER_DIR) clean

trainer_clean:
	make -C $(TRAINER_DIR) clean

# Clean the binaries produced

fclean: runner_fclean trainer_fclean 

runner_fclean:
	make -C $(RUNNER_DIR) fclean

trainer_fclean:
	make -C $(TRAINER_DIR) fclean

# Run the tests for the programs

tests_run: runner_tests_run trainer_tests_run 

runner_tests_run:
	make -C $(RUNNER_DIR) tests_run

trainer_tests_run:
	make -C $(TRAINER_DIR) tests_run

# Check the coverage for the programs

coverage: runner_coverage trainer_coverage 

runner_coverage:
	make -C $(RUNNER_DIR) coverage

trainer_coverage:
	make -C $(TRAINER_DIR) coverage

# Create the debug versions for the program

debug: runner_debug trainer_debug 

runner_debug:
	make -C $(RUNNER_DIR) debug

trainer_debug:
	make -C $(TRAINER_DIR) debug

re: fclean all

# The .PHONY to to avoid functions being overriden

.PHONY: all clean fclean tests_run coverage debug re	\
		runner runner_clean runner_fclean runner_tests_run runner_coverage \
		runner_debug \
		trainer trainer_clean trainer_fclean trainer_tests_run \
		trainer_coverage trainer_debug \


