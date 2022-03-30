Vd 1 0; down=1.5, l={$4 u(t)$}
Rs 1 2; right
W 0 0_2; right
Cable1; right=2, l=$Z_0$,  kind=tline, aspect=6, thick
W 2 Cable1.in; right=0.6
W Cable1.out 3; right, l={$i_l(t)$}
W 0_2 Cable1.ignd; right, steps=-|, free
Rt 3 4; right=1.5
Vt 4 0_4; down=1.5
W Cable1.ognd 0_3; right, steps=|-, free
W 0_3 0_4; right
O 2 0_2; down, v^={$v_s(t)$}
O 3 0_3; down, v^={$v_l(t)$}
; draw_nodes=connections, label_nodes=none
