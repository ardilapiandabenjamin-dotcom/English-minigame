import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import random 


# ==================================
# CONFIGURACIONES
# ==================================

duration = 10
sample_rate = 44100

vidas = 3
reputacion = 0
juego_activo = True


# ==================================
# PALABRAS POR CATEGORÍA
# ==================================

palabras_categoria = {

    "1": { # Videojuegos

        "nivel1": [
            ("juego", "game"),
            ("jugador", "player"),
            ("enemigo", "enemy")
        ],

        "nivel2": [
            ("espada", "sword"),
            ("poder", "power"),
            ("batalla", "battle")
        ]
    },


    "2": { # Comida

        "nivel1": [
            ("pan", "bread"),
            ("queso", "cheese"),
            ("manzana", "apple")
        ],

        "nivel2": [
            ("hamburguesa", "hamburger"),
            ("ensalada", "salad"),
            ("postre", "dessert")
        ]
    },


    "3": { # Animales

        "nivel1": [
            ("perro", "dog"),
            ("gato", "cat"),
            ("pez", "fish")
        ],

        "nivel2": [
            ("tigre", "tiger"),
            ("elefante", "elephant"),
            ("delfín", "dolphin")
        ]
    }
}



# ==================================
# MENÚ PRINCIPAL
# ==================================

print("==================================")
print("🎤 ENGLISH SURVIVOR 🌎")
print("==================================")


print()
print("🚨 ¡Alerta!")
print("Un grupo de aliens llegó a la Tierra.")
print("No entienden inglés y necesitan tu ayuda.")
print()


print("1️⃣ 🎮 Videojuegos")
print("2️⃣ 🍔 Comida")
print("3️⃣ 🐶 Animales")


opcion = input("👉 Elige una categoría: ")



# ==================================
# COMPROBAR CATEGORÍA
# ==================================

if opcion == "1":

    print("🎮 Categoría: Videojuegos")

elif opcion == "2":

    print("🍔 Categoría: Comida")

elif opcion == "3":

    print("🐶 Categoría: Animales")

else:

    print("❌ Categoría no válida")
    exit()



# ==================================
# SISTEMA DE NIVELES
# ==================================

nivel = "nivel1"


while juego_activo:


    palabra = random.choice(
        palabras_categoria[opcion][nivel]
    )


    print()
    print("----------------------------------")
    print("👽 Nueva misión")
    print("🔥 Nivel actual:", nivel)
    print("🌎 Traduce esta palabra:")
    print("👉", palabra[0])
    print()
    print("⭐ Reputación:", reputacion, "/100")
    print("❤️ Vidas:", vidas)
    print("----------------------------------")


    # ==================================
    # GRABAR VOZ
    # ==================================

    print("🎙️ Hablar ahora...")


    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )


    sd.wait()



    wav.write(
        "output.wav",
        sample_rate,
        recording
    )



    # ==================================
    # RECONOCER VOZ
    # ==================================

    recognizer = sr.Recognizer()


    with sr.AudioFile("output.wav") as source:

        audio = recognizer.record(source)



    # ==================================
    # REVISAR RESPUESTA
    # ==================================

    try:


        respuesta = recognizer.recognize_google(
            audio,
            language="en"
        )


        respuesta = respuesta.lower()


        print("Dijiste:", respuesta)



        if respuesta == palabra[1]:


            print("✅ Correcto")
            print("👽 Los aliens aprendieron una palabra")


            reputacion += 10


            print("⭐ +10 reputación")


            # SUBIDA DE NIVEL

            if reputacion >= 50 and nivel == "nivel1":

                nivel = "nivel2"

                print()
                print("🚀 SUBISTE DE NIVEL")
                print("🔥 Ahora estás en NIVEL 2")
                print("👽 Los aliens necesitan palabras más difíciles")



            if reputacion >= 100:

                print()
                print("🏆 GANASTE")
                print("🌎 La Tierra logró comunicarse con los aliens.")

                break



        else:


            print("❌ Incorrecto")
            print("La respuesta correcta era:", palabra[1])


            vidas -= 1


            print("❤️ Perdiste una vida")
            print("❤️ Vidas restantes:", vidas)



            if vidas <= 0:

                print()
                print("💀 GAME OVER")
                print("👽 Los aliens perdieron la confianza.")

                break



    except sr.UnknownValueError:


        print("❌ No pude entender la respuesta.")



    except sr.RequestError as error:


        print("❌ Error del servicio:")
        print(error)import sounddevice as sd
