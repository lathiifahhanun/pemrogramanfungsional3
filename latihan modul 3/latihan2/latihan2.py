def konversi_minggu(minggu):
    def konversi_hari(hari):
        def konversi_jam(jam):
            def konversi_menit(menit):
                total_menit = ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)
                return total_menit
            return konversi_menit
        return konversi_jam
    return konversi_hari

data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit"
]

OutputData = []

for item in data:
    parts = item.split()
    minggu = int(parts[0])
    hari = int(parts[2])
    jam = int(parts[4])
    menit = int(parts[6])

    konvert = konversi_minggu(minggu)(hari)(jam)(menit)
    OutputData.append(konvert)

print("OutputData =", OutputData)

integer_values = []
for item in OutputData:
    item_values = list(filter(str.isdigit, str(item)))
    integer_values.append(item_values)

for item in integer_values:
    print(item)