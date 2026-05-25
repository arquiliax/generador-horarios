import streamlit as st
import random
import pandas as pd
import io
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# --- BASE DE DATOS DE MATERIAS (TERCER SEMESTRE) ---
MATERIAS_TERCER_SEMESTRE = [
    {"nrc": "40108", "clave": "FGUS 006", "materia": "Lengua Extranjera III", "secc": "421", "dias": "AJ", "hora": "0700-0859", "profesor": "ORTEGA-CASTILLO KARINA"},
    {"nrc": "40252", "clave": "FGUS 001", "materia": "Formacion Humana y Social", "secc": "421", "dias": "LM", "hora": "0900-1059", "profesor": "PEREZ-XOCHIPA MARCO POLO"},
    {"nrc": "56817", "clave": "PSIS 012", "materia": "Teorias del Aprendizaje", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "BENAVIDES - VALDERRABANO MARICELA"},
    {"nrc": "56827", "clave": "PSIS 013", "materia": "Psi.del Desarrollo Humano III", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "LIMATIZCARENO SILVIA CAROLINA"},
    {"nrc": "56833", "clave": "PSIS 014", "materia": "Psicopatologia Interaccional", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "AGUILAR-DAVILA YADIRA"},
    {"nrc": "56837", "clave": "PSIS 015", "materia": "Teorias de los Sistemas Ciber", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA"},
    {"nrc": "56849", "clave": "PSIS 016", "materia": "Teor. en Psicologia Social II", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "HERNANDEZ - ESCOBAR VERONICA"},
    
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
        return None, False, materias_omitidas, omitidas_prof_unico, "El bloqueo de horas eliminó todas las opciones de materias válidas."

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
                incluido_en_resultado = any(coincide_profesor(p_p, m['profesor']) for m in calendario_propuesto)
                if existe_en_filtro and not incluido_en_resultado:
                    prioridad_completa = False; break
            return calendario_propuesto, prioridad_completa, materias_omitidas, omitidas_prof_unico, ""

    return None, False, materias_omitidas, omitidas_prof_unico, "No se encontró una combinación válida sin traslapes con las condiciones dadas."

# --- FUNCIÓN PARA LOGRAR GUARDAR Y CREAR EL PDF ---
def exportar_horario_pdf(calendario_data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter), rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor('#1E3A8A'), spaceAfter=12)
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=9, leading=11)
    header_style = ParagraphStyle('HeaderStyle', parent=styles['Normal'], fontSize=10, textColor=colors.white, fontName='Helvetica-Bold')

    story.append(Paragraph("<b>Reporte de Horario Escolar Generado</b>", title_style))
    story.append(Paragraph("Planificación académica de materias - Tercer Semestre", styles['Normal']))
    story.append(Spacer(1, 15))
    
    headers = ['NRC', 'Clave', 'Materia', 'Secc.', 'Días', 'Horario', 'Profesor']
    data_tabla = [headers]
    
    for m in calendario_data:
        data_tabla.append([m['nrc'], m['clave'], m['materia'], m['secc'], m['dias'], m['hora'], m['profesor']])
        
    tabla = Table(data_tabla, colWidths=[50, 60, 180, 40, 40, 80, 230])
    tabla.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#F8F9FA'), colors.white]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#D1D5DB')),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
    ]))
    
    story.append(tabla)
    doc.build(story)
    buffer.seek(0)
    return buffer

# --- CONFIGURACIÓN DE LA PÁGINA WEB ---
st.set_page_config(page_title="Generador de Horarios Estricto", layout="wide", page_icon="🗓️")

# Inicializar estado del calendario en memoria interna de Streamlit
if 'calendario_activo' not in st.session_state:
    st.session_state['calendario_activo'] = None
if 'prioridad_cumplida' not in st.session_state:
    st.session_state['prioridad_cumplida'] = False
if 'omitidas' not in st.session_state:
    st.session_state['omitidas'] = []
if 'omitidas_prof_unico' not in st.session_state:
    st.session_state['omitidas_prof_unico'] = []
