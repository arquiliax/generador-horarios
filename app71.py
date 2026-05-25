import streamlit as st
import random
import pandas as pd

# =========================================================================
# 📚 BASE DE DATOS MATRICIAL: MAPA CURRICULAR COMPLETO (1° A 10° SEMESTRE)
# =========================================================================
CATALOGO_MATERIAS = [
    # --- PRIMER SEMESTRE ---
    {"nrc": "10101", "clave": "PSI-101", "materia": "Epistemología de la Psicología", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "GONZALEZ SANCHEZ JORGE", "semestre": "1° Semestre"},
    {"nrc": "10102", "clave": "PSI-101", "materia": "Epistemología de la Psicología", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "RAMIREZ MIRELES ANA", "semestre": "1° Semestre"},
    {"nrc": "10103", "clave": "PSI-102", "materia": "Bases Biológicas de la Conducta", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "MARTINEZ REYES LUIS", "semestre": "1° Semestre"},
    {"nrc": "10104", "clave": "PSI-103", "materia": "Historia de la Psicología", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "CASTRO OLMOS ELENA", "semestre": "1° Semestre"},
    {"nrc": "10105", "clave": "FGUS-001", "materia": "Formación Humana y Social", "secc": "401", "dias": "LM", "hora": "1300-1459", "profesor": "PEREZ RAMOS PEDRO", "semestre": "1° Semestre"},

    # --- SEGUNDO SEMESTRE ---
    {"nrc": "20101", "clave": "PSI-201", "materia": "Procesos Psicológicos Básicos", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "HERNANDEZ MAZA RAUL", "semestre": "2° Semestre"},
    {"nrc": "20102", "clave": "PSI-202", "materia": "Neuroanatomía Funcional", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "GOMEZ ALVAREZ ALBERTO", "semestre": "2° Semestre"},
    {"nrc": "20103", "clave": "PSI-203", "materia": "Estadística Descriptiva", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "LOPEZ PACHECO MARÍA", "semestre": "2° Semestre"},
    {"nrc": "20104", "clave": "FGUS-002", "materia": "Desarrollo de Habilidades del Pensamiento", "secc": "402", "dias": "AJ", "hora": "1300-1459", "profesor": "SÁNCHEZ LARA DIEGO", "semestre": "2° Semestre"},

    # --- TERCER SEMESTRE ---
    {"nrc": "40108", "clave": "FGUS-006", "materia": "Lengua Extranjera III", "secc": "421", "dias": "AJ", "hora": "0700-0859", "profesor": "ORTEGA-CASTILLO KARINA", "semestre": "3° Semestre"},
    {"nrc": "40252", "clave": "FGUS-001", "materia": "Formacion Humana y Social", "secc": "421", "dias": "LM", "hora": "0900-1059", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "3° Semestre"},
    {"nrc": "56817", "clave": "PSIS-012", "materia": "Teorias del Aprendizaje", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "BENAVIDES - VALDERRABANO MARICELA", "semestre": "3° Semestre"},
    {"nrc": "56827", "clave": "PSIS-013", "materia": "Psi.del Desarrollo Humano III", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "3° Semestre"},
    {"nrc": "56833", "clave": "PSIS-014", "materia": "Psicopatologia Interaccional", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "3° Semestre"},
    {"nrc": "56837", "clave": "PSIS-015", "materia": "Teorias de los Sistemas Ciber", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "3° Semestre"},
    {"nrc": "56849", "clave": "PSIS-016", "materia": "Teor. en Psicologia Social II", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "HERNANDEZ - ESCOBAR VERONICA", "semestre": "3° Semestre"},
    {"nrc": "56876", "clave": "PSIS-012", "materia": "Teorias del Aprendizaje", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "3° Semestre"},
    {"nrc": "56881", "clave": "PSIS-013", "materia": "Psi.del Desarrollo Humano III", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "CANTERO-ANGULO MARIA DEL PILAR", "semestre": "3° Semestre"},
    {"nrc": "56884", "clave": "PSIS-014", "materia": "Psicopatologia Interaccional", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "RODRIGUEZ - SANCHEZ JOSE LUIS", "semestre": "3° Semestre"},
    {"nrc": "56887", "clave": "PSIS-015", "materia": "Teorias de los Sistemas Ciber", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "3° Semestre"},
    {"nrc": "56895", "clave": "PSIS-016", "materia": "Teor. en Psicologia Social II", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "MARTINEZ MENDEZ DULCE MARIA", "semestre": "3° Semestre"},

    # --- CUARTO SEMESTRE ---
    {"nrc": "40101", "clave": "PSI-401", "materia": "Psicometría Teórica", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "CABELLO ROSARIO", "semestre": "4° Semestre"},
    {"nrc": "40102", "clave": "PSI-402", "materia": "Métodos de Investigación Cualitativa", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "FLORES JAVIER", "semestre": "4° Semestre"},
    {"nrc": "40103", "clave": "PSI-403", "materia": "Evaluación Psicológica Infantil", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "RUIZ GUTIERREZ ROSA", "semestre": "4° Semestre"},
    {"nrc": "40104", "clave": "PSI-404", "materia": "Psicología Social Avanzada", "secc": "001", "dias": "AJ", "hora": "1300-1459", "profesor": "TIRADO SANCHEZ JUAN", "semestre": "4° Semestre"},

    # --- QUINTO SEMESTRE ---
    {"nrc": "50101", "clave": "PSI-501", "materia": "Entrevista Psicopedagógica", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "MEZA ARROYO CONCEPCION", "semestre": "5° Semestre"},
    {"nrc": "50102", "clave": "PSI-502", "materia": "Psicopatología del Adulto", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "VALENCIA ROJAS ARTURO", "semestre": "5° Semestre"},
    {"nrc": "50103", "clave": "PSI-503", "materia": "Diseño de Instrumentos de Medición", "secc": "001", "dias": "LM", "hora": "1500-1659", "profesor": "SORREL GONZALO", "semestre": "5° Semestre"},

    # --- SEXTO SEMESTRE ---
    {"nrc": "60101", "clave": "PSI-601", "materia": "Terapia Cognitivo Conductual (TCC)", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "BECK AARON", "semestre": "6° Semestre"},
    {"nrc": "60102", "clave": "PSI-602", "materia": "Evaluación del Talento Humano", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "CHIAVENATO IDALBERTO", "semestre": "6° Semestre"},
    {"nrc": "60103", "clave": "PSI-603", "materia": "Psicología Dinámica de Grupos", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "LEWIN KURT", "semestre": "6° Semestre"},

    # --- SÉPTIMO SEMESTRE ---
    {"nrc": "70101", "clave": "PSI-701", "materia": "Ética Profesional en Psicología", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "KANT IMMANUEL", "semestre": "7° Semestre"},
    {"nrc": "70102", "clave": "PSI-702", "materia": "Técnicas de Intervención Grupal", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "PERLS FRITZ", "semestre": "7° Semestre"},

    # --- OCTAVO SEMESTRE ---
    {"nrc": "80101", "clave": "PSI-801", "materia": "Diseño de Proyectos de Tesis", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "HERNANDEZ SAMPIERI ROBERTO", "semestre": "8° Semestre"},
    {"nrc": "80102", "clave": "PSI-802", "materia": "Psicofarmacología Clínica", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "SALAZAR VILLARREAL LUIS", "semestre": "8° Semestre"},

    # --- NOVENO SEMESTRE ---
    {"nrc": "90111", "clave": "PSI-901", "materia": "Prácticas Profesionales Supervisoras I", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "PALACIOS LUNA ROCIO", "semestre": "9° Semestre"},
    {"nrc": "90112", "clave": "PSI-902", "materia": "Seminario de Integración de Casos", "secc": "001", "dias": "AJ", "hora": "1500-1659", "profesor": "RODRIGUEZ REYES MAURO", "semestre": "9° Semestre"},

    # --- DÉCIMO SEMESTRE ---
    {"nrc": "10011", "clave": "PSI-1001", "materia": "Prácticas Profesionales Supervisoras II", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "PALACIOS LUNA ROCIO", "semestre": "10° Semestre"},
    {"nrc": "10012", "clave": "PSI-1002", "materia": "Deontología y Práctica Legal", "secc": "001", "dias": "AJ", "hora": "1300-1459", "profesor": "BARRAZA MEZA ABRAHAM", "semestre": "10° Semestre"},

    # --- MATERIAS OPTATIVAS (SÓLO ACCESIBLES DESDE 7° A 10°) ---
    # Clínica
    {"nrc": "99101", "clave": "OPT-CLIN1", "materia": "Psicoterapia Humanista Existencial", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "ROGERS CARL", "semestre": "Optativa - Clínica"},
    {"nrc": "99102", "clave": "OPT-CLIN2", "materia": "Modelos de Terapia Sistémica", "secc": "001", "dias": "AJ", "hora": "1700-1859", "profesor": "MINUCHIN SALVADOR", "semestre": "Optativa - Clínica"},
    # Educativa
    {"nrc": "99201", "clave": "OPT-EDU1", "materia": "Problemas de Aprendizaje Temprano", "secc": "001", "dias": "AJ", "hora": "1500-1659", "profesor": "VYGOTSKY LEV", "semestre": "Optativa - Educativa"},
    {"nrc": "99202", "clave": "OPT-EDU2", "materia": "Orientación Vocacional y Prof.", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "HOLLAND JOHN", "semestre": "Optativa - Educativa"},
    # Organizacional
    {"nrc": "99301", "clave": "OPT-ORG1", "materia": "Estrategias de Outplacement Efectivo", "secc": "001", "dias": "LM", "hora": "1500-1659", "profesor": "MARISTANY LUIS", "semestre": "Optativa - Organizacional"},
    {"nrc": "99302", "clave": "OPT-ORG2", "materia": "Auditoría de Competencias Laborales", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "ALLES MARTHA", "semestre": "Optativa - Organizacional"},
    # Social
    {"nrc": "99401", "clave": "OPT-SOC1", "materia": "Psicología Comunitaria Contemporánea", "secc": "001", "dias": "AJ", "hora": "1700-1859", "profesor": "MONTERO MARITZA", "semestre": "Optativa - Social"},
    {"nrc": "99402", "clave": "OPT-SOC2", "materia": "Análisis de Conflictos Colectivos", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "MOSCOVICI SERGE", "semestre": "Optativa - Social"}
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
        if clave not in materias_unicas: materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    prioridades = [p.strip() for p in profesores_prioritarios if p.strip()]
    materias_omitidas, omitidas_prof_unico = [], []
    materias_filtradas = {}
    
    for clave, opciones in materias_unicas.items():
        opciones_con_profesor = [op for op in opciones if any(coincide_profesor(p_p, op['profesor']) for p_p in prioridades)]
        usuario_pidio_profesor = len(opciones_con_profesor) > 0
        opciones_a_evaluar = opciones_con_profesor if usuario_pidio_profesor else opciones
        opciones_validas = [op for op in opciones_a_evaluar if not choca_con_bloqueo_por_dia(op, lm_ini, lm_fin, aj_ini, aj_fin)]
        
        if opciones_validas:
            materias_filtradas[clave] = opciones_validas
        else:
            es_unico_profesor = len(set(op['profesor'] for op in opciones)) == 1
            if usuario_pidio_profesor or es_unico_profesor:
                omitidas_prof_unico.append(nombres_materias[clave])
            else:
                materias_omitidas.append(nombres_materias[clave])

    if not materias_filtradas:
        return None, False, materias_omitidas, omitidas_prof_unico, "El bloqueo de horas eliminó todas las opciones válidas."

    for _ in range(max_intentos):
        calendario_propuesto, conflicto = [], False
        for clave, opciones in materias_filtradas.items():
            seleccion = random.choice(opciones)
            if any(hay_sobreposicion(seleccion, m_g) for m_g in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(seleccion)
            
        if not conflicto and len(calendario_propuesto) == len(materias_filtradas):
            prioridad_completa = True
            for p_p in prioridades:
                existe_en_filtro = any(coincide_profesor(p_p, op['profesor']) for opciones in materias_filtradas.values() for op in opciones)
                if existe_en_filtro and not any(coincide_profesor(p_p, m['profesor']) for m in calendario_propuesto):
                    prioridad_completa = False; break
            return calendario_propuesto, prioridad_completa, materias_omitidas, omitidas_prof_unico, ""

    return None, False, materias_omitidas, omitidas_prof_unico, "No se encontró una combinación sin traslapes para los filtros dados."

# --- CONFIGURACIÓN DE INTERFAZ ---
st.set_page_config(page_title="Generador de Horarios Universitario", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR): FILTROS ---
st.sidebar.title("🛠️ Configuración del Horario")

# SELECTOR DE SEMESTRES ACTUALIZADO DE 1° A 10°
MAPA_SEMESTRES = {
    "1° Semestre": 1, "2° Semestre": 2, "3° Semestre": 3, "4° Semestre": 4, 
    "5° Semestre": 5, "6° Semestre": 6, "7° Semestre": 7, "8° Semestre": 8, 
    "9° Semestre": 9, "10° Semestre": 10
}
semestre_seleccionado = st.sidebar.selectbox("📆 Selecciona tu Semestre:", list(MAPA_SEMESTRES.keys()), index=2)
numero_semestre = MAPA_SEMESTRES[semestre_seleccionado]

# BLOQUEOS DE HORARIO
st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueos de Horario")
lm_inicio = st.sidebar.number_input("Inicio Lunes/Miércoles (HHMM)", min_value=0, max_value=2400, value=0, step=100)
lm_fin = st.sidebar.number_input("Fin Lunes/Miércoles (HHMM)", min_value=0, max_value=2400, value=0, step=100)
aj_inicio = st.sidebar.number_input("Inicio Martes/Jueves (HHMM)", min_value=0, max_value=2400, value=0, step=100)
aj_fin = st.sidebar.number_input("Fin Martes/Jueves (HHMM)", min_value=0, max_value=2400, value=0, step=100)

# PROFESORES PRIORITARIOS
st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 6):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}")
    if pref_name.strip(): profesores_inputs.append(pref_name.strip())

