from models.__init__ import CONN, CURSOR

class CarModel:

    all = []

    def __init__(self, model_name, year, brand_id):
        self.id = None
        self.model_name = model_name
        self.year = year
        self.brand_id = brand_id

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS car_models (
                id INTEGER PRIMARY KEY,
                model_name TEXT,
                year INTEGER,
                brand_id INTEGER
            )
        """

        CURSOR.execute(sql)

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS car_models
        """

        CURSOR.execute(sql)

    @classmethod
    def instance_from_db(cls, row):
        car_model = cls(row[1], row[2], row[3])
        car_model.id = row[0]
        return car_model


    def __repr__(self):
        return f"<CarModel # {self.id} - Model Name: {self.model_name}, Year: {self.year}, Brand ID: {self.brand_id}>"


    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM car_models
        """
        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all

    def __repr__(self):
        return f"<CarModel #{self.id} - Model Name: {self.model_name}, Year: {self.year}, Brand ID: {self.brand_id}>"

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM car_models
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_db()
        else:
            return None

    # Car model belongs to brand
    def brand(self):
        from models.brand import Brand
        sql = """
            SELECT * FROM brands
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (self.brand_id,)).fetchone()
        if row:
            return Brand.instance_from_db(row)
        else:
            return None
    # @property
    # def model_name(self):
    #     return self._model_name

    # @model_name.setter
    # def model_name(self, value):