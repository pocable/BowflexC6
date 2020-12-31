# Bowflex C6 Research Data

def main():

    # Data recieved from Serial Bluetooth Terminal. 
    # It is cleaned up to remove timestamps, connection and placed on one line.
    f = open("bfserial6.txt", 'r')
    data = f.read()
    f.close()
    data = data.replace(" ", "")
    n = 2
    arry = [data[i:i+n] for i in range(0, len(data), n)]

    # View binary and int values of the raw data
    view_binary(arry, 9)
    print("===============")
    view_hex(arry, 9)
    print("===============")
    view_int(arry, 9)

    # View column of interesting data
    ind4 = extract_col_int(arry, 4)
    print("==================")
    print(ind4)

    # Print normalized rescaled cadence
    ind4 = [(i / 250) * 125 for i in ind4]
    print(ind4)

# Thought that col 3 was a bit fishy as the number followed the cadence.
# Looked at binary, still have no clue what this is (range 0-9)
def odd_bit_concat_exper(arry):
    ind3 = extract_col(arry, 3)
    ind4 = extract_col_int(arry, 4)
    
    x = zip(ind3, ind4)
    x = [z[0] + z[1] for z in x]
    x = [z[:-1] for z in x]
    print(x)
    view_int_lin(x)

# Reading the other service uuid. This data appears to be something else
# it changes with peddling, but I found cadence and stopped investigating.
# What is interesting is that column 2 counts up with time.
def main2():
    f = open("bfserial2.txt", 'r')
    data = f.read()
    f.close()
    data = data.replace(" ", "")
    n = 2
    arry = [data[i:i+n] for i in range(0, len(data), n)]
    view_hex(arry, 11)
    print("=====================")
    view_int(arry, 11)
    print("===============")
    view_binary(arry, 11)

# Extract col from array
def extract_col(arry, indx):
    return arry[indx::9]

# Extract columns from array as integers.
def extract_col_int(arry, indx):
    return [int(x, 16) for x in arry[indx::9]]

# View the hex as an array linearily
def view_int_lin(arry):
    built = ""
    for i in range(0, len(arry)):
        built += str(int(arry[i], 16)) + " "
    print(built)

# View as an integer
def view_int(arry, mod):
    built = ""
    for i in range(0, len(arry)):
        if i % mod == 0:
            built += "\n"
        built += str(int(arry[i], 16)) + " "
    print(built)

# View as hex data
def view_hex(arry, mod):
    built = ""
    for i in range(0, len(arry)):
        if i % mod == 0:
            built += "\n"
        built += str(arry[i]) + " "
    print(built)

# View as binary data
def view_binary(arry, mod):
    z = [str(bin(int(x, 16))[2:].zfill(8)) for x in arry]
    built = ""
    for i in range(0, len(arry)):
        if i % mod == 0:
            built += "\n"
        built += z[i] + " "
    print(built)

main2()

# ======== MAIN 1 ==============
# 00001826-0000-1000-8000-00805F9B34FB Service UUID
# 00002AD2-0000-1000-8000-00805F9B34FB Read Characteristic
# 00002AD9-0000-1000-8000-00805F9B34FB Write Characteristic
# ~125 max cadence on display


# ========== MAIN 2 =================
# 00001816-0000-1000-8000-00805F9B34FB Service UUID
# 00002A5B-0000-1000-8000-00805F9B34FB Read Characteristic
# 00002A55-0000-1000-8000-00805F9B34FB Write Characteristic


# Files
# bowflex serial : going up and then down
# bfserial2: MAIN 2
# bfserial3: Consistant in middle of the 75 on the bowflex screen
# bfserial4: Max
# bfserial5: ~50 resistance, fast as can go.
# bfserial6: Semi consistant middle of 75, while resistance goes up and down (wattage check)


# Futher notes:
"""
250 appears to be the maximum value for this item. Since the display can only go to around 125,
it looks like it is normalized to be within the range (num/250) * 125. This is confirmed with
bfserial3 reading reading close to 75 in the peolton app and on the display.
"""