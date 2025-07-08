import subprocess
import sys

# Test the flexible name matching
test_cases = [
    ("diluc", "wolf"),  # Partial matches
    ("xiao", "jade"),   # Partial matches
    ("ganyu", "amos"),  # Partial matches
    ("hutao", "homa"),  # Should work even without space
    ("hu", "staff"),    # Very partial matches
]

print("Testing flexible name matching:")
print("=" * 50)

for character, weapon in test_cases:
    print(f"\nTesting: Character='{character}', Weapon='{weapon}'")
    try:
        # Create input for the program
        input_data = f"{character}\n{weapon}\n"
        
        # Run the program with input
        result = subprocess.run(
            [sys.executable, "EffectiveAttack.py"],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=10
        )
        
        print("Output:")
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("Test timed out")
    except Exception as e:
        print(f"Error running test: {e}")
    
    print("-" * 30)