# --- NÚCLEO DE LA REGLA: MATERIAS OPTATIVAS CONDICIONADAS ---
st.sidebar.markdown("---")
st.sidebar.subheader("🎯 Módulo de Materias Optativas")

optativas_seleccionadas = []

if numero_semestre <= 6:
    st.sidebar.info("🔒 Las materias optativas se habilitan a partir de **7° Semestre** de acuerdo al plan de estudios.")
else:
    st.sidebar.write("Selecciona las materias optativas que deseas cursar:")
    opt_clinica = [m for m in CATALOGO_MATERIAS if m['semestre'] == "Optativa - Clínica"]
    opt_educativa = [m for m in CATALOGO_MATERIAS if m['semestre'] == "Optativa - Educativa"]
    opt_organizacional = [m for m in CATALOGO_MATERIAS if m['semestre'] == "Optativa - Organizacional"]
    opt_social = [m for m in CATALOGO_MATERIAS if m['semestre'] == "Optativa - Social"]

    with st.sidebar.expander("🧠 Área Clínica"):
        for o in opt_clinica:
            if st.checkbox(f"{o['materia']}", key=f"opt_{o['nrc']}"): optativas_seleccionadas.append(o)
    with st.sidebar.expander("🏫 Área Educativa"):
        for o in opt_educativa:
            if st.checkbox(f"{o['materia']}", key=f"opt_{o['nrc']}"): optativas_seleccionadas.append(o)
    with st.sidebar.expander("💼 Área Organizacional"):
        for o in opt_organizacional:
            if st.checkbox(f"{o['materia']}", key=f"opt_{o['nrc']}"): optativas_seleccionadas.append(o)
    with st.sidebar.expander("🌍 Área Social"):
        for o in opt_social:
            if st.checkbox(f"{o['materia']}", key=f"opt_{o['nrc']}"): optativas_seleccionadas.append(o)

