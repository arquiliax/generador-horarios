import streamlit as st
import random
import pandas as pd

# --- BASE DE DATOS GLOBAL MULTISEMESTRE Y OPTATIVAS ---
CATALOGO_MATERIAS = [
    # --- PRIMER SEMESTRE (Ejemplo Base) ---
    {"nrc": "10001", "clave": "PSIS 001", "materia": "Introducción a la Psicología", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "GARCIA LOPEZ ANAMARIA", "semestre": "Primer Semestre"},
    {"nrc": "10002", "clave": "FGUS 002", "materia": "Pensamiento Crítico", "secc": "421", "dias": "AJ", "hora": "0900-1059", "profesor": "ZAVALA RUIZ HUGO", "semestre": "Primer Semestre"},
    
    # --- TERCER SEMESTRE (Tu Tronco Común Actual) ---
    {"nrc": "40108", "clave": "FGUS 006", "materia": "Lengua Extranjera III", "secc": "421", "dias": "AJ", "hora": "0700-0859", "profesor": "ORTEGA-CASTILLO KARINA", "semestre": "Tercer Semestre"},
    {"nrc": "40252", "clave": "FGUS 001", "materia": "Formacion Humana y Social", "secc": "421", "dias": "LM", "hora": "0900-1059", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "Tercer Semestre"},
    {"nrc": "56817", "clave": "PSIS 012", "materia": "Teorias del Aprendizaje", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "BENAVIDES - VALDERRABANO MARICELA", "semestre": "Tercer Semestre"},
    {"nrc": "56827", "clave": "PSIS 013", "materia": "Psi.del Desarrollo Humano III", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "Tercer Semestre"},
    {"nrc": "56833", "clave": "PSIS 014", "materia": "Psicopatologia Interaccional", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "Tercer Semestre"},
    {"nrc": "56837", "clave": "PSIS 015", "materia": "Teorias de los Sistemas Ciber", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "Tercer Semestre"},
    {"nrc": "56849", "clave": "PSIS 016", "materia": "Teor. en Psicologia Social II", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "HERNANDEZ - ESCOBAR VERONICA", "semestre": "Tercer Semestre"},
    
    {"nrc": "56876", "clave": "PSIS 012", "materia": "Teorias del Aprendizaje", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "Tercer Semestre"},
    {"nrc": "56881", "clave": "PSIS 013", "materia": "Psi.del Desarrollo Humano III", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "CANTERO-ANGULO MARIA DEL PILAR", "semestre": "Tercer Semestre"},
    {"nrc": "56884", "clave": "PSIS 014", "materia": "Psicopatologia Interaccional", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "RODRIGUEZ - SANCHEZ JOSE LUIS", "semestre": "Tercer Semestre"},
    {"nrc": "56887", "clave": "PSIS 015", "materia": "Teorias de los Sistemas Ciber", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "Tercer Semestre"},
    {"nrc": "56895", "clave": "PSIS 016", "materia": "Teor. en Psicologia Social II", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "MARTINEZ MENDEZ DULCE MARIA", "semestre": "Tercer Semestre"},
    {"nrc": "56900", "clave": "FGUS 001", "materia": "Formacion Humana y Social", "secc": "422", "dias": "LM", "hora": "1900-2059", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "Tercer Semestre"},
    {"nrc": "56907", "clave": "FGUS 006", "materia": "Lengua Extranjera III", "secc": "422", "dias": "AJ", "hora": "1900-2059", "profesor": "DIAZ-CARREON GRACIELA", "semestre": "Tercer Semestre"},

    # --- SECCIÓN: MATERIAS OPTATIVAS POR ÁREA ---
    # Área Clínica
    {"nrc": "90101", "clave": "OPT CLIN1", "materia": "Entrevista Clínica", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "BECK AARON", "semestre": "Optativa - Clínica"},
    {"nrc": "90102", "clave": "OPT CLIN2", "materia": "Evaluación Psicométrica", "secc": "001", "dias": "AJ", "hora": "1500-1659", "profesor": "SORREL GONZALO", "semestre": "Optativa - Clínica"},
    
    # Área Educativa
    {"nrc": "90201", "clave": "OPT EDU1", "materia": "Psicopedagogía de la Inclusión", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "ROGERS CARL", "semestre": "Optativa - Educativa"},
    {"nrc": "90202", "clave": "OPT EDU2", "materia": "Diseño de Programas Educativos", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "PIAGET JEAN", "semestre": "Optativa - Educativa"},
    
    # Área Organizacional
    {"nrc": "90301", "clave": "OPT ORG1", "materia": "Gestión del Talento y Competencias", "secc": "001", "dias": "LM", "hora": "1500-1659", "profesor": "CHIAVENATO IDALBERTO", "semestre": "Optativa - Organizacional"},
    {"nrc": "90302", "clave": "OPT ORG2", "materia": "Estrategias de Outplacement", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "MARISTANY LUIS", "semestre": "Optativa - Organizacional"},
    
    # Área Social
    {"nrc": "90401", "clave": "OPT SOC1", "materia": "Psicología Comunitaria y de Campo", "secc": "001", "dias": "AJ", "hora": "1700-1859", "profesor": "MONTERO MARITZA", "semestre": "Optativa - Social"},
    {"nrc": "90402", "clave": "OPT SOC2", "materia": "Intervención en Procesos Colectivos", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "MOSCOVICI SERGE", "semestre": "Optativa - Social"}
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
    ini_mat, fin_mat = parse_hora(materia['hora'])
    dias = materia['dias']
    if 'L' in dias or 'M' in dias:
        if lm_ini < lm_fin: return ini_mat < lm_fin and lm_ini < fin_mat
    if 'A' in dias or 'J' in dias:
        if aj_ini < aj_fin: return ini_mat < aj_fin and aj_ini < fin_mat
    return False

def coincide_profesor(nombre_ingresado, nombre_catalogo):
    tokens = nombre_ingresado.lower().replace('-', ' ').split()
    catalogo_limpio = nombre_catalogo.lower().replace('-', ' ')
    if not tokens: return False
    return all(t in catalogo_limpio for t in tokens)

def generar_horario_estricto(lista_materias, profesores_prioritarios, lm_ini, lm_fin, aj_ini, aj_fin, max_intentos=5000):
    materias_unicas = {}
    nombres_materias = {}
    
    for m in lista_materias:
        clave = m['clave']
        nombres_materias[clave] = m['materia']
        if clave not in materias_unicas:
            materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    prioridades = [p.strip() for p in profesores_prioritarios if p.strip()]
    materias_omitidas = []
    omitidas_prof_unico = []
    materias_filtradas = {}
    
    for clave, opciones in materias_unicas.items():
        opciones_con_profesor = [op for op in opciones if any(coincide_profesor(p_p, op['profesor']) for p_p in prioridades)]
        usuario_pidio_profesor = len(opciones_con_profesor) > 0
        opciones_a_evaluar = opciones_con_profesor if usuario_pidio_profesor else opciones
        opciones_validas = [op for op in opciones_a_evaluar if not choca_con_bloqueo_por_dia(op, lm_ini, lm_fin, aj_ini, aj_fin)]
        
        if opciones_validas:
            materias_filtradas[clave] = opciones_validas
        else:
            es_unico_profesor_en_toda_la_materia = len(set(op['profesor'] for op in opciones)) == 1
            if usuario_pidio_profesor or es_unico_profesor_en_toda_la_materia:
                omitidas_prof_unico.append(nombres_materias[clave])
            else:
                materias_omitidas.append(nombres_materias[clave])

    if not materias_filtradas:
        return None, False, materias_omitidas, omitidas_prof_unico, "El bloqueo de horas eliminó todas las opciones de materias válidas."

    for _ in range(max_intentos):
        calendario_propuesto = []
        conflicto = False
        
        for clave, opciones in materias_filtradas.items():
            seleccion = random.choice(opciones)
            if any(hay_sobreposicion(seleccion, m_g) for m_g in calendario_propuesto):
                conflicto = True
                break
            calendario_propuesto.append(seleccion)
            
        if not conflicto and len(calendario_propuesto) == len(materias_filtradas):
            prioridad_completa = True
            for p_p in prioridades:
                existe_en_filtro = any(coincide_profesor(p_p, op['profesor']) for opciones in materias_filtradas.values() for op in opciones)
                if existe_en_filtro and not any(coincide_profesor(p_p, m['profesor']) for m in calendario_propuesto):
                    prioridad_completa = False
                    break
            return calendario_propuesto, prioridad_completa, materias_omitidas, omitidas_prof_unico, ""

    return None, False, materias_omitidas, omitidas_prof_unico, "No se encontró una combinación válida sin traslapes con las condiciones dadas."

# --- CONFIGURACIÓN DE STREAMLIT ---
st.set_page_config(page_title="Generador de Horarios General", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR): CONFIGURACIÓN GENERAL ---
st.sidebar.title("🛠️ Configuración del Horario")

# 1. SELECTOR DE SEMESTRE GENERAL
semestre_seleccionado = st.sidebar.selectbox(
    "📆 Selecciona tu Semestre:",
    ["Primer Semestre", "Segundo Semestre", "Tercer Semestre", "Cuarto Semestre", "Quinto Semestre", "Sexto Semestre", "Séptimo Semestre", "Octavo Semestre"],
    index=2 # Tercer semestre por defecto
)

# BLOQUEOS DE HORAS
st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo: Lunes y Miércoles")
lm_inicio = st.sidebar.number_input("Hora de Inicio LM (HHMM)", min_value=0, max_value=2400, value=0, step=100)
lm_fin = st.sidebar.number_input("Hora de Fin LM (HHMM)", min_value=0, max_value=2400, value=0, step=100)

st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo: Martes y Jueves")
aj_inicio = st.sidebar.number_input("Hora de Inicio MA (HHMM)", min_value=0, max_value=2400, value=0, step=100)
aj_fin = st.sidebar.number_input("Hora de Fin MA (HHMM)", min_value=0, max_value=2400, value=0, step=100)

# PROFESORES PRIORITARIOS
st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 6):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Nombre Completo o Apellido")
    if pref_name.strip():
        profesores_inputs.append(pref_name.strip())

