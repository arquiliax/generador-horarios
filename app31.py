import streamlit as st
import random
import pandas as pd

# =========================================================================
# 📚 BASE DE DATOS MAESTRA UNIFICADA (TODOS LOS SEMESTRES: 1er A 10mo)
# =========================================================================
CATALOGO_MATERIAS = [
    # --- 1er SEMESTRE ---
    {"nrc": "40110", "clave": "FGMA 001", "materia": "Introduccion a la FGU", "secc": "421", "dias": "AJ", "hora": "0700-0829", "profesor": "TLALPAN-RUIZ MARIA GUADALUPE", "semestre": "1er Semestre"},
    {"nrc": "40112", "clave": "FGMA 004", "materia": "Ingles I", "secc": "422", "dias": "LM", "hora": "0700-0859", "profesor": "GONZALEZ - VALERDI YESENIA", "semestre": "1er Semestre"},
    {"nrc": "56329", "clave": "PSIA 007", "materia": "Psicobiologia I", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "LOPEZ-CORTES VICENTE ARTURO", "semestre": "1er Semestre"},
    {"nrc": "56349", "clave": "PSIA 001", "materia": "Teorias de la Personalidad", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "SANCHEZ-ALONSO LUIS FERNANDO", "semestre": "1er Semestre"},
    {"nrc": "56492", "clave": "PSIA 002", "materia": "Historia de la Psicologia", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56525", "clave": "PSIA 008", "materia": "Psi. del Desarrollo Humano I", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "CANTERO-ANGULO MARIA DEL PILAR", "semestre": "1er Semestre"},
    {"nrc": "56616", "clave": "PSIA 017", "materia": "Epistemologia y Psicologia", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56622", "clave": "PSIA 018", "materia": "T.Lec. Redaccion Textos Disc.", "secc": "001", "dias": "V", "hora": "0900-1259", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDE", "semestre": "1er Semestre"},
    {"nrc": "56440", "clave": "PSIA 001", "materia": "Teorias de la Personalidad", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "1er Semestre"},
    {"nrc": "56506", "clave": "PSIA 002", "materia": "Historia de la Psicologia", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56518", "clave": "FGMA 001", "materia": "Introduccion a la FGU", "secc": "422", "dias": "AJ", "hora": "1500-1629", "profesor": "ROMERO - HORAN MARIA GUILLERMINA", "semestre": "1er Semestre"},
    {"nrc": "56538", "clave": "PSIA 008", "materia": "Psi. del Desarrollo Humano I", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "CANTERO-ANGULO MARIA DEL PILAR", "semestre": "1er Semestre"},
    {"nrc": "56605", "clave": "PSIA 007", "materia": "Psicobiologia I", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "GARCIA-FLORES MARCO ANTONIO", "semestre": "1er Semestre"},
    {"nrc": "56620", "clave": "PSIA 017", "materia": "Epistemologia y Psicologia", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "SANCHEZ-ALONSO LUIS FERNANDO", "semestre": "1er Semestre"},
    {"nrc": "56624", "clave": "PSIA 018", "materia": "T.Lec. Redaccion Textos Disc.", "secc": "002", "dias": "V", "hora": "1300-1659", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "1er Semestre"},
    {"nrc": "56657", "clave": "FGMA 004", "materia": "Ingles I", "secc": "421", "dias": "AJ", "hora": "1900-2059", "profesor": "HERNANDEZ - CASIANO OSCAR", "semestre": "1er Semestre"},

    # --- 2do SEMESTRE ---
    {"nrc": "56766", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56851", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "MARTINEZ-VELAZQUEZ EDUARDO SALVADOR", "semestre": "2do Semestre"},
    {"nrc": "56800", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "BECERRA - ALLENDE JORGE FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56916", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "57083", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "SILVARIOS CARLOS ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57127", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "61668", "clave": "FGMA 005", "materia": "Ingles II", "secc": "426", "dias": "LM", "hora": "0700-0859", "profesor": "POR DESIGNAR", "semestre": "2do Semestre"},
    {"nrc": "56740", "clave": "FGMA 005", "materia": "Ingles II", "secc": "422", "dias": "AJ", "hora": "1900-2059", "profesor": "REYES-OSORIO MARIA ISABEL", "semestre": "2do Semestre"},
    {"nrc": "56775", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "2do Semestre"},
    {"nrc": "56885", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "BECERRA - ALLENDE JORGE FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56922", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "OREA-HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57091", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57134", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},
    {"nrc": "59416", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "56696", "clave": "FGMA 005", "materia": "Ingles II", "secc": "423", "dias": "AJ", "hora": "0900-1059", "profesor": "BARRIENTOS - CANTORAN LUCIA", "semestre": "2do Semestre"},
    {"nrc": "56807", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "003", "dias": "LM", "hora": "0900-1059", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56861", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "003", "dias": "LM", "hora": "1300-1459", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56892", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "003", "dias": "LM", "hora": "1100-1259", "profesor": "BERRA - BORTOLOTTI MARIA JUANA", "semestre": "2do Semestre"},
    {"nrc": "56928", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "003", "dias": "AJ", "hora": "0700-0859", "profesor": "DIAZ-CARDENAS ALFONSO FELIPE", "semestre": "2do Semestre"},
    {"nrc": "57097", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "003", "dias": "AJ", "hora": "1100-1259", "profesor": "SILVARIOS CARLOS ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57139", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56714", "clave": "FGMA 005", "materia": "Ingles II", "secc": "424", "dias": "AJ", "hora": "1500-1659", "profesor": "PIANTZI - VARELA LETICIA", "semestre": "2do Semestre"},
    {"nrc": "56814", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "004", "dias": "LM", "hora": "1500-1659", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "2do Semestre"},
    {"nrc": "56864", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56896", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "004", "dias": "LM", "hora": "1700-1859", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "56930", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "004", "dias": "LM", "hora": "1900-2059", "profesor": "RAMOS-PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57104", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "004", "dias": "AJ", "hora": "1900-2059", "profesor": "MARTINEZ-MENDEZ DULCE MARIA", "semestre": "2do Semestre"},
    {"nrc": "57155", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "004", "dias": "AJ", "hora": "1700-1859", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},
    {"nrc": "56720", "clave": "FGMA 005", "materia": "Ingles II", "secc": "425", "dias": "LM", "hora": "0700-0859", "profesor": "ISIDRO DE JESUS JACOBO", "semestre": "2do Semestre"},
    {"nrc": "56836", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "005", "dias": "LM", "hora": "0900-1059", "profesor": "TENORIO-MARTINEZ ROSALIA", "semestre": "2do Semestre"},
    {"nrc": "56867", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "005", "dias": "AJ", "hora": "1100-1259", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56901", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "005", "dias": "AJ", "hora": "0900-1059", "profesor": "CANTERO-ANGULO MARIA DEL PILAR", "semestre": "2do Semestre"},
    {"nrc": "56933", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "005", "dias": "LM", "hora": "1300-1459", "profesor": "RAMOS - PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57113", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "005", "dias": "AJ", "hora": "0700-0859", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57163", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "005", "dias": "LM", "hora": "1100-1259", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "56841", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "006", "dias": "LM", "hora": "1500-1659", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56871", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "006", "dias": "AJ", "hora": "1300-1459", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "56906", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "006", "dias": "AJ", "hora": "1500-1659", "profesor": "CANTERO-ANGULO MARIA DEL PILAR", "semestre": "2do Semestre"},
    {"nrc": "56936", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "006", "dias": "AJ", "hora": "1700-1859", "profesor": "RAMOS-PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57117", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "006", "dias": "V", "hora": "1300-1659", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "2do Semestre"},
    {"nrc": "57171", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "006", "dias": "LM", "hora": "1700-1859", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "56753", "clave": "FGMA 005", "materia": "Ingles II", "secc": "427", "dias": "LM", "hora": "0700-0859", "profesor": "ALCARAZ-BARRIOS MARISOL", "semestre": "2do Semestre"},
    {"nrc": "56845", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "2do Semestre"},
    {"nrc": "56873", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "007", "dias": "LM", "hora": "1100-1259", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "2do Semestre"},
    {"nrc": "56910", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "007", "dias": "LM", "hora": "1300-1459", "profesor": "LIMA-TIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "56938", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "007", "dias": "AJ", "hora": "1100-1259", "profesor": "OREA-HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57119", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "007", "dias": "AJ", "hora": "0900-1059", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57175", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "007", "dias": "AJ", "hora": "0700-0859", "profesor": "RODRIGUEZ - MARTINEZ RICARDO ALEJANDRO", "semestre": "2do Semestre"},
    {"nrc": "56759", "clave": "FGMA 005", "materia": "Ingles II", "secc": "428", "dias": "LM", "hora": "1900-2059", "profesor": "REYES-OSORIO MARIA ISABEL", "semestre": "2do Semestre"},
    {"nrc": "57738", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "008", "dias": "LM", "hora": "1700-1859", "profesor": "SANCHEZ-ALONSO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57741", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "008", "dias": "LM", "hora": "1500-1659", "profesor": "OREA-HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57746", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "008", "dias": "AJ", "hora": "1300-1459", "profesor": "LIMA-TIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "57752", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "008", "dias": "AJ", "hora": "1500-1659", "profesor": "RAMOS - PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57761", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "57766", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "008", "dias": "AJ", "hora": "1900-2059", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},

    # --- 3er SEMESTRE ---
    {"nrc": "57321", "clave": "PSIS 101", "materia": "Estadistica Descriptiva", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "GARCIA-BENITEZ ALEJANDRO", "semestre": "3er Semestre"},
    {"nrc": "57325", "clave": "PSIS 102", "materia": "Neuroanatomia", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "LOPEZ-CORTES VICENTE ARTURO", "semestre": "3er Semestre"},
    {"nrc": "57330", "clave": "PSIS 103", "materia": "Procesos Cognitivos Ejecutivos", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "OREA-HERNANDEZ RICARDO ENRIQUE", "semestre": "3er Semestre"},

    # --- 4to SEMESTRE ---
    {"nrc": "40109", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "421", "dias": "AJ", "hora": "0900-1059", "profesor": "ORTEGA-CASTILLO KARINA", "semestre": "4to Semestre"},
    {"nrc": "56915", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "4to Semestre"},
    {"nrc": "56927", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "56931", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "4to Semestre"},

    # --- 5to SEMESTRE ---
    {"nrc": "57518", "clave": "PSIS 250", "materia": "Evaluacion del Desarrollo", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "5to Semestre"},
    {"nrc": "57523", "clave": "PSIS 250", "materia": "Evaluacion del Desarrollo", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "5to Semestre"},
    {"nrc": "57532", "clave": "PSIS 251", "materia": "Alteraciones del Desarrollo", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "5to Semestre"},
    {"nrc": "57540", "clave": "PSIS 252", "materia": "Entrevista Psicologica", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "VAZQUEZ - CASTELLANOS ARMANDO", "semestre": "5to Semestre"},

    # --- 6to SEMESTRE ---
    {"nrc": "58102", "clave": "PSIS 301", "materia": "Psicopatologia Infantil", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "6to Semestre"},
    {"nrc": "58110", "clave": "PSIS 302", "materia": "Psicometria Clinica", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "DIAZ-CARDENAS ALFONSO FELIPE", "semestre": "6to Semestre"},

    # --- 7mo SEMESTRE ---
    {"nrc": "58540", "clave": "PSIS 401", "materia": "Psicoterapia Cognitivo Conductual", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "OREA-HERNANDEZ RICARDO ENRIQUE", "semestre": "7mo Semestre"},
    {"nrc": "58551", "clave": "PSIS 402", "materia": "Psicologia de la Salud", "secc": "001", "dias": "AJ", "hora": "1300-1459", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "7mo Semestre"},

    # --- 8vo SEMESTRE ---
    {"nrc": "59120", "clave": "PSIS 501", "materia": "Intervencion en Crisis", "secc": "001", "dias": "LM", "hora": "1500-1659", "profesor": "TENORIO-MARTINEZ ROSALIA", "semestre": "8vo Semestre"},
    {"nrc": "59132", "clave": "PSIS 502", "materia": "Psicologia Juridica y Forense", "secc": "001", "dias": "AJ", "hora": "1700-1859", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "8vo Semestre"},

    # --- 9no SEMESTRE ---
    {"nrc": "59601", "clave": "PSIS 601", "materia": "Practica Clinica Supervisada I", "secc": "001", "dias": "V", "hora": "0800-1259", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "9no Semestre"},
    {"nrc": "59612", "clave": "PSIS 602", "materia": "Etica Profesional Clinica", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "9no Semestre"},

    # --- 10mo SEMESTRE ---
    {"nrc": "59910", "clave": "PSIS 701", "materia": "Practica Clinica Supervisada II", "secc": "001", "dias": "V", "hora": "0800-1259", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "10mo Semestre"},
    {"nrc": "59925", "clave": "PSIS 702", "materia": "Seminario de Titulacion", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "10mo Semestre"}
]

# =========================================================================
# ⚙️ INTERFAZ DE USUARIO - STREAMLIT
# =========================================================================
st.set_page_config(page_title="Generador de Horarios UAP", layout="wide")

st.title("🤖 Generador de Horarios Automatizado")
st.write("Configura tus preferencias y encuentra las mejores opciones de combinaciones sin choques de hora.")

# 🛠️ BARRA LATERAL: Filtros y Selección
st.sidebar.header("🎯 Parámetros de Búsqueda")

# Generar lista limpia y ordenada de semestres basados en la base de datos
def ordenar_semestres(s):
    try:
        return int(s.split('er')[0].split('do')[0].split('to')[0].split('vo')[0].split('no')[0])
    except:
        return 99

semestres_disponibles = sorted(list(set(m['semestre'] for m in CATALOGO_MATERIAS)), key=ordenar_semestres)
semestre_seleccionado = st.sidebar.selectbox("Selecciona tu Semestre:", semestres_disponibles)

# Filtrar materias disponibles para este semestre específico
materias_semestre = [m for m in CATALOGO_MATERIAS if m['semestre'] == semestre_seleccionado]
nombres_materias = sorted(list(set(m['materia'] for m in materias_semestre)))

st.sidebar.subheader("📚 Materias a Cursar")
materias_seleccionadas = []
for mat in nombres_materias:
    if st.sidebar.checkbox(mat, value=True):
        materias_seleccionadas.append(mat)

# Filtros avanzados
st.sidebar.subheader("🚫 Restricciones de Horario")
bloquear_viernes = st.sidebar.checkbox("Intentar no tener clases los Viernes", value=False)

st.sidebar.subheader("👨‍🏫 Profesores Preferidos (Opcional)")
todos_profesores = sorted(list(set(m['profesor'] for m in materias_semestre)))
profesores_favoritos = st.sidebar.multiselect("Sugerir profesores:", todos_profesores)

# =========================================================================
# 🧮 LÓGICA DEL MOTOR DE ASIGNACIÓN (BACKEND)
# =========================================================================
def verificar_choque(materia_nueva, horario_actual):
    for m in horario_actual:
        # Verificar si comparten al menos un día
        dias_comunes = set(materia_nueva['dias']).intersection(set(m['dias']))
        if dias_comunes:
            # Separar horas y minutos
            h_ini_n, h_fin_n = int(materia_nueva['hora'].split('-')[0]), int(materia_nueva['hora'].split('-')[1])
            h_ini_a, h_fin_a = int(m['hora'].split('-')[0]), int(m['hora'].split('-')[1])
            
            # Comprobar traslape numérico de intervalos
            if not (h_fin_n <= h_ini_a or h_ini_n >= h_fin_a):
                return True
    return False

def calcular_puntuacion(calendario, profesores_fav, evitar_v):
    score = 0
    for m in calendario:
        if m['profesor'] in profesores_fav:
            score += 15  # Recompensa por profesor ideal
        if evitar_v and 'V' in m['dias']:
            score -= 20  # Penalización por clases en viernes
    return score

# Agrupar las secciones por el nombre de la materia
secciones_por_materia = {}
for mat in materias_semestre:
    if mat['materia'] in materias_seleccionadas:
        if mat['materia'] not in secciones_por_materia:
            secciones_por_materia[mat['materia']] = []
        secciones_por_materia[mat['materia']].append(mat)

# Algoritmo de backtracking para hallar combinaciones válidas sin colisiones
horarios_validos = []

def buscar_combinaciones(lista_materias, index, horario_acumulado):
    if index == len(lista_materias):
        horarios_validos.append(list(horario_acumulado))
        return
    
    materia_actual = lista_materias[index]
    secciones_disponibles = secciones_por_materia[materia_actual]
    
    for seccion in secciones_disponibles:
        if not verificar_choque(seccion, horario_acumulado):
            horario_acumulado.append(seccion)
            buscar_combinaciones(lista_materias, index + 1, horario_acumulado)
            horario_acumulado.pop()

if secciones_por_materia:
    buscar_combinaciones(list(secciones_por_materia.keys()), 0, [])

# =========================================================================
# 📺 RENDERIZADO Y PRESENTACIÓN DE RESULTADOS
# =========================================================================
st.write(f"Se han encontrado **{len(horarios_validos)}** combinaciones posibles sin choques para el **{semestre_seleccionado}**.")

if horarios_validos:
    # Ordenar las combinaciones usando la puntuación de las preferencias del usuario
    horarios_validos.sort(key=lambda x: calcular_puntuacion(x, profesores_favoritos, bloquear_viernes), reverse=True)
    
    # Selector de opción de horario
    opciones_indices = [f"Opción {i+1} (Puntaje de afinidad: {calcular_puntuacion(h, profesores_favoritos, bloquear_viernes)})" for i, h in enumerate(horarios_validos)]
    seleccion_horario = st.selectbox("🎯 Elige una alternativa de horario para visualizar:", opciones_indices)
    
    idx_seleccionado = opciones_indices.index(seleccion_horario)
    calendario = horarios_validos[idx_seleccionado]
    
    # Matriz para construir el calendario visual semanal
    bloques_horas = sorted(list(set(m['hora'] for m in CATALOGO_MATERIAS)))
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    df_horario = pd.DataFrame("", index=bloques_horas, columns=dias_semana)
    
    for m in calendario:
        info_celda = f"📚 {m['materia']}\n🪪 Secc: {m['secc']} | NRC: {m['nrc']}\n👨‍🏫 {m['profesor']}"
        if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
        if 'M' in m['dias']: df_horario.at[m['hora'], "Miércoles"] = info_celda
        if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
        if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda
        if 'V' in m['dias']: df_horario.at[m['hora'], "Viernes"] = info_celda

    # Quitar columnas de días y renglones de horas vacías para compactar la vista
    columnas_activas = [col for col in df_horario.columns if not (df_horario[col] == "").all()]
    filas_activas = [row for row in df_horario.index if not (df_horario.loc[row] == "").all()]
    df_horario_filtrado = df_horario.loc[filas_activas, columnas_activas]

    st.write("### 📅 Vista de Calendario Semanal")
    st.markdown("<style>table { font-size: 13px !important; width: 100% !important; } th { background-color: #1E3A8A !important; color: white !important; } td { white-space: pre-line !important; height: 90px !important; vertical-align: top !important; background-color: #F8F9FA; border: 1px solid #D1D5DB !important; }</style>", unsafe_allow_html=True)
    st.table(df_horario_filtrado)
    
    st.write("### 📝 Detalle del Horario Activo")
    df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
    st.dataframe(df_lista, use_container_width=True)
else:
    st.error("❌ No existen combinaciones viables con los filtros seleccionados. Intenta reducir el número de materias o cambiar las restricciones.")