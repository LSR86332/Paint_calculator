def paint_calculator():
    # Define realistic limits (in meters)
    LIMITS = {
        "wall": {"height": (1.8, 10.0), "width": (0.5, 20.0)},
        "door": {"height": (1.5, 3.0), "width": (0.5, 2.5)},
        "window": {"height": (0.5, 3.0), "width": (0.5, 3.0)}
    }

    print("\U0001f3a8 Welcome to the Multi-Room Paint Calculator!")

    # Ask user for unit scale
    scale_in = input("Enter the scale for measurement (m for meters, f for feet): ").lower()
    conversion_factor = 1
    unit = "meters"
    if scale_in == 'f':
        conversion_factor = 0.092903
        unit = "feet"
        # Convert limits from meters to feet
        for item in LIMITS:
            for dim in LIMITS[item]:
                min_val, max_val = LIMITS[item][dim]
                LIMITS[item][dim] = (min_val / 0.3048, max_val / 0.3048)
        print("Using feet. All areas will be converted to square meters.")
    elif scale_in != 'm':
        print("Invalid scale. Defaulting to meters.")

    try:
        num_rooms = int(input("\nEnter the number of rooms: "))
        if num_rooms <= 0:
            raise ValueError("Number of rooms must be at least 1.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    total_paint_area = 0

    for room in range(1, num_rooms + 1):
        print(f"\n\U0001f3e0 Room {room}:")

        try:
            num_walls = int(input("  Enter the number of walls: "))
            if num_walls <= 0:
                raise ValueError("  Number of walls must be positive.")
        except ValueError as e:
            print(f"  Invalid wall count: {e}")
            return

        wall_area = 0
        for i in range(num_walls):
            print(f"    Wall {i+1}:")
            try:
                h = float(input("      Enter height: "))
                w = float(input("      Enter width: "))
                min_h, max_h = LIMITS["wall"]["height"]
                min_w, max_w = LIMITS["wall"]["width"]
                if not (min_h <= h <= max_h) or not (min_w <= w <= max_w):
                    raise ValueError(f"Wall dimensions should be between {min_h:.2f}-{max_h:.2f} and {min_w:.2f}-{max_w:.2f} {unit}.")
                wall_area += h * w * conversion_factor
            except ValueError as e:
                print(f"      Invalid wall dimensions: {e}")
                return

        # Doors
        try:
            num_doors = int(input("  Enter number of doors: "))
            if num_doors < 0:
                raise ValueError("Can't have negative doors.")
        except ValueError as e:
            print(f"  Invalid door count: {e}")
            return

        door_area = 0
        for i in range(num_doors):
            print(f"    Door {i+1}:")
            try:
                h = float(input("      Enter height: "))
                w = float(input("      Enter width: "))
                min_h, max_h = LIMITS["door"]["height"]
                min_w, max_w = LIMITS["door"]["width"]
                if not (min_h <= h <= max_h) or not (min_w <= w <= max_w):
                    raise ValueError(f"Door dimensions should be between {min_h:.2f}-{max_h:.2f} and {min_w:.2f}-{max_w:.2f} {unit}.")
                door_area += h * w * conversion_factor
            except ValueError as e:
                print(f"      Invalid door dimensions: {e}")
                return

        # Windows
        try:
            num_windows = int(input("  Enter number of windows: "))
            if num_windows < 0:
                raise ValueError("Can't have negative windows.")
        except ValueError as e:
            print(f"  Invalid window count: {e}")
            return

        window_area = 0
        for i in range(num_windows):
            print(f"    Window {i+1}:")
            try:
                h = float(input("      Enter height: "))
                w = float(input("      Enter width: "))
                min_h, max_h = LIMITS["window"]["height"]
                min_w, max_w = LIMITS["window"]["width"]
                if not (min_h <= h <= max_h) or not (min_w <= w <= max_w):
                    raise ValueError(f"Window dimensions should be between {min_h:.2f}-{max_h:.2f} and {min_w:.2f}-{max_w:.2f} {unit}.")
                window_area += h * w * conversion_factor
            except ValueError as e:
                print(f"      Invalid window dimensions: {e}")
                return

        effective_area = wall_area - (door_area + window_area)
        if effective_area <= 0:
            print("⚠️  Effective area is zero or negative. Skipping this room.")
            continue

        print(f"  ✅ Paintable area for Room {room}: {effective_area:.2f} square meters")
        total_paint_area += effective_area

    if total_paint_area == 0:
        print("\n⚠️ No valid paintable area found in any room.")
        return

    try:
        coverage_per_litre = float(input("\nEnter paint coverage per litre (in sq. meters): "))
        num_coats = int(input("Enter number of coats: "))
        if coverage_per_litre <= 0 or num_coats <= 0:
            raise ValueError("Coverage and coats must be positive.")
    except ValueError as e:
        print(f"Invalid input for paint data: {e}")
        return

    total_paint_required = (total_paint_area * num_coats) / coverage_per_litre
    print(f"\n\U0001f3af TOTAL paintable area: {total_paint_area:.2f} sq.m")
    print(f"\U0001faa3 TOTAL paint required: {total_paint_required:.2f} litres\n")

# Run it
paint_calculator()
