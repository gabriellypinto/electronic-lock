import mfrc522
rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

class RfidPorteiro:

    def __init__(self):
        print ("Rfid ativo")

    def get(self):
        tag = "SemTag"
        (stat, tag_type) = rdr.request(rdr.REQIDL)

        if stat == rdr.OK:

            (stat, raw_uid) = rdr.anticoll()

            if stat == rdr.OK:
                print("Card detected: ")
                print(str(raw_uid[0])+ str(raw_uid[1]) + str(raw_uid[2])+ str(raw_uid[3]))
                print("")
                if rdr.select_tag(raw_uid) == rdr.OK:
                    tag = str(raw_uid[0])+ str(raw_uid[1]) + str(raw_uid[2])+ str(raw_uid[3])
                else:
                    return tag
        return tag


    def key(self,tags):
        try:
            tag = self.get()
        except KeyboardInterrupt:
            tag = '12345'
            print("Bye")

        if tag in tags:
            return True
        else:
            return False


