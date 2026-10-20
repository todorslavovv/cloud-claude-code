# Makefile for "Mathematics for Machine Learning and Deep Learning:
#               From Absolute Beginner to Prerequisites"
#
#   make                  Build the complete notes -> mathematics-for-ml-and-dl.pdf
#   make chapter CH=04    Build only Chapter 4 and its solutions
#                         -> build/chapter-04.pdf
#                         (chapter numbers, page numbers and cross-references
#                         are taken from a full build, which is run first if
#                         none exists yet)
#   make clean            Remove the build directory (keeps the final PDF)
#   make distclean        Remove the build directory and the final PDF
#
# Requirements: a TeX distribution with pdfLaTeX, latexmk and makeindex
# (TeX Live, MacTeX or MiKTeX all qualify).

MAIN     := main
OUTDIR   := build
PDF      := mathematics-for-ml-and-dl.pdf
LATEXMK  := latexmk
LATEXMK_FLAGS := -pdf -interaction=nonstopmode -halt-on-error \
                 -file-line-error -outdir=$(OUTDIR)

SOURCES  := $(MAIN).tex preamble.tex \
            $(wildcard frontmatter/*.tex chapters/*.tex appendices/*.tex)

# chapters/04-linear-algebra-basics.tex -> chapters/04-linear-algebra-basics
CHAPTER_FILE = $(basename $(firstword $(wildcard chapters/$(CH)-*.tex)))

.PHONY: all chapter clean distclean dirs

all: $(PDF)

dirs:
	@mkdir -p $(OUTDIR)/frontmatter $(OUTDIR)/chapters $(OUTDIR)/appendices

$(PDF): $(SOURCES) | dirs
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex
	cp $(OUTDIR)/$(MAIN).pdf $@

# A full build provides the .aux files that a partial build relies on.
$(OUTDIR)/$(MAIN).aux: | dirs
	$(LATEXMK) $(LATEXMK_FLAGS) $(MAIN).tex

chapter: | dirs $(OUTDIR)/$(MAIN).aux
	@test -n "$(CH)" || { echo "Usage: make chapter CH=04"; exit 1; }
	@test -n "$(CHAPTER_FILE)" || \
	  { echo "No file matches chapters/$(CH)-*.tex"; exit 1; }
	$(LATEXMK) $(LATEXMK_FLAGS) -jobname=chapter-$(CH) \
	  -usepretex='\def\MLSelectedParts{$(CHAPTER_FILE),appendices/C-solutions}' \
	  $(MAIN).tex
	@echo "Output written to $(OUTDIR)/chapter-$(CH).pdf"

clean:
	rm -rf $(OUTDIR)

distclean: clean
	rm -f $(PDF)
