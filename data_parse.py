import struct 
from dataclasses import dataclass

""" 
对应的C结构体:
#pragma pack(push, 1)   // 强制对齐，方便解析，但是引用速度变慢
typedef struct {        // 长一点帧头，防止误判
    uint8_t head1;  // 0xAF
    uint8_t head2;  // 0xAA
    uint8_t head3;  // 0xFA
    int target;
    int current;
    int last_err;
    int new_err;
    float P;
    float I;
    float D;
    float out;
} PID_Result_Frame_t;
#pragma pack(pop)
"""


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
     
        
        