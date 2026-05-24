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

def choca_con_bloqueo(materia, hora_bloqueo_inicio, hora_bloqueo_fin):
    """Verifica si el horario de una materia invade el rango de horas prohibidas."""
    ini_mat, fin_mat = parse_hora(materia['hora'])
    # Hay choque si la clase empieza antes del fin del bloqueo y termina después del inicio del bloqueo
    return ini_mat < hora_bloqueo_fin and hora_bloqueo_inicio < fin_mat

def generar_horario_prioritario(lista_materias, profesores_preferidos, hora_bloq_ini, hora_bloq_fin, max_intentos=4000):
    materias_unicas = {}
    for m in lista_materias:
        clave = m['clave']
        if clave not in materias_unicas:
            materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    preferencias = [p.lower() for p in profesores_preferidos if p.strip()]

    # Filtrado inicial: Remover secciones que de por sí chocan con las horas prohibidas
    materias_filtradas = {}
    for clave, opciones in materias_unicas.items():
        opciones_validas = [op for op in opciones if not choca_con_bloqueo(op, hora_bloq_ini, hora_bloq_fin)]
        if opciones_validas:
            materias_filtradas[clave] = opciones_validas
        else:
            # Si una materia obligatoria se queda con 0 opciones por culpa del bloqueo, es imposible armar el horario
            return None, False, f"Imposible armar horario: El bloqueo de horas elimina todas las opciones para la materia con clave {clave}."

    # Intentar combinación respetando profesores preferidos + horas prohibidas
    for _ in range(max_intentos):
        calendario_propuesto = []
        materias_restantes = list(materias_filtradas.keys())
        conflicto = False

        # PASO 1: Colocar profesores preferidos que pasaron el filtro de bloqueo
        for clave in list(materias_restantes):
            opciones = materias_filtradas[clave]
            opciones_preferidas = [op for op in opciones if any(pref in op['profesor'].lower() for pref in preferencias)]
            
            if opciones_preferidas:
                seleccion = random.choice(opciones_preferidas)
                if any(hay_sobreposicion(seleccion, m_g) for m_g in calendario_propuesto):
                    conflicto = True; break
                calendario_propuesto.append(seleccion)
                materias_restantes.remove(clave)
        
        if conflicto: continue

        # PASO 2: Rellenar el resto de materias al azar
        for clave in materias_restantes:
            opciones = materias_filtradas[clave]
            seleccion = random.choice(opciones)
            if any(hay_sobreposicion(seleccion, m_g) for m_g in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(seleccion)
            
        if not conflicto and len(calendario_propuesto) == len(materias_filtradas):
            return calendario_propuesto, True, ""

    # PLAN DE RESPALDO: Si no coinciden tus profesores prioritarios por los choques, 
    # busca al menos un horario que respete de forma estricta las horas prohibidas.
    for _ in range(max_intentos):
        calendario_propuesto = []
        conflicto = False
        for clave, opciones in materias_filtradas.items():
            opcion_seleccionada = random.choice(opciones)
            if any(hay_sobreposicion(opcion_seleccionada, mg) for mg in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(opcion_seleccionada)
            
        if not conflicto and len(calendario_propuesto) == len(materias_filtradas):
            return calendario_propuesto, False, ""

    return None, False, "No se encontró ninguna combinación matemática válida que respete tus horas prohibidas."

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Generador de Horarios Inteligente", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🛠️ Filtros y Ajustes")

# NUEVA SECCIÓN: BLOQUEO DE HORAS PROHIBIDAS
st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo de Horas")
st.sidebar.write("Especifica un rango en formato de 24 horas (Ej: 1300 a 1500) en el que **no puedas tomar clases**:")

# Controladores numéricos para evitar que el usuario meta texto inválido
hora_inicio_input = st.sidebar.number_input("Hora de Inicio (HHMM)", min_value=0, max_value=2400, value=0, step=100, help="Ejemplo: 0700 para 7:00 AM o 1400 para 2:00 PM")
hora_fin_input = st.sidebar.number_input("Hora de Fin (HHMM)", min_value=0, max_value=2400, value=0, step=100, help="Ejemplo: 0900 para 9:00 AM o 1600 para 4:00 PM")

# SECCIÓN: PROFESORES
st.sidebar.markdown("---")
st.sidebar.subheader("⭐ Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Profesor {i}", key=f"prof_{i}", placeholder="Ej. Aguilar")
    if pref_name.strip():
        profesores_inputs.append(pref_name.strip())

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios con Restricción de Tiempo")
st.subheader("Tercer Semestre")
st.write("El sistema descartará las secciones de clases que se crucen con tus horas bloqueadas y priorizará a tus docentes.")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    # Ejecutar el algoritmo con todos los parámetros
    calendario, prioridad_cumplida, mensaje_error = generar_horario_prioritario(
        MATERIAS_TERCER_SEMESTRE, profesores_inputs, hora_inicio_input, hora_fin_input
    )
    
    if calendario:
        # Informar al usuario sobre las reglas aplicadas
        if hora_inicio_input < hora_fin_input:
            st.info(f"🚫 Restricción aplicada: Se dejaron libres las horas comprendidas entre las {hora_inicio_input:04d} y las {hora_fin_input:04d} horas.")
            
        if len(profesores_inputs) > 0:
            if prioridad_cumplida:
                st.balloons()
                st.success("🎯 ¡Excelente! Se protegió tu rango de horas libre, se asignaron tus profesores prioritarios y el resto se rellenó al azar.")
            else:
                st.warning("⚠️ Horario generado respetando tus horas prohibidas, pero se tuvieron que omitir algunos profesores elegidos porque sus clases chocaban horariamente.")
        else:
            st.success("🎲 ¡Horario generado exitosamente con el espacio de tiempo libre que solicitaste!")

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
        
        # Tabla detallada abajo
        st.write("### 📝 Detalle del Horario Activo")
        df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
        df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
        st.dataframe(df_lista, use_container_width=True, hide_index=True)
    else:
        # Mostrar el error detallado si es imposible cumplir con la restricción
        st.error(mensaje_error)
else:
    st.info("💡 Modifica las horas prohibidas y tus preferencias en el panel izquierdo y haz clic en el botón para procesar.")