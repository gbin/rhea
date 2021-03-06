
from __future__ import print_function
from __future__ import division

from myhdl import Signal, intbv, instances, always_seq

from rhea.cores.uart import uart_lite
from rhea.cores.misc import glbl_timer_ticks
from rhea.system import Global


def cathat(clock, reset, led):
    """ Xess CAT board RPi Hat example
    """

    glbl = Global(clock, reset)
    gticks = glbl_timer_ticks(glbl, include_seconds=True)

    
    lcnt = Signal(modbv(0, min=0, max=4))

    @always(clock.posedge)
    def beh_led_count():
        if glbl.tick_sec:
            lcnt.next = lcnt + 1;
        led.next = (1 << lcnt)

    # RPi interface

    # SDRAM controller

    # 
        
    return instances()
            