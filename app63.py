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
    ini_mat, fin_mat = parse_hora(materia['hora'])
    dias = materia['dias']
    
    if 'L' in dias or 'M' in dias:
        if lm_ini < lm_fin:
            return ini_mat < lm_fin and lm_ini < fin_mat
            
    if 'A' in dias or 'J' in dias:
        if aj_ini < aj_fin:
            return ini_mat < aj_fin and aj_ini < fin_mat
            
    return False

# NUEVA FUNCIÓN: Valida si la entrada del usuario coincide de forma flexible con el nombre del profesor
def coincide_profesor(nombre_ingresado, nombre_catalogo):
    # Dividir lo ingresado por el usuario en palabras individuales (ignorando guiones y espacios extras)
    tokens_ingresados = nombre_ingresado.lower().replace('-', ' ').split()
    nombre_catalogo_limpio = nombre_catalogo.lower().replace('-', ' ')
    
    if not tokens_ingresados:
        return False
        
    # Verificar que TODAS las palabras ingresadas por el usuario existan en el nombre del catálogo
    return all(token in nombre_catalogo_limpio for token in tokens_ingresados)

def generar_horario_estricto(lista_materias, profesores_prioritarios, lm_ini, lm_fin, aj_ini, aj_fin, max_intentos=5000):
    materias_unicas = {}
    nombres_materias = {}
    
    for m in lista_materias:
        clave = m['clave']
        nombres_materias[clave] = m['materia']
        if clave not in materias_unicas:
            materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    # Limpiamos las entradas de texto vacías
    prioridades = [p.strip() for p in profesores_prioritarios if p.strip()]
    materias_omitidas = []
    omitidas_prof_unico = []
    
    materias_filtradas = {}
    
    # 1. FILTRADO MATEMÁTICO INICIAL
    for clave, opciones in materias_unicas.items():
        # Ver si el usuario ingresó un profesor coincidente para esta materia usando la nueva función flexible
        opciones_con_profesor = [
            op for op in opciones 
            if any(coincide_profesor(p_p, op['profesor']) for p_p in prioridades)
        ]
        
        usuario_pidio_profesor = len(opciones_con_profesor) > 0
        opciones_a_evaluar = opciones_con_profesor if usuario_pidio_profesor else opciones
        
        # Validar cuáles sobreviven a las horas bloqueadas
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

    # 2. MOTOR DE COMBINATORIA
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
            # 3. VERIFICACIÓN FINAL COMPLETA
            prioridad_completa = True
            
            for p_p in prioridades:
                # Comprobar si este profesor prioritario existe en las opciones que sobrevivieron al bloqueo
                existe_en_filtro = any(coincide_profesor(p_p, op['profesor']) for opciones in materias_filtradas.values() for op in opciones)
                # Comprobar si efectivamente se incluyó en el calendario final generado
                incluido_en_resultado = any(coincide_profesor(p_p, m['profesor']) for m in calendario_propuesto)
                
                if existe_en_filtro and not incluido_en_resultado:
                    prioridad_completa = False
                    break
                    
            return calendario_propuesto, prioridad_completa, materias_omitidas, omitidas_prof_unico, ""

    return None, False, materias_omitidas, omitidas_prof_unico, "No se encontró una combinación válida sin traslapes con las condiciones dadas."

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Generador de Horarios Estricto", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🛠️ Filtros de Control")

# BLOQUEO: LUNES Y MIÉRCOLES
st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo: Lunes y Miércoles")
lm_inicio = st.sidebar.number_input("Hora de Inicio LM (HHMM)", min_value=0, max_value=2400, value=0, step=100)
lm_fin = st.sidebar.number_input("Hora de Fin LM (HHMM)", min_value=0, max_value=2400, value=0, step=100)

# BLOQUEO: MARTES Y JUEVES
st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo: Martes y Jueves")
aj_inicio = st.sidebar.number_input("Hora de Inicio MA (HHMM)", min_value=0, max_value=2400, value=0, step=100)
aj_fin = st.sidebar.number_input("Hora de Fin MA (HHMM)", min_value=0, max_value=2400, value=0, step=100)

# SECCIÓN: PROFESORES PRIORITARIOS
st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
st.sidebar.write("Puedes escribir el nombre completo, apellidos o solo un nombre:")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Ej. ORTEGA-CASTILLO KARINA")
    if pref_name.strip():
        profesores_inputs.append(pref_name.strip())

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Dinámico y Prioritario")
st.subheader("Tercer Semestre")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    calendario, prioridad_cumplida, omitidas, omitidas_prof_unico, mensaje_error = generar_horario_estricto(
        MATERIAS_TERCER_SEMESTRE, profesores_inputs, lm_inicio, lm_fin, aj_inicio, aj_fin
    )
    
    if calendario:
        # Alerta Emergente 1: Materia Omitida por Espacio General
        if omitidas:
            for mat_om in omitidas:
                st.toast(f"⚠️ Materia Omitida: {mat_om}", icon="🚫")
            st.warning(f"⚠️ **Atención:** Para cumplir tus restricciones de tiempo, se omitieron del horario: {', '.join(omitidas)}.")
            
        # Alerta 2: Materia excluida debido al choque del profesor prioritario/único
        if omitidas_prof_unico:
            for mat_prof in omitidas_prof_unico:
                st.toast(f"🚨 Omitida por Docente: {mat_prof}", icon="👤")
            st.error(f"👤 **Materia Omitida:** La asignatura **{', '.join(omitidas_prof_unico)}** se omitió porque el profesor prioritario asignado (o el único docente disponible) choca de forma directa con tus horas bloqueadas.")

        # Banner de Estado de Filtros (Prioridades)
        if len(profesores_inputs) > 0:
            if prioridad_cumplida:
                st.balloons()
                st.info("💎 **Filtro Aplicado Correctamente:** Se fijaron exitosamente tus profesores prioritarios en el 100% de sus asignaturas.")
            else:
                st.warning("⚠️ **Filtro No Aplicado Completamente:** Uno o más profesores prioritarios no se pudieron implementar en el horario debido a que sus secciones entraban en conflicto con tus horas bloqueadas.")
        else:
            st.success("🎯 ¡Horario estructurado correctamente!")

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

        # --- VISTA DE CALENDARIO ---
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
        df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
        df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
        st.dataframe(df_lista, use_container_width=True, hide_index=True)
    else:
        st.error(mensaje_error)