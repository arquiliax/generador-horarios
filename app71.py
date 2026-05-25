import streamlit as st
import random
import pandas as pd

# =========================================================================
# 📚 CATÁLOGO REAL EXTRAÍDO DE TU DOCUMENTO OFICIAL (PRIMAVERA 2026)
# =========================================================================
CATALOGO_MATERIAS = [
    # --- 1er SEMESTRE ---
    {"nrc": "40110", "clave": "FGMA 001", "materia": "Introduccion a la FGU", "secc": "421", "dias": "AJ", "hora": "0700-0829", "profesor": "TLALPAN-RUIZ MARIA GUADALUPE", "semestre": "1er Semestre"},
    {"nrc": "40112", "clave": "FGMA 004", "materia": "Ingles I", "secc": "422", "dias": "LM", "hora": "0700-0859", "profesor": "GONZALEZ-VALERDI YESENIA", "semestre": "1er Semestre"},
    {"nrc": "56329", "clave": "PSIA 007", "materia": "Psicobiologia I", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "LOPEZ-CORTES VICENTE ARTURO", "semestre": "1er Semestre"},
    {"nrc": "56349", "clave": "PSIA 001", "materia": "Teorias de la Personalidad", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "SANCHEZ - ALONSO LUIS FERNANDO", "semestre": "1er Semestre"},
    {"nrc": "56492", "clave": "PSIA 002", "materia": "Historia de la Psicologia", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56525", "clave": "PSIA 008", "materia": "Psi. del Desarrollo Humano I", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "CANTERO - ANGULO MARIA DEL PILAR", "semestre": "1er Semestre"},
    {"nrc": "56616", "clave": "PSIA 017", "materia": "Epistemologia y Psicologia", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56622", "clave": "PSIA 018", "materia": "T.Lec. Redaccion Textos Disc.", "secc": "001", "dias": "V", "hora": "0900-1259", "profesor": "HERNANDEZ- RODRIGUEZ GUADALUPE LOURDE", "semestre": "1er Semestre"},
    {"nrc": "56440", "clave": "PSIA 001", "materia": "Teorias de la Personalidad", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "1er Semestre"},
    {"nrc": "56506", "clave": "PSIA 002", "materia": "Historia de la Psicologia", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56518", "clave": "FGMA 001", "materia": "Introduccion a la FGU", "secc": "422", "dias": "AJ", "hora": "1500-1629", "profesor": "ROMERO-HORAN MARIA GUILLERMINA", "semestre": "1er Semestre"},
    {"nrc": "56538", "clave": "PSIA 008", "materia": "Psi. del Desarrollo Humano I", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "CANTERO - ANGULO MARIA DEL PILAR", "semestre": "1er Semestre"},
    {"nrc": "56605", "clave": "PSIA 007", "materia": "Psicobiologia I", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "GARCIA - FLORES MARCO ANTONIO", "semestre": "1er Semestre"},
    {"nrc": "56620", "clave": "PSIA 017", "materia": "Epistemologia y Psicologia", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "SANCHEZ - ALONSO LUIS FERNANDO", "semestre": "1er Semestre"},
    {"nrc": "56624", "clave": "PSIA 018", "materia": "T.Lec. Redaccion Textos Disc.", "secc": "002", "dias": "V", "hora": "1300-1659", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "1er Semestre"},
    {"nrc": "56657", "clave": "FGMA 004", "materia": "Ingles I", "secc": "421", "dias": "AJ", "hora": "1900-2059", "profesor": "HERNANDEZ - CASIANO OSCAR", "semestre": "1er Semestre"},

    # --- 2do SEMESTRE ---
    {"nrc": "56766", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56851", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "MARTINEZ-VELAZQUEZ EDUARDO SALVADOR", "semestre": "2do Semestre"},
    {"nrc": "56880", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "BECERRA - ALLENDE JORGE FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56916", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "PEREZ BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "57083", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "SILVARIOS CARLOS ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57127", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "61668", "clave": "FGMA 005", "materia": "Ingles II", "secc": "426", "dias": "LM", "hora": "0700-0859", "profesor": "SIN ASIGNAR", "semestre": "2do Semestre"},
    {"nrc": "56740", "clave": "FGMA 005", "materia": "Ingles II", "secc": "422", "dias": "AJ", "hora": "1900-2059", "profesor": "REYES-OSORIO MARIA ISABEL", "semestre": "2do Semestre"},
    {"nrc": "56775", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "ROJAS HERNANDEZ GUADALUPE JANET", "semestre": "2do Semestre"},
    {"nrc": "56885", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "BECERRA-ALLENDE JORGE FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56922", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57091", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57134", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "DURAN - SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},
    {"nrc": "59416", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "56696", "clave": "FGMA 005", "materia": "Ingles II", "secc": "423", "dias": "AJ", "hora": "0900-1059", "profesor": "BARRIENTOS - CANTORAN LUCIA", "semestre": "2do Semestre"},
    {"nrc": "56807", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "003", "dias": "LM", "hora": "0900-1059", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56861", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "003", "dias": "LM", "hora": "1300-1459", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56892", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "003", "dias": "LM", "hora": "1100-1259", "profesor": "BERRABORTOLOTTI MARIA JUANA", "semestre": "2do Semestre"},
    {"nrc": "56928", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "003", "dias": "AJ", "hora": "0700-0859", "profesor": "DIAZ-CARDENAS ALFONSO FELIPE", "semestre": "2do Semestre"},
    {"nrc": "57097", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "003", "dias": "AJ", "hora": "1100-1259", "profesor": "SILVARIOS CARLOS ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57139", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56714", "clave": "FGMA 005", "materia": "Ingles II", "secc": "424", "dias": "AJ", "hora": "1500-1659", "profesor": "PIANTZI-VARELA LETICIA", "semestre": "2do Semestre"},
    {"nrc": "56814", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "004", "dias": "LM", "hora": "1500-1659", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "2do Semestre"},
    {"nrc": "56864", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56896", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "004", "dias": "LM", "hora": "1700-1859", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "56930", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "004", "dias": "LM", "hora": "1900-2059", "profesor": "RAMOS PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57104", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "004", "dias": "AJ", "hora": "1900-2059", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "2do Semestre"},
    {"nrc": "57155", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "004", "dias": "AJ", "hora": "1700-1859", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},
    {"nrc": "56720", "clave": "FGMA 005", "materia": "Ingles II", "secc": "425", "dias": "LM", "hora": "0700-0859", "profesor": "ISIDRO DE JESUS JACOBO", "semestre": "2do Semestre"},
    {"nrc": "56836", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "005", "dias": "LM", "hora": "0900-1059", "profesor": "TENORIO - MARTINEZ ROSALIA", "semestre": "2do Semestre"},
    {"nrc": "56867", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "005", "dias": "AJ", "hora": "1100-1259", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56901", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "005", "dias": "AJ", "hora": "0900-1059", "profesor": "CANTERO - ANGULO MARIA DEL PILAR", "semestre": "2do Semestre"},
    {"nrc": "56933", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "005", "dias": "LM", "hora": "1300-1459", "profesor": "RAMOS PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57113", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "005", "dias": "AJ", "hora": "0700-0859", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57163", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "005", "dias": "LM", "hora": "1100-1259", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "56841", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "006", "dias": "LM", "hora": "1500-1659", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56871", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "006", "dias": "AJ", "hora": "1300-1459", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "56906", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "006", "dias": "AJ", "hora": "1500-1659", "profesor": "CANTERO - ANGULO MARIA DEL PILAR", "semestre": "2do Semestre"},
    {"nrc": "56936", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "006", "dias": "AJ", "hora": "1700-1859", "profesor": "RAMOS-PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57117", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "006", "dias": "V", "hora": "1300-1659", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "2do Semestre"},
    {"nrc": "57171", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "006", "dias": "LM", "hora": "1700-1859", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "56753", "clave": "FGMA 005", "materia": "Ingles II", "secc": "427", "dias": "LM", "hora": "0700-0859", "profesor": "ALCARAZ-BARRIOS MARISOL", "semestre": "2do Semestre"},
    {"nrc": "56845", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "RODRIGUEZ-CASTILLO KARINA", "semestre": "2do Semestre"},
    {"nrc": "56873", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "007", "dias": "LM", "hora": "1100-1259", "profesor": "HERNANDEZ-RODRIGUEZ GUADALUPE LOURDES", "semestre": "2do Semestre"},
    {"nrc": "56910", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "007", "dias": "LM", "hora": "1300-1459", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "56938", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "007", "dias": "AJ", "hora": "1100-1259", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57119", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "007", "dias": "AJ", "hora": "0900-1059", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57175", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "007", "dias": "AJ", "hora": "0700-0859", "profesor": "RODRIGUEZ-MARTINEZ RICARDO ALEJANDRO", "semestre": "2do Semestre"},
    {"nrc": "56759", "clave": "FGMA 005", "materia": "Ingles II", "secc": "428", "dias": "LM", "hora": "1900-2059", "profesor": "REYES-OSORIO MARIA ISABEL", "semestre": "2do Semestre"},
    {"nrc": "57738", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "008", "dias": "LM", "hora": "1700-1859", "profesor": "SANCHEZ - ALONSO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57741", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "008", "dias": "LM", "hora": "1500-1659", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57746", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "008", "dias": "AJ", "hora": "1300-1459", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "57752", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "008", "dias": "AJ", "hora": "1500-1659", "profesor": "RAMOS PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57761", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "57766", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "008", "dias": "AJ", "hora": "1900-2059", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},

    # --- 3er SEMESTRE ---
    {"nrc": "40108", "clave": "FGUS 006", "materia": "Lengua Extranjera III", "secc": "421", "dias": "AJ", "hora": "0700-0859", "profesor": "ORTEGA-CASTILLO KARINA", "semestre": "3er Semestre"},
    {"nrc": "40252", "clave": "FGUS 001", "materia": "Formacion Humana y Social", "secc": "421", "dias": "LM", "hora": "0900-1059", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "3er Semestre"},
    {"nrc": "56817", "clave": "PSIS 012", "materia": "Teorias del Aprendizaje", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "BENAVIDES - VALDERRABANO MARICELA", "semestre": "3er Semestre"},
    {"nrc": "56827", "clave": "PSIS 013", "materia": "Psi.del Desarrollo Humano III", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "3er Semestre"},
    {"nrc": "56833", "clave": "PSIS 014", "materia": "Psicopatologia Interaccional", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "3er Semestre"},
    {"nrc": "56837", "clave": "PSIS 015", "materia": "Teorias de los Sistemas Ciber", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "3er Semestre"},
    {"nrc": "56849", "clave": "PSIS 016", "materia": "Teor. en Psicologia Social II", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "HERNANDEZ - ESCOBAR VERONICA", "semestre": "3er Semestre"},
    {"nrc": "56876", "clave": "PSIS 012", "materia": "Teorias del Aprendizaje", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "3er Semestre"},
    {"nrc": "56881", "clave": "PSIS 013", "materia": "Psi.del Desarrollo Humano III", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "CANTERO-ANGULO MARIA DEL PILAR", "semestre": "3er Semestre"},
    {"nrc": "56884", "clave": "PSIS 014", "materia": "Psicopatologia Interaccional", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "RODRIGUEZ - SANCHEZ JOSE LUIS", "semestre": "3er Semestre"},
    {"nrc": "56887", "clave": "PSIS 015", "materia": "Teorias de los Sistemas Ciber", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "3er Semestre"},
    {"nrc": "56895", "clave": "PSIS 016", "materia": "Teor. en Psicologia Social II", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "MARTINEZ MENDEZ DULCE MARIA", "semestre": "3er Semestre"},
    {"nrc": "56900", "clave": "FGUS 001", "materia": "Formacion Humana y Social", "secc": "422", "dias": "LM", "hora": "1900-2059", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "3er Semestre"},
    {"nrc": "56907", "clave": "FGUS 006", "materia": "Lengua Extranjera III", "secc": "422", "dias": "AJ", "hora": "1900-2059", "profesor": "DIAZ-CARREON GRACIELA", "semestre": "3er Semestre"},

    # --- 4to SEMESTRE ---
    {"nrc": "40109", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "421", "dias": "AJ", "hora": "0900-1059", "profesor": "ORTEGACASTILLO KARINA", "semestre": "4to Semestre"},
    {"nrc": "56915", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "4to Semestre"},
    {"nrc": "56927", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "ROJAS - HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "56931", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "4to Semestre"},
    {"nrc": "57116", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "4to Semestre"},
    {"nrc": "57123", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "001", "dias": "V", "hora": "0700-1059", "profesor": "GARCIA AGUILAR GREGORIO", "semestre": "4to Semestre"},
    {"nrc": "57129", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "CARRO - MEZA DULCE CAROLINA", "semestre": "4to Semestre"},
    {"nrc": "57149", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "RAMOS-PEREZ CECILIA", "semestre": "4to Semestre"},
    {"nrc": "57162", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "4to Semestre"},
    {"nrc": "57202", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "4to Semestre"},
    {"nrc": "57207", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "HUERTA-RAMIREZ FEDERICO", "semestre": "4to Semestre"},
    {"nrc": "57219", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "4to Semestre"},
    {"nrc": "57227", "clave": "PSIS 022", "materia": "Intro. a la Psi. Organizacional", "secc": "002", "dias": "AJ", "hora": "1900-2059", "profesor": "TAPIA - LOPEZ SANDRA LUCIA", "semestre": "4to Semestre"},
    {"nrc": "57252", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "422", "dias": "LM", "hora": "1900-2059", "profesor": "HERNANDEZ - CASIANO OSCAR", "semestre": "4to Semestre"},
    {"nrc": "57263", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "003", "dias": "LM", "hora": "0900-1059", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "4to Semestre"},
    {"nrc": "57267", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "57273", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "003", "dias": "LM", "hora": "1100-1259", "profesor": "ROJAS - HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "57520", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "003", "dias": "LM", "hora": "1300-1459", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "4to Semestre"},
    {"nrc": "57522", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "003", "dias": "AJ", "hora": "1100-1259", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "4to Semestre"},
    {"nrc": "57524", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "003", "dias": "AJ", "hora": "0900-1059", "profesor": "MERCADO CARNALLA MARIO RENATO", "semestre": "4to Semestre"},
    {"nrc": "57529", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "423", "dias": "AJ", "hora": "0700-0859", "profesor": "GONZALEZ - VALERDI YESENIA", "semestre": "4to Semestre"},
    {"nrc": "57539", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "GALINDO-MOTO MANUEL ALEJANDRO", "semestre": "4to Semestre"},
    {"nrc": "57537", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "004", "dias": "LM", "hora": "1700-1859", "profesor": "RAMOS PEREZ CECILIA", "semestre": "4to Semestre"},
    {"nrc": "57542", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "004", "dias": "LM", "hora": "1900-2059", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "4to Semestre"},
    {"nrc": "57543", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "004", "dias": "LM", "hora": "1500-1659", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "4to Semestre"},
    {"nrc": "57545", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "004", "dias": "AJ", "hora": "1900-2059", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "4to Semestre"},
    {"nrc": "57549", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "004", "dias": "AJ", "hora": "1700-1859", "profesor": "TAPIA - LOPEZ SANDRA LUCIA", "semestre": "4to Semestre"},
    {"nrc": "57551", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "424", "dias": "AJ", "hora": "1500-1659", "profesor": "MARTINEZ - ARENALDE CESAR", "semestre": "4to Semestre"},
    {"nrc": "57555", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "005", "dias": "LM", "hora": "0900-1059", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "4to Semestre"},
    {"nrc": "57558", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "005", "dias": "LM", "hora": "1300-1459", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "57562", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "005", "dias": "LM", "hora": "1100-1259", "profesor": "BRAMBILA - LOPEZ TERESITA", "semestre": "4to Semestre"},
    {"nrc": "57567", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "RODRIGUEZ - MARTINEZ RICARDO ALEJANDRO", "semestre": "4to Semestre"},
    {"nrc": "57569", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "005", "dias": "AJ", "hora": "1100-1259", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "4to Semestre"},
    {"nrc": "57614", "clave": "PSIS 022", "materia": "Intro. a la Psi. Organizacional", "secc": "005", "dias": "AJ", "hora": "0900-1059", "profesor": "TLALPAN-RUIZ MARIA GUADALUPE", "semestre": "4to Semestre"},
    {"nrc": "57619", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "425", "dias": "AJ", "hora": "0700-0859", "profesor": "SERRANO - RAMIREZ ANA LUCIA", "semestre": "4to Semestre"},
    {"nrc": "57631", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "006", "dias": "AJ", "hora": "1900-2059", "profesor": "RAMOS PEREZ CECILIA", "semestre": "4to Semestre"},
    {"nrc": "57639", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "006", "dias": "AJ", "hora": "1300-1459", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "4to Semestre"},
    {"nrc": "57645", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "006", "dias": "LM", "hora": "1900-2059", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "4to Semestre"},
    {"nrc": "57652", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "006", "dias": "AJ", "hora": "1700-1859", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "4to Semestre"}
]

# =========================================================================
# ⚙️ MOTOR ALGORÍTMICO Y LOGICA DEL GENERADOR
# =========================================================================
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

    return None, False, materias_omitidas, omitidas_prof_unico, "No se encontró una combinación válida sin traslapes."

# --- CONFIGURACIÓN DE STREAMLIT ---
st.set_page_config(page_title="Generador de Horarios Oficial", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🛠️ Filtros de Control")

st.sidebar.subheader("Subir y Seleccionar Periodo")
semestre_seleccionado = st.sidebar.selectbox(
    "Selecciona tu semestre activo:",
    ["1er Semestre", "2do Semestre", "3er Semestre", "4to Semestre"],
    index=2  # Inicia por defecto en 3er semestre
)

st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo: Lunes y Miércoles")
lm_inicio = st.sidebar.number_input("Hora de Inicio LM (HHMM)", min_value=0, max_value=2400, value=0, step=100)
lm_fin = st.sidebar.number_input("Hora de Fin LM (HHMM)", min_value=0, max_value=2400, value=0, step=100)

st.sidebar.markdown("---")
st.sidebar.subheader("🚫 Bloqueo: Martes y Jueves")
aj_inicio = st.sidebar.number_input("Hora de Inicio MA/JU (HHMM)", min_value=0, max_value=2400, value=0, step=100)
aj_fin = st.sidebar.number_input("Hora de Fin MA/JU (HHMM)", min_value=0, max_value=2400, value=0, step=100)

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Ej. PEREZ-XOCHIPA")
    if pref_name.strip(): profesores_inputs.append(pref_name.strip())

# --- FILTRADO EN TIEMPO REAL POR SEMESTRE ---
lista_materias_trabajo = [m for m in CATALOGO_MATERIAS if m['semestre'] == semestre_seleccionado]

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Dinámico y Prioritario")
st.subheader(f"Esquema Activo: {semestre_seleccionado}")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    if not lista_materias_trabajo:
        st.warning(f"La base de datos para el **{semestre_seleccionado}** no contiene información.")
    else:
        calendario, prioridad_cumplida, om, om_prof, err = generar_horario_estricto(
            lista_materias_trabajo, profesores_inputs, lm_inicio, lm_fin, aj_inicio, aj_fin
        )
        
        if calendario:
            if om:
                st.warning(f"⚠️ **Atención:** Para cumplir tus restricciones de tiempo, se omitieron: {', '.join(om)}.")
            if om_prof:
                st.error(f"👤 **Materia Omitida:** La asignatura **{', '.join(om_prof)}** se omitió porque el profesor prioritario choca con tus bloqueos.")

            if len(profesores_inputs) > 0:
                if prioridad_cumplida:
                    st.info("💎 **Filtro Aplicado Correctamente:** Se fijaron exitosamente tus profesores prioritarios.")
                else:
                    st.warning("⚠️ **Filtro No Aplicado Completamente:** Ciertos profesores prioritarios no se incluyeron por cruce con horas bloqueadas.")
            else:
                st.success("🎯 ¡Horario estructurado correctamente!")

            # Armar la matriz del horario semanal (Se normalizaron los bloques horarios más comunes)
            bloques_horas = ["0700-0829", "0700-0859", "0900-1059", "1100-1259", "1300-1459", "1500-1629", "1500-1659", "1700-1859", "1900-2059"]
            df_horario = pd.DataFrame("", index=bloques_horas, columns=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
            
            for m in calendario:
                info_celda = f"📚 {m['materia']} (Sec. {m['secc']})\n👤 {m['profesor']}\n[NRC: {m['nrc']}]"
                if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
                if 'M' in m['dias']: df_horario.at[m['hora'], "Miércoles"] = info_celda
                if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda
                if 'V' in m['dias']: df_horario.at[m['hora'], "Viernes"] = info_celda

            st.write("### 📅 Vista de Calendario Semanal")
            st.markdown("<style>table { font-size: 13px !important; width: 100% !important; } th { background-color: #1E3A8A !important; color: white !important; } td { white-space: pre-line !important; height: 90px !important; vertical-align: top !important; background-color: #F8F9FA; border: 1px solid #D1D5DB !important; }</style>", unsafe_allow_html=True)
            st.table(df_horario)
            
            st.write("### 📝 Detalle del Horario Activo")
            df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
            df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
            st.dataframe(df_lista, use_container_width=True, hide_index=True)
        else:
            st.error(err)