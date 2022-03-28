.include lossless_txline_unbalanced2.sch as a
#;; \usetikzlibrary{decorations.markings}
;; \tikzset{->-/.style={decoration={markings, mark=at position .5 with {\arrow{triangle 60}}},postaction={decorate}}}
;; \draw[->-, thick, blue] (a@1) to (a@7) (a@0_7) to (a@0_1);
;; \draw[->-, thick, red] (a@7) to (a@5) .. controls (a@4) and (a@0_4) .. (a@0_5) to (a@0_7);
A a.1; l=3, anchor=south
A a.2; l=3, anchor=south
A a.3; l=3, anchor=south
#A a.4; l=3, anchor=south
A a.5; l=6, anchor=south
A a.6; l=6, anchor=south
A a.7; l=6, anchor=south
