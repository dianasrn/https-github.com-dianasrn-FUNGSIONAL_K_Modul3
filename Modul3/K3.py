random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
is_float = lambda x: isinstance(x, float)
is_int = lambda x: isinstance(x, int)
is_string = lambda x: isinstance(x, str)

float_list = list(filter(is_float, random_list))
int_list = list(filter(is_int, random_list))
string_list = list(filter(is_string, random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_int_to_dict(num):
    satuan = num % 10
    puluhan = (num % 100) // 10
    ratusan = num // 100
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

int_dict = list(map(map_int_to_dict, int_list))

# Output
print("Data Float:", float_list)
print("Data Int:")
for item in int_dict:
    print(item)
print("Data String:", string_list)
