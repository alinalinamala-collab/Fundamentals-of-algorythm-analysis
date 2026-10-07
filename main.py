import sys
import re

class Database:
    def __init__(self):
        self.tables = {}

    def execute(self, command):
        cmd = command.strip().rstrip(";").strip()
        if not cmd:
            return

        # create
        match_create = re.match(r"CREATE\s+(\w+)\s*\((.*)\)", cmd, re.I)
        if match_create:
            table_name, cols_str = match_create.groups()
            if table_name in self.tables:
                raise ValueError("Table '{table_name}' already exists")

            cols = [c.strip() for c in cols_str.split(",") if c.strip()]
            self.tables[table_name] = cols
            return f"[OK] create table '{table_name}' with collums {cols}"

        # Insert
        match_insert = re.match(r"INSERT\s+(?:INTO\s+)?(\w+)\s*\((.*)\)", cmd, re.I)
        if match_insert:
            table_name, vals_str = match_insert.groups()
            if table_name not in self.tables:
                raise ValueError("Table '{table_name}' do not exists")
        
            values = [v.strip().strip('"\"') for v in vals_str.split(",") if v.strip()]
            expected = len(self.tables[table_name])
            if len(values) != expected:
                raise ValueError(f"Expected {expected} value(s)', get {len(values)} value(s)")

            return f"[OK] INSERT in '{table_name}' value {values}"

        # SELECT
        match_select = re.match(r"SELECT\s+FROM\s+(\w+)", cmd, re.I)
        if match_select:
            table_name = match_select.group(1)
            if table_name not in self.tables:
                raise ValueError("Table '{table_name}' do not exists")
        
            return f"[OK] SELECT from table '{table_name}'"
        raise ValueError("incorect or unknown command")


# CLI

def main():
    db = Database()
    buffer = ""

    for line in sys.stdin:
        buffer += " " + line.strip()
        while ";" in buffer:
            cmd, buffer = buffer.split(";", 1)
            try:
                res = db.execute(cmd)
                if res:
                    print(res)
            except Exception as e:
                print(f"Помилка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
     