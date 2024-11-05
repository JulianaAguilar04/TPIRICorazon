import numpy as np
import matplotlib.pyplot as plt



# función para calcular frecuencia y periodo
def frec_periodo(frecuencia):
    frec = frecuencia / 60 
    per = 1 / frec
    return frec, per

# simulación de estados
normal = {120, 80, 100, 70}

# función para calcular la presión sistólica en función del tiempo
def presion_sistolica(p_sistolica=120, frecuencia=1, tiempo=None):
    if tiempo is None:
        tiempo = np.linspace(0, 10, 1000)  # Genera 1000 puntos en el tiempo de 0 a 10 segundos
    frec_ang = 2 * np.pi * frecuencia
    presion_sis = p_sistolica * np.maximum(0, np.sin(frec_ang * tiempo))
    return presion_sis
def presion_diastolica(p_diastolica, frecuencia, tiempo=None):
    if tiempo is None:
        tiempo = np.linspace(0, 10, 1000)  # Genera 1000 puntos en el tiempo de 0 a 10 segundos
    frec_ang = 2 * np.pi * frecuencia
    presion_dias = p_diastolica * np.maximum(0, np.sin(frec_ang * tiempo))
    return presion_dias

# función para graficar 
def graf_p(p_sistolica,p_diastolica,frecuencia):
    tiempo = np.linspace(0, 5, 1000)  # Genera 1000 puntos en el tiempo de 0 a 5 segundos
    presis = presion_sistolica(p_sistolica, frecuencia, tiempo)
    presdias=presion_diastolica(p_diastolica,frecuencia,tiempo)
    prestotal=presis+presdias
    plt.figure(figsize=(10, 5))
    plt.plot(tiempo, prestotal, label="Presión")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Presión")
    plt.title("Variación de la presión en el tiempo")
    plt.ylim(0, p_sistolica + 20)
    plt.legend()
    plt.grid(True)
    plt.show()

graf_p(list(normal)[0],list(normal)[1],list(normal)[3]/60)
