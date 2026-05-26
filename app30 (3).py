import streamlit as st
import random
import pandas as pd

# =========================================================================
# 📚 BASE DE DATOS REAL EXTRAÍDA DE TU DOCUMENTO (MATERIAS BASE)
# =========================================================================
CATALOGO_MATERIAS = [
    # --- 1er SEMESTRE ---
    {"nrc": "40110", "clave": "FGMA 001", "materia": "Introduccion a la FGU", "secc": "421", "dias": "AJ", "hora": "0700-0829", "profesor": "TLALPAN - RUIZ MARIA GUADALUPE", "semestre": "1er Semestre"},
    {"nrc": "40112", "clave": "FGMA 004", "materia": "Ingles I", "secc": "422", "dias": "LM", "hora": "0700-0859", "profesor": "GONZALEZ - VALERDI YESENIA", "semestre": "1er Semestre"},
    {"nrc": "56329", "clave": "PSIA 007", "materia": "Psicobiologia I", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "LOPEZ - CORTES VICENTE ARTURO", "semestre": "1er Semestre"},
    {"nrc": "56349", "clave": "PSIA 001", "materia": "Teorias de la Personalidad", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "SANCHEZ - ALONSO LUIS FERNANDO", "semestre": "1er Semestre"},
    {"nrc": "56492", "clave": "PSIA 002", "materia": "Historia de la Psicologia", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56525", "clave": "PSIA 008", "materia": "Psi. del Desarrollo Humano I", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "CANTERO - ANGULO MARIA DEL PILAR", "semestre": "1er Semestre"},
    {"nrc": "56616", "clave": "PSIA 017", "materia": "Epistemologia y Psicologia", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56622", "clave": "PSIA 018", "materia": "T.Lec. Redaccion Textos Disc.", "secc": "001", "dias": "V", "hora": "0900-1259", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDE", "semestre": "1er Semestre"},
    {"nrc": "56440", "clave": "PSIA 001", "materia": "Teorias de la Personalidad", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "1er Semestre"},
    {"nrc": "56506", "clave": "PSIA 002", "materia": "Historia de la Psicologia", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "1er Semestre"},
    {"nrc": "56518", "clave": "FGMA 001", "materia": "Introduccion a la FGU", "secc": "422", "dias": "AJ", "hora": "1500-1629", "profesor": "ROMERO - HORAN MARIA GUILLERMINA", "semestre": "1er Semestre"},
    {"nrc": "56538", "clave": "PSIA 008", "materia": "Psi. del Desarrollo Humano I", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "CANTERO - ANGULO MARIA DEL PILAR", "semestre": "1er Semestre"},
    {"nrc": "56605", "clave": "PSIA 007", "materia": "Psicobiologia I", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "GARCIA - FLORES MARCO ANTONIO", "semestre": "1er Semestre"},
    {"nrc": "56620", "clave": "PSIA 017", "materia": "Epistemologia y Psicologia", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "SANCHEZ - ALONSO LUIS FERNANDO", "semestre": "1er Semestre"},
    {"nrc": "56624", "clave": "PSIA 018", "materia": "T.Lec. Redaccion Textos Disc.", "secc": "002", "dias": "V", "hora": "1300-1659", "profesor": "SANCHEZ - CID JOSE ELIAS", "semestre": "1er Semestre"},
    {"nrc": "56657", "clave": "FGMA 004", "materia": "Ingles I", "secc": "421", "dias": "AJ", "hora": "1900-2059", "profesor": "HERNANDEZ - CASIANO OSCAR", "semestre": "1er Semestre"},

    # --- 2do SEMESTRE ---
    {"nrc": "56766", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56851", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "MARTINEZ - VELAZQUEZ EDUARDO SALVADOR", "semestre": "2do Semestre"},
    {"nrc": "56880", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "BECERRA - ALLENDE JORGE FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56916", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "57083", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "SILVA - RIOS CARLOS ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57127", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "61668", "clave": "FGMA 005", "materia": "Ingles II", "secc": "426", "dias": "LM", "hora": "0700-0859", "profesor": "", "semestre": "2do Semestre"},
    {"nrc": "56740", "clave": "FGMA 005", "materia": "Ingles II", "secc": "422", "dias": "AJ", "hora": "1900-2059", "profesor": "REYES - OSORIO MARIA ISABEL", "semestre": "2do Semestre"},
    {"nrc": "56775", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "ROJAS - HERNANDEZ GUADALUPE JANET", "semestre": "2do Semestre"},
    {"nrc": "56885", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "BECERRA - ALLENDE JORGE FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56922", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57091", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "LUNA - PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57134", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "DURAN - SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},
    {"nrc": "59416", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "56696", "clave": "FGMA 005", "materia": "Ingles II", "secc": "423", "dias": "AJ", "hora": "0900-1059", "profesor": "BARRIENTOS - CANTORAN LUCIA", "semestre": "2do Semestre"},
    {"nrc": "56807", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "003", "dias": "LM", "hora": "0900-1059", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56861", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "003", "dias": "LM", "hora": "1300-1459", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56892", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "003", "dias": "LM", "hora": "1100-1259", "profesor": "BERRA - BORTOLOTTI MARIA JUANA", "semestre": "2do Semestre"},
    {"nrc": "56928", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "003", "dias": "AJ", "hora": "0700-0859", "profesor": "DIAZ - CARDENAS ALFONSO FELIPE", "semestre": "2do Semestre"},
    {"nrc": "57097", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "003", "dias": "AJ", "hora": "1100-1259", "profesor": "SILVA - RIOS CARLOS ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57139", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "LUNA - PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "56714", "clave": "FGMA 005", "materia": "Ingles II", "secc": "424", "dias": "AJ", "hora": "1500-1659", "profesor": "PIANTZI - VARELA LETICIA", "semestre": "2do Semestre"},
    {"nrc": "56814", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "004", "dias": "LM", "hora": "1500-1659", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "2do Semestre"},
    {"nrc": "56864", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56896", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "004", "dias": "LM", "hora": "1700-1859", "profesor": "LIMA - TIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "56930", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "004", "dias": "LM", "hora": "1900-2059", "profesor": "RAMOS - PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57104", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "004", "dias": "AJ", "hora": "1900-2059", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "2do Semestre"},
    {"nrc": "57155", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "004", "dias": "AJ", "hora": "1700-1859", "profesor": "DURAN - SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},
    {"nrc": "56720", "clave": "FGMA 005", "materia": "Ingles II", "secc": "425", "dias": "LM", "hora": "0700-0859", "profesor": "ISIDRO - DE JESUS JACOBO", "semestre": "2do Semestre"},
    {"nrc": "56836", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "005", "dias": "LM", "hora": "0900-1059", "profesor": "TENORIO - MARTINEZ ROSALIA", "semestre": "2do Semestre"},
    {"nrc": "56867", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "005", "dias": "AJ", "hora": "1100-1259", "profesor": "PEREZ - BARROSO MARLENE", "semestre": "2do Semestre"},
    {"nrc": "56901", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "005", "dias": "AJ", "hora": "0900-1059", "profesor": "CANTERO - ANGULO MARIA DEL PILAR", "semestre": "2do Semestre"},
    {"nrc": "56933", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "005", "dias": "LM", "hora": "1300-1459", "profesor": "RAMOS - PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57113", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "005", "dias": "AJ", "hora": "0700-0859", "profesor": "LUNA - PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57163", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "005", "dias": "LM", "hora": "1100-1259", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "56841", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "006", "dias": "LM", "hora": "1500-1659", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "2do Semestre"},
    {"nrc": "56871", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "006", "dias": "AJ", "hora": "1300-1459", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "56906", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "006", "dias": "AJ", "hora": "1500-1659", "profesor": "CANTERO - ANGULO MARIA DEL PILAR", "semestre": "2do Semestre"},
    {"nrc": "56936", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "006", "dias": "AJ", "hora": "1700-1859", "profesor": "RAMOS - PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57117", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "006", "dias": "V", "hora": "1300-1659", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "2do Semestre"},
    {"nrc": "57171", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "006", "dias": "LM", "hora": "1700-1859", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "56753", "clave": "FGMA 005", "materia": "Ingles II", "secc": "427", "dias": "LM", "hora": "0700-0859", "profesor": "ALCARAZ - BARRIOS MARISOL", "semestre": "2do Semestre"},
    {"nrc": "56845", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "RODRIGUEZ - CASTILLO KARINA", "semestre": "2do Semestre"},
    {"nrc": "56873", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "007", "dias": "LM", "hora": "1100-1259", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "2do Semestre"},
    {"nrc": "56910", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "007", "dias": "LM", "hora": "1300-1459", "profesor": "LIMA - TIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "56938", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "007", "dias": "AJ", "hora": "1100-1259", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57119", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "007", "dias": "AJ", "hora": "0900-1059", "profesor": "LUNA - PANDO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57175", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "007", "dias": "AJ", "hora": "0700-0859", "profesor": "RODRIGUEZ - MARTINEZ RICARDO ALEJANDRO", "semestre": "2do Semestre"},
    {"nrc": "56759", "clave": "FGMA 005", "materia": "Ingles II", "secc": "428", "dias": "LM", "hora": "1900-2059", "profesor": "REYES - OSORIO MARIA ISABEL", "semestre": "2do Semestre"},
    {"nrc": "57738", "clave": "PSIA 003", "materia": "Psicopatologia General", "secc": "008", "dias": "LM", "hora": "1700-1859", "profesor": "SANCHEZ - ALONSO LUIS FERNANDO", "semestre": "2do Semestre"},
    {"nrc": "57741", "clave": "PSIA 009", "materia": "Psicobiologia II", "secc": "008", "dias": "LM", "hora": "1500-1659", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "2do Semestre"},
    {"nrc": "57746", "clave": "PSIA 010", "materia": "Psi. del Desarrollo Humano II", "secc": "008", "dias": "AJ", "hora": "1300-1459", "profesor": "LIMA - TIZCARENO SILVIA CAROLINA", "semestre": "2do Semestre"},
    {"nrc": "57752", "clave": "PSIA 011", "materia": "Psicologia Cognitiva", "secc": "008", "dias": "AJ", "hora": "1500-1659", "profesor": "RAMOS - PEREZ CECILIA", "semestre": "2do Semestre"},
    {"nrc": "57761", "clave": "PSIA 019", "materia": "Teorias en Psicologia Social I", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "PEREZ - XOCHIPA MARCO POLO", "semestre": "2do Semestre"},
    {"nrc": "57766", "clave": "PSIA 020", "materia": "Psicologia y Comunicacion", "secc": "008", "dias": "AJ", "hora": "1900-2059", "profesor": "DURAN - SORIANO MARIA DEL ROSIO", "semestre": "2do Semestre"},

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

    # --- 4to SEMESTRE (BASE DE DATOS COMPLETA ACTUALIZADA SECC 001 - 008) ---
    {"nrc": "40109", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "421", "dias": "AJ", "hora": "0900-1059", "profesor": "ORTEGA-CASTILLO KARINA", "semestre": "4to Semestre"},
    {"nrc": "56915", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "4to Semestre"},
    {"nrc": "56927", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "56931", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "4to Semestre"},
    {"nrc": "57116", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "4to Semestre"},
    {"nrc": "57123", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "001", "dias": "V", "hora": "0700-1059", "profesor": "GARCIA-AGUILAR GREGORIO", "semestre": "4to Semestre"},
    {"nrc": "57129", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "CARRO-MEZA DULCE CAROLINA", "semestre": "4to Semestre"},
    
    {"nrc": "57149", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "RAMOS-PEREZ CECILIA", "semestre": "4to Semestre"},
    {"nrc": "57162", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "4to Semestre"},
    {"nrc": "57202", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "4to Semestre"},
    {"nrc": "57207", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "HUERTA-RAMIREZ FEDERICO", "semestre": "4to Semestre"},
    {"nrc": "57219", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "4to Semestre"},
    {"nrc": "57227", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "002", "dias": "AJ", "hora": "1900-2059", "profesor": "TAPIA-LOPEZ SANDRA LUCIA", "semestre": "4to Semestre"},
    {"nrc": "57252", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "422", "dias": "LM", "hora": "1900-2059", "profesor": "HERNANDEZ - CASIANO OSCAR", "semestre": "4to Semestre"},
    
    {"nrc": "57263", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "003", "dias": "LM", "hora": "0900-1059", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "4to Semestre"},
    {"nrc": "57267", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "57273", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "003", "dias": "LM", "hora": "1100-1259", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "57520", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "003", "dias": "LM", "hora": "1300-1459", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "4to Semestre"},
    {"nrc": "57522", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "003", "dias": "AJ", "hora": "1100-1259", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "4to Semestre"},
    {"nrc": "57524", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "003", "dias": "AJ", "hora": "0900-1059", "profesor": "MERCADO-CARNALLA MARIO RENATO", "semestre": "4to Semestre"},
    {"nrc": "57529", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "423", "dias": "AJ", "hora": "0700-0859", "profesor": "GONZALEZ-VALERDI YESENIA", "semestre": "4to Semestre"},
    
    {"nrc": "57537", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "004", "dias": "LM", "hora": "1700-1859", "profesor": "RAMOS-PEREZ CECILIA", "semestre": "4to Semestre"},
    {"nrc": "57539", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "GALINDO-MOTO MANUEL ALEJANDRO", "semestre": "4to Semestre"},
    {"nrc": "57542", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "004", "dias": "LM", "hora": "1900-2059", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "4to Semestre"},
    {"nrc": "57543", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "004", "dias": "LM", "hora": "1500-1659", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "4to Semestre"},
    {"nrc": "57545", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "004", "dias": "AJ", "hora": "1900-2059", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "4to Semestre"},
    {"nrc": "57549", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "004", "dias": "AJ", "hora": "1700-1859", "profesor": "TAPIA-LOPEZ SANDRA LUCIA", "semestre": "4to Semestre"},
    {"nrc": "57551", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "424", "dias": "AJ", "hora": "1500-1659", "profesor": "MARTINEZ - ARENALDE CESAR", "semestre": "4to Semestre"},
    
    {"nrc": "57555", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "005", "dias": "LM", "hora": "0900-1059", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "4to Semestre"},
    {"nrc": "57558", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "005", "dias": "LM", "hora": "1300-1459", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "4to Semestre"},
    {"nrc": "57562", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "005", "dias": "LM", "hora": "1100-1259", "profesor": "BRAMBILA - LOPEZ TERESITA", "semestre": "4to Semestre"},
    {"nrc": "57567", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "RODRIGUEZ-MARTINEZ RICARDO ALEJANDRO", "semestre": "4to Semestre"},
    {"nrc": "57569", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "005", "dias": "AJ", "hora": "1100-1259", "profesor": "MARTINEZ-MENDEZ DULCE MARIA", "semestre": "4to Semestre"},
    {"nrc": "57614", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "005", "dias": "AJ", "hora": "0900-1059", "profesor": "TLALPAN - RUIZ MARIA GUADALUPE", "semestre": "4to Semestre"},
    {"nrc": "57619", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "425", "dias": "AJ", "hora": "0700-0859", "profesor": "SERRANO-RAMIREZ ANA LUCIA", "semestre": "4to Semestre"},
    
    {"nrc": "57631", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "006", "dias": "AJ", "hora": "1900-2059", "profesor": "RAMOS - PEREZ CECILIA", "semestre": "4to Semestre"},
    {"nrc": "57639", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "006", "dias": "AJ", "hora": "1300-1459", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "4to Semestre"},
    {"nrc": "57645", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "006", "dias": "LM", "hora": "1900-2059", "profesor": "LUNA - PEREZ PERLA WENDOLINE", "semestre": "4to Semestre"},
    {"nrc": "57652", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "006", "dias": "AJ", "hora": "1700-1859", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "4to Semestre"},
    {"nrc": "57659", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "006", "dias": "LM", "hora": "1500-1659", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "4to Semestre"},
    {"nrc": "57663", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "006", "dias": "AJ", "hora": "1500-1659", "profesor": "TAPIA-LOPEZ SANDRA LUCIA", "semestre": "4to Semestre"},
    {"nrc": "57667", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "426", "dias": "LM", "hora": "1700-1859", "profesor": "HERNANDEZ - CASIANO OSCAR", "semestre": "4to Semestre"},
    
    {"nrc": "57672", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "007", "dias": "V", "hora": "0700-1059", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "4to Semestre"},
    {"nrc": "57677", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "007", "dias": "LM", "hora": "1100-1259", "profesor": "PEREZ - LIMON ROMUALDO", "semestre": "4to Semestre"},
    {"nrc": "57680", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "BRAMBILA - LOPEZ TERESITA", "semestre": "4to Semestre"},
    {"nrc": "57685", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "007", "dias": "AJ", "hora": "0700-0859", "profesor": "DEGANTE - REYES MONICA ALEJANDRA", "semestre": "4to Semestre"},
    {"nrc": "57689", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "007", "dias": "LM", "hora": "1300-1459", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "4to Semestre"},
    {"nrc": "57693", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "007", "dias": "AJ", "hora": "1100-1259", "profesor": "MERCADO-CARNALLA MARIO RENATO", "semestre": "4to Semestre"},
    {"nrc": "57696", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "427", "dias": "AJ", "hora": "0900-1059", "profesor": "SERRANO - RAMIREZ ANA LUCIA", "semestre": "4to Semestre"},
    
    {"nrc": "57699", "clave": "PSIS 017", "materia": "Pruebas de Inteligencia", "secc": "008", "dias": "AJ", "hora": "1300-1459", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "4to Semestre"},
    {"nrc": "57703", "clave": "PSIS 018", "materia": "Sexualidad", "secc": "008", "dias": "AJ", "hora": "1900-2059", "profesor": "LUNA - PEREZ PERLA WENDOLINE", "semestre": "4to Semestre"},
    {"nrc": "57706", "clave": "PSIS 019", "materia": "Fund. de la Psicoterapia", "secc": "008", "dias": "LM", "hora": "1700-1859", "profesor": "SANCHEZ-MORALES REBECA", "semestre": "4to Semestre"},
    {"nrc": "57716", "clave": "PSIS 020", "materia": "Psicologia de los Grupos", "secc": "008", "dias": "LM", "hora": "1500-1659", "profesor": "MARTINEZ-MENDEZ DULCE MARIA", "semestre": "4to Semestre"},
    {"nrc": "57722", "clave": "PSIS 021", "materia": "Inv. I: Planteamiento del Pro.", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "4to Semestre"},
    {"nrc": "57726", "clave": "PSIS 022", "materia": "Intro. a la Psi.Organizacional", "secc": "008", "dias": "AJ", "hora": "1500-1659", "profesor": "MERCADO-CARNALLA MARIO RENATO", "semestre": "4to Semestre"},
    {"nrc": "57733", "clave": "FGUS 007", "materia": "Lengua Extranjera IV", "secc": "428", "dias": "V", "hora": "1600-1959", "profesor": "DE ITA-LUNA DANIEL", "semestre": "4to Semestre"},

    # --- 5to SEMESTRE ---
    {"nrc": "57518", "clave": "PSIS 250", "materia": "Evaluacion del Desarrollo", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "5to Semestre"},
    {"nrc": "57523", "clave": "PSIS 250", "materia": "Evaluacion del Desarrollo", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "5to Semestre"},
    {"nrc": "57532", "clave": "PSIS 251", "materia": "Alteraciones del Desarrollo", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "5to Semestre"},
    {"nrc": "57540", "clave": "PSIS 252", "materia": "Psicologia y Educacion", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "DE LA OLIVA - GRANIZO DAVID", "semestre": "5to Semestre"},
    {"nrc": "57559", "clave": "PSIS 254", "materia": "Evaluacion de la Personalidad", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDE", "semestre": "5to Semestre"},
    {"nrc": "57889", "clave": "PSIS 255", "materia": "Enfoques Contempo en Psico", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "5to Semestre"},
    {"nrc": "57616", "clave": "PSIS 258", "materia": "Psicologia Institucional", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "ROMERO-HORAN MARIA GUILLERMINA", "semestre": "5to Semestre"},
    {"nrc": "57628", "clave": "PSIS 259", "materia": "Investigacion II: Disenos y En", "secc": "001", "dias": "V", "hora": "0700-1059", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "5to Semestre"},
    {"nrc": "57641", "clave": "PSIS 263", "materia": "Comportamiento Organizacional", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "CARRO-MEZA DULCE CAROLINA", "semestre": "5to Semestre"},
    {"nrc": "57670", "clave": "PSIS 263", "materia": "Comportamiento Organizacional", "secc": "003", "dias": "LM", "hora": "1100-1259", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "5to Semestre"},
    {"nrc": "57526", "clave": "PSIS 250", "materia": "Evaluacion del Desarrollo", "secc": "002", "dias": "V", "hora": "1300-1659", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "5to Semestre"},
    {"nrc": "57536", "clave": "PSIS 251", "materia": "Alteraciones del Desarrollo", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "5to Semestre"},
    {"nrc": "57553", "clave": "PSIS 252", "materia": "Psicologia y Educacion", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "5to Semestre"},
    {"nrc": "57564", "clave": "PSIS 254", "materia": "Evaluacion de la Personalidad", "secc": "002", "dias": "LM", "hora": "1100-1259", "profesor": "SANCHEZ - ALONSO LUIS FERNANDO", "semestre": "5to Semestre"},
    {"nrc": "57602", "clave": "PSIS 255", "materia": "Enfoques Contempo en Psico", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "5to Semestre"},
    {"nrc": "57622", "clave": "PSIS 258", "materia": "Psicologia Institucional", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "ROMERO-HORAN MARIA GUILLERMINA", "semestre": "5to Semestre"},
    {"nrc": "57632", "clave": "PSIS 259", "materia": "Investigacion II: Disenos y En", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "5to Semestre"},
    {"nrc": "57676", "clave": "PSIS 263", "materia": "Comportamiento Organizacional", "secc": "002", "dias": "AJ", "hora": "1900-2059", "profesor": "MORALES-REYES JOSE LUIS", "semestre": "5to Semestre"},
    {"nrc": "57681", "clave": "PSIS 258", "materia": "Psicologia Institucional", "secc": "003", "dias": "AJ", "hora": "1900-2059", "profesor": "CERVANTES - HERNANDEZ MARIA LETICIA", "semestre": "5to Semestre"},

    # --- 6to SEMESTRE ---
    {"nrc": "57686", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "BECERRA - ALLENDE JORGE FERNANDO", "semestre": "6to Semestre"},
    {"nrc": "57709", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "6to Semestre"},
    {"nrc": "57784", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "6to Semestre"},
    {"nrc": "57825", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "MENDEZ-BALBUENA IGNACIO", "semestre": "6to Semestre"},
    {"nrc": "57866", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "ARELLANO BAUTISTA CLAUDIA ANGELICA", "semestre": "6to Semestre"},
    {"nrc": "57904", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "6to Semestre"},
    {"nrc": "57960", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "PEREZ BARROSO MARLENE", "semestre": "6to Semestre"},
    {"nrc": "57691", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "002", "dias": "AJ", "hora": "1900-2059", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "6to Semestre"},
    {"nrc": "57791", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "6to Semestre"},
    {"nrc": "57832", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "ROJAS-SOLIS JOSE LUIS", "semestre": "6to Semestre"},
    {"nrc": "57871", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "DE LA ROSA - DIAZ BRENDA ELENA", "semestre": "6to Semestre"},
    {"nrc": "57914", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "ZEPEDA-ASTORGA FRANCISCO", "semestre": "6to Semestre"},
    {"nrc": "57966", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "6to Semestre"},
    {"nrc": "59844", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "SANCHEZ-MORALES REBECA", "semestre": "6to Semestre"},
    {"nrc": "57695", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "003", "dias": "LM", "hora": "0900-1059", "profesor": "BECERRA - ALLENDE JORGE FERNANDO", "semestre": "6to Semestre"},
    {"nrc": "57714", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "BRAMBILA-LOPEZ TERESITA", "semestre": "6to Semestre"},
    {"nrc": "57795", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "003", "dias": "AJ", "hora": "0700-0859", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "6to Semestre"},
    {"nrc": "57838", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "003", "dias": "LM", "hora": "1100-1259", "profesor": "MENDEZ-BALBUENA IGNACIO", "semestre": "6to Semestre"},
    {"nrc": "57879", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "003", "dias": "LM", "hora": "1300-1459", "profesor": "ARELLANO BAUTISTA CLAUDIA ANGELICA", "semestre": "6to Semestre"},
    {"nrc": "57922", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "003", "dias": "AJ", "hora": "0900-1059", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "6to Semestre"},
    {"nrc": "57972", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "003", "dias": "V", "hora": "1300-1659", "profesor": "RAMOS-PEREZ CECILIA", "semestre": "6to Semestre"},
    {"nrc": "57698", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "004", "dias": "V", "hora": "1300-1659", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "6to Semestre"},
    {"nrc": "57720", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "004", "dias": "LM", "hora": "1500-1659", "profesor": "LUNA - PEREZ PERLA WENDOLINE", "semestre": "6to Semestre"},
    {"nrc": "57842", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "004", "dias": "AJ", "hora": "1500-1659", "profesor": "ROJAS-SOLIS JOSE LUIS", "semestre": "6to Semestre"},
    {"nrc": "59847", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "004", "dias": "LM", "hora": "1900-2059", "profesor": "LARA-LOPEZ ALINE BENJAMIN", "semestre": "6to Semestre"},
    {"nrc": "57885", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "004", "dias": "AJ", "hora": "1700-1859", "profesor": "MERCADO CARNALLA MARIO RENATO", "semestre": "6to Semestre"},
    {"nrc": "57926", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "6to Semestre"},
    {"nrc": "57994", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "004", "dias": "V", "hora": "1700-2059", "profesor": "RAMOS PEREZ CECILIA", "semestre": "6to Semestre"},
    {"nrc": "57700", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "TLALPAN RUIZ MARIA GUADALUPE", "semestre": "6to Semestre"},
    {"nrc": "57725", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "005", "dias": "LM", "hora": "0900-1059", "profesor": "GALINDO-MOTO MANUEL ALEJANDRO", "semestre": "6to Semestre"},
    {"nrc": "57798", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "005", "dias": "LM", "hora": "1300-1459", "profesor": "DEGANTEREYES MONICA ALEJANDRA", "semestre": "6to Semestre"},
    {"nrc": "57847", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "005", "dias": "AJ", "hora": "1100-1259", "profesor": "ROJAS-SOLIS JOSE LUIS", "semestre": "6to Semestre"},
    {"nrc": "57887", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "005", "dias": "AJ", "hora": "0900-1059", "profesor": "ARELLANO BAUTISTA CLAUDIA ANGELICA", "semestre": "6to Semestre"},
    {"nrc": "57931", "clave": "ISPS 200", "materia": "Psicdiagnostico", "secc": "005", "dias": "AJ", "hora": "0700-0859", "profesor": "ZEPEDA-ASTORGA FRANCISCO", "semestre": "6to Semestre"},
    {"nrc": "58000", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "005", "dias": "LM", "hora": "1100-1259", "profesor": "PEREZ-BARROSO MARLENE", "semestre": "6to Semestre"},
    {"nrc": "57802", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "006", "dias": "LM", "hora": "1700-1859", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "6to Semestre"},
    {"nrc": "57854", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "006", "dias": "LM", "hora": "1500-1659", "profesor": "MENDEZ-BALBUENA IGNACIO", "semestre": "6to Semestre"},
    {"nrc": "57891", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "006", "dias": "AJ", "hora": "1300-1459", "profesor": "TAPIA - LOPEZ SANDRA LUCIA", "semestre": "6to Semestre"},
    {"nrc": "57943", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "006", "dias": "AJ", "hora": "1500-1659", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "6to Semestre"},
    {"nrc": "58007", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "006", "dias": "AJ", "hora": "1900-2059", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "6to Semestre"},
    {"nrc": "59850", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "006", "dias": "AJ", "hora": "1900-2059", "profesor": "SANCHEZ-MORALES REBECA", "semestre": "6to Semestre"},
    {"nrc": "57704", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "BENAVIDES - VALDERRABANO MARICELA", "semestre": "6to Semestre"},
    {"nrc": "59830", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "007", "dias": "L", "hora": "0700-0859", "profesor": "RIVERA TAPIA JOSE ANTONIO", "semestre": "6to Semestre"},
    {"nrc": "57810", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "007", "dias": "LM", "hora": "1300-1459", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "6to Semestre"},
    {"nrc": "57814", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "007", "dias": "LM", "hora": "1100-1259", "profesor": "GALINDO-MOTO MANUEL ALEJANDRO", "semestre": "6to Semestre"},
    {"nrc": "57893", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "007", "dias": "V", "hora": "0700-1059", "profesor": "GONZALEZ-CRUZ VICTOR GERARDO", "semestre": "6to Semestre"},
    {"nrc": "57947", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "007", "dias": "AJ", "hora": "0900-1059", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "6to Semestre"},
    {"nrc": "58015", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "007", "dias": "AJ", "hora": "1100-1259", "profesor": "DIAZ - CARDENAS ALFONSO FELIPE", "semestre": "6to Semestre"},
    {"nrc": "57707", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "008", "dias": "LM", "hora": "1500-1659", "profesor": "DEGANTE REYES MONICA ALEJANDRA", "semestre": "6to Semestre"},
    {"nrc": "57818", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "008", "dias": "AJ", "hora": "1500-1659", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "6to Semestre"},
    {"nrc": "57859", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "008", "dias": "AJ", "hora": "1300-1459", "profesor": "MARTINEZ-MENDEZ DULCE MARIA", "semestre": "6to Semestre"},
    {"nrc": "58178", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "008", "dias": "LM", "hora": "1700-1859", "profesor": "MERCADO-CARNALLA MARIO RENATO", "semestre": "6to Semestre"},
    {"nrc": "58185", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "6to Semestre"},

    # --- 7mo SEMESTRE ---
    {"nrc": "57767", "clave": "PSIS 257", "materia": "Psicoterapia de Pareja", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "STANGE-ESPINOLA ISABEL DEL ROSARIO", "semestre": "7mo Semestre"},
    {"nrc": "57772", "clave": "PSIS 262", "materia": "Investigacion IV: Analisis Cua", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "SILVARIOS CARLOS ENRIQUE", "semestre": "7mo Semestre"},
    {"nrc": "57780", "clave": "PSIS 265", "materia": "Diagnostico Organizacional", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "ARELLANO-BAUTISTA CLAUDIA ANGELICA", "semestre": "7mo Semestre"},
    {"nrc": "57787", "clave": "ISPS 203", "materia": "Psicologia Social Latinoameri", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "CERVANTES - HERNANDEZ MARIA LETICIA", "semestre": "7mo Semestre"},
    {"nrc": "57796", "clave": "ISPS 202", "materia": "Educacion Especial", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "7mo Semestre"},
    {"nrc": "57853", "clave": "ISPS 202", "materia": "Educacion Especial", "secc": "003", "dias": "LM", "hora": "1300-1459", "profesor": "DE LA OLIVA - GRANIZO DAVID", "semestre": "7mo Semestre"},
    {"nrc": "57822", "clave": "PSIS 257", "materia": "Psicoterapia de Pareja", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "ROJAS-HERNANDEZ GUADALUPE JANET", "semestre": "7mo Semestre"},
    {"nrc": "57827", "clave": "PSIS 262", "materia": "Investigacion IV: Analysis Cua", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "ROMERO RODRIGUEZ EULOGIO", "semestre": "7mo Semestre"},
    {"nrc": "57833", "clave": "PSIS 265", "materia": "Diagnostico Organizacional", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "ALVAREZ-CARRILLO PAULINA", "semestre": "7mo Semestre"},
    {"nrc": "57839", "clave": "ISPS 203", "materia": "Psicologia Social Latinoameri", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "ROMERO-RODRIGUEZ EULOGIO", "semestre": "7mo Semestre"},
    {"nrc": "57845", "clave": "ISPS 202", "materia": "Educacion Especial", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "7mo Semestre"},

    # --- 8vo SEMESTRE ---
    {"nrc": "57876", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "8vo Semestre"},
    {"nrc": "57883", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "SANCHEZ - HERNANDEZ GRACIELA", "semestre": "8vo Semestre"},
    {"nrc": "57888", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "8vo Semestre"},
    {"nrc": "57913", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "MERCADO CARNALLA MARIO RENATO", "semestre": "8vo Semestre"},
    {"nrc": "57916", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "ROMERO RODRIGUEZ EULOGIO", "semestre": "8vo Semestre"},
    {"nrc": "57920", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "AGUILAR ALVAREZ EDGAR ANDRES", "semestre": "8vo Semestre"},
    {"nrc": "57930", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "003", "dias": "AJ", "hora": "0700-0859", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN", "semestre": "8vo Semestre"},
    {"nrc": "57934", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "003", "dias": "AJ", "hora": "0900-1059", "profesor": "MORALES-JUAREZ BARTOLA", "semestre": "8vo Semestre"},
    {"nrc": "57940", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "003", "dias": "AJ", "hora": "1100-1259", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "8vo Semestre"},
    {"nrc": "57944", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "FRAGOSOLUZURIAGA ROCIO", "semestre": "8vo Semestre"},
    {"nrc": "57949", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "004", "dias": "AJ", "hora": "1700-1859", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "8vo Semestre"},
    {"nrc": "57954", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "004", "dias": "AJ", "hora": "1900-2059", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "8vo Semestre"},
    {"nrc": "57968", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "005", "dias": "LM", "hora": "0900-1059", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "8vo Semestre"},
    {"nrc": "57975", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "005", "dias": "LM", "hora": "1100-1259", "profesor": "SANCHEZ-HERNANDEZ GRACIELA", "semestre": "8vo Semestre"},
    {"nrc": "57982", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "GALINDO-MOTO MANUEL ALEJANDRO", "semestre": "8vo Semestre"},
    {"nrc": "57992", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "006", "dias": "LM", "hora": "1700-1859", "profesor": "LUNA-PANDO LUIS FERNANDO", "semestre": "8vo Semestre"},
    {"nrc": "57998", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "006", "hora": "1500-1659", "profesor": "ROMERO RODRIGUEZ EULOGIO", "semestre": "8vo Semestre"},
    {"nrc": "58004", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "006", "dias": "AJ", "hora": "1900-2059", "profesor": "AGUILAR ALVAREZ EDGAR ANDRES", "semestre": "8vo Semestre"},
    {"nrc": "58009", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "007", "dias": "AJ", "hora": "0900-1059", "profesor": "FRAGOSOLUZURIAGA ROCIO", "semestre": "8vo Semestre"},
    {"nrc": "58025", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "007", "dias": "LM", "hora": "1300-1459", "profesor": "ROMERO RODRIGUEZ EULOGIO", "semestre": "8vo Semestre"},
    {"nrc": "58033", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "007", "dias": "AJ", "hora": "1100-1259", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "8vo Semestre"},
    {"nrc": "58045", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "008", "dias": "AJ", "hora": "1900-2059", "profesor": "MERCADO CARNALLA MARIO RENATO", "semestre": "8vo Semestre"},
    {"nrc": "58059", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "LARA-LOPEZ ALINE BENJAMIN", "semestre": "8vo Semestre"},
    {"nrc": "58067", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "008", "dias": "AJ", "hora": "1500-1659", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "8vo Semestre"},

    # --- 9no SEMESTRE ---
    {"nrc": "58206", "clave": "ISPS 208", "materia": "Intervencion en Crisis", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "9no Semestre"},
    {"nrc": "58207", "clave": "ISPS 209", "materia": "Psicoterapia Grupal", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "9no Semestre"},
    {"nrc": "59425", "clave": "ISPS 207", "materia": "Estrategias de inter en psi org", "secc": "004", "dias": "LM", "hora": "0900-1029", "profesor": "ARELLANO BAUTISTA CLAUDIA ANGELICA", "semestre": "9no Semestre"},
    {"nrc": "58204", "clave": "ISPS 206", "materia": "Estrategias de inter en psi ed", "secc": "001", "dias": "AJ", "hora": "0900-1029", "profesor": "COYOTECATL FABIAN FRANCISCA", "semestre": "9no Semestre"},

    # --- 10mo SEMESTRE ---
    {"nrc": "58255", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "GONZALEZ - CRUZ VICTOR GERARDO", "semestre": "10mo Semestre"},
    {"nrc": "58643", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "CARRO-MEZA DULCE CAROLINA", "semestre": "10mo Semestre"},
    {"nrc": "58714", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "003", "dias": "AJ", "hora": "1700-1859", "profesor": "GONZALEZ-CRUZ VICTOR GERARDO", "semestre": "10mo Semestre"},
    {"nrc": "59139", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "10mo Semestre"},
    {"nrc": "59156", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN", "semestre": "10mo Semestre"},
    {"nrc": "57809", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "006", "dias": "LM", "hora": "1300-1459", "profesor": "MERCADO CARNALLA MARIO RENATO", "semestre": "10mo Semestre"},
    {"nrc": "57864", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "10mo Semestre"},
    {"nrc": "57889", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "ALVAREZ-CARRILLO PAULINA", "semestre": "10mo Semestre"},
    {"nrc": "58249", "clave": "ISPS 210", "materia": "Estrategias de inte en psi cli", "secc": "001", "dias": "AJ", "hora": "1300-1429", "profesor": "RODRIGUEZ CASTILLO KARINA", "semestre": "10mo Semestre"},
    {"nrc": "58442", "clave": "ISPS 211", "materia": "Estrategias de inte en psi soc", "secc": "001", "dias": "AJ", "hora": "0700-0829", "profesor": "LARA LOPEZ ALINE BENJAMIN", "semestre": "10mo Semestre"}
]

# =========================================================================
# 🔗 MAPA DE PREREQUISITOS (clave_materia -> lista de claves prerequisito)
# =========================================================================
# Cada entrada indica: para cursar la materia CLAVE, se necesitan las CLAVES listadas.
PREREQUISITOS = {
    # 2do semestre
    "PSIA 003": [],   # Psicopatologia General - S/R (segun mapa, Teorias Personalidad implicita)
    "PSIA 009": [],   # Psicobiologia II - S/R prerequisito formal
    "PSIA 010": ["PSIA 008"],  # Psi Desarrollo Humano II <- Psi Desarrollo Humano I
    "PSIA 011": [],   # Psicologia Cognitiva - S/R
    "PSIA 019": ["PSIA 017"],  # Teorias Psi Social I <- Epistemologia y Psicologia
    "PSIA 020": ["PSIA 018", "PSIA 017"],  # Psicologia y Comunicacion <- Taller Lec + Epistemologia
    # 3er semestre
    "PSIS 012": ["PSIA 009", "PSIA 010"],  # Teorias del Aprendizaje <- Psicobiologia II + DesHumano II
    "PSIS 013": ["PSIA 010", "PSIA 008"],  # Psi Desarrollo Humano III <- DesHumano II + (I implicito)
    "PSIS 014": [],                         # Psicopatologia Interaccional - S/R
    "PSIS 015": ["PSIA 004", "PSIA 020"],  # Teorias Sistemas Ciber <- Historia+Paradigmas + Psi y Com
    "PSIS 016": ["PSIA 017", "PSIA 019"],  # Teorias Psi Social II <- Epistemologia + T.Psi.Social I
    # 4to semestre
    "PSIS 017": [],                         # Pruebas de Inteligencia - S/R (prerequisito de 3er)
    "PSIS 018": [],                         # Sexualidad - S/R
    "PSIS 019": ["PSIA 001"],              # Fundamentos de la Psicoterapia <- Teorias Personalidad
    "PSIS 020": ["PSIS 016"],              # Psicologia de los Grupos <- Teorias Psi Social II
    "PSIS 021": ["PSIA 017", "PSIA 018"],  # Inv I: Planteamiento <- Epistemologia + Taller Lec
    "PSIS 022": ["PSIA 017", "PSIS 016"],  # Intro Psi Organizacional <- Epistemologia + T.Psi.Social II
    # 5to semestre
    "PSIS 250": ["PSIS 013", "PSIA 009", "PSIS 017"],  # Evaluacion del Desarrollo <- DesHum III + PsicoBio II + Pruebas Intel
    "PSIS 251": ["PSIA 009", "PSIS 013", "PSIS 012"],  # Alteraciones del Desarrollo <- PsicoBio II + DesHum III + T.Aprendizaje
    "PSIS 252": ["PSIS 012"],              # Psicologia y Educacion <- Teorias del Aprendizaje
    "PSIS 254": ["PSIA 001", "PSIS 017", "PSIS 019"],  # Evaluacion Personalidad <- T.Personalidad + Pruebas Intel + Fund.Psicoterapia
    "PSIS 255": ["PSIS 019"],              # Enfoques Contemporaneos <- Fund. Psicoterapia
    "PSIS 258": ["PSIS 016", "PSIS 020"],  # Psicologia Institucional <- T.Psi.Social II + Psi Grupos
    "PSIS 259": ["PSIS 021"],              # Inv II: Diseños y Enfoques <- Inv I
    "PSIS 263": ["PSIS 022", "PSIA 001", "PSIA 020", "PSIS 020"],  # Comportamiento Org <- IntroOrg + T.Personal + PsiCom + PsiGrupos
    # 6to semestre
    "PSIS 253": ["PSIA 009", "PSIS 013"],  # Psicopedagogia <- PsicoBio II + DesHum III (+ PsicoBio I implicito)
    "PSIS 256": ["PSIA 001", "PSIS 019"],  # Psicoterapia Individual <- T.Personalidad + Fund.Psicoterapia
    "PSIS 260": ["PSIS 016", "PSIS 259"],  # Psi de las Actitudes <- T.Psi.Social II + Inv II
    "PSIS 261": ["PSIS 259"],              # Inv III: Analisis Cuantitativos <- Inv II
    "PSIS 264": ["PSIS 263", "PSIS 254", "PSIS 017", "PSIS 258"],  # Aprovisionamiento RH <- ComportOrg + EvalPersonalidad + Pruebas + PsiInstit
    "ISPS 200": ["PSIS 017", "PSIS 254", "PSIS 251", "PSIS 250"],  # Psicodiagnostico <- Pruebas + EvalPersonalidad + Alteraciones + EvalDesarrollo
    "ISPS 201": ["PSIS 013", "PSIS 012", "PSIS 017"],  # Psicologia Cognitiva (ISPS) <- DesHum III + T.Aprendizaje + Pruebas Intel
    # 7mo semestre
    "PSIS 257": ["PSIS 019", "PSIS 256"],  # Psicoterapia de Pareja <- Fund.Psicoterapia + Psi Individual
    "PSIS 262": ["PSIS 261"],              # Inv IV: Analisis Cualitativos <- Inv III
    "PSIS 265": ["PSIS 263"],              # Diagnostico Organizacional <- Comportamiento Org
    "ISPS 203": ["PSIS 016"],              # Psi Social Latinoamericana <- T.Psi.Social II
    "ISPS 202": ["PSIS 013", "PSIS 251", "PSIS 252"],  # Educacion Especial <- DesHum III + Alteraciones + Psi y Educacion
    # 8vo semestre
    "PSIS 266": ["PSIS 263"],              # Capacitacion <- Comportamiento Org
    "ISPS 205": ["PSIS 258", "PSIS 262", "ISPS 203"],  # Psi Comunitaria <- PsiInstit + Inv IV + PsiSocLatino
    "ISPS 204": ["PSIS 014", "PSIS 255", "PSIS 257"],  # Terapia Familiar <- PsicopatInteracc + EnfoquesContemp + PsiTerapiaPar
    # 9no semestre
    "ISPS 208": ["PSIS 019", "PSIS 256", "PSIS 257"],  # Intervencion en Crisis <- Fund.Psi + PsiIndiv + PsiPareja
    "ISPS 209": ["PSIS 019", "PSIS 256"],  # Psicoterapia Grupal <- Fund.Psi + PsiIndiv
    "ISPS 206": ["PSIS 252", "PSIS 253"],  # Estrategias Psi Educativa <- PsiEducacion + Psicopedagogia
    "ISPS 207": ["PSIS 266"],              # Estrategias Psi Organizacional <- Capacitacion
    # 10mo semestre
    "ISPS 212": ["ISPS 207"],              # Desarrollo Organizacional <- Estrategias PsiOrg
    "ISPS 210": ["PSIS 019", "PSIS 256", "PSIS 257", "ISPS 204", "ISPS 209"],  # Estrategias Psi Clinica
    "ISPS 211": ["ISPS 205", "PSIS 262"],  # Estrategias Psi Social <- PsiComunitaria + Inv IV
}

# Función para obtener todas las materias bloqueadas dado un conjunto de materias atrasadas
def get_materias_bloqueadas(claves_atrasadas):
    """Dado un set de claves atrasadas, retorna todas las claves que NO se pueden cursar."""
    bloqueadas = set()
    for clave_materia, prereqs in PREREQUISITOS.items():
        if any(p in claves_atrasadas for p in prereqs):
            bloqueadas.add(clave_materia)
    return bloqueadas

# =========================================================================
# 🧬 CATÁLOGO DE OPTATIVAS
# =========================================================================
OPTATIVAS_POR_AREA = {
    "Clinica": [
        {"nrc": "58248", "clave": "PSIS 609", "materia": "Prev. e Interv. en Adicciones", "secc": "001", "dias": "LM", "hora": "1100-1229", "profesor": "RODRIGUEZ CASTILLO KARINA"},
        {"nrc": "58434", "clave": "PSIS 609", "materia": "Prev. e Interv. en Adicciones", "secc": "003", "dias": "V", "hora": "1300-1559", "profesor": "VELASCO VALLEJO MARIA DEL ROSARIO"},
        {"nrc": "58250", "clave": "PSIS 611", "materia": "Terapia Breve", "secc": "002", "dias": "AJ", "hora": "1100-1229", "profesor": "STANGE ESPINOLA ISABEL DEL ROSARIO"},
        {"nrc": "58253", "clave": "PSIS 614", "materia": "Violencia Intrafamiliar", "secc": "001", "dias": "AJ", "hora": "1700-1829", "profesor": "RODRIGUEZ CASTILLO KARINA"},
        {"nrc": "58435", "clave": "PSIS 614", "materia": "Violencia Intrafamiliar", "secc": "002", "dias": "LM", "hora": "0700-0829", "profesor": "VELASCO-VALLEJO MARIA DEL ROSARIO"},
        {"nrc": "58492", "clave": "PSIS 614", "materia": "Violencia Intrafamiliar", "secc": "003", "dias": "V", "hora": "1000-1259", "profesor": "RODRIGUEZ CASTILLO KARINA"},
        {"nrc": "58254", "clave": "PSIS 612", "materia": "Terapia Cognitivo Conductual", "secc": "002", "dias": "AJ", "hora": "1500-1629", "profesor": "RODRIGUEZ CASTILLO KARINA"},
        {"nrc": "59836", "clave": "PSIS 612", "materia": "Terapia Cognitivo Conductual", "secc": "003", "dias": "LM", "hora": "1700-1829", "profesor": "AGUILAR ALVAREZ EDGAR ANDRES"},
        {"nrc": "58257", "clave": "PSIS 613", "materia": "Terapia Psicoanalitica", "secc": "001", "dias": "A", "hora": "1300-1429", "profesor": "VEGA SIMONT EDMUNDO"},
        {"nrc": "58437", "clave": "PSIS 613", "materia": "Terapia Psicoanalitica", "secc": "002", "dias": "A", "hora": "0900-1029", "profesor": "VEGA SIMONT EDMUNDO"},
        {"nrc": "58438", "clave": "PSIS 613", "materia": "Terapia Psicoanalitica", "secc": "003", "dias": "AJ", "hora": "1100-1229", "profesor": "VEGASIMONT EDMUNDO"},
        {"nrc": "58499", "clave": "PSIS 608", "materia": "Mod Sist Ciber en Psicoterapia", "secc": "003", "dias": "V", "hora": "1300-1559", "profesor": "GALINDO MOTO MANUEL ALEJANDRO"}
    ],
    "Social": [
        {"nrc": "58439", "clave": "PSIS 620", "materia": "Psicologia Social de las Masas", "secc": "001", "dias": "LM", "hora": "1500-1629", "profesor": "CHAVEZ GONZALEZ ERIKA"},
        {"nrc": "59873", "clave": "PSIS 620", "materia": "Psicologia Social de las Masas", "secc": "002", "dias": "AJ", "hora": "1500-1629", "profesor": "LARA - LOPEZ ALINE BENJAMIN"},
        {"nrc": "59879", "clave": "PSIS 620", "materia": "Psicologia Social de las Masas", "secc": "003", "dias": "A", "hora": "1300-1429", "profesor": "LARA LOPEZ ALINE BENJAMIN"},
        {"nrc": "58444", "clave": "PSIS 615", "materia": "Perspectiva de Genero y Psi", "secc": "001", "dias": "AJ", "hora": "1100-1229", "profesor": "SANCHEZ HERNANDEZ GRACIELA"},
        {"nrc": "58452", "clave": "PSIS 616", "materia": "Perspectivas Medioambientales", "secc": "001", "dias": "LM", "hora": "1100-1229", "profesor": "ROMEROHORAN MARIA GUILLERMINA"},
        {"nrc": "58561", "clave": "PSIS 616", "materia": "Perspectivas Medioambientales", "secc": "002", "dias": "LM", "hora": "1300-1429", "profesor": "ROMEROHORAN MARIA GUILLERMINA"},
        {"nrc": "58565", "clave": "PSIS 617", "materia": "Psicologia Politica", "secc": "002", "dias": "LM", "hora": "0700-0829", "profesor": "MEZA FLORES ABIGAIL"},
        {"nrc": "58571", "clave": "PSIS 618", "materia": "Psicologia Social de la Educ.", "secc": "002", "dias": "LM", "hora": "1100-1229", "profesor": "RODRIGUEZ MARTINEZ RICARDO ALEJANDRO"},
        {"nrc": "58604", "clave": "PSIS 619", "materia": "Psicologia Social de la Salud", "secc": "002", "dias": "AJ", "hora": "0900-1029", "profesor": "SANCHEZ HERNANDEZ GRACIELA"},
        {"nrc": "58615", "clave": "PSIS 621", "materia": "Psicología Soc de las Minorias", "secc": "002", "dias": "AJ", "hora": "0900-1029", "profesor": "RODRIGUEZ MARTINEZ RICARDO ALEJANDRO"},
        {"nrc": "58931", "clave": "PSIS 802", "materia": "Taller Titulacion por Tesina", "secc": "001", "dias": "LM", "hora": "1100-1229", "profesor": "SANCHEZ-CID JOSE ELIAS"},
        {"nrc": "58942", "clave": "PSIS 802", "materia": "Taller Titulacion por Tesina", "secc": "002", "dias": "LM", "hora": "1700-1829", "profesor": "SANCHEZ CID JOSE ELIAS"},
        {"nrc": "58957", "clave": "PSIS 800", "materia": "Seminario de Tesis", "secc": "001", "dias": "AJ", "hora": "0900-1029", "profesor": "SOLOVIEVA - YULIA"},
        {"nrc": "58963", "clave": "PSIS 800", "materia": "Seminario de Tesis", "secc": "002", "dias": "AJ", "hora": "1100-1229", "profesor": "SOLOVIEVA-. YULIA"}
    ],
    "Organizacional": [
        {"nrc": "58581", "clave": "PSIS 622", "materia": "Calidad Org. e ISO 14000", "secc": "001", "dias": "LM", "hora": "0900-1029", "profesor": "CARRO-MEZA DULCE CAROLINA"},
        {"nrc": "58595", "clave": "PSIS 622", "materia": "Calidad Org. e ISO 14000", "secc": "002", "dias": "LM", "hora": "1100-1229", "profesor": "CARRO MEZA DULCE CAROLINA"},
        {"nrc": "58649", "clave": "PSIS 626", "materia": "Liderazgo en las Organizacion", "secc": "001", "dias": "AJ", "hora": "1100-1229", "profesor": "MOTO MARTINEZ TERESA LEDOΙΝΑ"},
        {"nrc": "58705", "clave": "PSIS 626", "materia": "Liderazgo en las Organizacion", "secc": "002", "dias": "LM", "hora": "1300-1429", "profesor": "ALVAREZ CARRILLO PAULINA"},
        {"nrc": "58905", "clave": "PSIS 626", "materia": "Liderazgo en las Organizacion", "secc": "003", "dias": "LM", "hora": "1100-1229", "profesor": "ALVAREZ CARRILLO PAULINA"},
        {"nrc": "58662", "clave": "PSIS 627", "materia": "Psicologia del Consumidor", "secc": "001", "dias": "LM", "hora": "1500-1629", "profesor": "FRAGOSOLUZURIAGA ROCIO"},
        {"nrc": "58912", "clave": "PSIS 627", "materia": "Psicologia del Consumidor", "secc": "002", "dias": "LM", "hora": "1700-1829", "profesor": "FRAGOSOLUZURIAGA ROCIO"},
        {"nrc": "58679", "clave": "PSIS 624", "materia": "Ergonomia, Higiene y Seg. Org.", "secc": "002", "dias": "LM", "hora": "1100-1229", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN"},
        {"nrc": "58968", "clave": "PSIS 624", "materia": "Ergonomia, Higiene y Seg. Org.", "secc": "003", "dias": "LM", "hora": "0900-1029", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN"},
        {"nrc": "58689", "clave": "PSIS 625", "materia": "Estres y Salud en las Organi..", "secc": "002", "dias": "AJ", "hora": "1100-1229", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN"}
    ],
    "Educativa": [
        {"nrc": "58202", "clave": "PSIS 600", "materia": "Educacion Inclusiva", "secc": "001", "dias": "AJ", "hora": "1100-1229", "profesor": "DE LA OLIVA - GRANIZO DAVID"},
        {"nrc": "58237", "clave": "PSIS 600", "materia": "Educacion Inclusiva", "secc": "003", "dias": "AJ", "hora": "1100-1229", "profesor": "LIMATIZCARENO SILVIA CAROLINA"},
        {"nrc": "58203", "clave": "PSIS 601", "materia": "Educacion No Formal", "secc": "001", "dias": "LM", "hora": "0900-1029", "profesor": "TLALPAN-RUIZ MARIA GUADALUPE"},
        {"nrc": "58239", "clave": "PSIS 601", "materia": "Educacion No Formal", "secc": "003", "dias": "A", "hora": "1100-1229", "profesor": "TLALPAN-RUIZ MARIA GUADALUPE"},
        {"nrc": "58205", "clave": "PSIS 602", "materia": "Modeliz de Procesos Cognitivos", "secc": "001", "dias": "AJ", "hora": "1300-1429", "profesor": "DIAZ-CARDENAS ALFONSO FELIPE"},
        {"nrc": "58210", "clave": "PSIS 605", "materia": "Orientacion Familiar en Ed.", "secc": "001", "dias": "AJ", "hora": "1100-1229", "profesor": "DEGANTE REYES MONICA ALEJANDRA"},
        {"nrc": "59868", "clave": "PSIS 605", "materia": "Orientacion Familiar en Ed.", "secc": "003", "dias": "LM", "hora": "1300-1429", "profesor": "SANCHEZ MORALES REBECA"},
        {"nrc": "58218", "clave": "PSIS 606", "materia": "Procesos de Adq y Dilo de la L", "secc": "001", "dias": "A", "hora": "1300-1429", "profesor": "SANCHEZ-CID JOSE ELIAS"},
        {"nrc": "58432", "clave": "PSIS 606", "materia": "Procesos de Adq y Dilo de la L", "secc": "003", "dias": "AJ", "hora": "0900-1029", "profesor": "DIAZ-CARDENAS ALFONSO FELIPE"},
        {"nrc": "58222", "clave": "PSIS 603", "materia": "Neuropsicologia", "secc": "001", "dias": "AJ", "hora": "0900-1029", "profesor": "BONILLA SANCHEZ MARIA DEL ROSARIO"},
        {"nrc": "58233", "clave": "PSIS 603", "materia": "Neuropsicologia", "secc": "002", "dias": "AJ", "hora": "1500-1629", "profesor": "OREA HERNANDEZ RICARDO ENRIQUE"},
        {"nrc": "58241", "clave": "PSIS 603", "materia": "Neuropsicologia", "secc": "003", "dias": "LM", "hora": "1700-1829", "profesor": "OREA HERNANDEZ RICARDO ENRIQUE"},
        {"nrc": "58226", "clave": "PSIS 607", "materia": "Psicologia y Creatividad", "secc": "001", "dias": "LM", "hora": "1100-1229", "profesor": "DEGANTEREYES MONICA ALEJANDRA"},
        {"nrc": "58231", "clave": "PSIS 607", "materia": "Psicologia y Creatividad", "secc": "002", "dias": "LM", "hora": "0900-1029", "profesor": "DEGANTE - REYES MONICA ALEJANDRA"},
        {"nrc": "58262", "clave": "PSIS 607", "materia": "Psicologia y Creatividad", "secc": "003", "dias": "V", "hora": "1000-1259", "profesor": "VELASCO VALLEJO MARIA DEL ROSARIO"},
        {"nrc": "58245", "clave": "PSIS 604", "materia": "Orientacion Educativa", "secc": "001", "dias": "AJ", "hora": "0900-1029", "profesor": "COYOTECATL FABIAN FRANCISCA"}
    ]
}

# =========================================================================
# ⚙️ MOTOR ALGORÍTMICO Y LÓGICA DE CONTROL DE INTERVALOS ESTRICTOS
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

def entra_en_rango_permitido(materia, lm_lims, aj_lims, v_lims, omitir_viernes):
    if 'hora' not in materia or not materia['hora']: return False
    ini_mat, fin_mat = parse_hora(materia['hora'])
    dias = materia['dias']
    
    if 'L' in dias or 'M' in dias:
        if ini_mat < lm_lims[0] or fin_mat > lm_lims[1]: return False
            
    if 'A' in dias or 'J' in dias:
        if ini_mat < aj_lims[0] or fin_mat > aj_lims[1]: return False
            
    if 'V' in dias:
        if omitir_viernes: return False
        if ini_mat < v_lims[0] or fin_mat > v_lims[1]: return False
            
    return True

def coincide_profesor(nombre_ingresado, nombre_catalogo):
    tokens = nombre_ingresado.lower().replace('-', ' ').split()
    catalogo_limpio = nombre_catalogo.lower().replace('-', ' ')
    if not tokens: return False
    return all(t in catalogo_limpio for t in tokens)

def generar_horario_estricto(lista_materias, optativas_seleccionadas, profesores_prioritarios, lm_lims, aj_lims, v_lims, omitir_viernes, max_intentos=5000):
    materias_unicas = {}
    nombres_materias = {}
    for m in lista_materias:
        clave = m['clave']
        nombres_materias[clave] = m['materia']
        if clave not in materias_unicas: materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    prioridades = [p.strip() for p in profesores_prioritarios if p.strip()]
    materias_omitidas, omitidas_prof_unico, omitidas_por_viernes = [], [], []
    materias_filtradas = {}
    
    for clave, opciones in materias_unicas.items():
        opciones_con_profesor = [op for op in opciones if any(coincide_profesor(p_p, op['profesor']) for p_p in prioridades)]
        usuario_pidio_profesor = len(opciones_con_profesor) > 0
        opciones_a_evaluar = opciones_con_profesor if usuario_pidio_profesor else opciones
        
        opciones_validas = [op for op in opciones_a_evaluar if entra_en_rango_permitido(op, lm_lims, aj_lims, v_lims, omitir_viernes)]
        
        if opciones_validas:
            materias_filtradas[clave] = opciones_validas
        else:
            es_unico_profesor = len(set(op['profesor'] for op in opciones)) == 1
            tiene_viernes = any('V' in op['dias'] for op in opciones_a_evaluar)
            
            if omitir_viernes and tiene_viernes and not any('V' not in op['dias'] for op in opciones_a_evaluar):
                omitidas_por_viernes.append(nombres_materias[clave])
            elif usuario_pidio_profesor or es_unico_profesor:
                omitidas_prof_unico.append(nombres_materias[clave])
            else:
                materias_omitidas.append(nombres_materias[clave])

    optativas_filtradas = {}
    for clave_opt, opciones_opt in optativas_seleccionadas.items():
        opciones_con_profesor = [op for op in opciones_opt if any(coincide_profesor(p_p, op['profesor']) for p_p in prioridades)]
        opciones_a_evaluar = opciones_con_profesor if opciones_con_profesor else opciones_opt

        opciones_validas = [op for op in opciones_a_evaluar if entra_en_rango_permitido(op, lm_lims, aj_lims, v_lims, omitir_viernes)]
        if opciones_validas:
            optativas_filtradas[clave_opt] = opciones_validas
        else:
            materias_omitidas.append(opciones_opt[0]['materia'])

    if not materias_filtradas and not optativas_filtradas and omitidas_por_viernes:
        return [], True, materias_omitidas, omitidas_prof_unico, omitidas_por_viernes, ""

    if not materias_filtradas and not optativas_filtradas:
        return None, False, materias_omitidas, omitidas_prof_unico, omitidas_por_viernes, "Las restricciones de los Horarios de Referencia eliminaron todas las opciones disponibles."

    for _ in range(max_intentos):
        calendario_propuesto, conflicto = [], False
        
        for clave, opciones in materias_filtradas.items():
            seleccion = random.choice(opciones)
            if any(hay_sobreposicion(seleccion, m_g) for m_g in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(seleccion)
            
        if conflicto: continue

        for clave_opt, opciones_opt in optativas_filtradas.items():
            seleccion_opt = random.choice(opciones_opt)
            if any(hay_sobreposicion(seleccion_opt, m_g) for m_g in calendario_propuesto):
                conflicto = True; break
            calendario_propuesto.append(seleccion_opt)

        if not conflicto and len(calendario_propuesto) == (len(materias_filtradas) + len(optativas_filtradas)):
            prioridad_completa = True
            for p_p in prioridades:
                existe_en_filtro = any(coincide_profesor(p_p, op['profesor']) for opciones in materias_filtradas.values() for op in opciones) or any(coincide_profesor(p_p, op['profesor']) for opciones in optativas_filtradas.values() for op in opciones)
                if existe_en_filtro and not any(coincide_profesor(p_p, m['profesor']) for m in calendario_propuesto):
                    prioridad_completa = False; break
            return calendario_propuesto, prioridad_completa, materias_omitidas, omitidas_prof_unico, omitidas_por_viernes, ""

    return None, False, materias_omitidas, omitidas_prof_unico, omitidas_por_viernes, "No se encontró una combinación válida sin traslapes dentro de las horas de referencia."

# --- CONFIGURACIÓN DE STREAMLIT ---
st.set_page_config(page_title="Generador de Horarios Oficial", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🛠️ Filtros de Control")

st.sidebar.subheader("Periodo Académico")
semestre_seleccionado = st.sidebar.selectbox(
    "Selecciona tu semestre activo:",
    ["1er Semestre", "2do Semestre", "3er Semestre", "4to Semestre", "5to Semestre", "6to Semestre", "7mo Semestre", "8vo Semestre", "9no Semestre", "10mo Semestre"],
    index=3  # Posición del 4to Semestre por comodidad en esta prueba
)

st.sidebar.markdown("---")
st.sidebar.subheader("⏱️ Horario de Referencia")
st.sidebar.markdown("<small style='color: gray; display:block; margin-bottom: 10px;'>Establece los rangos permitidos para tus clases.</small>", unsafe_allow_html=True)

horas_visibles = {
    700: "07:00 AM", 829: "08:29 AM", 830: "08:30 AM", 900: "09:00 AM", 1029: "10:29 AM", 1030: "10:30 AM",
    1100: "11:00 AM", 1229: "12:29 PM", 1259: "12:59 PM", 1300: "01:00 PM", 
    1429: "02:29 PM", 1459: "02:59 PM", 1500: "03:00 PM", 1600: "04:00 PM", 1629: "04:29 PM", 
    1659: "04:59 PM", 1700: "05:00 PM", 1829: "06:29 PM", 1859: "06:59 PM", 
    1900: "07:00 PM", 1959: "07:59 PM", 2059: "08:59 PM", 2100: "09:00 PM"
}
valores_horas = sorted(list(horas_visibles.keys()))

st.sidebar.markdown("**Lunes y Miércoles**")
lm_rango = st.sidebar.select_slider(
    "Límites LM:", options=valores_horas, value=(700, 2100),
    format_func=lambda x: horas_visibles[x], key="slider_lm"
)

st.sidebar.markdown("**Martes y Jueves**")
aj_rango = st.sidebar.select_slider(
    "Límites MA/JU:", options=valores_horas, value=(700, 2100),
    format_func=lambda x: horas_visibles[x], key="slider_aj"
)

st.sidebar.markdown("**Viernes**")
omitir_viernes = st.sidebar.checkbox("Omitir completamente el viernes", value=False)

if omitir_viernes:
    st.sidebar.caption("🚫 Clases en viernes desactivadas.")
    v_rango = (700, 2100)
else:
    v_rango = st.sidebar.select_slider(
        "Límites Viernes:", options=valores_horas, value=(700, 2100),
        format_func=lambda x: horas_visibles[x], key="slider_v"
    )

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Ej. LUNA-PEREZ")
    if pref_name.strip(): profesores_inputs.append(pref_name.strip())

st.sidebar.markdown("---")
optativas_expander = st.sidebar.expander("✨ Selección de Optativas", expanded=False)
optativas_seleccionadas_usuario = {}

with optativas_expander:
    for area, materias in OPTATIVAS_POR_AREA.items():
        st.markdown(f"**Área {area}**")
        materias_unicas_nombre = {}
        for m in materias:
            if m['materia'] not in materias_unicas_nombre:
                materias_unicas_nombre[m['materia']] = []
            materias_unicas_nombre[m['materia']].append(m)
            
        for nom_materia, opciones in materias_unicas_nombre.items():
            marcado = st.checkbox(nom_materia, key=f"opt_{opciones[0]['clave']}_{area}")
            if marcado:
                optativas_seleccionadas_usuario[opciones[0]['clave']] = opciones

# =========================================================================
# 📛 MATERIAS ATRASADAS
# =========================================================================
st.sidebar.markdown("---")
atrasadas_expander = st.sidebar.expander("⚠️ Materias Atrasadas", expanded=False)

claves_atrasadas = set()
nombres_atrasadas = []
materias_atrasadas_a_incluir = []   # lista de dicts con la sección elegida para incluir en el horario

SEMESTRES_ORDENADOS = [
    "1er Semestre", "2do Semestre", "3er Semestre", "4to Semestre",
    "5to Semestre", "6to Semestre", "7mo Semestre", "8vo Semestre",
    "9no Semestre", "10mo Semestre"
]

with atrasadas_expander:
    st.markdown(
        "<small style='color:#e57373;'>Selecciona las materias que tienes atrasadas. "
        "Se eliminarán las materias del semestre activo que las necesiten como prerequisito "
        "y podrás elegir el horario y profesor para cursarlas ahora.</small>",
        unsafe_allow_html=True
    )

    idx_actual = SEMESTRES_ORDENADOS.index(semestre_seleccionado) if semestre_seleccionado in SEMESTRES_ORDENADOS else len(SEMESTRES_ORDENADOS)
    semestres_previos = SEMESTRES_ORDENADOS[:idx_actual]

    if not semestres_previos:
        st.caption("Estás en 1er semestre, no hay materias previas posibles.")
    else:
        sem_atr = st.selectbox(
            "Semestre de la materia atrasada:",
            semestres_previos,
            key="sem_atrasada_sel"
        )

        # Materias únicas de ese semestre
        materias_del_sem = {}
        for m in CATALOGO_MATERIAS:
            if m['semestre'] == sem_atr:
                if m['clave'] not in materias_del_sem:
                    materias_del_sem[m['clave']] = m['materia']

        if materias_del_sem:
            opciones_display = {f"{nombre} ({clave})": clave for clave, nombre in materias_del_sem.items()}
            seleccionadas_display = st.multiselect(
                "Materia(s) atrasada(s):",
                options=list(opciones_display.keys()),
                key="materias_atrasadas_ms"
            )

            for disp in seleccionadas_display:
                clave_atr = opciones_display[disp]
                claves_atrasadas.add(clave_atr)
                nombres_atrasadas.append(disp)

                # Obtener todas las secciones disponibles para esta materia
                secciones_disponibles = [
                    m for m in CATALOGO_MATERIAS
                    if m['clave'] == clave_atr and m['semestre'] == sem_atr
                ]

                if secciones_disponibles:
                    st.markdown(f"**📌 Configurar: {materias_del_sem[clave_atr]}**")

                    # Obtener profesores únicos para filtrar
                    profesores_unicos = sorted(list({
                        m['profesor'] for m in secciones_disponibles if m['profesor'].strip()
                    }))

                    prof_elegido = st.selectbox(
                        f"Profesor preferente:",
                        ["(Cualquiera)"] + profesores_unicos,
                        key=f"prof_atr_{clave_atr}"
                    )

                    # Filtrar secciones según profesor elegido
                    if prof_elegido == "(Cualquiera)":
                        secciones_filtradas = secciones_disponibles
                    else:
                        secciones_filtradas = [
                            m for m in secciones_disponibles if m['profesor'] == prof_elegido
                        ]
                        if not secciones_filtradas:
                            secciones_filtradas = secciones_disponibles

                    # Armar opciones de horario con label legible
                    def label_seccion(m):
                        dias_label = m['dias'].replace('L','Lun').replace('M','Mié').replace('A','Mar').replace('J','Jue').replace('V','Vie')
                        hora_fmt = m['hora']
                        return f"Secc {m['secc']} | {dias_label} {hora_fmt} | {m['profesor']}"

                    opciones_horario = {label_seccion(m): m for m in secciones_filtradas}

                    horario_elegido_label = st.selectbox(
                        f"Horario / Sección:",
                        list(opciones_horario.keys()),
                        key=f"hora_atr_{clave_atr}"
                    )

                    materia_elegida = opciones_horario[horario_elegido_label]
                    # Marcamos la materia atrasada elegida para inyectarla en el calendario
                    materias_atrasadas_a_incluir.append(materia_elegida)
                    st.success(f"✅ Se añadirá al horario: {materia_elegida['materia']} — {materia_elegida['hora']}")
                    st.markdown("---")
        else:
            st.caption("No hay materias registradas en ese semestre.")

# Calcular qué materias del semestre activo quedan bloqueadas
claves_bloqueadas = get_materias_bloqueadas(claves_atrasadas)

# Construir lista de trabajo filtrando las bloqueadas
lista_materias_trabajo_raw = [m for m in CATALOGO_MATERIAS if m['semestre'] == semestre_seleccionado]
lista_materias_trabajo = [m for m in lista_materias_trabajo_raw if m['clave'] not in claves_bloqueadas]

# Inyectar las materias atrasadas elegidas directamente en la lista de trabajo
for mat_atr in materias_atrasadas_a_incluir:
    # Evitar duplicados si la clave ya estuviera en la lista
    if not any(m['nrc'] == mat_atr['nrc'] for m in lista_materias_trabajo):
        lista_materias_trabajo.append(mat_atr)

# Detectar qué materias se omitieron por prerrequisitos faltantes (para avisar al usuario)
materias_omitidas_por_prereq = list({
    m['materia'] for m in lista_materias_trabajo_raw if m['clave'] in claves_bloqueadas
})

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Dinámico y Prioritario")
st.subheader(f"Esquema Activo: {semestre_seleccionado}")

# Aviso de materias bloqueadas por prerequisitos faltantes
if claves_atrasadas and materias_omitidas_por_prereq:
    st.error(
        f"🚫 **Materias eliminadas del horario por prerequisitos incompletos:** "
        f"{', '.join(sorted(materias_omitidas_por_prereq))}  \n"
        f"_(Causa: tienes atrasada(s): {', '.join(nombres_atrasadas)})_"
    )
elif claves_atrasadas and not materias_omitidas_por_prereq:
    st.success("✅ Las materias atrasadas seleccionadas no bloquean ninguna materia de este semestre.")

if materias_atrasadas_a_incluir:
    nombres_incl = [f"**{m['materia']}** (Secc {m['secc']}, {m['hora']}, {m['profesor']})" for m in materias_atrasadas_a_incluir]
    st.info(f"📌 **Materias atrasadas que se incluirán en el horario:** {', '.join(nombres_incl)}")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    total_materias_solicitadas = len(set(m['clave'] for m in lista_materias_trabajo)) + len(optativas_seleccionadas_usuario)
    
    if total_materias_solicitadas > 8:
        st.error(f"❌ No fue posible crear el horario porque sobrepasa el límite de materias por semestre. (Solicitadas: {total_materias_solicitadas}, Máximo permitido: 8)")
    elif not lista_materias_trabajo and not optativas_seleccionadas_usuario:
        st.warning(f"La base de datos para el **{semestre_seleccionado}** está vacía.")
    else:
        calendario, prioridad_cumplida, om, om_prof, om_viernes, err = generar_horario_estricto(
            lista_materias_trabajo, optativas_seleccionadas_usuario, profesores_inputs, lm_rango, aj_rango, v_rango, omitir_viernes
        )
        
        if calendario is not None:
            if om_viernes:
                for mat in set(om_viernes):
                    st.warning(f"⚠️ La materia **{mat}** no se seleccionó por cruce o límites en viernes.")
            if om:
                st.warning(f"⚠️ **Atención:** Por restricciones se omitieron: {', '.join(set(om))}.")
            if om_prof:
                st.error(f"👤 **Materia Omitida:** La asignatura **{', '.join(set(om_prof))}** quedó fuera por restricciones de profesor prioritario.")

            if len(profesores_inputs) > 0 and len(calendario) > 0:
                if prioridad_cumplida:
                    st.info("💎 **Filtro Aplicado Correctamente:** Se fijaron exitosamente tus profesores prioritarios.")
                else:
                    st.warning("⚠️ **Filtro No Aplicado Completamente:** Ciertos profesores prioritarios no se incluyeron por restricciones de cruce horaria.")
            elif len(calendario) > 0:
                st.success(f"🎯 Horario estructurado correctamente. Carga final armada: {len(calendario)} materias.")

            if calendario:
                # 📅 ORDENAMIENTO ESTRICTO DESDE LAS 07:00 AM HASTA LAS 21:00 PM
                bloques_fijos = [
                    "0700-0829", "0700-0859", "0700-1059",
                    "0900-1029", "0900-1059", "1000-1259",
                    "1100-1229", "1100-1259",
                    "1300-1429", "1300-1459", "1300-1559", "1300-1659",
                    "1500-1629", "1500-1659", "1600-1959",
                    "1700-1829", "1700-1859", "1700-2059",
                    "1900-2059"
                ]
                
                df_horario = pd.DataFrame("", index=bloques_fijos, columns=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
                
                for m in calendario:
                    info_celda = f"📚 {m['materia']}\nSecc: {m['secc']}\n👤 {m['profesor']}\n[NRC: {m['nrc']}]"
                    if m['hora'] in df_horario.index:
                        if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
                        if 'M' in m['dias']: df_horario.at[m['hora'], "Miércoles"] = info_celda
                        if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                        if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda
                        if 'V' in m['dias']: df_horario.at[m['hora'], "Viernes"] = info_celda
                    else:
                        df_horario.loc[m['hora']] = ""
                        df_horario = df_horario.sort_index()
                        if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
                        if 'M' in m['dias']: df_horario.at[m['hora'], "Miércoles"] = info_celda
                        if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                        if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda
                        if 'V' in m['dias']: df_horario.at[m['hora'], "Viernes"] = info_celda

                columnas_activas = [col for col in df_horario.columns if not (df_horario[col] == "").all()]
                df_horario_filtrado = df_horario[columnas_activas]

                st.write("### 📅 Vista de Calendario Semanal")
                st.markdown("<style>table { font-size: 13px !important; width: 100% !important; } th { background-color: #1E3A8A !important; color: white !important; } td { white-space: pre-line !important; height: 90px !important; vertical-align: top !important; background-color: #F8F9FA; border: 1px solid #D1D5DB !important; }</style>", unsafe_allow_html=True)
                st.table(df_horario_filtrado)
                
                st.write("### 📝 Detalle del Horario Activo")
                df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
                df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
                df_lista = df_lista.sort_values(by=['Horario']).reset_index(drop=True)
                st.dataframe(df_lista, use_container_width=True, hide_index=True)
            else:
                st.info("💡 No hay clases por mostrar en la cuadrícula debido a las restricciones activas.")
        else:
            st.error(err)