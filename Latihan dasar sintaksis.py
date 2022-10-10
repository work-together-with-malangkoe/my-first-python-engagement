"""
Semua sintaksis dasar pemrograman terdiri dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sequential
print('Mom said, "go to the shop"')
print('Jack answer, "Okay, what should i buy in the shop?"')
print('Mom said, "Buy 1 bottle of milk. If there is egg, buy 6"')
print("So Jack go to te shop and start shopping")

# Percabangan
print("There is a condition")

milk_bottle_count = 173
egg_number_count = 0
print(f"milk bottle count {milk_bottle_count} btl")
print(f"egg count {egg_number_count} egg")

if egg_number_count > 0:
    print("Jack will buy 6 bottles of milk")

else:
    print("Jack will buy only 1 bottle of milk")

print("Jack back to his house")
print("Jack gives the milk to his mom")
