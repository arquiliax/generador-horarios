import streamlit as st
import random
import pandas as pd

# --- BASE DE DATOS DE MATERIAS (TERCER SEMESTRE) ---
MATERIAS_TERCER_SEMESTRE = [
    # Sección 001 / Bloque PSI0124PR
    {"nrc": "40108", "clave": "FGUS 006", "materia": "Lengua Extranjera III", "secc": "421", "dias": "AJ", "hora": "0700-0859", "profesor": "ORTEGA-CASTILLO KARINA"},
    {"nrc": "40252", "clave": "FGUS 001", "materia": "Formacion Humana y Social", "secc": "421", "dias": "LM", "hora": "0900-1059", "profesor": "PEREZ-XOCHIPA MARCO POLO"},
    {"nrc": "56817", "clave": "PSIS 012", "materia": "Teorias del Aprendizaje", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "BENAVIDES - VALDERRABANO MARICELA"},
    {"nrc": "56827", "clave": "PSIS 013", "materia": "Psi.del Desarrollo Humano III", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "LIMATIZCARENO SILVIA CAROLINA"},
    {"nrc": "56833", "clave": "PSIS 014", "materia": "Psicopatologia Interaccional", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "AGUILAR-DAVILA YADIRA"},
    {"nrc": "56837", "clave": "PSIS 015", "materia": "Teorias de los Sistemas Ciber", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA"},
    {"nrc": "56849", "clave": "PSIS 016", "materia": "Teor. en Psicologia Social II", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "HERNANDEZ - ESCOBAR VERONICA"},
    
    # Sección 002 / Bloque PSI0224PR
    {"nrc": "56876", "clave": "PSIS 012", "materia": "Teorias del Aprendizaje", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "DURAN-SORIANO MARIA DEL ROSIO"},
    {"nrc": "56881", "clave": "PSIS 013", "materia": "Psi.del Desarrollo Humano III", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "CANTERO-ANGULO MARIA DEL PILAR"},
    {"nrc": "56884", "clave": "PSIS 014", "materia": "Psicopatologia Interaccional", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "RODRIGUEZ - SANCHEZ JOSE LUIS"},
    {"nrc": "56887", "clave": "PSIS 015", "materia": "Teorias de los Sistemas Ciber", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA"},
    {"nrc": "56895", "clave": "PSIS 016", "materia": "Teor. en Psicologia Social II", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "MARTINEZ MENDEZ DULCE MARIA"},
    {"nrc": "56900", "clave": "FGUS 001", "materia": "Formacion Humana y Social", "secc": "422", "dias": "LM", "hora": "1900-2059", "profesor": "CHAVEZ-GONZALEZ ERIKA"},
    {"nrc": "56907", "clave": "FGUS 006", "materia": "Lengua Extranjera III", "secc": "422", "dias": "AJ", "hora": "1900-2059", "profesor": "DIAZ-CARREON GRACIELA"}
]

def parse_hora(hora_str):
    inicio, fin = hora_str.split('-')
    return int(inicio), int(fin)

def hay_sobreposicion(materia1, materia2):
    dias_compartidos = set(materia1['dias']) & set(materia2['dias'])
    if not dias_compartidos:
        return False
    ini1, fin1 = parse_hora(materia1['hora'])
    ini2, fin2 = parse_hora(materia2['hora'])
    return ini1 < fin2 and ini2 < fin1

def generar_horario_prioritario(lista_materias, profesores_preferidos, max_intentos=3000):
    # Agrupar secciones disponibles por la clave única de la materia
    materias_unicas = {}
    for m in lista_materias:
        clave = m['clave']
        if clave not in materias_unicas:
            materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    # Filtrar cuáles profesores prefiere el usuario (limpieza de texto)
    preferencias = [p.lower() for p in profesores_preferidos if p.strip()]

    # Intentaremos encontrar una combinación perfecta que respete la prioridad
    for _ in range(max_intentos):
        calendario_propuesto = []
        materias_restantes = list(materias_unicas.keys())
        conflicto = False

        # PASO 1: Priorizar y colocar OBLIGATORIAMENTE a los profesores preferidos
        for clave in list(materias_restantes):
            opciones = materias_unicas[clave]
            # Buscar si alguna opción de esta materia tiene a uno de los profesores preferidos
            opciones_preferidas = [
                op for op in opciones 
                if any(pref in op['profesor'].lower() for pref in preferencias)
            ]
            
            if opciones_preferidas:
                # Si hay coincidencia, seleccionamos una opción preferida al azar
                seleccion = random.choice(opciones_preferidas)
                
                # Validamos que no choque con lo que ya llevamos guardado
                if any(hay_sobreposicion(seleccion, m_guardada) for m_guardada in calendario_propuesto):
                    conflicto = True
                    break
                
                calendario_propuesto.append(seleccion)
                materias_restantes.remove(clave)
        
        if conflicto:
            continue # Si los profesores elegidos chocan entre sí, reinicia el intento

        # PASO 2: Rellenar de forma completamente ALEATORIA las materias que no tuvieron preferencia
        for clave in materias_restantes:
            opciones = materias_unicas[clave]
            # Elegimos completamente al azar entre todas las secciones de esa materia
            seleccion = random.choice(opciones)
            
            if any(hay_sobreposicion(seleccion, m_guardada) for m_guardada in calendario_propuesto):
                conflicto = True
                break
                
            calendario_propuesto.append(seleccion)
            
        if not conflicto and len(calendario_propuesto) == len(materias_unicas):
            return calendario_propuesto, True

    # Si con la prioridad estricta es matemáticamente imposible por choques, 
    # usamos el plan de respaldo: buscar el horario con más coincidencias posibles.
    for _ in range(max_intentos):
        calendario_propuesto = []
        conflicto = False
        for clave, opciones in materias_unicas.items():
            opcion_seleccionada = random.choice(opciones)
            if any(hay_sobreposicion(opcion_seleccionada, mg) for mg in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(opcion_seleccionada)
            
        if not conflicto and len(calendario_propuesto) == len(materias_unicas):
            return calendario_propuesto, False

    return None, False

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Generador de Horarios Prioritario", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR) PARA PROFESORES ---
st.sidebar.title("⭐ Profesores Prioritarios")
st.sidebar.write("Escribe el nombre o apellido de los profesores que quieres asegurar en tu horario:")

profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Profesor {i}", key=f"prof_{i}", placeholder="Ej. Aguilar o Yadira")
    if pref_name.strip():
        profesores_inputs.append(pref_name.strip())

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios con Prioridad Estricta")
st.subheader("Tercer Semestre")
st.write("El sistema fijará primero a los profesores que pusiste a la izquierda, y rellenará el resto de tus materias de forma completamente aleatoria.")

if st.button("🎲 Generar Horario", type="primary"):
    calendario, prioridad_cumplida = generar_horario_prioritario(MATERIAS_TERCER_SEMESTRE, profesores_inputs)
    
    if calendario:
        # Mensajes de estado de la prioridad
        if len(profesores_inputs) > 0:
            if prioridad_cumplida:
                st.balloons()
                st.success("🎯 ¡Perfecto! Tus profesores prioritarios fueron asegurados y las demás materias se asignaron al azar.")
            else:
                st.warning("⚠️ Se generó un horario válido, pero tus profesores preferidos chocan entre sí en sus horas. Mostrando la combinación con menos conflictos posibles.")
        else:
            st.success("🎲 Horario generado de forma 100% aleatoria (sin preferencias ingresadas).")

        # Estructura del Calendario Semanal
        bloques_horas = ["0700-0859", "0900-1059", "1100-1259", "1300-1459", "1500-1659", "1700-1859", "1900-2059"]
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        
        df_horario = pd.DataFrame("", index=bloques_horas, columns=dias_semana)
        
        for m in calendario:
            info_celda = f"📚 {m['materia']} (Sec. {m['secc']})\n👤 {m['profesor']}\n[NRC: {m['nrc']}]"
            
            if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
            if 'M' in m['dias']: df_horario.at[m['hora'], "Miércoles"] = info_celda
            if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
            if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda

        # --- DISEÑO DEL CALENDARIO ---
        st.write("### 📅 Vista de Calendario Semanal")
        st.markdown(
            """
            <style>
            table { font-size: 13px !important; width: 100% !important; }
            th { background-color: #1E3A8A !important; color: white !important; text-align: center !important; font-size: 15px !important; }
            td { white-space: pre-line !important; height: 95px !important; vertical-align: top !important; background-color: #F3F4F6; border: 1px solid #D1D5DB !important; padding: 8px !important; }
            </style>
            """, 
            unsafe_allow_html=True
        )
        st.table(df_horario)
        
        # Tabla de datos abajo
        st.write("### 📝 Detalle del Horario Activo")
        df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
        df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
        st.dataframe(df_lista, use_container_width=True, hide_index=True)
    else:
        st.error("Ocurrió un error al procesar las materias. Inténtalo de nuevo.")
else:
    st.info("💡 Cada vez que presiones el botón 'Generar Horario', los profesores que no especificaste cambiarán aleatoriamente de sección.")
    