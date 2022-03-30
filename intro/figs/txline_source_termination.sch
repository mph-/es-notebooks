U1 inverter; right, l=
W U1.vss 0; down
Rs U1.out 2; right
W 0 0_2; right
Cable1; right=2, l=$Z_0$,  kind=tline, aspect=6, thick
W 2 Cable1.in; right=0.6
W Cable1.out 3; right
W 0_2 Cable1.ignd; right, steps=-|, free
W Cable1.ognd 0_3; right, steps=|-, free
O 2 0_2; down
W 3 U2.in; right=0.25
U2 inverter; right, l=
W U2.vss 0_3; down
O 0_2 0_3; right
; draw_nodes=connections, label_nodes=none
