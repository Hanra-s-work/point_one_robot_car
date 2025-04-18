##
## EPITECH PROJECT, 2024
## Makefile
## File description:
## jitter jitter
##

# The variables in charge of tracking the files for the program
SRC_DIR	=	./src

SRC	=	$(SRC_DIR)/main.py	\

# The variables concerning unit testing

TEST_DIR	=	./tests

TEST_FILES	=	$(TEST_DIR)/test_main.py	\
				$(TEST_DIR)/test_constants.py	\

# Coverage report location

COVERAGE_DIR	=	./coverage_data

# Binary name

NAME	=	r2

#  Level precision of the build process

LOG_LEVEL	=	WARN

# The name of the python environement that will be used

ENV_NAME	=	srunner_env

# The location in which the dependencies used during the build process
# will be stored

BUILD_LOCATION	=	./build/

# The location of the final built binary

BINARY_LOCATION	=	./dist/

# The desired destinations for the binary

BINARY_DESTINATION_ONE	=	./

BINARY_DESTINATION_TWO	=	../

# The python binary that is available on the system

CC	=	$(shell command -v python3.9 2>/dev/null || \
			command -v python3 2>/dev/null || \
			command -v python 2>/dev/null || \
			command -v py 2>/dev/null \
)

# Break the code if no python instance was found

ifndef CC
	$(error Python interpreter not found. Please install Python.)
endif

# Search for pip version
MY_PIP_BIN	=	pip3 # Please update it manually {the automation check seems to break the environment}

# Break the code if no python instance was found

ifndef MY_PIP_BIN
	$(error Pip interpreter not found. Please install a pip interpreter.)
endif

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
all: install_dependencies build_binary update_binary_location

# Create the python environement
create_environement:
	@echo -e "$(C_CYAN)Creating python environment$(C_RESET)"
	$(SILENT) $(CC) -m venv $(ENV_NAME)

# Install the python dependencies
install_dependencies: create_environement
	$(SILENT) echo -e "$(C_CYAN)Upgrading pip$(C_RESET)" &&\
	$(CC) -m pip install --upgrade pip && \
	. $(ENV_NAME)/bin/activate && \
	$(MY_PIP_BIN) install --upgrade pip && \
\
	$(MY_PIP_BIN) list && \
	echo -e "$(C_CYAN)Installing python dependencies$(C_RESET)" &&\
	$(MY_PIP_BIN) install -r requirements.txt 

# Activate the python environement (
#	this is a shortcut to help you keep your
#   environement up to date and also avoid mistakes in the name or process
# )
activate_environement:	install_dependencies
	@echo -e "$(C_PINK)Activating environement '$(ENV_NAME)'$(C_RESET)"
	$(SILENT) . ./$(ENV_NAME)/bin/activate && \
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
	@echo -e "$(C_BLUE)Building binary '$(C_YELLOW)$(NAME)$(C_BLUE)'$(C_RESET)"
	$(SILENT) . ./$(ENV_NAME)/bin/activate && \
	pyinstaller \
				$(SRC)	\
				--workpath $(BUILD_LOCATION) --distpath $(BINARY_LOCATION)	\
				--onefile --noconfirm	\
				--name $(NAME)	\
				--log-level=$(LOG_LEVEL)	\
				-y
	@echo -ne "$(C_BLUE)Binary '$(C_YELLOW)$(NAME)$(C_BLUE)' "
	@echo -e  "$(C_GREEN)built$(C_RESET)"

# Update the location of the binary so that it can be easily accessed
update_binary_location:
	@echo -e "$(C_PINK)Updating binary locations$(C_RESET)"
	$(SILENT) cp -vf $(BINARY_LOCATION)$(NAME) $(BINARY_DESTINATION_ONE)
	$(SILENT) cp -vf $(BINARY_LOCATION)$(NAME) $(BINARY_DESTINATION_TWO)
	@echo -e "$(C_PINK)Binary locations $(C_GREEN)updated$(C_RESET)"


