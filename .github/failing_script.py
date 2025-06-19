def main():
    print("This script is about to fail...")
    
    # This will raise a ZeroDivisionError
    result = 10 / 0
    
    print("This line will never be reached")

if __name__ == "__main__":
    main()