# --- ENSAMBLADO Y ANÁLISIS DE CARGA DE MATERIAS (REGLA DE LÍMITE DE 8) ---
materias_tronco_comun = [m for m in CATALOGO_MATERIAS if m['semestre'] == semestre_seleccionado]

# Agrupamos las materias del tronco común por su clave para saber cuántas asignaturas base son realmente
materias_unicas_tronco = len(set(m['clave'] for m in materias_tronco_comun))
materias_unicas_optativas = len(set(m['clave'] for m in optativas_seleccionadas))
total_materias_solicitadas = materias_unicas_tronco + materias_unicas_optativas

banco_materias_final = materias_tronco_comun + optativas_seleccionadas

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Universitario Inteligente")
st.subheader(f"Esquema Activo: {semestre_seleccionado}")

# Métrica de control del límite de carga
col_m1, col_m2 = st.columns(2)
with col_m1:
    st.metric(label="Total de Asignaturas en Proceso", value=f"{total_materias_solicitadas} / 8")

# VERIFICACIÓN DEL LÍMITE REQUERIDO
if total_materias_solicitadas > 8:
    st.error(f"🚨 **Carga Académica Excedida:** Has seleccionado un total de **{total_materias_solicitadas}** materias. El límite permitido por reglamento de la aplicación es de máximo **8 materias** cargadas en total. Desmarca alguna optativa para continuar.")
    boton_deshabilitado = True
