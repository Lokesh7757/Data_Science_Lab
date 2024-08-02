from statistics import mean, median, mode, StatisticsError

def calculate_central_tendency(numbers, choice):
    if choice == "mean":
        return mean(numbers)
    elif choice == "median":
        return median(numbers)
    elif choice == "mode":
        try:
            return mode(numbers)
        except StatisticsError:
            return "No unique mode" 
    else:
        return "Invalid choice"

def main():
    numbers = [float(x) for x in input("Enter numbers :").split()]
    
    if not numbers:
        print("No numbers provided.")
        return
    
    choice = input("Which measure of central tendency would you like to calculate (mean/median/mode)? ").strip().lower()
    
    if choice not in ["mean", "median", "mode"]:
        print("Invalid choice. Please select from mean, median, or mode.")
        return
    
    result = calculate_central_tendency(numbers, choice)
    
    print(f"{choice.capitalize()}: {result}")

if __name__ == "__main__":
    main()