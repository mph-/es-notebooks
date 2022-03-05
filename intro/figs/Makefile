SCH = $(wildcard *.sch)
PNG = $(SCH:.sch=.png)

all: $(PNG)

%.png: %.sch
	cd $(dir $@); schtex $(notdir $<) $(notdir $@)
