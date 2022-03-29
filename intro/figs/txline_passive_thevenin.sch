U1 inverter; right, l=
W U1.vss 0; down
W U1.out 2; right=0.5
W U1.vdd vdd; up
W 0 0_2; right
Cable1; right=2, l=$Z_0$,  kind=tline, aspect=6, thick
W 2 Cable1.in; right=0.6
W Cable1.out 3; right
W 0_2 Cable1.ignd; right, steps=-|, free
R2 3 0_3; down
R1 vdd2 3; down
W vdd vdd2; right
W Cable1.ognd 0_3; right, steps=|-, free
O 2 0_2; down
W 3 U2.in; right
U2 inverter; right, l=
O 0_2 0_3; right
; draw_nodes=connections, label_nodes=none
