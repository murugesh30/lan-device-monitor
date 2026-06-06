from database import create_table
from monitor import start_monitoring

if __name__ == "__main__":

    create_table()

    start_monitoring()