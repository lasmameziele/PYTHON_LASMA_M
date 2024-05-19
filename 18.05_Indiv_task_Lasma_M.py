print("Welcome to the bank. We are happy to see you!")
balance = 0

while True:
  user_input=input("Please Enter a deposit amount or type 'exit' to quit.")
  
  if user_input.lower() == "exit":
    print(f'Your total balance is: {balance} euros. See you next time!')
    break

  try:
    deposit_int=int(user_input)
    balance +=deposit_int
    print(f'You deposited {deposit_int} euros')
    print(f'Your current balance is: {balance} euros.')
    
  except ValueError:
    print("Please enter a valid amount to your balance or 'exit' to quit")