if 'filtros_activos' not in st.session_state:
    st.session_state['filtros_activos'] = False

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🛠️ Filtros de Control")
lm_inicio = st.sidebar.number_input("Hora de Inicio LM (HHMM)", min_value=0, max_value=2400, value=0, step=100)
lm_fin = st.sidebar.number_input("Hora de Fin LM (HHMM)", min_value=0, max_value=2400, value=0, step=100)
aj_inicio = st.sidebar.number_input("Hora de Inicio MA (HHMM)", min_value=0, max_value=2400, value=0, step=100)
aj_fin = st.sidebar.number_input("Hora de Fin MA (HHMM)", min_value=0, max_value=2400, value=0, step=100)

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Ej. ORTEGA-CASTILLO KARINA")
    if pref_name.strip(): profesores_inputs.append(pref_name.strip())

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Dinámico y Prioritario")
st.subheader("Tercer Semestre")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    cal, pr_cumplida, om, om_prof, err = generar_horario_estricto(
        MATERIAS_TERCER_SEMESTRE, profesores_inputs, lm_inicio, lm_fin, aj_inicio, aj_fin
    )
    if cal:
        st.session_state['calendario_activo'] = cal
        st.session_state['prioridad_cumplida'] = pr_cumplida
        st.session_state['omitidas'] = om
        st.session_state['omitidas_prof_unico'] = om_prof
        st.session_state['filtros_activos'] = len(profesores_inputs) > 0
    else:
        st.error(err)
        st.session_state['calendario_activo'] = None

# Si existe un horario cargado en memoria, lo renderizamos
if st.session_state['calendario_activo']:
    cal = st.session_state['calendario_activo']
    
    if st.session_state['omitidas']:
        st.warning(f"⚠️ **Atención:** Para cumplir tus restricciones de tiempo, se omitieron: {', '.join(st.session_state['omitidas'])}.")
    if st.session_state['omitidas_prof_unico']:
        st.error(f"👤 **Materia Omitida:** La asignatura **{', '.join(st.session_state['omitidas_prof_unico'])}** se omitió porque el profesor prioritario asignado es el único que la imparte y no está disponible en tus horarios accesibles.")

    if st.session_state['filtros_activos']:
        if st.session_state['prioridad_cumplida']:
            st.info("💎 **Filtro Aplicado Correctamente:** Se fijaron exitosamente tus profesores prioritarios.")
        else:
            st.warning("⚠️ **Filtro No Aplicado Completamente:** Tus profesores prioritarios no se pudieron implementar en el horario por los horarios bloqueados.")
    else:
        st.success("🎯 ¡Horario estructurado correctamente!")

    # --- TABLA VISUAL ---
    bloques_horas = ["0700-0859", "0900-1059", "1100-1259", "1300-1459", "1500-1659", "1700-1859", "1900-2059"]
    df_horario = pd.DataFrame("", index=bloques_horas, columns=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
    
    for m in cal:
        info_celda = f"📚 {m['materia']} (Sec. {m['secc']})\n👤 {m['profesor']}\n[NRC: {m['nrc']}]"
        if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
        if 'M' in m['dias']: df_horario.at[m['hora'], "Miércoles"] = info_celda
        if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
        if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda

    st.write("### 📅 Vista de Calendario Semanal")
    st.markdown("<style>table { font-size: 13px !important; width: 100% !important; } th { background-color: #1E3A8A !important; color: white !important; } td { white-space: pre-line !important; height: 90px !important; vertical-align: top !important; background-color: #F8F9FA; border: 1px solid #D1D5DB !important; }</style>", unsafe_allow_html=True)
    st.table(df_horario)
    
    st.write("### 📝 Detalle del Horario Activo")
    df_lista = pd.DataFrame(cal)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
    df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
    st.dataframe(df_lista, use_container_width=True, hide_index=True)

    # --- REGLA SOLICITADA: IMPRESORA Y GUARDADO EN PDF EN LA PARTE BAJA ---
    st.markdown("---")
    
    # Renderizado centrado del Icono de Impresora SVG nativo y el texto inferior
    st.markdown(
        """
        <div style="text-align: center; margin-top: 15px; margin-bottom: 5px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="55" height="55" viewBox="0 0 24 24" fill="none" stroke="#1E3A8A" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 6 2 18 2 18 9"></polyline>
              <path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"></path>
              <rect x="6" y="14" width="12" height="8"></rect>
            </svg>
            <p style="font-family: sans-serif; color: #1E3A8A; font-weight: bold; margin-top: 8px; font-size: 15px;">Imprimir Horario</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Creación y renderizado dinámico del botón de guardado en PDF
    pdf_data = exportar_horario_pdf(cal)
    
    # Columnas para centrar perfectamente el botón de guardado debajo de la impresora
    col1, col2, col3 = st.columns([2, 1, 2])
    with col2:
        st.download_button(
            label="💾 Descargar Horario (PDF)",
            data=pdf_data,
            file_name="Mi_Horario_Tercer_Semestre.pdf",
            mime="application/pdf",
            use_container_width=True
        )