.include lossless_txline_unbalanced2.sch as a
#;; \usetikzlibrary{decorations.markings}
;; \tikzset{->-/.style={decoration={markings, mark=at position .5 with {\arrow{triangle 60}}},postaction={decorate}}}
;; \draw[->-, thick, blue] (a@1) to (a@5) .. controls (a@6) and (a@0_6) .. (a@0_5) to (a@0_1);