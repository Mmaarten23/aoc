

from collections import defaultdict


def orient_coord(orientation, coord):
    remap, negation = orientation
    x = coord[remap[0]] * negation[0]
    y = coord[remap[1]] * negation[1]
    z = coord[remap[2]] * negation[2]

    return (x, y, z)


def coord_diff(coord1, coord2):
    return (coord1[0] - coord2[0], coord1[1] - coord2[1], coord1[2] - coord2[2])


class Beacon:
    def __init__(self, pos, dist_map=None):
        self.pos = pos
        if not dist_map:
            self.dist_map = defaultdict(list)
        else:
            self.dist_map = dist_map

    def calc_distance_to_beacon(self, beacon):
        # Gets squared euclidean distance to another beacon
        dx = self.pos[0] - beacon.pos[0]
        dy = self.pos[1] - beacon.pos[1]
        dz = self.pos[2] - beacon.pos[2]
        return (dx ** 2 + dy ** 2 + dz ** 2)

    def mark_beacon_dist(self, dist_coord_pair, beacon_num):
        self.dist_map[beacon_num] = dist_coord_pair

    def orient_then_slide(self, orientation, dpos):
        x, y, z = orient_coord(orientation, self.pos)

        dx, dy, dz = dpos
        new_pos = (x + dx, y + dy, z + dz)

        new_dist_map = {}
        for k, v in self.dist_map.items():
            dist, coord = v
            bx, by, bz = orient_coord(orientation, coord)
            new_dist_map[k] = (dist, (bx + dx, by + dy, bz + dz))

        return Beacon(pos=new_pos, dist_map=new_dist_map)

    @property
    def dist_set(self):
        return set(dist_coord_pair[0] for dist_coord_pair in self.dist_map.values())

    @property
    def dist_pair_set(self):
        return set(dist_coord_pair for dist_coord_pair in self.dist_map.values())


class Scanner:
    def __init__(self, sid):
        self.pos = None
        self.sid = sid
        self.beacons = []

    def add_beacon(self, beacon_coord):
        self.beacons.append(Beacon(beacon_coord))

    def finalize(self):
        for i, beacon in enumerate(self.beacons):
            for j, beacon2 in enumerate(self.beacons):
                dist = beacon.calc_distance_to_beacon(beacon2)
                beacon.mark_beacon_dist((dist, beacon2.pos), j)

    def orient_then_slide(self, orientation, pos):
        self.pos = pos

        new_beacons = [
            beacon.orient_then_slide(orientation, pos) for beacon in self.beacons
        ]
        self.beacons = new_beacons

    def beacon_matches(self, other_scanner):
        potential_overlaps = {}
        for i, beacon in enumerate(self.beacons):
            for j, other_beacon in enumerate(other_scanner.beacons):
                if len(beacon.dist_set & other_beacon.dist_set) >= 12:
                    potential_overlaps[(self.sid, i)] = (other_scanner.sid, j)
        return potential_overlaps

    def get_beacon(self, beacon_id):
        return self.beacons[beacon_id]

remaps = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
negations = [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]
NEGATE_X = [(0, 2, 1), (1, 0, 2), (2, 1, 0)]

orientations = []
for remap in remaps:
    for negation in negations:
        negation_ = (
            negation
            if remap not in NEGATE_X
            else (negation[0] * -1, negation[1], negation[2])
        )
        orientations.append((remap, negation_))

f = open("input.txt", "r")
input_data = f.read().strip().split("\n")

scanners = []
scanner = None
scanner_count = 0
for row in input_data:
    if not row:
        continue
    if row.startswith("---"):
        scanner = Scanner(sid=scanner_count)
        scanners.append(scanner)
        scanner_count += 1
    else:
        assert scanner is not None
        coord = tuple(map(int, row.split(",")))
        scanner.add_beacon(coord)

for scanner in scanners:
    scanner.finalize()
beacon_matches = defaultdict(set)
for sid, scanner in enumerate(scanners):
    for scanner2 in scanners[sid:]:
        potential_beacon_matches = scanner.beacon_matches(scanner2)
        for beacon, beacon_match in potential_beacon_matches.items():
            beacon_matches[beacon].add(beacon_match)
            beacon_matches[beacon_match].add(beacon)


# Arbitrarily assign one scanner to be facing up at the canonical origin
canonical = [0]
scanners[0].pos = (0, 0, 0)
scanners[0].orientation = (remaps[0], negations[0])

iterations = 0
while len(canonical) < len(scanners) and iterations <= len(scanners):
    for sb1, v in beacon_matches.items():
        if not sb1[0] in canonical:
            continue
        beacon1 = scanners[sb1[0]].get_beacon(sb1[1])
        for sb2 in v:
            # If the scanner is already canonical then don't worry about it
            if sb2[0] in canonical:
                continue
            beacon2 = scanners[sb2[0]].get_beacon(sb2[1])
            for orientation in orientations:
                # Reorient the second beacon, try to set its coordinates to that of canonical
                #  and see if its overlapping beacons have the same coordinates relative to canonical
                #  If they do, then you can apply same transformation to its scanner

                dpos = coord_diff(beacon1.pos, orient_coord(orientation, beacon2.pos))
                beacon2_ = beacon2.orient_then_slide(orientation, dpos)
                if len(beacon1.dist_pair_set & beacon2_.dist_pair_set) >= 12:
                    canonical.append(sb2[0])
                    scanners[sb2[0]].orient_then_slide(orientation, dpos)
                    break
    iterations += 1

canonical_coords = set()
for scanner in scanners:
    canonical_coords |= {beacon.pos for beacon in scanner.beacons}


ans = 0
for sid, scanner in enumerate(scanners):
    for scanner2 in scanners[sid:]:
        ans = max(ans, sum(map(abs, list(coord_diff(scanner.pos, scanner2.pos)))))
print(f"Part 1: {len(canonical_coords)}")
print(f"Part 2: {ans}")
