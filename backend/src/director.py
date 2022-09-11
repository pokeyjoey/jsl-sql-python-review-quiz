class Director:
    __table__ = 'director'
    columns = ['id', 'full_name']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

    def first_name(self):
        first_name = self.full_name.split(' ')[0]

        return first_name

    def last_name(self):
        last_name = self.full_name.split(' ')[-1]

        return last_name

    def movies(self, cursor):
        query = \
            f"""SELECT m.id, m.title, m.year FROM movies m
                JOIN movie_directors md
                ON md.movie_id = m.id
                WHERE md.director_id = {self.id}"""
        cursor.execute(query)
        records = cursor.fetchall()

        return records
