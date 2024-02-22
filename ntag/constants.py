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

_CONFIG_PAGE_START = 0x29
_CONFIG_PAGE_END = 0x2C

_MIRROR_CONF_BIT_POS = 6
_MIRROR_BYTE_BIT_POS = 4
_MIRROR_PAGE_BYTE_POS = 2
_STRG_MOD_EN_BIT_POS = 0

_MIRROR_CONF_DEFAULT = 0b00
_MIRROR_BYTE_DEFAULT = 0b00
_STRG_MOD_EN_DEFAULT = 0b1

MIRROR_CONF_VALUE = 0b11 