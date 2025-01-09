import argparse
from datetime import datetime


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def main():
    parser = argparse.ArgumentParser(description="Проверка корректности даты.")
    parser.add_argument("date", type=str, help="Дата в формате YYYY-MM-DD")
    args = parser.parse_args()

    if is_valid_date(args.date):
        print(f"Дата {args.date} является корректной.")
    else:
        print(f"Дата {args.date} некорректна.")


if __name__ == "__main__":
    main()
