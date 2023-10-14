
for i in [0]: # 0-6
    print(f"\n# {i}")
    for size in [500, 1369]: 
        print(f"\n[] {size}")
        """
        print("Top Numbers")
        print(f"num1={((i + size / 1500) * (size / 7.5) + size / 22)}, | num2={size * 0.1}")
    for size in [500, 1369]:
        print(f"\n[] {size}")
        print("Bottom Numbers")
        print(f"num1={((i + size / 1500) * (size / 7.5) + size / 22)}, | num2={size - size * 0.1}") 
    """
        x_coordinate = ((i + size / 1500) * (size / 7.5))
        for j in [0,5]: # 0-5
            num2 = ((j + size / 1500) * (size / 7) + size * 0.1)
            print(f"{j} = {num2}")

