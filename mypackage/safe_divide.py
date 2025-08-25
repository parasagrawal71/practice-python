def safe_divide(a, b):
    try:
        result = a / b
    except Exception as e: # ZeroDivisionError
        print("Error:", e)
        result = None
    finally:
        print("Execution completed (cleanup can go here).")
    return result

print("\n")
print(safe_divide(10, 2))   # ✅ Works fine
print(safe_divide(10, 0))   # ❌ Triggers exception
print("\n")