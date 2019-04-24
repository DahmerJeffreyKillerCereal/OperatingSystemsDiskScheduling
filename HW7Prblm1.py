def first_come_first_serve(start, disk_locations):
    current_place = start
    total = 0
    for i in disk_locations:
        total += abs(current_place - i)
        current_place = i
    print(total)


def shortest_seek_time_first(start, disk_locations):
    current_place = start
    total = 0
    while len(disk_locations) != 0:
        r = min(range(len(disk_locations)), key=lambda i: abs(disk_locations[i] - current_place))
        total += abs(current_place - disk_locations[r])
        current_place = disk_locations[r]
        del disk_locations[r]
    print(total)


def scan(start, end, disk_locations):
    if disk_locations:
        dist_to_end = abs(start - end)
        if start < dist_to_end:
            total = start
            value = max(disk_locations)
            total += value
        print(total)
    else:
        print("List is empty")

def c_scan(start, end, disk_locations):
    disk_locations.sort()
    if start < abs(start-end):
        total = start
        res = next(x for x, val in enumerate(disk_locations) if val > start)
        total += abs(disk_locations[res] - end)
        print(total)
        return
    else:
        total = abs(start-end)
        temp_list = []
        for res in disk_locations:
            if res < start:
                temp_list.append(res)
        if temp_list:
            total += max(temp_list)
        print(total)
        return


def look(start, end,  disk_locations):

    disk_locations.sort()
    if disk_locations:
        if start < abs(start - end):
                if min(disk_locations) < start:
                    total = abs(min(disk_locations) - start)
                    total += abs(min(disk_locations) - max(disk_locations))
                    print(total)
                else:
                    total = abs(start - max(disk_locations))
                    print(total)
        else:
                if max(disk_locations) > start:
                    total = abs(max(disk_locations) - start)
                    total += abs(min(disk_locations) - max(disk_locations))
                    print(total)
                else:
                    total = abs(start-mix(disk_locations))
                    print(total)
    else:
        print("Empty List, no values to calculate")


def c_look(start, end, disk_locations):
    disk_locations.sort()
    if disk_locations:
        if start < abs(start - end):
            total = abs(start - min(disk_locations))
            res = next(x for x, val in enumerate(disk_locations) if val > start)
            total += abs(disk_locations[res] - max(disk_locations))
            print(total)
        else:
            total = abs(start - max(disk_locations))
            res = next(x for x, val in enumerate(disk_locations) if val < start)
            total += abs(disk_locations[res] - min(disk_locations))
            print(total)
    else:
        print("Empty list, no values to calculate")

a = [98, 183, 37, 122, 14, 124, 65, 67]
b = [46, 73, 11, 20, 151, 115, 130, 49]
a1 = [98, 183, 37, 122, 14, 124, 65, 67]
b1 = [46, 73, 11, 20, 151, 115, 130, 49]
start_position = 53
end_position = 199

shortest_seek_time_first(start_position, a)
shortest_seek_time_first(start_position, b)

scan(start_position, end_position, a1)
scan(start_position, end_position, b1)

c_scan(start_position, end_position, a1)

example3 = [23, 89, 132, 42, 187]


new_start = 100
new_end = 199

b1 = [46, 73, 11, 20, 151, 115, 130, 49]
c_scan(new_start, new_end, example3)
c_scan(start_position, end_position, b1)

look(start_position, end_position, a1)
look(start_position, end_position, b1)

c_look(start_position, end_position, a1)
c_look(start_position, end_position, b1)
