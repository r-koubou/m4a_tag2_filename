 # Makefile for OS independent build rules

.DEFAULT_GOAL:=none

depends:
	pip3 install -r requirements.txt

win32:
	@cd os_specific/win32/; $(MAKE)

macos:
	@cd os_specific/macos/; $(MAKE)

none:
	@echo Do nothing
	@echo Edit '.DEFAULT_GOAL' in Makefile
