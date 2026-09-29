import FreeSimpleGUI as sg
from datetime import date
from logica import FinanceManager
from persistencia import save_categories,load_categories,save_movements,load_movements,export_movements_csv


def get_category_names(manager):

    category_names=[]

    for category in manager.categories_list:

        category_names.append(category.name)

    return category_names


def update_movements_table(window, manager, movements=None):

    if movements is None:

        movements = manager.movements_list


    movements_data = []
    row_colors = []

    for index, movement in enumerate(movements):

        movements_data.append([
            movement.date,
            movement.title,
            movement.amount,
            movement.category,
            movement.type_movement
        ])


        category = manager.find_a_category(movement.category)

        if category:

            row_colors.append(
                (
                    index,
                    "black",
                    category.color
                )
            )


    window["movements"].update(
        values=movements_data,
        row_colors=row_colors
    )


def update_summary(window, manager):

    summary = manager.calculate_summary()

    window["income"].update(f"Ingresos: ₡{summary['income']}")
    window["expenses"].update(f"Gastos: ₡{summary['expense']}")
    window["saving"].update(f"Ahorros: ₡{summary['saving']}")
    window["balance"].update(f"Balance: ₡{summary['balance']}")


def save_data(manager):

    save_categories(manager, "data/categorias.json")
    save_movements(manager, "data/movimientos.json")


def open_movement_window(manager, movement_type, window):

    if not manager.categories_list:

        sg.popup(
            "No hay categorías disponibles.\n"
            "Debe agregar una categoría primero."
        )

        return


    category_names = get_category_names(manager)

    today = date.today().strftime("%d/%m/%Y")


    movement_layout=[
        [sg.Text(f"Agregar {movement_type}",text_color="white"),sg.Push(),sg.Button("Salir",key="close",button_color=("black","#E06A5E"))],
        [sg.Text("Titulo:",text_color="white"),sg.Input(key="title",background_color="LightBlue",text_color="black")],
        [sg.Text("Monto:",text_color="white"),sg.Input(key="amount",background_color="LightBlue",text_color="black")],
        [sg.Text("Categoría:",text_color="white"),sg.Combo(category_names,
            key="category",background_color="LightBlue",text_color="black")],
        [sg.Text("Fecha:",text_color="white"),sg.Input(today,key="date",background_color="LightBlue",text_color="black")],
        [sg.Button("Guardar",key="save",button_color=("black","LightGreen"))]
    ]


    movement_window = sg.Window("",movement_layout,no_titlebar=True)


    while True:

        event, values = movement_window.read()

        if event == "close":

            break

        if event == "save":

            try:

                amount = float(values["amount"])

            except ValueError:

                sg.popup("El monto debe ser un número válido.")
                continue

            try:

                if movement_type == "Gasto":

                    manager.add_expense(
                        values["title"],
                        amount,
                        values["category"],
                        values["date"],)

                    sg.popup("Gasto agregado correctamente!")


                elif movement_type == "Ingreso":

                    manager.add_income(
                        values["title"],
                        amount,
                        values["category"],
                        values["date"],)

                    sg.popup("Ingreso agregado correctamente!")


                elif movement_type == "Ahorro":

                    manager.add_saving(
                        values["title"],
                        amount,
                        values["category"],
                        values["date"],)

                    sg.popup("Ahorro agregado correctamente!")


                save_data(manager)

                update_movements_table(window, manager)
                update_summary(window, manager)

                break


            except ValueError as error:

                sg.popup(str(error))


    movement_window.close()


manager = FinanceManager()

load_categories(manager, "data/categorias.json")
load_movements(manager, "data/movimientos.json")


movements_data = []

for movement in manager.movements_list:

    movements_data.append([
        movement.date,
        movement.title,
        movement.amount,
        movement.category,
        movement.type_movement
    ])


category_names = get_category_names(manager)


sg.theme("DarkBlue")

