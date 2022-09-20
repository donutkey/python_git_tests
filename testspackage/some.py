def get_out_line(ip_to_find:int):
    result = -1
    for x in global_table:
        ip = x[0]
        netmask = x[1]
        out_line = x[2]
        if (ip==ip_to_find):
            return out_line
    return result

global_table = [(1,111,11),(2,222,22),(3,333,33)]

if __name__ == '__main__':
    print('begining')
    for i in range(0,7):
        out_line = get_out_line(i)
        print('ip is: ' + str(i))
        print('outline found: ' + str(out_line))

new_master_update = 1
new_feature_update = 2