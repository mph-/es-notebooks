U1 inverter; right, fill=blue!50, l=
W U1.vss 0; down, color=blue
W U1.out 2; right=0.5, color=blue
W 0 1; right=0.5, color=blue
P 2 1; down, v^=V_o
W 2 2a; right, i=I_o
W 1 1a; right
VL 2a 1a; down
VDD 4 0_4; down=1.5, color=blue
W 0_4 0; right=1.5, color=blue
W 4 5; right=1.5, color=blue
W 5 U1.vdd; down=0.75, color=blue
; draw_nodes=connections, label_nodes=none
