a=input("Enter the number:")
print(f"Multipliction table for{a} is:")
try:
  for i in range(1,20):
    print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
 print(e)
 print("thanks")