from mysql.connector import pooling, errors
from database_commands.product import ProductModel
from database_commands.orders import OrdersModel
from database_commands.admin import AdminModel
from database_commands.customers import CustomersModel
from database_commands.warehouse_inventory import WarehuseInventoryModel
from database_commands.warehouse import WarehouseModel

class DatabaseManager:
    def __init__(self, host, user, password, dbname, pool_size = 10):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        
        self.pool_size = pool_size
        self.pool = None
        
        self.product = ProductModel(self)
        self.orders = OrdersModel(self)
        self.admin = AdminModel(self)
        self.customers = CustomersModel(self)
        self.warehouse = WarehouseModel(self)
        self.warehouse_inventory = WarehuseInventoryModel(self)

        self.connect()

    def connect(self):
        try:
            self.pool = pooling.MySQLConnectionPool(
                pool_name="my_sql_pool",
                pool_size=self.pool_size,
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.dbname
            )
        except errors.InterfaceError as e:
            #cant reach server
            print(f"Error: Can't reach sql database: {self.dbname}")
            self.pool = None
        except errors.ProgrammingError as e:
            # invalid credentials
            print(f"Error: Invalid credentials: {self.user}")
            self.pool = None
        except errors.DatabaseError as e:
            # database error
            print(f"Error: General database error")
            self.pool = None


    def is_connected(self):
        self.pool != None
 

    def get_connection(self):
        try:
            return self.pool.get_connection()
        except errors.PoolError as e:
            print(f"No available sql db pools: {e}")
            return None
        except errors.Error as e:
            print(f"Database error: {e}")
            return None

        
    
    