# --- NUEVO PANEL DE MATERIAS OPTATIVAS ---
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Módulo de Materias Optativas")
st.sidebar.write("Activa las materias que deseas anexar a tu mapa curricular:")

optativas_seleccionadas = []

# Filtrar las optativas disponibles por cada sección técnica del catálogo
opt_clinica = [m for m in CATALOGO_MATERIAS if m['semestre'] == "Optativa - Clínica"]
opt_educativa = [m for m in CATALOGO_MATERIAS if m['semestre'] == "Optativa - Educativa"]
opt_organizacional = [m for m in CATALOGO_MATERIAS if m['semestre'] == "Optativa - Organizacional"]
opt_social = [m for m in CATALOGO_MATERIAS if m['semestre'] == "Optativa - Social"]

with st.sidebar.expander("🧠 Área Clínica"):
    for o in opt_clinica:
        if st.checkbox(f"{o['materia']}", key=f"check_{o['nrc']}"):
            optativas_seleccionadas.append(o)

with st.sidebar.expander("🏫 Área Educativa"):
    for o in opt_educativa:
        if st.checkbox(f"{o['materia']}", key=f"check_{o['nrc']}"):
            optativas_seleccionadas.append(o)

with st.sidebar.expander("💼 Área Organizacional"):
    for o in opt_organizacional:
        if st.checkbox(f"{o['materia']}", key=f"check_{o['nrc']}"):
            optativas_seleccionadas.append(o)

