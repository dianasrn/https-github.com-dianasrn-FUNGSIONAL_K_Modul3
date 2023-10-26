def konversi(minggu=0):
    def hari(hari=0):
        def jam(jam=0):
            def menit(menit=0):
                return (((minggu * 7 + hari) * 24 + jam) * 60) + menit
            return menit
        return jam
    return hari

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
output_data = []

for item in data:
    parts = item.split()
    minggu = int(parts[0]) if 'minggu' in parts else 0
    hari = int(parts[2]) if 'hari' in parts else 0
    jam = int(parts[4]) if 'jam' in parts else 0
    menit = int(parts[6]) if 'menit' in parts else 0

    konvert = konversi(minggu)(hari)(jam)(menit)
    output_data.append(konvert)

print("output_data =", output_data)