layout=[
    [sg.Text("Gestor de Finanzas",text_color="white"),sg.Push(),sg.Button("Salir",key="close",button_color=("black","#E06A5E"))],

    [sg.Button("Agregar gasto",key="add_expense",button_color=("black","#E06A5E")),
        sg.Button("Agregar ingreso",key="add_income",button_color=("black","LightGreen")),
        sg.Button("Agregar ahorro",key="add_saving",button_color=("black","#71A5E3")),
        sg.Button("Agregar categoría",key="add_category",button_color=("black","#E3DA71")),
        sg.Button("Exportar a CSV",key="export_csv",button_color=("black","#C18BE8"))],

    [sg.Text("Fecha inicio:",text_color="white"),
        sg.Input(key="start_date",size=(12,1),background_color="LightBlue",text_color="black"),
        sg.Text("Fecha fin:",text_color="white"),
        sg.Input(key="end_date",size=(12,1),background_color="LightBlue",text_color="black"),
        sg.Button("Filtrar",key="filter",button_color=("black","#71A5E3")),
        sg.Button("Mostrar todos",key="show_all",button_color=("black","#B0B0B0"))],

    [sg.Text("Ingresos: ₡0",key="income",text_color="white")],
    [sg.Text("Gastos: ₡0",key="expenses",text_color="white")],
    [sg.Text("Ahorros: ₡0",key="saving",text_color="white")],
    [sg.Text("Balance: ₡0",key="balance",text_color="white")],

    [sg.Table(headings=["Fecha","Título","Monto","Categoría","Tipo"],values=movements_data,
            key="movements",expand_x=True,background_color="LightBlue",header_text_color="white",text_color="black")]
]


window = sg.Window("",layout,no_titlebar=True,finalize=True)


update_movements_table(window, manager)
update_summary(window, manager)


while True:

    event, values = window.read()

    if event == "close":

        save_data(manager)

        break


    if event == "add_expense":

        open_movement_window(
            manager,
            "Gasto",
            window
        )


    if event == "add_income":

        open_movement_window(
            manager,
            "Ingreso",
            window
        )


    if event == "add_saving":

        open_movement_window(
            manager,
            "Ahorro",
            window
        )


    if event == "filter":

        try:

            filtered_movements = manager.filter_movements(
                values["start_date"],
                values["end_date"]
            )

            update_movements_table(
                window,
                manager,
                filtered_movements
            )

        except ValueError as error:

            sg.popup(str(error))


    if event == "show_all":

        update_movements_table(
            window,
            manager
        )


    if event == "export_csv":

        export_movements_csv(
            manager,
            "movimientos.csv"
        )

        sg.popup(
            "Archivo movimientos.csv creado correctamente!"
        )


    if event == "add_category":

        category_layout=[
            [sg.Text("Agregar Categoria",text_color="white"),sg.Push(),sg.Button("Salir",key="close",button_color=("black","#E06A5E"))],
            [sg.Text("Nombre:",text_color="white"),sg.Input(key="name",background_color="LightBlue",text_color="black")],
            [sg.Text("Color:",text_color="white"),
                sg.Input("#FFFFFF",key="color",readonly=True,background_color="LightBlue",text_color="black",disabled_readonly_background_color="LightBlue",disabled_readonly_text_color="black"),
                sg.ColorChooserButton("Seleccionar color",target="color")],
            [sg.Button("Guardar",key="save_category",button_color=("black","LightGreen"))]

        ]


        category_window = sg.Window("",category_layout,no_titlebar=True)


        while True:

            event, values = category_window.read()

            if event == "close":

                break

            if event == "save_category":

                try:

                    selected_color = values["color"]

                    if not selected_color:

                        selected_color = "#FFFFFF"


                    manager.add_category(
                        values["name"],
                        selected_color
                    )


                    category_names = get_category_names(manager)

                    category_window["name"].update("")

                    save_data(manager)

                    sg.popup("Categoria agregada correctamente!")

                    break


                except ValueError as error:

                    sg.popup(str(error))

        category_window.close()


window.close()