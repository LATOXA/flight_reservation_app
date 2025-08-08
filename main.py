from database import initialize_db
import home

if __name__ == "__main__":
    initialize_db()
    home.run_home_page()
