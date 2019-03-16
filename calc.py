import add
import mul
import div

# calc.py
# Main Function
def main():
  x = input("Please input number 1: ")
  y = input("Please input number 2: ")
  print("Addition: " + add.add(x,y))
  print("Division: " + div.div(x,y)) 

if __name__== "__main__":
  main()
