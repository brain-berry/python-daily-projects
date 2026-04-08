from datetime import date

# ──────────────────────────────────────────────
#  AGE CALCULATOR
# ──────────────────────────────────────────────

print("\n" + "=" * 35)
print("  AGE CALCULATOR")
print("=" * 35)

name = input("\nEnter your name: ").strip()

if not name:
    print("\n  No name entered.")
else:
    # Get birth date
    try:
        print("\nEnter your birth date:")
        birth_year = int(input("  Year (e.g., 1990): "))
        birth_month = int(input("  Month (1-12): "))
        birth_day = int(input("  Day (1-31): "))

        # Validate and create date
        birth_date = date(birth_year, birth_month, birth_day)
        today = date.today()

        # Check if birth date is in the future
        if birth_date > today:
            print("\n  Birth date cannot be in the future.")
        else:
            # Calculate years
            years = today.year - birth_date.year

            # Calculate months
            months = today.month - birth_date.month

            # Calculate days
            days = today.day - birth_date.day

            # Adjust for negative days
            if days < 0:
                months -= 1
                # Get days in previous month
                if today.month == 1:
                    prev_month = 12
                else:
                    prev_month = today.month - 1
                
                prev_month_days = (date(today.year, today.month, 1) - date(today.year, prev_month, 1)).days
                days += prev_month_days

            # Adjust for negative months
            if months < 0:
                years -= 1
                months += 12

            # Calculate total months and days
            total_months = years * 12 + months
            total_days = (today - birth_date).days

            # Display results
            print("\n" + "-" * 35)
            print(f"  Name: {name.title()}")
            print(f"  Born: {birth_date.strftime('%B %d, %Y')}")
            print("-" * 35)
            print(f"  Age: {years} year(s), {months} month(s), {days} day(s)")
            print("-" * 35)
            print(f"  Total Months: {total_months}")
            print(f"  Total Days:   {total_days}")
            print("-" * 35)

    except ValueError:
        print("\n  Invalid date. Please enter valid numbers.")
