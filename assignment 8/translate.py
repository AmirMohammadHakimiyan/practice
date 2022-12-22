import gtts
import os 

def read_from_file():
  
 #filename="my_python/translate.txt"
 filename="session8/translate.txt"

 try:
  global words_bank
  f = open(filename , "r")

  temp = f.read().split("\n")

  words_bank = []
  for i in range (0,len(temp),2):
    my_dic = {"en": temp[i],"fa": temp[i+1]}

    words_bank.append(my_dic)

  f.close()
 except OSError as e:
   print("File " + filename + " is not available, please upload the file.")

def convert_text_to_voice(my_text):
  x = gtts.gTTS(my_text, lang="en", slow = False )
  return x

def translate_english_to_persian():
 user_text = input("enter your english text:")

 user_texts = user_text.split(".")
 out_put= " " 
 for sentence in user_texts:
    user_words = sentence.split(" ")
    for user_word in user_words:
     for word in words_bank:
        if user_word == word["en"]:
            out_put += word["fa"] + " "
            break
     else:
        out_put += word["fa"] + " "
    out_put += "."
 print(out_put)
 x = convert_text_to_voice(out_put)
 x.save("session8/voice1.mp3")

def translate_persian_to_english():
 user_text = input("enter your persian text:")

 user_texts = user_text.split(".")
 out_put= " " 
 for sentence in user_texts:
    user_words = sentence.split(" ")
    for user_word in user_words:
     for word in words_bank:
        if user_word == word["fa"]:
            out_put += word["en"] + " "
            break
     else:
        out_put += word["fa"] + " "
    out_put += "."
 print(out_put)
 x = convert_text_to_voice(out_put)
 x.save("session8/voice2.mp3")

def write_in_file():

 #filename="my_python/translate.txt"
 filename="session8/translate.txt"
 try:
   f = open(filename, 'a')
   first_word = input("enter your english word:")
   f.write("\n" + first_word)
   second_word = input("enter your persian word:")
   f.write("\n" + second_word)

   f.close()
 except OSError as e:
   print("File " + filename + " is not available, please upload the file.")
 
def show_menu():
  print("\nwelcom to my translate")
  print("1_translate english to persian")
  print("2_translate persian to english")
  print("3_add a new word to database")
  print("4_exit")

def main():
 while True:

  read_from_file()
  show_menu()

  choice = int(input("enter your choice:"))
  if choice == 1 :
    translate_english_to_persian()
  elif choice == 2:
    translate_persian_to_english()
  elif choice == 3:
     write_in_file()
  elif choice == 4:
    exit()

main()