with st.sidebar.expander("🌍 Área Social"):
    for o in opt_social:
        if st.checkbox(f"{o['materia']}", key=f"check_{o['nrc']}"):
            optativas_seleccionadas.append(o)


# --- CONSTRUCCIÓN DEL BANCO DE MATERIAS DE TRABAJO ---
# 1. Filtrar las del Tronco Común del Semestre elegido
materias_tronco_comun = [m for m in CATALOGO_MATERIAS if m['semestre'] == semestre_seleccionado]

# 2. Unir el tronco común con las optativas marcadas por el usuario
banco_materias_final = materias_tronco_comun + optativas_seleccionadas


# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Universitario Multisemestre")
st.subheader(f"Esquema Activo: {semestre_seleccionado}")
if optativas_seleccionadas:
    st.caption(f" Optativas añadidas al cálculo: {', '.join([m['materia'] for m in optativas_seleccionadas])}")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    if not banco_materias_final:
        st.error("No hay materias cargadas en este semestre ni optativas seleccionadas.")
    else:
        calendario, prioridad_cumplida, omitidas, omitidas_prof_unico, mensaje_error = generar_horario_estricto(
            banco_materias_final, profesores_inputs, lm_inicio, lm_fin, aj_inicio, aj_fin
        )
        
        if calendario:
            # Alertas de Omisión por Bloqueo Temporal
            if omitidas:
                for mat_om in omitidas:
                    st.toast(f"⚠️ Materia Omitida: {mat_om}", icon="🚫")
                st.warning(f"⚠️ **Atención:** Para cumplir tus restricciones de tiempo, se omitieron: {', '.join(omitidas)}.")
                
            # Alerta Especial de Profesor Prioritario/Único Inaccesible
            if omitidas_prof_unico:
                for mat_prof in omitidas_prof_unico:
                    st.toast(f"🚨 Omitida por Docente: {mat_prof}", icon="👤")
                st.error(f"👤 **Materia Omitida:** La asignatura **{', '.join(omitidas_prof_unico)}** se descartó porque el docente prioritario (o único disponible) choca de forma directa con tus horas bloqueadas.")

            # Banner del Estado del Filtro de Profesores
            if len(profesores_inputs) > 0:
                if prioridad_cumplida:
                    st.balloons()
                    st.info("💎 **Filtro Aplicado Correctamente:** Se fijaron exitosamente tus profesores prioritarios en el 100% de las opciones asignadas.")
                else:
                    st.warning("⚠️ **Filtro No Aplicado Completamente:** Uno o más profesores prioritarios no se pudieron implementar debido a colisiones con tus horarios bloqueados.")
            else:
                st.success("🎯 ¡Horario base estructurado correctamente!")

            # Armar Matriz Horaria
            bloques_horas = ["0700-0859", "0900-1059", "1100-1259", "1300-1459", "1500-1659", "1700-1859", "1900-2059"]
            dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
            df_horario = pd.DataFrame("", index=bloques_horas, columns=dias_semana)
            
            for m in calendario:
                info_celda = f"📚 {m['materia']} (Sec. {m['secc']})\n👤 {m['profesor']}\n[NRC: {m['nrc']}]"
                if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
                if 'M' in m['dias']: df_horario.at[m['hora'], "Miércoles"] = info_celda
                if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda

            # --- RENDERIZADO DE TABLAS ---
            st.write("### 📅 Vista de Calendario Semanal")
            st.markdown(
                """
                <style>
                table { font-size: 13px !important; width: 100% !important; }
                th { background-color: #1E3A8A !important; color: white !important; text-align: center !important; }
                td { white-space: pre-line !important; height: 95px !important; vertical-align: top !important; background-color: #F8F9FA; border: 1px solid #D1D5DB !important; padding: 8px !important; }
                </style>
                """, 
                unsafe_allow_html=True
            )
            st.table(df_horario)
            
            st.write("### 📝 Detalle del Horario Activo")
            df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor', 'semestre']]
            df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente', 'Tipo/Semestre']
            st.dataframe(df_lista, use_container_width=True, hide_index=True)
        else:
            st.error(mensaje_error)