# Clean the cache projects

clean:
	@echo -e "$(C_YELLOW)Cleaning $(C_CYAN)cache and build data$(C_RESET)"
# 	Removing the spec files that were used for the executable
	$(SILENT) rm -vf *.spec
# 	Removing the build and distribution folder of the executable
	$(SILENT) rm -rvf $(BUILD_LOCATION)
	$(SILENT) rm -rvf $(BINARY_LOCATION)
#  Removing python runtime cache
	$(SILENT) find . -type d -name __pycache__ -exec rm -rvf {} +
	@echo -e "$(C_GREEN)Cleaned $(C_CYAN)cache and build data$(C_RESET)"

# Clean the binaries produced
clean_env:
	@echo -ne "$(C_YELLOW)Cleaning $(C_CYAN)environement "
	@echo -e  "'$(C_RED)$(ENV_NAME)$(C_CYAN)'$(C_RESET)"
	$(SILENT) rm -rf ./$(ENV_NAME)
	@echo -ne "$(C_CYAN)Environement '$(C_RED)$(ENV_NAME)$(C_CYAN)' "
	@echo -e  "$(C_GREEN)cleaned$(C_RESET)"

# Clean the coverage produced
clean_coverage:
	@echo -e "$(C_YELLOW)Cleaning coverage$(C_RESET)"
	$(SILENT) rm -rf $(COVERAGE_DIR)
	$(SILENT) rm -rf .coverage
	@echo -e "$(C_GREEN)Coverage cleaned$(C_RESET)"

# Proceed to a full environement wipe (
#	ex: usefull when changing python version
# )
fclean: clean clean_env clean_coverage
	$(SILENT) rm -vf $(BINARY_DESTINATION_ONE)$(NAME)
	$(SILENT) rm -vf $(BINARY_DESTINATION_TWO)$(NAME)

# Run the tests for the programs
tests_run: install_dependencies
	@echo -e "$(C_RED)Running unit tests$(C_RESET)"
#	Updating the path for python to find the imports
	$(SILENT) export PYTHONPATH=.:$$PYTHONPATH;	\
	. ./$(ENV_NAME)/bin/activate && \
	$(CC) -m unittest discover -s $(TEST_DIR)
	@echo -e "$(C_RED)Unit tests $(C_GREEN)run$(C_RESET)"

# Check the coverage for the programs
coverage: install_dependencies
	@echo -e "$(C_CYAN)Generating coverage report$(C_RESET)"
	$(SILENT) mkdir -p $(COVERAGE_DIR)
	$(SILENT) . ./$(ENV_NAME)/bin/activate && \
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
	@echo -e "$(C_CYAN)Coverage report $(C_GREEN)generated$(C_RESET)"

# Create the debug versions for the program (no idea what to put in it)

debug: all

# Rule to re-build everything

re: fclean all

# Disable silent build
noisy:
	@echo -e "$(C_PINK)Silent mode is $(C_RED)inactive$(C_RESET)"
	$(eval SILENT=)
	$(eval LOG_LEVEL=INFO)

# This is a no operation function, it is used
# by the parent makefile for silent builds
noop:
	@echo -e "$(C_PINK)Silent mode is $(C_GREEN)active$(C_RESET)"
	$(eval SILENT=@)
	$(eval LOG_LEVEL=WARN)

silent: noop

run: clean install_dependencies
	$(SILENT) echo -e "$(C_CYAN) Activating environement $(C_RESET)" && \
	. ./$(ENV_NAME)/bin/activate && \
	echo -e "$(C_CYAN) Starting program $(C_RESET)" && \
	$(CC) $(SRC_DIR)/main.py && \
	deactivate && \
	echo -e "$(C_CYAN) Environement deactivated $(C_RESET)"

# The .PHONY to to avoid functions being overridden

.PHONY: all create_environement install_dependencies activate_environement \
		activate build_binary update_binary_location clean clean_env \
		clean_coverage fclean tests_run coverage debug re noop silent run
