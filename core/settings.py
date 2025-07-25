from pathlib import Path

from dotenv import load_dotenv

env_path = Path(__file__).parent.parent.parent / ".template.env"
load_dotenv(env_path)