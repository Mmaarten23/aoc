import math


class Packet:
    version = 0
    type = 0
    value = None
    sub = None


def main():
    f = open("input/input16.txt", "r")
    line = f.readline().replace("\n", "")
    f.close()
    translated = [a for a in translateHex(line)]
    packet, ignored = readPacket(translated)
    print(sumAllVersionNumbers(packet))
    print(evaluate(packet))


def translateHex(strHex):
    return strHex \
        .replace("0", "G") \
        .replace("1", "H") \
        .replace("G", "0000") \
        .replace("H", "0001") \
        .replace("2", "0010") \
        .replace("3", "0011") \
        .replace("4", "0100") \
        .replace("5", "0101") \
        .replace("6", "0110") \
        .replace("7", "0111") \
        .replace("8", "1000") \
        .replace("9", "1001") \
        .replace("A", "1010") \
        .replace("B", "1011") \
        .replace("C", "1100") \
        .replace("D", "1101") \
        .replace("E", "1110") \
        .replace("F", "1111")


def readPacket(p_l):
    packet = Packet()
    original_length = len(p_l)
    packet.version = int("".join(p_l[:3]), 2)
    p_l = p_l[3:]
    packet.type = int("".join(p_l[:3]), 2)
    p_l = p_l[3:]
    if packet.type == 4:
        number = ""
        while p_l[0] == '1':
            p_l = p_l[1:]
            number += "".join(p_l[:4])
            p_l = p_l[4:]

        p_l = p_l[1:]
        number += "".join(p_l[:4])
        p_l = p_l[4:]
        packet.value = int(number, 2)
        return packet, p_l
    if p_l[0] == "0":
        p_l = p_l[1:]
        packet.sub = []
        bit_length = int("".join(p_l[:15]), 2)
        p_l = p_l[15:]
        org_bit_length = len(p_l)
        while org_bit_length - len(p_l) < bit_length:
            p, p_l = readPacket(p_l)
            packet.sub.append(p)
        return packet, p_l
    if p_l[0] == "1":
        p_l = p_l[1:]
        packet.sub = []
        amount_of_subs = int("".join(p_l[:11]), 2)
        p_l = p_l[11:]
        org_bit_length = len(p_l)
        for _ in range(amount_of_subs):
            p, p_l = readPacket(p_l)
            packet.sub.append(p)
        return packet, p_l


def sumAllVersionNumbers(packet):
    total = packet.version
    if packet.sub is not None:
        for p in packet.sub:
            total += sumAllVersionNumbers(p)
    return total


def evaluate(packet):
    if packet.type == 0:
        return sum([evaluate(a) for a in packet.sub])
    if packet.type == 1:
        return math.prod([evaluate(a) for a in packet.sub])
    if packet.type == 2:
        return min([evaluate(a) for a in packet.sub])
    if packet.type == 3:
        return max([evaluate(a) for a in packet.sub])
    if packet.type == 4:
        return packet.value
    if packet.type == 5:
        return 1 if evaluate(packet.sub[0]) > evaluate(packet.sub[1]) else 0
    if packet.type == 6:
        return 1 if evaluate(packet.sub[0]) < evaluate(packet.sub[1]) else 0
    if packet.type == 7:
        return 1 if evaluate(packet.sub[0]) == evaluate(packet.sub[1]) else 0



if __name__ == '__main__':
    main()
