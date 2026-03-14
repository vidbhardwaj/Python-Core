#exception_handling
def divide_numbers():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        result = a / b
        print(f"Result = {result}")
    except Exception as e:   
        print(f"❌ Error occurred: {e}")
    finally:
        print("✅ Program finished (finally always runs).")
if __name__ == "__main__":
    divide_numbers()