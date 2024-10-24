import datetime

frases_filosoficas = [
    {
        "fecha": datetime.date(2023, 6, 18),
        "frase": "Conócete a ti mismo.",
        "explicacion": "Esta famosa frase del filósofo griego Sócrates destaca la importancia del autoconocimiento. Al explorar nuestras creencias, emociones y motivaciones, podemos comprender mejor quiénes somos realmente. El conocimiento de uno mismo es el primer paso para el crecimiento personal y la búsqueda de la sabiduría."
    },
    {
        "fecha": datetime.date(2023, 6, 19),
        "frase": "La vida no examinada no vale la pena ser vivida.",
        "explicacion": "Esta famosa frase de Sócrates destaca la importancia de la reflexión y el autoconocimiento. Al examinar nuestras creencias, valores y acciones, nos embarcamos en un viaje hacia una vida más auténtica y significativa. Sólo al cuestionar y explorar continuamente nuestras vidas podemos descubrir nuestro propósito y encontrar la verdadera felicidad."
    },
    {
        "fecha": datetime.date(2023, 6, 20),
        "frase": "Solo sé que no sé nada.",
        "explicacion": "Sócrates, conocido por su humildad intelectual, pronunció esta frase para enfatizar la importancia de reconocer nuestras limitaciones y estar abiertos al aprendizaje constante. Al admitir que no sabemos todo, nos volvemos más humildes y dispuestos a escuchar a los demás, a considerar diferentes perspectivas y a buscar la verdad con una mente abierta."
    },
    {
        "fecha": datetime.date(2023, 6, 21),
        "frase": "No hay viento favorable para el que no sabe a qué puerto se dirige.",
        "explicacion": "Esta cita de Séneca nos invita a reflexionar sobre la importancia de tener metas y objetivos claros en la vida. Si no tenemos una dirección clara hacia la cual avanzar, nos volvemos presa de la indecisión y de las circunstancias externas. Al definir nuestros propósitos, podemos aprovechar las oportunidades y enfrentar los desafíos con determinación y enfoque."
    },
    {
        "fecha": datetime.date(2023, 6, 22),
        "frase": "Pienso, luego existo.",
        "explicacion": "Esta famosa frase de René Descartes es un punto de partida para la filosofía moderna. Al afirmar que nuestra capacidad de pensar prueba nuestra existencia, Descartes busca establecer la certeza y la base sólida del conocimiento. Esta afirmación nos invita a reflexionar sobre la importancia de nuestra conciencia y pensamiento como elementos fundamentales de nuestra existencia y identidad."
    },
    {
        "fecha": datetime.date(2023, 6, 23),
        "frase": "El hombre es un animal político.",
        "explicacion": "Aristóteles sostiene que los seres humanos somos animales sociales y políticos por naturaleza. La vida en sociedad, el intercambio de ideas y la participación en la toma de decisiones son fundamentales para nuestro desarrollo y bienestar. Esta frase nos recuerda la importancia de la comunidad y la política en la vida humana."
    },
    {
        "fecha": datetime.date(2023, 6, 24),
        "frase": "El objetivo último de la vida humana es la felicidad.",
        "explicacion": "Aristóteles consideraba que el objetivo último de la vida humana es alcanzar la felicidad. Sin embargo, la felicidad para Aristóteles no se basa en el placer momentáneo, sino en el florecimiento de nuestras capacidades y virtudes como seres humanos. Esta frase nos invita a reflexionar sobre cómo podemos desarrollar nuestras habilidades, encontrar significado y buscar la realización personal en busca de una vida plena y feliz."
    },
    {
        "fecha": datetime.date(2023, 6, 25),
        "frase": "La razón es el órgano del juicio.",
        "explicacion": "Esta afirmación de Immanuel Kant destaca la importancia de la razón en nuestra capacidad para tomar decisiones y evaluar la realidad. Según Kant, la razón nos permite comprender y juzgar el mundo de manera objetiva y racional, superando los prejuicios y la influencia de nuestras emociones. Nos invita a confiar en el poder de la razón como guía para nuestras acciones y decisiones éticas."
    }
]

def obtener_frase_filosofica():
    fecha_actual = datetime.date.today()
    for frase in frases_filosoficas:
        if frase["fecha"] == fecha_actual:
            return frase

def mostrar_frase_diaria():
    frase = obtener_frase_filosofica()
    fecha_actual = datetime.date.today().strftime("%d-%m-%Y")
    print("Frase filosófica del día (", fecha_actual, "):")
    print(frase["frase"])
    print("Explicación:")
    print(frase["explicacion"])

print("¡Bienvenido al programa de frases filosóficas diarias!")
print("A continuación, se mostrará una frase de filosofía diferente cada día durante una semana.")
print()

for _ in range(7):
    mostrar_frase_diaria()
    print()
    # Esperar un día antes de mostrar la siguiente frase
    datetime.datetime.now() + datetime.timedelta(days=1)
