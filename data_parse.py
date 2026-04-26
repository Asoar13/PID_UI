import struct 
from dataclasses import dataclass

@dataclass
class PidResult:
    # 类常量
    PID_RESULT_HAED_  = b"\xaf\xaa\xfa"
    PID_RESULT_HEAD_1 = 0xAF
    PID_RESULT_HEAD_2 = 0xAA
    PID_RESULT_HEAD_3 = 0xFA
    PID_RESULT_FORMAT = "<BBBiiiiffff"
    PID_RESULT_SIZE = struct.calcsize(PID_RESULT_FORMAT)
    
    head1:int
    head2:int
    head3:int
    target:int
    current:int
    last_err:int
    new_err:int
    P:float
    I:float
    D:float
    out:float

    @classmethod
    def from_frame(cls, frame:bytes):
        return cls(*struct.unpack(cls.PID_RESULT_FORMAT, frame))

    def is_valid(self) -> bool:
        return self.head1 == self.PID_RESULT_HEAD_1 and \
            self.head2 == self.PID_RESULT_HEAD_2 and \
            self.head3 == self.PID_RESULT_HEAD_3
     
        
        