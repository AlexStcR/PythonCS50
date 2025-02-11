def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break  # Exit the loop if everything is successful
        except ValueError:
            continue  # Prompt again if input is invalid
        except ZeroDivisionError:
            continue  # Prompt again if denominator is 0


def convert(fraction):
    try:
        # Split the fraction into numerator and denominator
        x = fraction.split("/")
        if len(x) != 2:
            raise ValueError("Invalid format")

        numerator, denominator = int(x[0]), int(x[1])

        # Check for division by zero
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero")


        y=numerator/denominator*100
            #print(y)
        if y>100:
            raise ValueError# Calculate and return the rounded tank level as a decimal
        return y

    except (ValueError, ZeroDivisionError):
        raise  # Re-raise the exception to be handled in `main`


def gauge(percentage):
    # Check percentage levels and return the corresponding gauge value
    if percentage <= 1:
        return ("E")  # Empty
    elif 99 <= percentage <= 100:
        return("F")  # Full
    elif 0 < percentage < 100:

       return(f"{int(round(percentage))}%")  # Convert to percentage format
    else:
        raise ValueError("Invalid percentage value")



if __name__ == "__main__":
    main()
