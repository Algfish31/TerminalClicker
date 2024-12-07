# Make sure to use the exact same code as this, just formatted in another language. Your code will get rejected if not!

# Variables

clicks = 0
cpc = 1
upgrade_price = 100
game_loop = True
command = ""

# Functions

def add_clicks():
  global clicks, cpc
  clicks = clicks + cpc  
  print("Clicks:", clicks)

def buy_upgrade():
  global clicks, cpc, upgrade_price
  if clicks >= upgrade_price:
    clicks = clicks - upgrade_price
    cpc = cpc + 1
    upgrade_price = upgrade_price * 2
    print("Upgrade - Purchase Sucessfull!\n")
    print("Clicks:", clicks)
    print("Clicks per click:", cpc)
    print("Upgrade price:", upgrade_price)
  else:
    print("Upgrade - Purchase Unsucessfull\n")
    print("Required Clicks:", upgrade_price)
    print("Current Clicks:", clicks)

def help():
  print("List of Commands:\n")
  print('"" - Earns one click')
  print('"upgrade" - Buys the Upgrade')
  print('"help" - Shows this')
  print('"about" - Gives details about the game')
  print('"quit" - Quits the game')
  
def about():
  print("ABOUT\n")
  print("Created by: Algfish31") # Replace this with your GitHub username.
  print("Part of the Terminal Clicker Challenge")
  print("https://github.com/Algfish31/TerminalClicker/") 
  print("Enter \"help\" for more info about commands.")

def quit():
  global game_loop
  print("Quitting Game")
  game_loop == False

# MAIN LOOP

print("Terminal Clicker")
print("Enter to click - \"help\" for more info about commands")

while game_loop == True:
  command = input("> ")
  if command == "":
    add_clicks()
  elif command == "upgrade":
    buy_upgrade()
  elif command == "help":
    help()
  elif command == "about":
    about()
  elif command == "quit":
    quit()
    break
  else:
    print("Command not recognized")