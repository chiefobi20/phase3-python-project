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
            return cls.instance_from_db(row)
        else:
            return None


    def save(self):
        sql = """
            INSERT INTO car_models (
                model_name,
                year,
                brand_id
            )
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.model_name, self.year, self.brand_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        CarModel.all.append(self)

    @classmethod
    def create(cls, model_name, year, brand_id):
        car_model = cls(model_name, year, brand_id)
        car_model.save()
        return car_model


    def delete(self):
        sql = """
            DELETE FROM car_models
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        CarModel.all = [model for model in CarModel.all if model.id != self.id]

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

    @property
    def model_name_getter(self):
        return self._model_name

    @model_name_getter.setter
    def model_name(self, value):
        if (type(value) == str) and (len(value) > 0):
            self._model_name = value
        else:
            raise Exception("Error: Model name must be a string that is at least 1 character long")

    @property
    def year_getter(self):
        return self._year

    @year_getter.setter
    def year(self, value):
        if (type(value) == int):
            self._year = value
        else:
            raise Exception("Error: Year must be an integer")


    @property
    def brand_id_getter(self):
        return self._brand_id

    @brand_id_getter.setter
    def brand_id(self, value):
        if (type(value) == int):
            self._brand_id = value
        else:
            raise Exception("Error: Brand ID must be an integer")
