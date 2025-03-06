from models.__init__ import CONN, CURSOR

class Brand:
    all = []

    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.id = None

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS brands (
                id INTEGER PRIMARY KEY,
                name TEXT,
                country TEXT
            )
        """

        CURSOR.execute(sql)


    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS brands
        """

        CURSOR.execute(sql)

    def save(self):
        sql = """
            INSERT INTO brands (
                name,
                country
            )
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.country))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Brand.all.append(self)

    @classmethod
    def create(cls, name, country):
        brand = cls(name, country)
        brand.save()
        return brand

    @classmethod
    def instance_from_db(cls, row):
        brand = cls(row[1], row[2])
        brand.id = row[0]
        return brand


    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM brands
        """

        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all

    def __repr__(self):
        return f"<Brand #{self.id} - Name: {self.name}, Country: {self.country}>"


    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM brands
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.instance_from_db(row)
        else:
            return None

    def delete(self):
        sql = """
            DELETE FROM brands
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Brand.all = [brand for brand in Brand.all if brand.id != self.id]

    # One brand has many car models
    def car_models(self):
        from models.car_model import CarModel
        sql = """
            SELECT * FROM car_models
            WHERE brand_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [CarModel.instance_from_db(row) for row in rows]


    @property
    def name_getter(self):
        return self._name

    @name_getter.setter
    def name(self, value):
        if (type(value) == str) and (len(value) >= 4):
            self._name = value
        else:
            raise Exception("Error: Name must be a string that is at least 4 characters long")


    @property
    def country_getter(self):
        return self._country

    @country_getter.setter
    def country(self, value):
        if (type(value) == str) and (len(value) >= 4):
            self._country = value
        else:
            raise Exception("Error: Name must be a string that is at least 4 characters long")
