import struct

class BaseClass:
    def __init__(self):
        self.headerData = bytearray(30)
        self.xAlive = False
        self.xRemote = False
        self.Tnumber = 0

    def decode_header(self, data: bytes) -> bool:
        if len(data) < len(self.headerData):
            # Handle error: insufficient data
            return False

        self.headerData[:] = data[:len(self.headerData)]

        # Extract boolean values using bitwise operations
        self.xAlive = bool(self.headerData[0] & 0x80)
        self.xRemote = bool(self.headerData[0] & 0x40)

        # Extract uint16 value
        self.Tnumber = struct.unpack_from('<H', self.headerData, 1)[0]

        return True

    def encode_header(self) -> bytes:
        self.headerData[0] = 0  # Clear initial bits
        if self.xAlive:
            self.headerData[0] |= 0x80
        if self.xRemote:
            self.headerData[0] |= 0x40

        # Add uint16 value
        struct.pack_into('<H', self.headerData, 1, self.Tnumber)

        return bytes(self.headerData)
