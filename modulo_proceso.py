def calcular_promedio(notas):
  
    if not notas:
        return 0  
    return sum(notas) / len(notas)

if __name__ == "__main__":
    sample_notas = [10, 8, 9, 7]
    print("Promedio:", calcular_promedio(sample_notas))
