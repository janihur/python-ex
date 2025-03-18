# TODO: BUILD_DIR will accumulate all application specific files (src/program?.py)

MAKEFLAGS += --no-builtin-rules --no-builtin-variables
COMMON_MODULES := src/module1.py src/module2.py

# TODO: will be copied but missing as a dependency
RESOURCES_PACKAGE := src/resources

BUILD_DIR := build
BUILD_STAMP := $(BUILD_DIR)/.stamp

.PHONY: all
all: check-venv program1.pyz program2.pyz

program1.pyz: src/program1.py $(BUILD_STAMP)
	cp $< $(BUILD_DIR)
	python -m zipapp --compress --main program1:main --output $@ $(BUILD_DIR)

program2.pyz: src/program2.py $(BUILD_STAMP)
	cp $< $(BUILD_DIR)
	python -m zipapp --compress --main program2:main --output $@ $(BUILD_DIR)

$(BUILD_STAMP): $(COMMON_MODULES) requirements.txt
	rm -rf $(BUILD_DIR)
	mkdir -p $(BUILD_DIR)
	cp $(COMMON_MODULES) $(BUILD_DIR)
	cp -r $(RESOURCES_PACKAGE) $(BUILD_DIR)
	pip install -r requirements.txt --target $(BUILD_DIR)/
	touch $@

.PHONY: check-venv
check-venv:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "ERROR: virtual environment not activated"; \
		echo "ERROR: run 'source .venv/bin/activate' first"; \
		exit 1; \
	fi

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR) program1.pyz program2.pyz