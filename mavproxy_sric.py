#!/usr/bin/env python
# Author Jake Tarren
# Christopher Newport Unmanned Arial Systems Lab

import time, math
from pymavlink import mavutil

from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib.my_settings import MPSetting

class SRICModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(SRICModule, self).__init__(mpstate, 'SRIC', 'SRIC module')
        self.add_command('sric', self.sric, 'Some shit to manage the sric module')
    
    def mavlink_packet(self, m):
        # Do the things!!
        if m.get_type() == 'MSG':
            sric_script.main()
