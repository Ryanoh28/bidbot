def bidbot():
  print("Hello, I am Bidbot, how can I help you today?")
  
  while True:
    user_input = input("You: ").lower()
    
    if user_input == "hi" or user_input == "hello":
      print("Bidbot: Hello there! I can help you with admin operations and Reflex.")
    elif user_input == "spooler" or user_input == "spool":
      print("""Bidbot: To open the spooler, press F10. Then use the arrow keys to select 'Spool'. Go to edit then press F3 to view everything sent to print that you have permissions to view. Use arrow keys to go up and down and page up page down to go up and down a page. Enter into what you required and press F4 to reprint. Hope this helps""")
    elif user_input == "natop" or user_input == "na":
      print("""Bidbot: A NATOP is an item that is not available to pick. It will be noted on the pickers pick note and you will need to record this onto the nights NATOP report. You will need the account number, route and drop, product code, ordered amount, short amount, hub details and the hub invoice number if available.""")
    elif user_input == "sales report" or user_input == "sale report":
      print(""""Bidbot: Use the program W12002 to clear or cancel sales reports. Go through the sales report one by one and enter the remaining number into the system. You take away the number the dropdown driver wrote from the number that's already on the sheet. This leaves you with what remains.
      
      If there is an 'X' next to the available number, that means the dropdown driver didn't move anything. The stock remains unchanged so you put a zero into the system.
      
      If there is a '0' (zero) next to the available number, that means everything has moved. Do not change the number on the system as it all needs to be removed you can leave it unchanged.
      
      Once you've reached the end of the sheet you can press F7 to exit.
      
      Be careful when entering sales reports as when you confirm one, you cannot change what you've put in through K12002.""")
    elif user_input == "dropdown" or user_input == "dropdowns" or user_input == "drop down" or user_input == "drop downs":
      print("""Bidbot: To enter a dropdown, use the program W100002.
      
      The dropdown driver will write the product location and product code on the dropdown sheet and how much has gone back into the location. Subtract that number from the number on the system and enter the remaining number to update the stock. 
      
      If "0" (zero) has been written on the dropdown sheet, nothing has been returned. Leave the number on the system unchanged and confirm the move.""")
    elif user_input == "invoice" or user_input == "invoices":
      print("""Bidbot: To view invoices waiting to print, use the program RQAIP. This will display the invoices waiting to print and their delivery date.
      
      To print invoices, use program K13002.
      
      All invoices need to be printed before you're able to set the flag.""")
    elif user_input == "urban" or user_input == "urbans" or user_input == "urban delivery" or user_input == "urban delivery note" or user_input == "urban delivery notes":
      print("Bidbot: To print urban delivery notes, use the program K13300.")
    elif user_input == "picknote" or user_input == "picknotes" or user_input == "pick note" or user_input == "pick notes":
      print("""Bidbot: To print pick notes, use the program K13031.
      
      Only print picknotes after Stowmarket and/or Harlow have sent cut off emails. If picknotes are released before, they will not be routed correctly and you will need to call IT.
      
      If you need to reprint picknotes, you can use the spooler. Type "Spool" to see how to do this.""")
    elif user_input == "p12" or user_input == "picknote checklist" or user_input == "pick note checklist":
      print("""Bidbot: To print picknote checklists, use the program RQ0013.""")
    elif user_input == "manifest" or user_input == "order manifest":
      print("Bidbot: To view the order manifest, use the program K13011 or K13111.")
    elif user_input == "meat" or user_input == "meat weights" or user_input == "meat weight" or user_input == "weights" or user_input == "weight":
      print("""Bidbot: To print outstanding meat weights, use the program RQ0013.
      
      Once outstanding weights have been completed, enter them into K12006.""")
    elif user_input == "bulksheet" or user_input == "bulk" or user_input == "bulk sheet" or user_input == "bulksheets":
      print("Bidbot: To print bulk sheets, use the program W80104a. Specify bulk aisles to seperate Ambient and Chilled from Frozen or enter to the bottom without changing anything to print everything in one.") 



    else:
      print("Bidbot: I'm sorry, I don't have any answers for the term you wrote. I'm still being trained :)")



bidbot()