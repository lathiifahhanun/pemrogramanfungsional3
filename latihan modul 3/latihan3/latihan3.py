random_list = [412, 3.1, "Hello", 2.7, "Python", 5.5, 105, "world", "ai", 737]

float_data = list(filter(lambda x: isinstance(x, float), random_list))
int_data = list(filter(lambda x: isinstance(x, int), random_list))
str_data = list(filter(lambda x: isinstance(x, str), random_list))


def map_integer(value):
    ratusan = value // 100
    sisa_ratusan = value % 100
    puluhan = sisa_ratusan // 10
    satuan = sisa_ratusan % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}


int_mapped = list(map(map_integer, int_data))
print("Data Float:", (float_data))
print("\nData Int:")
for item in int_mapped:
    print(item)
print("\nData String:", str_data)
