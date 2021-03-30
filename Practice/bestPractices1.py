from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Begin Processing...")
    modified_data = data + " that has been modifed"
    sleep(3)
    print("Finished Processing.")
    return modified_data


if __name__ == "__main__":
    data = "My data read from Web"
    print(data)
    
    newData = process_data(data)
    print(newData)