from datetime import datetime

# Get today's date
today = datetime.today()

# Print in various formats
print("mm/dd/yyyy      :", today.strftime("%m/%d/%Y"))
print("mmddyyyy       :", today.strftime("%m%d%Y"))
print("yyyy-MMM-dd     :", today.strftime("%Y-%b-%d"))
print("mm-dd-yyyy      :", today.strftime("%m-%d-%Y"))