else:
    boton_deshabilitado = False

if st.button("🎲 Calcular Horario Óptimo", type="primary", disabled=boton_deshabilitado):
    if not banco_materias_final:
        st.error("No hay materias cargadas en el catálogo de este semestre.")
    else:
        calendario, prioridad_cumplida, omitidas, omitidas_prof_unico, mensaje_error = generar_horario_estricto(
            banco_materias_final, profesores_inputs, lm_inicio, lm_fin, aj_inicio, aj_fin
        )
        
        if calendario:
            if omitidas:
                st.warning(f"⚠️ **Atención:** Para cumplir tus restricciones de tiempo, se omitieron: {', '.join(omitidas)}.")
            if omitidas_prof_unico:
                st.error(f"👤 **Materia Omitida:** La asignatura **{', '.join(omitidas_prof_unico)}** se descartó porque el profesor prioritario (o único disponible) colisiona con tus bloqueos de hora.")

            if len(profesores_inputs) > 0:
                if prioridad_cumplida:
                    st.balloons()
                    st.info("💎 **Filtro Aplicado Correctamente:** Se fijaron exitosamente tus profesores prioritarios.")
                else:
                    st.warning("⚠️ **Filtro No Aplicado Completamente:** Ciertos profesores prioritarios no se integraron por restricciones horarias insalvables.")
            else:
                st.success("🎯 ¡Horario base estructurado correctamente!")

            # Matriz de Calendario Semanal
            bloques_horas = ["0700-0859", "0900-1059", "1100-1259", "1300-1459", "1500-1659", "1700-1859", "1900-2059"]
            dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
            df_horario = pd.DataFrame("", index=bloques_horas, columns=dias_semana)
            
            for m in calendario:
                info_celda = f"📚 {m['materia']} (Sec. {m['secc']})\n👤 {m['profesor']}\n[NRC: {m['nrc']}]"
                if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
                if 'M' in m['dias']: df_horario.at[m['hora'], "Miércoles"] = info_celda
                if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda

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
            df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente', 'Semestre Origen']
            st.dataframe(df_lista, use_container_width=True, hide_index=True)
        else:
            st.error(mensaje_error)