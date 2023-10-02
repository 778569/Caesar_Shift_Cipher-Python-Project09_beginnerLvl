alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    if char not in alphabet:
      
      end_text += char
    else: 
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo

print(logo);

Work_Cont = False

while not Work_Cont:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if shift > 25:
    shift %= 26 
    # print(shift)
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  
  Input_Type = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if Input_Type == "no":
    print("Good Bye.!")
    Work_Cont = True

  