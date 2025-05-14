import os, time
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv('config.env', override=True)

class Config(object):
    ##API_KEY get it from dev, dont edit if added
    API_KEY = os.environ.get("API_KEY", "https://api.hotstar.com/h/v1/play?contentId=1260132573")
    #telegram user session str for 4gb limit
    SESSION_STRING = os.environ.get("SESSION_STRING", "BQGlVqIAaQCW7onbtdCbesyxExwOHWBZeA-bYLODgc95BpZSiHbwqGA0CC8_9EDtVxhSjDnAlLRGO3wM-oFp4CGEWCIn1Q996Xz4jCAlXPbc4eHRI06yRuuE3K_rd1uuBoL2IrdDaOA3447-dwVkdWRhH2yYrisu0NhFPEX4tXORVGhAw6NJSv5wjZ1-wzsRZZFHpTsCPSr8RybxCOWYiBZUpjNc1JPkNBPgr1KU4XOQbvjU")
    #tg bot token
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    #api id and hash get it from my.telegram.org
    API_ID = int(os.environ.get("API_ID", 467))
    API_HASH = os.environ.get("API_HASH", "ff6bc6ad204ca7f5773")
    PROXY = os.environ.get("PROXY", "")
    DB_URL = os.environ.get("DB_URL", "?retryWrites=true&w=majority&appName=Cluster0")
    OWNER_ID = [int(i) for i in  os.environ.get("OWNER_ID", "7126874550").split(" ")]
    #log channel, where to send logs
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    #gdrive folder id for upload
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "1-geGQG9k7_idJ0876uDYqTe")
    #use service accounts or not, used to bypass daily upload limit
    USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS","False")
    #is team drive
    IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", "True")
    #index url of gdrive folder
    INDEX_LINK = os.environ.get("INDEX_LINK", "https://widewine.example.workers.dev/0:/BOT")
    HOTSTAR_USER_TOKEN = os.environ.get("HOTSTAR_USER_TOKEN", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6IiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTczNjQyOTEzMSwiaWF0IjoxNzM2MzQyNzMxLCJpc3MiOiJUUyIsImp0aSI6ImNmMmI0MWMwODVjZjRkYmM5YTg3NzhmYzViOWJjMmRhIiwic3ViIjoie1wiaElkXCI6XCJjMTkzZDJiZjM1MmQ0M2E0OTcxYWRiMjIzODQ5MGJlYVwiLFwicElkXCI6XCJkYTM0M2E0ZDc0Mzg0ZDQ5YWE1NjQyMTZkMDlhY2NmMFwiLFwiZHdIaWRcIjpcIjdmMDA5Mjk0OWY0ZDUwYzVlMWI4MDE2NGMzMzIxMjNhYWExYWFlY2NjNDZlMjJmNTg1MzFmNGEyZWRhMmJmNWZcIixcImR3UGlkXCI6XCJiMDJmYzZlYTUwMWM3ZGY4OGQxNmE4ZjM3ZjYzZTEzN2FhZWRmMGViMTZiYTNjMDgxYzZjYTg2OTI2ZWUwNWMxXCIsXCJvbGRIaWRcIjpcImMxOTNkMmJmMzUyZDQzYTQ5NzFhZGIyMjM4NDkwYmVhXCIsXCJvbGRQaWRcIjpcImRhMzQzYTRkNzQzODRkNDlhYTU2NDIxNmQwOWFjY2YwXCIsXCJpc1BpaVVzZXJNaWdyYXRlZFwiOmZhbHNlLFwibmFtZVwiOlwiTUFIRVNIXCIsXCJwaG9uZVwiOlwiODMzMTkxNTU3OFwiLFwiaXBcIjpcIjQ5LjQ3LjEzMy4xMzlcIixcImNvdW50cnlDb2RlXCI6XCJpblwiLFwiY3VzdG9tZXJUeXBlXCI6XCJudVwiLFwidHlwZVwiOlwicGhvbmVcIixcImlzRW1haWxWZXJpZmllZFwiOmZhbHNlLFwiaXNQaG9uZVZlcmlmaWVkXCI6dHJ1ZSxcImRldmljZUlkXCI6XCI0ZDdkZTktOGU2ZDU0LTJiZTcxMy04ZmY1ZjNcIixcInByb2ZpbGVcIjpcIkFEVUxUXCIsXCJ2ZXJzaW9uXCI6XCJ2MlwiLFwic3Vic2NyaXB0aW9uc1wiOntcImluXCI6e1wiSG90c3RhclN1cGVyXCI6e1wic3RhdHVzXCI6XCJDXCIsXCJleHBpcnlcIjpcIjIwMjUtMDMtMjZUMDU6NTU6NTYuMDAwWlwiLFwic2hvd0Fkc1wiOlwiMVwiLFwiY250XCI6XCIxXCJ9fX0sXCJlbnRcIjpcIkNyMEJDZ1VLQXdvQkJSS3pBUklIWVc1a2NtOXBaQklEYVc5ekVnTjNaV0lTQ1dGdVpISnZhV1IwZGhJR1ptbHlaWFIyRWdkaGNIQnNaWFIyRWdSdGQyVmlFZ2QwYVhwbGJuUjJFZ1YzWldKdmN4SUdhbWx2YzNSaUVnUnliMnQxRWdkcWFXOHRiSGxtRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0JtdGxjR3hsY2hvQ2MyUWFBbWhrR2dObWFHUWlBM05rY2lvR2MzUmxjbVZ2S2doa2IyeGllVFV1TVNvS1pHOXNZbmxCZEcxdmMxZ0JDZzBTQ3dnQ09BSkFBVkM0Q0ZnQkNpSUtHZ29PRWdVMU5UZ3pOaElGTmpRd05Ea0tDQ0lHWm1seVpYUjJFZ1E0WkZnQkN0QUJDZ1VLQXdvQkFCTEdBUklIWVc1a2NtOXBaQklEYVc5ekVnTjNaV0lTQ1dGdVpISnZhV1IwZGhJR1ptbHlaWFIyRWdkaGNIQnNaWFIyRWdSdGQyVmlFZ2QwYVhwbGJuUjJFZ1YzWldKdmN4SUdhbWx2YzNSaUVnUnliMnQxRWdkcWFXOHRiSGxtRWdwamFISnZiV1ZqWVhOMEVnUjBkbTl6RWdSd1kzUjJFZ05xYVc4U0JtdGxjR3hsY2hJRWVHSnZlQklMY0d4aGVYTjBZWFJwYjI0YUFuTmtHZ0pvWkJvRFptaGtJZ056WkhJcUJuTjBaWEpsYnlvSVpHOXNZbmsxTGpFcUNtUnZiR0o1UVhSdGIzTllBUko4Q0FFUTRKT1dpTjB5R2tRS0draHZkSE4wWVhKVGRYQmxjaTVKVGk0elRXOXVkR2d1TWpRNUVneEliM1J6ZEdGeVUzVndaWElhQkZObGJHWWc0T09rak1BeUtPQ1Rsb2pkTWpBR09BTkFCU2dCTUFFNkpRb2hTRzkwYzNSaGNsTjFjR1Z5TGtGa2MwWnlaV1V1U1U0dVdXVmhjaTR4TURrNUVBRklBUT09XCIsXCJpc3N1ZWRBdFwiOjE3MzYzNDI3MzE5MzcsXCJtYXR1cml0eUxldmVsXCI6XCJBXCIsXCJpbWdcIjpcIjVcIixcImRwaWRcIjpcImRhMzQzYTRkNzQzODRkNDlhYTU2NDIxNmQwOWFjY2YwXCIsXCJzdFwiOjEsXCJkYXRhXCI6XCJDZ1FJQUJJQUNnUUlBQ29BQ2hJSUFDSU9nQUUzaUFFQ2tBSCs2NHFEMVM0S0JBZ0FNZ0FLQkFnQU9nQUtMZ2dBUWlvS0tFSXdNV1UxTkRVMU1EY3dOemswTmpFeU9UZ3lNREF5TUdWalpqQXdOVEF4TUV4d1NIQk5hRms9XCJ9IiwidmVyc2lvb")
    HOTSTAR_DEVICE_ID = "41f"
    END_NAME = os.environ.get("END_NAME", "@aryanchy451")
    METADATA_NAME = os.environ.get("METADATA_NAME", "@aryanchy451")
    TEMP_DIR = os.environ.get("TEMP_DIR", "output")
    TG_SPLIT_SIZE = int(os.environ.get("TG_SPLIT_SIZE","2000000000"))
    if SESSION_STRING == "" or SESSION_STRING is None:
        TG_SPLIT_SIZE = TG_SPLIT_SIZE
    USE_SERVICE_ACCOUNTS = USE_SERVICE_ACCOUNTS.lower() == "true"
    IS_TEAM_DRIVE = IS_TEAM_DRIVE.lower() == "true"
    HOTSTAR_REFRESH = time.time()
