from datetime import datetime,date


class Category:

    def __init__(self, name, color="#FFFFFF"):

        self.name = name
        self.color = color


class Movement:

    def __init__(self,title,amount,category,type_movement,movement_date=None):

        self.title = title
        self.amount = amount
        self.category = category
        self.type_movement = type_movement

        if movement_date is None:

            self.date = date.today().strftime("%d/%m/%Y")

        else:

            self.date = movement_date


class FinanceManager:

    def __init__(self):

        self.categories_list = []
        self.movements_list = []


    def find_a_category(self, category_name):

        for category in self.categories_list: #self.categories_list es una lista de objetos, por lo tanto category es un objeto individual el cual tiene name por eso se hace category.name para asi poder acceder al nombre realmente*

            if category_name.lower() == category.name.lower():

                return category

        return None


    def add_category(self, type_category, color="#FFFFFF"):

        clean_category = type_category.strip()

        if not clean_category:

            raise ValueError("El nombre de la categoria no debe de estar vacio")

        if not self.find_a_category(clean_category):

            new_category = Category(
                clean_category,
                color
            )

            self.categories_list.append(new_category)

        else:

            raise ValueError("Categoria existente")


    def validate_date(self, movement_date):

        try:

            selected_date = datetime.strptime(
                movement_date,
                "%d/%m/%Y"
            ).date()

        except ValueError:

            raise ValueError(
                "Formato de fecha inválido (use dd/mm/yyyy)"
            )

        if selected_date > date.today():

            raise ValueError(
                "La fecha no puede ser en el futuro"
            )

        return movement_date


    def _data_movement(
        self,
        title,
        amount,
        category,
        movement_date=None
    ):

        clean_title = title.strip()
        clean_category = category.strip()

        if not clean_title:

            raise ValueError("El titulo no debe de estar vacio")

        if not amount:

            raise ValueError("Monto no puede estas vacio")

        if not isinstance(amount, (int, float)):

            raise ValueError("El monto debe de ser un numero")

        if amount <= 0:

            raise ValueError("Monto invalido")

        if not clean_category:

            raise ValueError("El nombre de la categoria no debe de estar vacio")

        found_category = self.find_a_category(clean_category)

        if not found_category:

            raise ValueError("La categoria no existe")

        if movement_date is None:

            movement_date = date.today().strftime("%d/%m/%Y")

        self.validate_date(movement_date)

        return found_category


    def add_expense(
        self,
        title,
        amount,
        category,
        movement_date=None
    ):

        found_category = self._data_movement(
            title,
            amount,
            category,
            movement_date
        )

        if movement_date is None:

            movement_date = date.today().strftime("%d/%m/%Y")

        new_movement = Movement(
            title,
            amount,
            found_category.name,
            "Gasto",
            movement_date
        )

        self.movements_list.append(new_movement)


    def add_income(
        self,
        title,
        amount,
        category,
        movement_date=None
    ):

        found_category = self._data_movement(
            title,
            amount,
            category,
            movement_date
        )

        if movement_date is None:

            movement_date = date.today().strftime("%d/%m/%Y")

        new_movement = Movement(
            title,
            amount,
            found_category.name,
            "Ingreso",
            movement_date
        )

        self.movements_list.append(new_movement)


    def add_saving(
        self,
        title,
        amount,
        category,
        movement_date=None
    ):

        found_category = self._data_movement(
            title,
            amount,
            category,
            movement_date
        )

        if movement_date is None:

            movement_date = date.today().strftime("%d/%m/%Y")

        new_movement = Movement(
            title,
            amount,
            found_category.name,
            "Ahorro",
            movement_date
        )

        self.movements_list.append(new_movement)


    def filter_movements(
        self,
        start_date,
        end_date
    ):

        self.validate_date(start_date)
        self.validate_date(end_date)

        start = datetime.strptime(
            start_date,
            "%d/%m/%Y"
        ).date()

        end = datetime.strptime(
            end_date,
            "%d/%m/%Y"
        ).date()

        if start > end:

            raise ValueError(
                "La fecha inicial no puede ser mayor que la fecha final"
            )

        filtered_movements = []

        for movement in self.movements_list:

            movement_date = datetime.strptime(
                movement.date,
                "%d/%m/%Y"
            ).date()

            if start <= movement_date <= end:

                filtered_movements.append(movement)

        return filtered_movements


    def calculate_summary(self):

        total_income = 0
        total_expense = 0
        total_saving = 0


        for movement in self.movements_list:

            if movement.type_movement=="Gasto":

                total_expense+=movement.amount

            elif movement.type_movement=="Ingreso":

                total_income+=movement.amount

            elif movement.type_movement == "Ahorro":

                total_saving += movement.amount

        balance = total_income - total_expense - total_saving

        return {
            "income":total_income,
            "expense":total_expense,
            "saving":total_saving,
            "balance":balance
        }