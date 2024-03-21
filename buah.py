def awal(*args):
	print("Toko Buah Koperasi UNJANI Yogyakarta")
	jumlah_buah = int(input("Masukan banyaknya buah yang dibeli : "))

	for i in range(jumlah_buah):
		buah = input(f"Buah {i+1} : ")
		args += (buah,)

		print("Buah yang anda beli adalah : ")
		for i, buah in enumerate (args):
			print(f"{i+1}. {buah}")
	print("Terimakasih")
awal()