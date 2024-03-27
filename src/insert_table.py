from verify_table_existence import verify_table_existence

def insert_table (table_name, keys, values) :
    if verify_table_existence (table_name=table_name) :
        for keyIndex in range(len(keys)) :
            with open (f"./database/{table_name}/{keys[keyIndex]}.txt", "a") as key_file :
                key_file.write(f"{values[keyIndex]}\n")
                key_file.close()