def load_library(library_file_path):
    library = {}
    with open(library_file_path) as f:
        for row in f:
            product_name, quantity = row.strip().split(".")

            if product_name and quantity in library:
                print(f"Warning: Duplicate value of {product_name}")

                library[product_name] = {
                    "product": product_name,
                    "quantity": quantity,
                }
        return library


def save_library(library, product_name, quantity,library_file_path):
    with open(library_file_path, "w") as f:
        for product_name, quantity in library.items():
            f.write("{}:{}\n".format(product_name["product_name"], quantity["quantity"]))

library = load_library("")
print(library)