import os
import sys

def check_env():
    print("🔍 Checking Environment...")
    if not os.path.exists(".env"):
        print("❌ .env file missing!")
        return False
    print("✅ .env file present.")
    return True

def check_dependencies():
    print("🔍 Checking Dependencies...")
    try:
        import crewai
        import fastapi
        print(f"✅ CrewAI version: {crewai.__version__}")
        print(f"✅ FastAPI version: {fastapi.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def main():
    print("=== CrewAI Production Blueprint Health Check ===")
    env_ok = check_env()
    deps_ok = check_dependencies()
    
    if env_ok and deps_ok:
        print("\n✨ System Health: EXCELLENT")
    else:
        print("\n⚠️ System Health: ISSUES FOUND")
        sys.exit(1)

if __name__ == "__main__":
    main()
