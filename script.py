import sys
if len(sys.argv) != 3:
  print("Error: se requieren dos argumentos")
else:
    if type(sys.argv[1])==int and type(sys.argv[2])==int:
        if (int(sys.argv[1]) + int(sys.argv[2])) >= 6:
            print("Aprobado")
        else:
            print("No aprobado")
    else:
        print("Error, deben ser dos enteros") 
print(sys.argv)