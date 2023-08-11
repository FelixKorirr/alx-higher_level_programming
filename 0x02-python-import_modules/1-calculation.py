#!/usr/bin/python3
def main():
 
  a = 10
  b = 5

  import calculator_1 as total

  print(f"{'10 + 5 = '} {total.add(a,b)}")
  print(f"{'10 - 5 = '} {total.sub(a,b)}")
  print(f"{'10 * 5 = '} {total.mul(a,b)}")
  print(f"{'10 / 5 = '} {total.div(a,b)}")

if __name__ == "__main__":
 main()
