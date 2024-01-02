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


class NTAG213:
    def __init__(self, pn532, debug=False):
        self.pn532 = pn532
        self.debug = debug

    def create_ndef_record(self, tnf=0x01, record_type='T', payload='', record_position='only', id=''):
        """
        Method to create the NDEF record with debug statements.
        """
        # Message Begin (MB), Message End (ME), and Chunk Flag (CF) bits
        MB = 0x80 if record_position == 'only' or record_position == 'first' else 0x00
        ME = 0x40 if record_position == 'only' or record_position == 'last' else 0x00
        CF = 0x20 if record_position == 'middle' else 0x00

        # Short Record (SR) bit: True if payload length is less than 256
        SR = 0x10 if len(payload) < 256 else 0x00

        # ID Length (IL) bit: True if ID is present
        IL = 0x08 if id else 0x00

        # Combine TNF with flags into a single byte
        message_flags = MB | ME | CF | SR | IL | tnf
        print(f"Message Flags: {message_flags:02x}")

        # Type length
        type_length = len(record_type).to_bytes(1, byteorder='big')
        print(f"Type Length: {type_length.hex()}")

        # Prepend URI identifier code if the record type is 'U' (URL)
        if record_type == 'U':
            uri_identifier_code = b'\x04'  # 0x03 for 'http://'
            payload = uri_identifier_code + payload.encode()
        else:
            payload = payload.encode()

        # Payload length: 1 if SR is set; 4 otherwise
        if SR:
            payload_length = len(payload).to_bytes(1, byteorder='big')
        else:
            payload_length = len(payload).to_bytes(4, byteorder='big')
        print(f"Payload Length: {payload_length.hex()}")

        # ID length: Present only if IL is set
        id_length = len(id).to_bytes(1, byteorder='big') if IL else b''
        print(f"ID Length: {id_length.hex()}")

        # Record type: Convert type to bytes
        record_type_bytes = record_type.encode()
        print(f"Record Type Bytes: {record_type_bytes.hex()}")

        # ID: Convert ID to bytes
        id_bytes = id.encode()
        print(f"ID Bytes: {id_bytes.hex()}")

        # Combine everything to form the header
        header = bytes([message_flags]) + type_length + payload_length + id_length + record_type_bytes + id_bytes
        print(f"Header: {header.hex()}")

        # Complete record: Header + Payload
        complete_record = header + payload
        print(f"Complete Record (Before Terminator): {complete_record.hex()}")

        # TLV Type for NDEF Message
        tlv_type = b'\x03'

        # Calculate TLV Length
        ndef_length = len(complete_record)
        if ndef_length < 255:
            tlv_length = bytes([ndef_length])
        else:
            tlv_length = b'\xFF' + ndef_length.to_bytes(2, byteorder='big')

        # Construct the TLV structure
        tlv = b'\x34' + tlv_type + tlv_length + complete_record

        # Append the Record Terminator TLV (0xFE) to the end of the record
        tlv += b'\xFE'
        print(f"Complete Record (With Terminator): {tlv.hex()}")

        return tlv
    
    def combine_ndef_records(self, records):
        """
        Combine multiple NDEF records into a single NDEF message.

        :param records: List of NDEF records
        :return: Combined NDEF message as a byte array
        """
        ndef_message = bytearray()
        for record in records:
            ndef_message.extend(record)

        if self.debug:
            print(f"Combining {len(records)} NDEF Records into a single message.")
            print(f"Combined NDEF Message: {ndef_message}")

        return ndef_message
    
    def write_ndef_message(self, ndef_message, start_block=4):
        """
        Write an NDEF message to an NTAG2XX NFC tag.

        :param ndef_message: NDEF message as a byte array (can contain multiple records)
        :param start_block: Starting block number to write the message
        :return: True if write is successful, False otherwise
        """
        try:
            for i in range(0, len(ndef_message), 4):
                block_data = ndef_message[i:i + 4]
                if len(block_data) < 4:
                    block_data += b'\x00' * (4 - len(block_data))  # Padding

                if self.debug:
                    print(f"Writing data to block {start_block + i // 4}: {block_data}")

                self.ntag2xx_write_block(start_block + i // 4, block_data)

            if self.debug:
                print("Successfully wrote NDEF message to the NFC tag.")

            return True
        except Exception as e:
            print("Error writing NDEF message to the tag:", e)
            return False
