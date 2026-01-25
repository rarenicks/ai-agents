import os
import sys

# Add root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def check_env():
    print("🔍 Checking Environment...")
    if not os.path.exists(".env"):
        print("❌ .env file missing!")
        return False
    
    from config.settings import settings
    if not settings.OPENAI_API_KEY or "your_" in settings.OPENAI_API_KEY:
        print("⚠️ OPENAI_API_KEY not configured correctly in .env")
        return False
        
    print("✅ Environment configured.")
    return True

def check_dependencies():
    print("🔍 Checking Dependencies...")
    try:
        import autogen
        import fastapi
        print(f"✅ AutoGen version: {autogen.__version__}")
        print(f"✅ FastAPI version: {fastapi.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return False

def main():
    print("=== AutoGen Production Blueprint Health Check ===")
    env_ok = check_env()
    deps_ok = check_dependencies()
    
    if env_ok and deps_ok:
        print("\n✨ System Health: EXCELLENT")
    else:
        print("\n⚠️ System Health: ISSUES FOUND")
        sys.exit(1)

if __name__ == "__main__":
    main()
