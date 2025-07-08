# Test the enhanced flexible matching with user-friendly features
import subprocess
import sys

def test_enhanced_version():
    print("Testing enhanced version with flexible matching...")
    
    # Test case: using partial names
    test_input = "diluc\nwolf\n"
    
    try:
        result = subprocess.run(
            [sys.executable, "EffectiveAttack.py"],
            input=test_input,
            text=True,
            capture_output=True,
            timeout=15,
            cwd="."
        )
        
        print("=== Test Output ===")
        print(result.stdout)
        
        if result.stderr:
            print("=== Errors ===")
            print(result.stderr)
            
    except subprocess.TimeoutExpired:
        print("Test timed out")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_enhanced_version()
