from src import get_config
from src.User import User



print(get_config("mongodb_connection_string"))

# uid = User.register("sabarish", "password123", "password123")
try:
    User.login("sabarish", "pdassword123")
    print("egeg")
except Exception as e:
    print(e)