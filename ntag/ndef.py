class NDEF:
    """
    Class for handling NDEF operations on an NTAG.

    This class should be subclassed to implement the read_ndef_message and write_ndef_message methods.

    :param ntag: An instance of the NTAG class that this NDEF class will operate on.
    """
    def __init__(self, ntag):
        """
        Initializes the NDEF class for handling NDEF operations on an NTAG.

        :param ntag: An instance of the NTAG class that this NDEF class will operate on.
        """
        self.ntag = ntag

    def _create_message_flags(self, payload, id, tnf):
        """
        Constructs the message flag byte for an NDEF record.

        :param payload: The payload of the NDEF record.
        :param id: The ID of the NDEF record.
        :param tnf: The Type Name Format of the NDEF record.
        :return: The constructed message flags byte.
        """
        MB, ME = 0x80, 0x40  # Message Begin, Message End
        CF, SR = 0x00, 0x10 if len(payload) < 256 else 0x00  # Chunk Flag, Short Record
        IL = 0x08 if id else 0x00  # ID Length
        return MB | ME | CF | SR | IL | tnf

    def _prepare_payload(self, record_type, payload):
        """
        Prepares the payload based on the record type.

        :param record_type: The type of the NDEF record.
        :param payload: The payload to be encoded.
        :return: The encoded payload.
        """
        uri_identifier_code = b'\x03' if self.ntag.debug else b'\x04'
        return uri_identifier_code + payload.encode() if record_type == 'U' else payload.encode()

    def _create_record_header(self, tnf, record_type, payload, id):
        """
        Creates the header for an NDEF record.

        :param tnf: The Type Name Format of the NDEF record.
        :param record_type: The type of the record.
        :param payload: The payload of the record.
        :param id: The ID of the record.
        :return: The constructed record header.
        """
        message_flags = self._create_message_flags(payload, id, tnf)
        prepared_payload = self._prepare_payload(record_type, payload)
        type_length, payload_length = len(record_type).to_bytes(1, 'big'), len(prepared_payload).to_bytes(1 if len(prepared_payload) < 256 else 4, 'big')
        id_length = len(id).to_bytes(1, 'big') if id else b''
        return bytes([message_flags]) + type_length + payload_length + id_length + record_type.encode() + (id.encode() if id else b''), prepared_payload

    def _construct_complete_record(self, tnf, record_type, payload, id):
        """
        Constructs the complete NDEF record including the TLV wrapper.

        :param tnf: The Type Name Format of the NDEF record.
        :param record_type: The type of the record.
        :param payload: The payload of the NDEF record.
        :param id: The ID of the record.
        :return: The complete NDEF record with TLV.
        """
        header, prepared_payload = self._create_record_header(tnf, record_type, payload, id)
        complete_record = header + prepared_payload
        tlv_length = len(complete_record).to_bytes(1 if len(complete_record) < 255 else 2, 'big')
        return b'\x03' + tlv_length + complete_record + b'\xFE'

    def write_ndef_message(self, tnf, record_type, payload, id='', start_block=4):
        """
        Writes an NDEF message to the specified NTAG, handling the message formatting,
        chunking, and writing process.

        :param tnf: Type Name Format for the NDEF record.
        :param record_type: The type of the record (e.g., 'T' for text, 'U' for URI).
        :param payload: The payload of the NDEF record.
        :param id: An optional record ID.
        :param start_block: The starting block number to write the message.
        """
        if start_block < 4 or start_block > self.ntag.max_block:
            self.ntag.log(f"Invalid start block {start_block} for NDEF message.", "error")
            raise ValueError("Invalid start block for NDEF message.")
        try:
            complete_record = self._construct_complete_record(tnf, record_type, payload, id)
            chunks = [complete_record[i:i+4] for i in range(0, len(complete_record), 4)]
            for i, chunk in enumerate(chunks, start=start_block):
                self.ntag.write_block(i, chunk + b'\x00' * (4 - len(chunk)))  # Pads chunk if necessary
            self.ntag.log("Successfully wrote NDEF message to the NFC tag.", "info")
        except IOError as e:
            self.ntag.log(f"I/O Error writing NDEF message to the tag: {e}", "error")
        except ValueError as e:
            self.ntag.log(f"Value Error in NDEF data: {e}", "error")

