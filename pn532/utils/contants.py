_HOSTTOPN532 = 0xD4
_PN532TOHOST = 0xD5
_PREAMBLE = 0x00
_STARTCODE1 = 0x00
_STARTCODE2 = 0xFF
_POSTAMBLE = 0x00
_WAKEUP = 0x55
_ISO14443A = 0x00
_VALIDATIONBIT = 0x80
_ACK = b'\x00\x00\xFF\x00\xFF\x00'
_NACK = b'\x00\xFF\x00\x00\xFF\x00'

# PN532 Miscellaneous Commands
_PN532_CMD_DIAGNOSE = 0x00
_PN532_CMD_GETFIRMWAREVERSION = 0x02
_PN532_CMD_GETGENERALSTATUS = 0x04
_PN532_CMD_READREGISTER = 0x06
_PN532_CMD_WRITEREGISTER = 0x08
_PN532_CMD_READGPIO = 0x0C
_PN532_CMD_WRITEGPIO = 0x0E
_PN532_CMD_SETSERIALBAUDRATE = 0x10
_PN532_CMD_SETPARAMETERS = 0x12
_PN532_CMD_SAMCONFIGURATION = 0x14
_PN532_CMD_POWERDOWN = 0x16

# PN532 Radio Frequency (RF) Communication Commands
_PN532_CMD_RFCONFIGURATION = 0x32
_PN532_CMD_RFREGULATIONTEST = 0x58

# PN532 initiator Commands
_PN532_CMD_INJUMPFORDEP = 0x56
_PN532_CMD_INJUMPFORPSL = 0x46
_PN532_CMD_INLISTPASSIVETARGET = 0x4A
_PN532_CMD_INATR = 0x50
_PN532_CMD_INPSL = 0x4E
_PN532_CMD_INDATAEXCHANGE = 0x40
_PN532_CMD_INCOMMUNICATETHRU = 0x42
_PN532_CMD_INDESELECT = 0x44
_PN532_CMD_INRELEASE = 0x52
_PN532_CMD_INSELECT = 0x54
_PN532_CMD_INAUTOPOLL = 0x60

# PN532 Target Commands
_PN532_CMD_TGINITASTARGET = 0x8C
_PN532_CMD_TGSETGENERALBYTES = 0x92
_PN532_CMD_TGGETDATA = 0x86
_PN532_CMD_TGSETDATA = 0x8E
_PN532_CMD_TGSETMETADATA = 0x94
_PN532_CMD_TGGETINITIATORCOMMAND = 0x88
_PN532_CMD_TGRESPONSETOINITIATOR = 0x90
_PN532_CMD_TGGETTARGETSTATUS = 0x8A

# NTAG Commands
_NTAG_CMD_GET_VERSION = 0x60
_NTAG_CMD_READ = 0x30
_NTAG_CMD_FAST_READ = 0x3A
_NTAG_CMD_WRITE = 0xA2
_NTAG_CMD_COMPATIBILITY_WRITE = 0xA0
_NTAG_CMD_READ_CNT = 0x39
_NTAG_ADDR_READ_CNT = 0x02
_NTAG_CMD_PWD_AUTH = 0x1B
_NTAG_CMD_READ_SIG = 0x3C
_NTAG_ADDR_READ_SIG = 0x00

# NDEF Record Types
_NDEF_URIPREFIX_NONE = 0x00
_NDEF_URIPREFIX_HTTP_WWWDOT = 0x01
_NDEF_URIPREFIX_HTTPS_WWWDOT = 0x02
_NDEF_URIPREFIX_HTTP = 0x03
_NDEF_URIPREFIX_HTTPS = 0x04
_NDEF_URIPREFIX_TEL = 0x05
_NDEF_URIPREFIX_MAILTO = 0x06
_NDEF_URIPREFIX_FTP_ANONAT = 0x07
_NDEF_URIPREFIX_FTP_FTPDOT = 0x08
_NDEF_URIPREFIX_FTPS = 0x09
_NDEF_URIPREFIX_SFTP = 0x0A
_NDEF_URIPREFIX_SMB = 0x0B
_NDEF_URIPREFIX_NFS = 0x0C
_NDEF_URIPREFIX_FTP = 0x0D
_NDEF_URIPREFIX_DAV = 0x0E
_NDEF_URIPREFIX_NEWS = 0x0F
_NDEF_URIPREFIX_TELNET = 0x10
_NDEF_URIPREFIX_IMAP = 0x11
_NDEF_URIPREFIX_RTSP = 0x12
_NDEF_URIPREFIX_URN = 0x13
_NDEF_URIPREFIX_POP = 0x14
_NDEF_URIPREFIX_SIP = 0x15
_NDEF_URIPREFIX_SIPS = 0x16
_NDEF_URIPREFIX_TFTP = 0x17
_NDEF_URIPREFIX_BTSPP = 0x18
_NDEF_URIPREFIX_BTL2CAP = 0x19
_NDEF_URIPREFIX_BTGOEP = 0x1A
_NDEF_URIPREFIX_TCPOBEX = 0x1B
_NDEF_URIPREFIX_IRDAOBEX = 0x1C
_NDEF_URIPREFIX_FILE = 0x1D
_NDEF_URIPREFIX_URN_EPC_ID = 0x1E
_NDEF_URIPREFIX_URN_EPC_TAG = 0x1F
_NDEF_URIPREFIX_URN_EPC_PAT = 0x20
_NDEF_URIPREFIX_URN_EPC_RAW = 0x21
_NDEF_URIPREFIX_URN_EPC = 0x22
_NDEF_URIPREFIX_URN_NFC = 0x23

PN532_ERRORS = {
    0x01: 'PN532 ERROR TIMEOUT',
    0x02: 'PN532 ERROR CRC',
    0x03: 'PN532 ERROR PARITY',
    0x04: 'PN532 ERROR COLLISION_BITCOUNT',
    0x05: 'PN532 ERROR MIFARE_FRAMING',
    0x06: 'PN532 ERROR COLLISION_BITCOLLISION',
    0x07: 'PN532 ERROR NOBUFS',
    0x09: 'PN532 ERROR RFNOBUFS',
    0x0a: 'PN532 ERROR ACTIVE_TOOSLOW',
    0x0b: 'PN532 ERROR RFPROTO',
    0x0d: 'PN532 ERROR TOOHOT',
    0x0e: 'PN532 ERROR INTERNAL_NOBUFS',
    0x10: 'PN532 ERROR INVAL',
    0x12: 'PN532 ERROR DEP_INVALID_PN532_CMD',
    0x13: 'PN532 ERROR DEP_BADDATA',
    0x14: 'PN532 ERROR MIFARE_AUTH',
    0x18: 'PN532 ERROR NOSECURE',
    0x19: 'PN532 ERROR I2CBUSY',
    0x23: 'PN532 ERROR UIDCHECKSUM',
    0x25: 'PN532 ERROR DEPSTATE',
    0x26: 'PN532 ERROR HCIINVAL',
    0x27: 'PN532 ERROR CONTEXT',
    0x29: 'PN532 ERROR RELEASED',
    0x2a: 'PN532 ERROR CARDSWAPPED',
    0x2b: 'PN532 ERROR NOCARD',
    0x2c: 'PN532 ERROR MISMATCH',
    0x2d: 'PN532 ERROR OVERCURRENT',
    0x2e: 'PN532 ERROR NONAD',
}
