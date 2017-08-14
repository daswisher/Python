while True:
    try:
        carYear = int(input("What year was your car produced?\n"))
        print("Your car's production year is %d" % carYear)
        break
    except ValueError:
        print("Make sure you're entering a year...")
    except ZeroDivisionError:
        print("This resulted in a car year of 0...")
    except:
        print("Crashing...")
        break
        # This handles all exceptions, but can be counterproductive
    finally:
        print("This looped successfully...")
        #This will run every iteration regardless of exception or not
