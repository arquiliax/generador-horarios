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

def generar_horario_prioritario(lista_materias, profesores_prioritarios, lm_ini, lm_fin, aj_ini, aj_fin, max_intentos=4000):
    materias_unicas = {}
    nombres_materias = {}
    
    for m in lista_materias:
        clave = m['clave']
        nombres_materias[clave] = m['materia']
        if clave not in materias_unicas:
            materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    prioridades = [p.lower() for p in profesores_prioritarios if p.strip()]
    materias_omitidas = []
    omitidas_por_profesor_unico = []

    # Filtrado inicial por horas bloqueadas
    materias_filtradas = {}
    for clave, opciones in materias_unicas.items():
        opciones_validas = [
            op for op in opciones 
            if not choca_con_bloqueo_por_dia(op, lm_ini, lm_fin, aj_ini, aj_fin)
        ]
        
        if opciones_validas:
            materias_filtradas[clave] = opciones_validas
        else:
            # Validación especial: ¿El usuario quería a un profesor que es el único que da esta materia?
            tiene_profesor_prioritario = any(any(p_p in op['profesor'].lower() for p_p in prioridades) for op in opciones)
            es_unico_profesor = len(set(op['profesor'] for op in opciones)) == 1
            
            if tiene_profesor_prioritario and es_unico_profesor:
                omitidas_por_profesor_unico.append(nombres_materias[clave])
            else:
                materias_omitidas.append(nombres_materias[clave])

    if not materias_filtradas:
        return None, False, materias_omitidas, omitidas_por_profesor_unico, "El bloqueo de horas eliminó absolutamente todas las materias disponibles."

    # Intentar combinación con PRIORIDAD ESTRICTA
    for _ in range(max_intentos):
        calendario_propuesto = []
        materias_restantes = list(materias_filtradas.keys())
        conflicto = False

        # PASO 1: Colocar profesores asignados prioritarios
        for clave in list(materias_restantes):
            opciones = materias_filtradas[clave]
            opciones_prioritarias = [op for op in opciones if any(p_p in op['profesor'].lower() for p_p in prioridades)]
            
            if opciones_prioritarias:
                seleccion = random.choice(opciones_prioritarias)
                if any(hay_sobreposicion(seleccion, m_g) for m_g in calendario_propuesto):
                    conflicto = True; break
                calendario_propuesto.append(seleccion)
                materias_restantes.remove(clave)
        
        if conflicto: continue

        # PASO 2: Rellenar materias libres
        for clave in materias_restantes:
            opciones = materias_filtradas[clave]
            seleccion = random.choice(opciones)
            if any(hay_sobreposicion(seleccion, m_g) for m_g in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(seleccion)
            
        if not conflicto and len(calendario_propuesto) == len(materias_filtradas):
            # Verificar si realmente se incluyeron TODOS los profesores prioritarios ingresados que sobrevivieron al filtro
            todos_los_prioritarios_incluidos = True
            for p_p in prioridades:
                # Si el profesor existe en las opciones válidas pero no quedó en el calendario final
                profe_disponible_en_filtro = any(p_p in op['profesor'].lower() for opciones in materias_filtradas.values() for op in opciones)
                profe_en_calendario = any(p_p in m['profesor'].lower() for m in calendario_propuesto)
                if profe_disponible_en_filtro and not profe_en_calendario:
                    todos_los_prioritarios_incluidos = False
                    
            return calendario_propuesto, todos_los_prioritarios_incluidos, materias_omitidas, omitidas_por_profesor_unico, ""

    # RESPALDO: Generar horario alternativo respetando bloqueos (No se cumplen profesores prioritarios)
    for _ in range(max_intentos):
        calendario_propuesto = []
        conflicto = False
        for clave, opciones in materias_filtradas.items():
            opcion_seleccionada = random.choice(opciones)
            if any(hay_sobreposicion(opcion_seleccionada, mg) for mg in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(opcion_seleccionada)
            
        if not conflicto and len(calendario_propuesto) == len(materias_filtradas):
            return calendario_propuesto, False, materias_omitidas, omitidas_por_profesor_unico, ""

    return None, False, materias_omitidas, omitidas_por_profesor_unico, "No se encontró una combinación válida sin traslapes."

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Generador de Horarios Estricto", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🛠️ Filtros e Inclusión")

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
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Ej. Aguilar")
    if pref_name.strip():
        profesores_inputs.append(pref_name.strip())

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Dinámico y Prioritario")
st.subheader("Tercer Semestre")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    calendario, prioridad_cumplida, omitidas, omitidas_prof_unico, mensaje_error = generar_horario_prioritario(
        MATERIAS_TERCER_SEMESTRE, profesores_inputs, lm_inicio, lm_fin, aj_inicio, aj_fin
    )
    
    if calendario:
        # 1. Gestionar alertas de Omisión General
        if omitidas:
            for mat_om in omitidas:
                st.toast(f"⚠️ Materia Omitida: {mat_om}", icon="🚫")
            st.warning(f"⚠️ **Atención:** Para cumplir tus restricciones de tiempo, se omitieron: {', '.join(omitidas)}.")
            
        # 2. NUEVA ALERTA: Ventana emergente para Profesor Único no disponible
        if omitidas_prof_unico:
            for mat_prof in omitidas_prof_unico:
                st.toast(f"🚨 Omitida por Docente: {mat_prof}", icon="👤")
            st.error(f"👤 **Materia Omitida:** La asignatura **{', '.join(omitidas_prof_unico)}** se descartó por completo debido a que el profesor prioritario asignado es el único que la imparte y no está disponible en tus horarios accesibles.")

        # 3. CAMBIO DE ICONO Y ESTADO DINÁMICO DEL FILTRO APALICADO
        if len(profesores_inputs) > 0:
            if prioridad_cumplida:
                st.balloons()
                st.info("💎 **Filtro Aplicado Correctamente:** Se fijaron exitosamente tus profesores prioritarios y el resto de materias se completaron al azar.")
            else:
                # Cambia el estado a advertencia si el profesor prioritario fue omitido o ignorado por culpa de los bloqueos
                st.warning("⚠️ **Filtro No Aplicado Completamente:** Tus profesores prioritarios no se pudieron implementar en el horario debido a las restricciones de tus horarios bloqueados.")
        else:
            st.success("🎯 ¡Horario base estructurado correctamente sin filtros de docente!")

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

        # --- VISTA DE TABLA ---
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