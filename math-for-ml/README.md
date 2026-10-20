# Mathematics for Machine Learning and Deep Learning
### From Absolute Beginner to Prerequisites

Lecture notes, written in LaTeX, that take a reader who knows only basic
arithmetic to the point where they can follow the mathematics of standard
machine learning and deep learning courses, textbooks and papers.

**Read the notes:** [`mathematics-for-ml-and-dl.pdf`](mathematics-for-ml-and-dl.pdf)
(276 pages, A4, with clickable cross-references, a full index and 405 exercises
with solutions).

## What is inside

| Chapter | Title | Main topics |
|---|---|---|
| 1 | Numbers, Arithmetic, and Algebraic Thinking | number systems, fractions, exponents, algebra, summation notation, equations, inequalities, absolute value |
| 2 | Functions and Graphs | linear and quadratic functions, exponentials, logarithms, composition, inverses, the sigmoid and other activation functions |
| 3 | Geometry, Coordinates and Trigonometry | coordinates, distance, lines and circles, radians, trigonometry, rotations |
| 4 | Linear Algebra I: Vectors and Matrices | vectors, dot products, matrices, linear maps, matrix multiplication, transposes, inverses, determinants, linear systems |
| 5 | Linear Algebra II: Core Ideas for Machine Learning | span, independence, rank, norms, orthogonality, least squares, eigenvalues, SVD, positive definite matrices, PCA |
| 6 | Calculus of One Variable | limits, derivatives, differentiation rules, extrema, Taylor approximation, integration, numerical derivatives |
| 7 | Multivariable Calculus | partial derivatives, gradients, chain rule on computation graphs, Jacobians, Hessians, multivariable Taylor |
| 8 | Optimization | empirical risk, gradient descent, learning rates, convexity, SGD, momentum, Adam, Newton's method, Lagrange multipliers |
| 9 | Probability | events, conditional probability, Bayes' theorem, random variables, expectation, variance, distributions, covariance, multivariate normal |
| 10 | Statistics for Machine Learning | estimators, LLN and Monte Carlo, CLT and confidence intervals, maximum likelihood, losses from likelihoods, MAP, hypothesis tests, overfitting and the bias–variance trade-off |
| 11 | Mathematics for Deep Learning | networks as compositions, softmax, entropy, cross-entropy and KL divergence, matrix calculus, backpropagation, vanishing gradients, autodiff, attention, a complete training loop |
| 12 | Where to Go Next | the big ideas, projects, topics beyond the notes, recommended reading |
| A | Notation and the Greek Alphabet | every symbol, with the section that introduces it |
| B | Formula Sheet | the key formulas of each chapter |
| C | Solutions to the Exercises | a solution or solution sketch for every exercise |

Every chapter follows the same pattern: a *Motivation* box, learning
objectives, intuition and numerical examples before general rules, colour-coded
boxes (definitions, theorems, worked examples, intuition, "why this matters for
ML", common pitfalls), exercises at the end of each section, and a summary.
The numerical examples were checked in Python, and the NumPy programs printed
in Chapters 4, 8 and 11 are available as runnable files in [`code/`](code).

## Building the PDF

Requirements: a TeX distribution with pdfLaTeX, `latexmk` and `makeindex`
(TeX Live 2023 or newer, MacTeX or MiKTeX), and `make`. On Debian or Ubuntu:

```sh
sudo apt install make latexmk texlive-latex-extra texlive-fonts-recommended lmodern
```

Then, in this directory:

```sh
make                  # full build -> mathematics-for-ml-and-dl.pdf
make chapter CH=04    # Chapter 4 with its solutions -> build/chapter-04.pdf
make clean            # remove the build/ directory
```

All intermediate files go to `build/`. A single-chapter build reuses the
chapter and page numbers and the cross-references of the last full build
(running a full build first if none exists), so the excerpt matches the
complete notes exactly.

Without `make`, run `latexmk -pdf main.tex` (or pdfLaTeX, makeindex and
pdfLaTeX twice more by hand).

### Overleaf and other editors

Upload the whole directory and compile `main.tex` with pdfLaTeX. To typeset only
part of the notes, uncomment the `\includeonly{...}` line near the top of
`main.tex` and list the files you want, always together with
`appendices/C-solutions`; compile the complete notes once beforehand so that
numbering and cross-references are known.

## Layout of the sources

```
main.tex                 document skeleton: front matter, \include of every part
preamble.tex             packages, colours, box environments, exercise and
                         solution machinery, notation macros
Makefile                 build commands
frontmatter/             title page and "How to Use These Notes"
chapters/NN-*.tex        one file per chapter
appendices/              notation, formula sheet, collected solutions
code/                    the Python listings of the notes as runnable files
```

### Writing conventions

* Vectors are `\vx`, `\vw`, … (bold lower case), matrices `\mA`, `\mW`, …
  (bold capitals); operators such as `\E`, `\Var`, `\softmax`, `\ReLU` and
  `\argmin` are defined in `preamble.tex` and listed in Appendix A.
* New terms are written `\term{...}`, which prints them in bold colour and adds
  them to the index.
* Boxes: `definition`, `theorem`, `proposition`, `corollary`, `example`,
  `algorithm`, `intuition`, `picturethis`, `mlnote`, `pitfall`, `remark`,
  `motivation`, `notation`, `objectives`, `keytakeaways`. Key formulas can be
  framed with `\keyeq{...}` inside display maths.
* Exercises: start a block with `\sectionexercises`, then write each
  `exercise` immediately followed by its `solution`. The solution is not
  printed in place; it is collected automatically into Appendix C, with links
  in both directions. Solutions must not contain verbatim material or `#`.
