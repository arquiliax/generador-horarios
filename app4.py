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

def choca_con_bloqueo_por_dia(materia, lm_ini, lm_fin, aj_ini, aj_fin):
    """Verifica si una materia invade las horas prohibidas dependiendo de sus días específicos."""
    ini_mat, fin_mat = parse_hora(materia['hora'])
    dias = materia['dias']
    
    # Si la materia es de Lunes y Miércoles (LM)
    if 'L' in dias or 'M' in dias:
        if lm_ini < lm_fin:  # Solo validar si se configuró un rango válido
            return ini_mat < lm_fin and lm_ini < fin_mat
            
    # Si la materia es de Martes y Jueves (AJ)
    if 'A' in dias or 'J' in dias:
        if aj_ini < aj_fin:  # Solo validar si se configuró un rango válido
            return ini_mat < aj_fin and aj_ini < fin_mat
            
    return False

def generar_horario_prioritario(lista_materias, profesores_preferidos, lm_ini, lm_fin, aj_ini, aj_fin, max_intentos=4000):
    materias_unicas = {}
    for m in lista_materias:
        clave = m['clave']
        if clave not in materias_unicas:
            materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    preferencias = [p.lower() for p in profesores_preferidos if p.strip()]

    # Filtrado inicial: Eliminar secciones que chocan con sus respectivos bloqueos de días
    materias_filtradas = {}
    for clave, opciones in materias_unicas.items():
        opciones_validas = [
            op for op in opciones 
            if not choca_con_bloqueo_por_dia(op, lm_ini, lm_fin, aj_ini, aj_fin)
        ]
        if opciones_validas:
            materias_filtradas[clave] = opciones_validas
        else:
            return None, False, f"Imposible armar horario: Las horas bloqueadas eliminan todas las opciones para la materia con clave {clave}."

    # Intentar combinación respetando restricciones combinadas
    for _ in range(max_intentos):
        calendario_propuesto = []
        materias_restantes = list(materias_filtradas.keys())
        conflicto = False

        # PASO 1: Colocar profesores prioritarios
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

        # PASO 2: Rellenar materias restantes al azar
        for clave in materias_restantes:
            opciones = materias_filtradas[clave]
            seleccion = random.choice(opciones)
            if any(hay_sobreposicion(seleccion, m_g) for m_g in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(seleccion)
            
        if not conflicto and len(calendario_propuesto) == len(materias_filtradas):
            return calendario_propuesto, True, ""

    # PLAN DE RESPALDO: Si no coinciden profesores por restricciones, asegurar al menos las horas bloqueadas
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

    return None, False, "No se encontró ninguna combinación válida que respete los bloqueos de horario solicitados."

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Generador de Horarios por Días", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🛠️ Filtros Inteligentes")

# SECCIÓN MODIFICADA: BLOQUEOS DIVIDIDOS POR GRUPOS DE DÍAS
st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo: Lunes y Miércoles")
lm_inicio = st.sidebar.number_input("Hora de Inicio LM (HHMM)", min_value=0, max_value=2400, value=0, step=100, help="Ej. 1100")
lm_fin = st.sidebar.number_input("Hora de Fin LM (HHMM)", min_value=0, max_value=2400, value=0, step=100, help="Ej. 1300")

st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo: Martes y Jueves")
aj_inicio = st.sidebar.number_input("Hora de Inicio MA (HHMM)", min_value=0, max_value=2400, value=0, step=100, help="Ej. 0700")
aj_fin = st.sidebar.number_input("Hora de Fin MA (HHMM)", min_value=0, max_value=2400, value=0, step=100, help="Ej. 0900")

# SECCIÓN: PROFESORES
st.sidebar.markdown("---")
st.sidebar.subheader("⭐ Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Profesor {i}", key=f"prof_{i}", placeholder="Ej. Ortega")
    if pref_name.strip():
        profesores_inputs.append(pref_name.strip())

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios con Bloqueo por Días")
st.subheader("Tercer Semestre")
st.write("Configura rangos de horas libres independientes para tus días de clase (Lunes/Miércoles y Martes/Jueves).")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    calendario, prioridad_cumplida, mensaje_error = generar_horario_prioritario(
        MATERIAS_TERCER_SEMESTRE, profesores_inputs, lm_inicio, lm_fin, aj_inicio, aj_fin
    )
    
    if calendario:
        # Informes informativos en pantalla
        if lm_inicio < lm_fin:
            st.info(f"📆 Espacio libre asegurado Lunes y Miércoles: {lm_inicio:04d} a {lm_fin:04d}")
        if aj_inicio < aj_fin:
            st.info(f"📆 Espacio libre asegurado Martes y Jueves: {aj_inicio:04d} a {aj_fin:04d}")
            
        if len(profesores_inputs) > 0:
            if prioridad_cumplida:
                st.balloons()
                st.success("🎯 ¡Completado! Se respetaron los bloqueos específicos por día y se incluyeron tus profesores prioritarios.")
            else:
                st.warning("⚠️ Se respetaron tus horas bloqueadas por día, pero tus profesores preferidos no pudieron incluirse por chocar con estas restricciones.")
        else:
            st.success("🎲 ¡Horario generado con éxito respetando tus especificaciones de tiempo por día!")

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
            td { white-space: pre-line !important; height: 95px !important; vertical-align: top !important; background-color: #F8F9FA; border: 1px solid #D1D5DB !important; padding: 8px !important; }
            </style>
            """, 
            unsafe_allow_html=True
        )
        st.table(df_horario)
        
        # Detalle inferior
        st.write("### 📝 Detalle del Horario Activo")
        df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
        df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
        st.dataframe(df_lista, use_container_width=True, hide_index=True)
    else:
        st.error(mensaje_error)
else:
    st.info("💡 Puedes configurar los bloqueos de forma independiente. Si dejas alguno en 0, no se aplicará restricción para esos días.")