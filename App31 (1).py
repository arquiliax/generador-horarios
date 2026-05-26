import streamlit as st
import random
import pandas as pd

# =========================================================================
# 📚 BASE DE DATOS REAL EXTRAÍDA DE TU DOCUMENTO (MATERIAS BASE)
# =========================================================================
CATALOGO_MATERIAS = [
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
    {"nrc": "57926", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "004", "dias": "LM", "hora": "1100-1259", "profesor": "RAMOS - PEREZ CECILIA", "semestre": "6to Semestre"},
    {"nrc": "57983", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "PEREZ BARROSO MARLENE", "semestre": "6to Semestre"},
    {"nrc": "57700", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "TLALPAN RUIZ MARIA GUADALUPE", "semestre": "6to Semestre"},
    {"nrc": "57725", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "005", "dias": "AJ", "hora": "1500-1659", "profesor": "ARCE-MUNOZ MOHAMED", "semestre": "6to Semestre"},
    {"nrc": "57805", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "005", "dias": "LM", "hora": "1300-1459", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "6to Semestre"},
    {"nrc": "57845", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "005", "dias": "LM", "hora": "1500-1659", "profesor": "MENDEZ-BALBUENA IGNACIO", "semestre": "6to Semestre"},
    {"nrc": "57888", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "005", "dias": "AJ", "hora": "1100-1259", "profesor": "TAPIA - LOPEZ SANDRA LUCIA", "semestre": "6to Semestre"},
    {"nrc": "57936", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "005", "dias": "AJ", "hora": "0700-0859", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "6to Semestre"},
    {"nrc": "57997", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "005", "dias": "AJ", "hora": "0900-1059", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "6to Semestre"},
    {"nrc": "57701", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "006", "dias": "LM", "hora": "1300-1459", "profesor": "TLALPAN RUIZ MARIA GUADALUPE", "semestre": "6to Semestre"},
    {"nrc": "57731", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "006", "dias": "LM", "hora": "1700-1859", "profesor": "SANCHEZ-MORALES REBECA", "semestre": "6to Semestre"},
    {"nrc": "57813", "clave": "PSIS 260", "materia": "Psicologia de las Actitudes", "secc": "006", "dias": "AJ", "hora": "1100-1259", "profesor": "ROMERO RODRIGUEZ EULOGIO", "semestre": "6to Semestre"},
    {"nrc": "57850", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "006", "dias": "LM", "hora": "1500-1659", "profesor": "MENDEZ-BALBUENA IGNACIO", "semestre": "6to Semestre"},
    {"nrc": "57891", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "006", "dias": "AJ", "hora": "1300-1459", "profesor": "TAPIA - LOPEZ SANDRA LUCIA", "semestre": "6to Semestre"},
    {"nrc": "57943", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "006", "dias": "AJ", "hora": "1500-1659", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "6to Semestre"},
    {"nrc": "58007", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "006", "dias": "AJ", "hora": "1900-2059", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "6to Semestre"},
    {"nrc": "59850", "clave": "PSIS 256", "materia": "Psicoterapia Individual", "secc": "006", "dias": "AJ", "hora": "1900-2059", "profesor": "SANCHEZ-MORALES REBECA", "semestre": "6to Semestre"},
    {"nrc": "57704", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "BENAVIDES - VALDERRABANO MARICELA", "semestre": "6to Semestre"},
    {"nrc": "59830", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "007", "dias": "LM", "hora": "0700-0859", "profesor": "MENDEZ-BALBUENA IGNACIO", "semestre": "6to Semestre"},
    {"nrc": "57896", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "007", "dias": "AJ", "hora": "1500-1659", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN", "semestre": "6to Semestre"},
    {"nrc": "57949", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "007", "dias": "AJ", "hora": "1300-1459", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "6to Semestre"},
    {"nrc": "58021", "clave": "ISPS 201", "materia": "Psicologia Cognitiva", "secc": "007", "dias": "AJ", "hora": "1700-1859", "profesor": "OREA - HERNANDEZ RICARDO ENRIQUE", "semestre": "6to Semestre"},
    {"nrc": "57707", "clave": "PSIS 253", "materia": "Psicopedagogia", "secc": "008", "dias": "LM", "hora": "1100-1259", "profesor": "BENAVIDES - VALDERRABANO MARICELA", "semestre": "6to Semestre"},
    {"nrc": "59833", "clave": "PSIS 261", "materia": "Investigacion III: Analisis Cu", "secc": "008", "dias": "LM", "hora": "0900-1059", "profesor": "MENDEZ-BALBUENA IGNACIO", "semestre": "6to Semestre"},
    {"nrc": "57901", "clave": "PSIS 264", "materia": "Aprovisionamiento de R H", "secc": "008", "dias": "AJ", "hora": "1900-2059", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN", "semestre": "6to Semestre"},
    {"nrc": "57954", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "008", "dias": "AJ", "hora": "1100-1259", "profesor": "ZEPEDA - ASTORGA FRANCISCO", "semestre": "6to Semestre"},

    # --- 7mo SEMESTRE ---
    {"nrc": "57767", "clave": "PSIS 257", "materia": "Psicoterapia de Pareja", "secc": "001", "dias": "AJ", "hora": "0900-1059", "profesor": "STANGE-ESPINOLA ISABEL DEL ROSARIO", "semestre": "7mo Semestre"},
    {"nrc": "57772", "clave": "PSIS 262", "materia": "Investigacion IV: Analisis Cua", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "SILVARIOS CARLOS ENRIQUE", "semestre": "7mo Semestre"},
    {"nrc": "57780", "clave": "PSIS 265", "materia": "Diagnostico Organizacional", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "ARELLANO-BAUTISTA CLAUDIA ANGELICA", "semestre": "7mo Semestre"},
    {"nrc": "57787", "clave": "ISPS 203", "materia": "Psicologia Social Latinoameri", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "CERVANTES - HERNANDEZ MARIA LETICIA", "semestre": "7mo Semestre"},
    {"nrc": "57796", "clave": "ISPS 202", "materia": "Educacion Especial", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "7mo Semestre"},
    {"nrc": "57853", "clave": "ISPS 202", "materia": "Educacion Especial", "secc": "003", "dias": "LM", "hora": "1300-1459", "profesor": "DE LA OLIVA - GRANIZO DAVID", "semestre": "7mo Semestre"},
    {"nrc": "57769", "clave": "PSIS 257", "materia": "Psicoterapia de Pareja", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "LUNA - PEREZ PERLA WENDOLINE", "semestre": "7mo Semestre"},
    {"nrc": "57776", "clave": "PSIS 262", "materia": "Investigacion IV: Analisis Cua", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "SILVARIOS CARLOS ENRIQUE", "semestre": "7mo Semestre"},
    {"nrc": "57782", "clave": "PSIS 265", "materia": "Diagnostico Organizacional", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "MORALES-REYES JOSE LUIS", "semestre": "7mo Semestre"},
    {"nrc": "57789", "clave": "ISPS 203", "materia": "Psicologia Social Latinoameri", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "CERVANTES - HERNANDEZ MARIA LETICIA", "semestre": "7mo Semestre"},
    {"nrc": "57812", "clave": "ISPS 202", "materia": "Educacion Especial", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "DURAN-SORIANO MARIA DEL ROSIO", "semestre": "7mo Semestre"},

    # --- 8vo SEMESTRE ---
    {"nrc": "57897", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "ARELLANO BAUTISTA CLAUDIA ANGELICA", "semestre": "8vo Semestre"},
    {"nrc": "57905", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "CERVANTES - HERNANDEZ MARIA LETICIA", "semestre": "8vo Semestre"},
    {"nrc": "57912", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "8vo Semestre"},
    {"nrc": "57900", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "002", "dias": "AJ", "hora": "1700-1859", "profesor": "DE LA ROSA - DIAZ BRENDA ELENA", "semestre": "8vo Semestre"},
    {"nrc": "57908", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "ROMERO RODRIGUEZ EULOGIO", "semestre": "8vo Semestre"},
    {"nrc": "57920", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "002", "dias": "LM", "hora": "1900-2059", "profesor": "AGUILAR ALVAREZ EDGAR ANDRES", "semestre": "8vo Semestre"},
    {"nrc": "57930", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "003", "dias": "AJ", "hora": "0700-0859", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN", "semestre": "8vo Semestre"},
    {"nrc": "57934", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "003", "dias": "AJ", "hora": "0900-1059", "profesor": "MORALES-JUAREZ BARTOLA", "semestre": "8vo Semestre"},
    {"nrc": "57940", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "003", "dias": "AJ", "hora": "1100-1259", "profesor": "AGUILAR-DAVILA YADIRA", "semestre": "8vo Semestre"},
    {"nrc": "57944", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "FRAGOSOLUZURIAGA ROCIO", "semestre": "8vo Semestre"},
    {"nrc": "57949", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "004", "dias": "AJ", "hora": "1700-1859", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "8vo Semestre"},
    {"nrc": "57954", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "004", "dias": "LM", "hora": "1500-1659", "profesor": "LUNA - PEREZ PERLA WENDOLINE", "semestre": "8vo Semestre"},
    {"nrc": "57959", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "005", "dias": "LM", "hora": "0900-1059", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "8vo Semestre"},
    {"nrc": "57963", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "CHAVEZ-GONZALEZ ERIKA", "semestre": "8vo Semestre"},
    {"nrc": "57967", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "005", "dias": "AJ", "hora": "1500-1659", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "8vo Semestre"},
    {"nrc": "57971", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "006", "dias": "LM", "hora": "1300-1459", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "8vo Semestre"},
    {"nrc": "57975", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "006", "dias": "LM", "hora": "1500-1659", "profesor": "MARTINEZ - MENDEZ DULCE MARIA", "semestre": "8vo Semestre"},
    {"nrc": "57979", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "006", "dias": "AJ", "hora": "1900-2059", "profesor": "SANCHEZ-MORALES REBECA", "semestre": "8vo Semestre"},
    {"nrc": "58051", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "TAPIA - LOPEZ SANDRA LUCIA", "semestre": "8vo Semestre"},
    {"nrc": "58056", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "007", "dias": "LM", "hora": "1300-1459", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "8vo Semestre"},
    {"nrc": "58061", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "007", "dias": "LM", "hora": "1700-1859", "profesor": "RODRIGUEZ - SANCHEZ JOSE LUIS", "semestre": "8vo Semestre"},
    {"nrc": "58062", "clave": "PSIS 266", "materia": "Capacitacion", "secc": "008", "dias": "LM", "hora": "1500-1659", "profesor": "TAPIA - LOPEZ SANDRA LUCIA", "semestre": "8vo Semestre"},
    {"nrc": "58064", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "LARA-LOPEZ ALINE BENJAMIN", "semestre": "8vo Semestre"},
    {"nrc": "58067", "clave": "ISPS 204", "materia": "Terapia Familiar", "secc": "008", "dias": "AJ", "hora": "1500-1659", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "8vo Semestre"},

    # --- 9no SEMESTRE ---
    {"nrc": "58206", "clave": "ISPS 208", "materia": "Intervencion en Crisis", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "9no Semestre"},
    {"nrc": "58207", "clave": "ISPS 209", "materia": "Psicoterapia Grupal", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "9no Semestre"},
    {"nrc": "59425", "clave": "ISPS 207", "materia": "Estrategias de inter en psi org", "secc": "004", "dias": "LM", "hora": "0900-1029", "profesor": "ARELLANO BAUTISTA CLAUDIA ANGELICA", "semestre": "9no Semestre"},
    {"nrc": "58204", "clave": "ISPS 206", "materia": "Estrategias de inter en psi ed", "secc": "001", "dias": "AJ", "hora": "0900-1029", "profesor": "COYOTECATL FABIAN FRANCISCA", "semestre": "9no Semestre"},

    # --- 10mo SEMESTRE ---
    {"nrc": "58255", "clave": "ISPS 212", "materia": "Desarrollo de Proy. de Inv.", "secc": "001", "dias": "LM", "hora": "1300-1429", "profesor": "SANCHEZ-CID JOSE ELIAS", "semestre": "10mo Semestre"}
]

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
        {"nrc": "58254", "clave": "PSIS 615", "materia": "Criminologia", "secc": "001", "dias": "LM", "hora": "0900-1029", "profesor": "GARCIA AGUILAR GREGORIO"}
    ],
    "Social": [
        {"nrc": "58212", "clave": "PSIS 616", "materia": "Perspectivas Medioambientales", "secc": "001", "dias": "AJ", "hora": "1100-1229", "profesor": "HERNANDEZ ESCOBAR VERONICA"},
        {"nrc": "58564", "clave": "PSIS 616", "materia": "Perspectivas Medioambientales", "secc": "002", "dias": "LM", "hora": "1300-1429", "profesor": "ROMEROHORAN MARIA GUILLERMINA"},
        {"nrc": "58565", "clave": "PSIS 617", "materia": "Psicologia Politica", "secc": "002", "dias": "LM", "hora": "0700-0829", "profesor": "MEZA FLORES ABIGAIL"},
        {"nrc": "58571", "clave": "PSIS 618", "materia": "Psicologia Social de la Educ.", "secc": "002", "dias": "LM", "hora": "1100-1229", "profesor": "RODRIGUEZ MARTINEZ RICARDO ALEJANDRO"},
        {"nrc": "58604", "clave": "PSIS 619", "materia": "Psicologia Social de la Salud", "secc": "002", "dias": "AJ", "hora": "0900-1029", "profesor": "SANCHEZ HERNANDEZ GRACIELA"},
        {"nrc": "58615", "clave": "PSIS 621", "materia": "Psicología Soc de las Minorias", "secc": "002", "dias": "AJ", "hora": "0900-1029", "profesor": "RODRIGUEZ MARTINEZ RICARDO ALEJANDRO"},
        {"nrc": "58931", "clave": "PSIS 802", "materia": "Taller Titulacion por Tesina", "secc": "001", "dias": "LM", "hora": "1100-1229", "profesor": "SANCHEZ-CID JOSE ELIAS"},
        {"nrc": "58942", "clave": "PSIS 802", "materia": "Taller Titulacion por Tesina", "secc": "002", "dias": "LM", "hora": "1700-1829", "profesor": "SANCHEZ-CID JOSE ELIAS"}
    ],
    "Organizacional": [
        {"nrc": "58223", "clave": "PSIS 622", "materia": "Auditoria de R.H.", "secc": "001", "dias": "AJ", "hora": "1500-1629", "profesor": "TAPIA LOPEZ SANDRA LUCIA"},
        {"nrc": "58231", "clave": "PSIS 624", "materia": "Desarrollo Organizacional", "secc": "001", "dias": "LM", "hora": "0900-1029", "profesor": "CARRO MEZA DULCE CAROLINA"},
        {"nrc": "58645", "clave": "PSIS 624", "materia": "Desarrollo Organizacional", "secc": "002", "dias": "LM", "hora": "1100-1229", "profesor": "CARRO MEZA DULCE CAROLINA"},
        {"nrc": "58233", "clave": "PSIS 625", "materia": "Estres y Salud en las Organi..", "secc": "001", "dias": "AJ", "hora": "0900-1029", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN"},
        {"nrc": "58689", "clave": "PSIS 625", "materia": "Estres y Salud en las Organi..", "secc": "002", "dias": "AJ", "hora": "1100-1229", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN"}
    ],
    "Educativa": [
        {"nrc": "58202", "clave": "PSIS 600", "materia": "Educacion Inclusiva", "secc": "001", "dias": "AJ", "hora": "1100-1229", "profesor": "DE LA OLIVA - GRANIZO DAVID"},
        {"nrc": "58237", "clave": "PSIS 600", "materia": "Educacion Inclusiva", "secc": "003", "dias": "AJ", "hora": "1100-1229", "profesor": "LIMATIZCARENO SILVIA CAROLINA"},
        {"nrc": "58203", "clave": "PSIS 601", "materia": "Educacion No Formal", "secc": "001", "dias": "LM", "hora": "0900-1029", "profesor": "TLALPAN-RUIZ MARIA GUADALUPE"},
        {"nrc": "58239", "clave": "PSIS 601", "materia": "Educacion No Formal", "secc": "003", "dias": "AJ", "hora": "1100-1229", "profesor": "TLALPAN-RUIZ MARIA GUADALUPE"},
        {"nrc": "58205", "clave": "PSIS 602", "materia": "Modeliz de Procesos Cognitivos", "secc": "001", "dias": "AJ", "hora": "1300-1429", "profesor": "DIAZ-CARDENAS ALFONSO FELIPE"},
        {"nrc": "58210", "clave": "PSIS 605", "materia": "Orientacion Familiar en Ed.", "secc": "001", "dias": "AJ", "hora": "1100-1229", "profesor": "DEGANTE REYES MONICA ALEJANDRA"}
    ]
}

# =========================================================================
# 🧬 MOTOR ALGORÍTMICO Y LÓGICA DE CONTROL DE INTERVALOS ESTRICTOS
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
    if 'hora' not in materia or not materia['hora']:
        return False
    ini_mat, fin_mat = parse_hora(materia['hora'])
    dias = materia['dias']
    
    if 'L' in dias or 'M' in dias:
        if ini_mat < lm_lims[0] or fin_mat > lm_lims[1]:
            return False
    if 'A' in dias or 'J' in dias:
        if ini_mat < aj_lims[0] or fin_mat > aj_lims[1]:
            return False
    if 'V' in dias:
        if omitir_viernes:
            return False
        if ini_mat < v_lims[0] or fin_mat > v_lims[1]:
            return False
    return True

def coincide_profesor(nombre_ingresado, nombre_catalogo):
    tokens = nombre_ingresado.lower().replace('-', ' ').split()
    catalogo_limpio = nombre_catalogo.lower().replace('-', ' ')
    if not tokens:
        return False
    return all(t in catalogo_limpio for t in tokens)

def generar_horario_estricto(lista_materias, optativas_seleccionadas, profesores_prioritarios, lm_lims, aj_lims, v_lims, omitir_viernes, max_intentos=5000):
    materias_unicas = {}
    nombres_materias = {}
    
    for m in lista_materias:
        clave = m['clave']
        nombres_materias[clave] = m['materia']
        if clave not in materias_unicas:
            materias_unicas[clave] = []
        materias_unicas[clave].append(m)
        
    prioridades = [p.strip() for p in profesores_prioritarios if p.strip()]
    
    materias_omitidas, omitidas_prof_unico, omitidas_por_viernes = [], [], []
    materias_filtradas = {}
    
    for clave, opciones in materias_unicas.items():
        opciones_con_profesor = [op for op in opciones if any(coincide_profesor(p, op['profesor']) for p in prioridades)]
        opciones_finales = opciones_con_profesor if opciones_con_profesor else opciones
        
        opciones_en_rango = [op for op in opciones_finales if entra_en_rango_permitido(op, lm_lims, aj_lims, v_lims, omitir_viernes)]
        
        if not opciones_en_rango:
            materias_omitidas.append(nombres_materias[clave])
            if len(opciones) == 1:
                omitidas_prof_unico.append(f"{nombres_materias[clave]} (Único NRC disponible)")
            if any('V' in op['dias'] for op in opciones) and omitir_viernes:
                omitidas_por_viernes.append(nombres_materias[clave])
        else:
            materias_filtradas[clave] = opciones_en_rango

    optativas_filtradas = {}
    for clave_opt, opciones_opt in optativas_seleccionadas.items():
        opciones_opt_con_prof = [op for op in opciones_opt if any(coincide_profesor(p, op['profesor']) for p in prioridades)]
        opciones_opt_finales = opciones_opt_con_prof if opciones_opt_con_prof else opciones_opt
        
        opciones_opt_en_rango = [op for op in opciones_opt_finales if entra_en_rango_permitido(op, lm_lims, aj_lims, v_lims, omitir_viernes)]
        
        if opciones_opt_en_rango:
            optativas_filtradas[clave_opt] = opciones_opt_en_rango

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
    ["3er Semestre", "4to Semestre", "5to Semestre", "6to Semestre", "7mo Semestre", "8vo Semestre", "9no Semestre", "10mo Semestre"],
    index=1  # Posición del 4to Semestre por comodidad en esta prueba
)

st.sidebar.markdown("---")
st.sidebar.subheader("⏱️ Horario de Referencia")

valores_horas = [700, 900, 1100, 1300, 1500, 1700, 1900, 2100]
horas_visibles = {
    700: "07:00 AM", 900: "09:00 AM", 1100: "11:00 AM", 1300: "01:00 PM",
    1500: "03:00 PM", 1700: "05:00 PM", 1900: "07:00 PM", 2100: "09:00 PM"
}

lm_rango = st.sidebar.select_slider(
    "Límites Lunes/Martes:",
    options=valores_horas,
    value=(700, 2100),
    format_func=lambda x: horas_visibles[x],
    key="slider_lm"
)

aj_rango = st.sidebar.select_slider(
    "Límites Miércoles/Jueves:",
    options=valores_horas,
    value=(700, 2100),
    format_func=lambda x: horas_visibles[x],
    key="slider_aj"
)

omitir_viernes = st.sidebar.checkbox("❌ Omitir clases en Viernes por completo", value=False)

if omitir_viernes:
    v_rango = (700, 2100)
else:
    v_rango = st.sidebar.select_slider(
        "Límites Viernes:",
        options=valores_horas,
        value=(700, 2100),
        format_func=lambda x: horas_visibles[x],
        key="slider_v"
    )

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Ej. LUNA-PEREZ")
    if pref_name.strip():
        profesores_inputs.append(pref_name.strip())

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

lista_materias_trabajo = [m for m in CATALOGO_MATERIAS if m['semestre'] == semestre_seleccionado]

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Dinámico y Prioritario")
st.subheader(f"Esquema Activo: {semestre_seleccionado}")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    total_materias_solicitadas = len(set(m['clave'] for m in lista_materias_trabajo)) + len(optativas_seleccionadas_usuario)
    
    with st.spinner("Buscando combinaciones válidas en la base de datos..."):
        calendario, prioridad_completa, omitidas, unico_prof, por_viernes, error_msg = generar_horario_estricto(
            lista_materias_trabajo, optativas_seleccionadas_usuario, profesores_inputs,
            lm_rango, aj_rango, v_rango, omitir_viernes
        )
        
    if calendario:
        if error_msg:
            st.warning(error_msg)
            
        if profesores_inputs:
            if prioridad_completa:
                st.success("✨ ¡Combinación perfecta! Se asignaron tus docentes prioritarios sin traslapes.")
            else:
                st.info("💡 Horario generado. No todas las prioridades se cumplieron para evitar traslapes o respetar límites de hora.")
        else:
            st.success("✅ ¡Horario generado exitosamente sin conflictos académicos!")
            
        if omitidas:
            with st.expander("⚠️ Ver materias que no pudieron incluirse por restricciones de hora", expanded=False):
                st.write("Las siguientes asignaturas quedaron fuera debido a que sus NRC disponibles no entran en tus Horarios de Referencia:")
                for o in set(omitidas):
                    st.markdown(f"- **{o}**")
                if unico_prof:
                    st.caption("**Nota crítica:** Algunas materias solo tienen un único profesor asignado institucionalmente en todo el periodo.")
                    
        # Inicialización de matriz del calendario semanal
        horas_bloque = ["0700-0859", "0900-1059", "1100-1259", "1300-1459", "1500-1659", "1700-1859", "1900-2059", "0900-1029", "1100-1229", "1300-1429", "1500-1629", "1700-1829", "1000-1259", "1300-1559", "1600-1959"]
        df_horario = pd.DataFrame(index=horas_bloque, columns=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]).fillna("")
        
        for m in calendario:
            info_celda = f"📚 **{m['materia']}**\n🔑 NRC: {m['nrc']} | Sec: {m['secc']}\n👤 {m['profesor']}"
            if m['hora'] in df_horario.index:
                if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
                if 'M' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda
                if 'V' in m['dias']: df_horario.at[m['hora'], "Viernes"] = info_celda
            else:
                df_horario.loc[m['hora']] = ""
                if 'L' in m['dias']: df_horario.at[m['hora'], "Lunes"] = info_celda
                if 'M' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                if 'A' in m['dias']: df_horario.at[m['hora'], "Martes"] = info_celda
                if 'J' in m['dias']: df_horario.at[m['hora'], "Jueves"] = info_celda
                if 'V' in m['dias']: df_horario.at[m['hora'], "Viernes"] = info_celda

        df_horario = df_horario.sort_index()
        columnas_activas = [col for col in df_horario.columns if not (df_horario[col] == "").all()]
        df_horario_filtrado = df_horario[columnas_activas]

        st.write("### 📅 Vista de Calendario Semanal")
        st.markdown("<style>table { font-size: 13px !important; width: 100% !important; } th { background-color: #1E3A8A !important; color: white !important; } td { white-space: pre-line !important; height: 90px !important; vertical-align: top !important; background-color: #F8F9FA; border: 1px solid #D1D5DB !important; }</style>", unsafe_allow_html=True)
        st.table(df_horario_filtrado)
        
        st.write("### 📝 Detalle del Horario Activo")
        df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
        df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
        st.dataframe(df_lista, use_container_width=True)
    else:
        st.error(f"❌ {error_msg}")
        if omitidas:
            st.error(f"Restricciones críticas: Las materias {list(set(omitidas))} no se pudieron posicionar.")