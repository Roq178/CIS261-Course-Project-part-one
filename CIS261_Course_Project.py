# Name : Roquia Ibrahim
# Class : CIS261
# Lab :Employee Payroll System
# 1/26/2025

def get_input(prompt, min_val=0, max_val= float('inf')):
    """Get and validate numeric input from user."""
    while True:
     try:
           value = float(input(prompt))
           if min_val <= value <= max_val:
              return value
           else:
              print(f"Value must be between {min_val} and {max_val}.")
     except ValueError:
         print("Invalid inout. Please enter a valid number value.")
               
def calculate_pay(hours, rate,tax_rate):
    """Calculate gross pay, tax amount, and net pay."""
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay


def display_employee(name, hours, rate, gross, tax_rate, tax, net):
    """Diaplay information for a single employee."""
    print(f"Employee Name: {name}")
    print(f"Hours Worked: {hours:.2f}")
    print(f"Hourly Rate: ${rate:.2f}")
    print(f"Gross Pay: ${gross:.2f}")
    print(f"Tax Rate: {tax_rate * 100:.2f}%")
    print(f"Tax Amount: ${tax:.2f}")
    print(f"Net Pay: ${net:.2f}")
   
    
def display_totals(emps, hours, gross, tax, net):
    """Display summary totals"""
    print("\nSummary Totals")
    print(f"Total Employees: {emps}")
    print(f"Total Hours Worked: {hours:.2f}")
    print(f"Total Gross Pay: ${gross:.2f}")
    print(f"Total Tax: ${tax:.2f}")
    print(f"Total Net Pay: ${net:.2f}")
    

def main():
    #initialize accumulators
    total_emps = 0
    total_hours = 0
    total_gross = 0
    total_tax = 0
    total_net = 0
     
    
    while True:
          name = input("Enter employee name (or type 'End' to finish): ")
          if name.lower() == "end":
             break
        
          hours = get_input("Enter total hours worked: ", min_val=0)
          rate = get_input("Enter hourly rate: $", min_val=0)
          tax_rate = get_input("Enter tax rate (e.g..0.15 for 15%): ", min_val=0, max_val=1)
        
                # Calculate pay
          gross, tax , net = calculate_pay(hours, rate, tax_rate)
        
                 # employee information
          display_employee(name, hours, rate, gross,  tax_rate, tax, net)
        
           # Totals
          total_emps += 1
          total_hours += hours
          total_gross += gross
          total_tax += tax
          total_net += net
        
         #Display final totals if employe were processed
    if total_emps > 0:
        display_totals(total_emps, total_hours, total_gross, total_tax, total_net)
    else:
        print("No employees were processed.")
        
if __name__ == "__main__":
    main()
    
