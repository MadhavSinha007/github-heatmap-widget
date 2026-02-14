APP_NAME=github-heatmap
PYTHON=python3
SCRIPT=heatmap.py
INSTALL_DIR=$(HOME)/.local/bin

.PHONY: run install uninstall deps clean

run:
	$(PYTHON) $(SCRIPT)

deps:
	sudo apt install -y python3-gi gir1.2-gtk-4.0 gir1.2-gdkx11-4.0 curl

install:
	mkdir -p $(INSTALL_DIR)
	cp $(SCRIPT) $(INSTALL_DIR)/$(APP_NAME)
	chmod +x $(INSTALL_DIR)/$(APP_NAME)
	@echo "Installed to $(INSTALL_DIR)/$(APP_NAME)"
	@echo "You can now run it using:"
	@echo "$(APP_NAME)"

uninstall:
	rm -f $(INSTALL_DIR)/$(APP_NAME)
	@echo "Uninstalled."

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +