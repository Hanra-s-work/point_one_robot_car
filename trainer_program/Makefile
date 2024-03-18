##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

# The variables in charge of tracking the files for the program
SRC_DIR	=	./src

SRC	=	$(SRC_DIR)/main.py	\
		$(SRC_DIR)/constants.py

# The variables concerning unit testing

TEST_DIR	=	./tests

TEST_FILES	=	$(TEST_DIR)/test_main.py	\
				$(TEST_DIR)/test_constants.py	\

# Coverage report location

COVERAGE_DIR	=	./coverage_data

# Binary name

NAME	=	trainer

#  Level precision of the build process

LOG_LEVEL	=	INFO

# The name of the python environement that will be used

ENV_NAME	=	trainer_env

# The location in which the dependencies used during the build process
# will be stored

BUILD_LOCATION	=	./build/

# The location of the final built binary

BINARY_LOCATION	=	./dist/

# The desired destinations for the binary

BINARY_DESTINATION_ONE	=	./

BINARY_DESTINATION_TWO	=	../

# The python binary that is available on the system

CC	=	$(shell command -v python3 2>/dev/null || \
			command -v python 2>/dev/null || \
			command -v py 2>/dev/null)

# Break the code if no python instance was found

ifndef CC
	$(error Python interpreter not found. Please install Python.)
endif

# Silence the outputs we wish not to listen to
SILENT	=	@

# Compile the projects
all: install_dependencies build_binary update_binary_location

# Create the python environement
create_environement:
	$(CC) -m venv $(ENV_NAME)

# Install the python dependencies
install_dependencies: create_environement
	. $(ENV_NAME)/bin/activate && \
	$(CC) -m pip install --upgrade pip
	pip3 list && \
	pip3 install -r requirements.txt

# Activate the python environement (
#	this is a shortcut to help you keep your
#   environement up to date and also avoid mistakes in the name or process
# )
activate_environement:	install_dependencies
	. $(ENV_NAME)/bin/activate && \
	export PYTHONPATH=.:$$PYTHONPATH; \
	echo "Environement activated" && \
	/bin/bash ; \
	STATUS=$$? ; \
	echo "Environement deactivated" && \
	echo "Exit code: $$STATUS" && \
	exit $$STATUS

activate: activate_environement

# Build the python code as a binary
build_binary:
	@echo "Building binary '$(NAME)'"
	. $(ENV_NAME)/bin/activate && \
	pyinstaller \
				$(SRC)	\
				--workpath $(BUILD_LOCATION) --distpath $(BINARY_LOCATION)	\
				--onefile --noconfirm	\
				--name $(NAME)	\
				--log-level=$(LOG_LEVEL)
	@echo "Binary '$(NAME)' built"

# Update the location of the binary so that it can be easily accessed
update_binary_location:
	cp -vf $(BINARY_LOCATION)$(NAME) $(BINARY_DESTINATION_ONE)
	cp -vf $(BINARY_LOCATION)$(NAME) $(BINARY_DESTINATION_TWO)


# Clean the cache projects

clean:
# 	Removing the spec files that were used for the executable
	rm -vf *.spec
# 	Removing the build and distribution folder of the executable
	rm -rf $(BUILD_LOCATION)
	rm -rf $(BINARY_LOCATION)
#  Removing python runtime cache
	find . -type d -name __pycache__ -exec rm -r {} +

# Clean the binaries produced
clean_env:
	@echo "Cleaning environement '$(ENV_NAME)'"
	rm -rf $(ENV_NAME)
	@echo "Environement '$(ENV_NAME)' cleaned"

# Clean the coverage produced
clean_coverage:
	@echo "Cleaning coverage"
	rm -rf $(COVERAGE_DIR)
	rm -rf .coverage
	@echo "Coverage cleaned"

# Proceed to a full environement wipe (
#	ex: usefull when changing python version
# )
fclean: clean clean_env clean_coverage
	rm -vf $(BINARY_DESTINATION_ONE)$(NAME)
	rm -vf $(BINARY_DESTINATION_TWO)$(NAME)

# Run the tests for the programs
tests_run: install_dependencies
#	Updating the path for python to find the imports
	export PYTHONPATH=.:$$PYTHONPATH;	\
	. $(ENV_NAME)/bin/activate && \
	$(CC) -m unittest discover -s $(TEST_DIR)

# Check the coverage for the programs
coverage: install_dependencies
	mkdir -p $(COVERAGE_DIR)
	. $(ENV_NAME)/bin/activate && \
	\
	coverage run --data-file $(COVERAGE_DIR)/report.coverage \
	-m unittest discover -s $(TEST_DIR) && \
	\
	coverage run --branch --data-file $(COVERAGE_DIR)/branch_report.coverage \
	-m unittest discover -s $(TEST_DIR) && \
	\
	coverage report \
	--data-file $(COVERAGE_DIR)/report.coverage > \
	$(COVERAGE_DIR)/report.txt && \
	\
	coverage report \
	--data-file $(COVERAGE_DIR)/branch_report.coverage > \
	$(COVERAGE_DIR)/branch_report.txt && \
	\
	cat $(COVERAGE_DIR)/report.txt && \
	cat $(COVERAGE_DIR)/branch_report.txt && \
	\
	coverage html --directory $(COVERAGE_DIR)/html_report \
	--data-file=$(COVERAGE_DIR)/report.coverage && \
	\
	coverage html --directory $(COVERAGE_DIR)/branch_html_report \
	--data-file=$(COVERAGE_DIR)/branch_report.coverage


# Create the debug versions for the program (no idea what to put in it)

debug: all

# Rule to re-build everything

re: fclean all

# The .PHONY to to avoid functions being overriden

.PHONY: all create_environement install_dependencies activate_environement \
		activate build_binary update_binary_location clean clean_env \
		clean_coverage fclean tests_run coverage debug re
