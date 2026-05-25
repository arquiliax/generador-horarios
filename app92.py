import streamlit as st
import random
import pandas as pd

# =========================================================================
# 📚 BASE DE DATOS REAL EXTRAÍDA DE TU DOCUMENTO (SOLO MATERIAS BASE)
# =========================================================================
CATALOGO_MATERIAS = [
    # --- 5to SEMESTRE ---
    {"nrc": "57518", "clave": "PSIS 250", "materia": "Evaluacion del Desarrollo", "secc": "001", "dias": "AJ", "hora": "1100-1259", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDES", "semestre": "5to Semestre"},
    {"nrc": "57523", "clave": "PSIS 250", "materia": "Evaluacion del Desarrollo", "secc": "003", "dias": "LM", "hora": "0700-0859", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "5to Semestre"},
    {"nrc": "57532", "clave": "PSIS 251", "materia": "Alteraciones del Desarrollo", "secc": "001", "dias": "LM", "hora": "0900-1059", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "5to Semestre"},
    {"nrc": "57540", "clave": "PSIS 252", "materia": "Psicologia y Educacion", "secc": "001", "dias": "LM", "hora": "1100-1259", "profesor": "DE LA OLIVA - GRANIZO DAVID", "semestre": "5to Semestre"},
    {"nrc": "57559", "clave": "PSIS 254", "materia": "Evaluacion de la Personalidad", "secc": "001", "dias": "LM", "hora": "1300-1459", "profesor": "HERNANDEZ - RODRIGUEZ GUADALUPE LOURDE", "semestre": "5to Semestre"},
    {"nrc": "57589", "clave": "PSIS 255", "materia": "Enfoques Contempo en Psico", "secc": "001", "dias": "AJ", "hora": "0700-0859", "profesor": "VAZQUEZ-CASTELLANOS ARMANDO", "semestre": "5to Semestre"},
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
    {"nrc": "57931", "clave": "ISPS 200", "materia": "Psicodiagnostico", "secc": "005", "dias": "AJ", "hora": "0700-0859", "profesor": "ZEPEDA-ASTORGA FRANCISCO", "semestre": "6to Semestre"},
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
    {"nrc": "57827", "clave": "PSIS 262", "materia": "Investigacion IV: Analisis Cua", "secc": "002", "dias": "AJ", "hora": "1500-1659", "profesor": "ROMERO RODRIGUEZ EULOGIO", "semestre": "7mo Semestre"},
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
    {"nrc": "57998", "clave": "ISPS 205", "materia": "Psicologia Comunitaria", "secc": "006", "dias": "LM", "hora": "1500-1659", "profesor": "ROMERO RODRIGUEZ EULOGIO", "semestre": "8vo Semestre"},
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
    {"nrc": "58215", "clave": "ISPS 206", "materia": "Estrategias de Inter en Psi Ed", "secc": "001", "dias": "LM", "hora": "0900-1029", "profesor": "DE LA OLIVA - GRANIZO DAVID", "semestre": "9no Semestre"},
    {"nrc": "58234", "clave": "ISPS 207", "materia": "Estrategias de Inte en Psi Org", "secc": "001", "dias": "LM", "hora": "0700-0829", "profesor": "HERNANDEZ - VICHIDO DONAXI", "semestre": "9no Semestre"},
    {"nrc": "58252", "clave": "ISPS 207", "materia": "Estrategias de Inte en Psi Org", "secc": "003", "dias": "AJ", "hora": "0900-1029", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "9no Semestre"},
    {"nrc": "58242", "clave": "ISPS 208", "materia": "Intervencion en Crisis", "secc": "002", "dias": "AJ", "hora": "1300-1459", "profesor": "STANGE-ESPINOLA ISABEL DEL ROSARIO", "semestre": "9no Semestre"},
    {"nrc": "58244", "clave": "ISPS 209", "materia": "Psicoterapia Grupal", "secc": "002", "dias": "LM", "hora": "1700-1859", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "9no Semestre"},
    {"nrc": "58246", "clave": "ISPS 206", "materia": "Estrategias de Inter en Psi Ed", "secc": "002", "dias": "AJ", "hora": "1500-1629", "profesor": "LIMATIZCARENO SILVIA CAROLINA", "semestre": "9no Semestre"},
    {"nrc": "58249", "clave": "ISPS 207", "materia": "Estrategias de Inte en Psi Org", "secc": "002", "dias": "LM", "hora": "1500-1629", "profesor": "ALVAREZ-CARRILLO PAULINA", "semestre": "9no Semestre"},
    {"nrc": "58251", "clave": "ISPS 206", "materia": "Estrategias de Inter en Psi Ed", "secc": "003", "dias": "LM", "hora": "0900-1029", "profesor": "COYOTECATL - FABIAN FRANCISCA", "semestre": "9no Semestre"},

    # --- 10mo SEMESTRE ---
    {"nrc": "58255", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "GONZALEZ - CRUZ VICTOR GERARDO", "semestre": "10mo Semestre"},
    {"nrc": "58258", "clave": "ISPS 210", "materia": "Estrategias de Inte en Psi Cli", "secc": "001", "dias": "LM", "hora": "0900-1029", "profesor": "VEGA-SIMONT EDMUNDO", "semestre": "10mo Semestre"},
    {"nrc": "58260", "clave": "ISPS 211", "materia": "Estrategias de Inte en Psi Soc", "secc": "001", "dias": "LM", "hora": "1100-1229", "profesor": "SILVARIOS CARLOS ENRIQUE", "semestre": "10mo Semestre"},
    {"nrc": "58643", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "CARRO-MEZA DULCE CAROLINA", "semestre": "10mo Semestre"},
    {"nrc": "58651", "clave": "ISPS 210", "materia": "Estrategias de Inte en Psi Cli", "secc": "002", "dias": "LM", "hora": "1300-1429", "profesor": "LUNA - PEREZ PERLA WENDOLINE", "semestre": "10mo Semestre"},
    {"nrc": "58714", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "003", "dias": "AJ", "hora": "1700-1859", "profesor": "GONZALEZ-CRUZ VICTOR GERARDO", "semestre": "10mo Semestre"},
    {"nrc": "59124", "clave": "ISPS 210", "materia": "Estrategias de Inte en Psi Cli", "secc": "003", "dias": "AJ", "hora": "1100-1229", "profesor": "ARCE - MUNOAMED", "semestre": "10mo Semestre"},
    {"nrc": "59133", "clave": "ISPS 211", "materia": "Estrategias de Inte en Psi Soc", "secc": "003", "dias": "AJ", "hora": "0900-1029", "profesor": "DEGANTE - REYES MONICA ALEJANDRA", "semestre": "10mo Semestre"},
    {"nrc": "59139", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "10mo Semestre"},
    {"nrc": "59149", "clave": "ISPS 210", "materia": "Estrategias de Inte en Psi Cli", "secc": "004", "dias": "AJ", "hora": "1700-1829", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "10mo Semestre"},
    {"nrc": "59152", "clave": "ISPS 211", "materia": "Estrategias de Inte en Psi Soc", "secc": "004", "dias": "AJ", "hora": "1500-1629", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "10mo Semestre"},
    {"nrc": "57786", "clave": "ISPS 211", "materia": "Estrategias de Inte en Psi Soc", "secc": "005", "dias": "AJ", "hora": "1100-1229", "profesor": "MORALES - JUAREZ BARTOLA", "semestre": "10mo Semestre"},
    {"nrc": "59156", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN", "semestre": "10mo Semestre"},
    {"nrc": "59162", "clave": "ISPS 210", "materia": "Estrategias de Inte en Psi Cli", "secc": "005", "dias": "LM", "hora": "0900-1029", "profesor": "LUNA-PEREZ PERLA WENDOLINE", "semestre": "10mo Semestre"},
    {"nrc": "57809", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "006", "dias": "LM", "hora": "1300-1459", "profesor": "MERCADO CARNALLA MARIO RENATO", "semestre": "10mo Semestre"},
    {"nrc": "57830", "clave": "ISPS 210", "materia": "Estrategias de Inte en Psi Cli", "secc": "006", "dias": "LM", "hora": "1500-1629", "profesor": "SANCHEZ-MORALES REBECA", "semestre": "10mo Semestre"},
    {"nrc": "57850", "clave": "ISPS 211", "materia": "Estrategias de Inte en Psi Soc", "secc": "006", "dias": "LM", "hora": "1700-1829", "profesor": "LARA - LOPEZ ALINE BENJAMIN", "semestre": "10mo Semestre"},
    {"nrc": "57864", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "10mo Semestre"},
    {"nrc": "57873", "clave": "ISPS 210", "materia": "Estrategias de Inte en Psi Cli", "secc": "007", "dias": "AJ", "hora": "0900-1029", "profesor": "ARCE - MUNOZ MOHAMED", "semestre": "10mo Semestre"},
    {"nrc": "57880", "clave": "ISPS 211", "materia": "Estrategias de Inte en Psi Soc", "secc": "007", "dias": "AJ", "hora": "1100-1229", "profesor": "RODRIGUEZ MARTINEZ RICARDO ALEJANDRO", "semestre": "10mo Semestre"},
    {"nrc": "57889", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "ALVAREZ-CARRILLO PAULINA", "semestre": "10mo Semestre"},
    {"nrc": "57895", "clave": "ISPS 210", "materia": "Estrategias de Inte en Psi Cli", "secc": "008", "dias": "AJ", "hora": "1500-1629", "profesor": "GALINDO-MOTO MANUEL ALEJANDRO", "semestre": "10mo Semestre"},
    {"nrc": "57898", "clave": "ISPS 211", "materia": "Estrategias de Inte en Psi Soc", "secc": "008", "dias": "AJ", "hora": "1300-1429", "profesor": "PEREZ-XOCHIPA MARCO POLO", "semestre": "10mo Semestre"}
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
    if 'hora' not in materia or not materia['hora']: return False
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

def generar_horario_estricto(lista_materias, profesores_prioritarios, lm_ini, lm_fin, aj_ini, aj_fin, omitir_viernes, max_intentos=5000):
    materias_unicas = {}
    nombres_materias = {}
    for m in lista_materias:
        clave = m['clave']
        nombres_materias[clave] = m['materia']
        if clave not in materias_unicas: materias_unicas[clave] = []
        materias_unicas[clave].append(m)

    prioridades = [p.strip() for p in profesores_prioritarios if p.strip()]
    materias_omitidas, omitidas_prof_unico, omitidas_por_viernes = [], [] , []
    materias_filtradas = {}
    
    for clave, opciones in materias_unicas.items():
        opciones_con_profesor = [op for op in opciones if any(coincide_profesor(p_p, op['profesor']) for p_p in prioridades)]
        usuario_pidio_profesor = len(opciones_con_profesor) > 0
        opciones_a_evaluar = opciones_con_profesor if usuario_pidio_profesor else opciones
        
        if omitir_viernes:
            opciones_sin_viernes = [op for op in opciones_a_evaluar if 'V' not in op['dias']]
            if len(opciones_sin_viernes) == 0 and len(opciones_a_evaluar) > 0:
                omitidas_por_viernes.append(nombres_materias[clave])
                continue 
            opciones_a_evaluar = opciones_sin_viernes

        opciones_validas = [op for op in opciones_a_evaluar if not choca_con_bloqueo_por_dia(op, lm_ini, lm_fin, aj_ini, aj_fin)]
        
        if opciones_validas:
            materias_filtradas[clave] = opciones_validas
        else:
            es_unico_profesor = len(set(op['profesor'] for op in opciones)) == 1
            if usuario_pidio_profesor or es_unico_profesor:
                omitidas_prof_unico.append(nombres_materias[clave])
            else:
                materias_omitidas.append(nombres_materias[clave])

    if not materias_filtradas and not omitidas_por_viernes:
        return None, False, materias_omitidas, omitidas_prof_unico, omitidas_por_viernes, "Las restricciones de bloqueo eliminaron todas las opciones válidas."

    if not materias_filtradas and omitidas_por_viernes:
        return [], True, materias_omitidas, omitidas_prof_unico, omitidas_por_viernes, ""

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
            return calendario_propuesto, prioridad_completa, materias_omitidas, omitidas_prof_unico, omitidas_por_viernes, ""

    return None, False, materias_omitidas, omitidas_prof_unico, omitidas_por_viernes, "No se encontró una combinación válida sin traslapes."

# --- CONFIGURACIÓN DE STREAMLIT ---
st.set_page_config(page_title="Generador de Horarios Oficial", layout="wide", page_icon="🗓️")

# --- BARRA LATERAL (SIDEBAR) ---
st.sidebar.title("🛠️ Filtros de Control")

st.sidebar.subheader("Periodo Académico")
semestre_seleccionado = st.sidebar.selectbox(
    "Selecciona tu semestre activo:",
    ["5to Semestre", "6to Semestre", "7mo Semestre", "8vo Semestre", "9no Semestre", "10mo Semestre"],
    index=0
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
st.sidebar.subheader("📅 Filtro de Días Específicos")
omitir_viernes = st.sidebar.checkbox("Omitir clases los viernes", value=False, help="Si marcas esta opción, el algoritmo descartará por completo los grupos que tengan clases en viernes.")

st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Ej. LUNA-PEREZ")
    if pref_name.strip(): profesores_inputs.append(pref_name.strip())

# --- FILTRADO EN TIEMPO REAL ---
lista_materias_trabajo = [m for m in CATALOGO_MATERIAS if m['semestre'] == semestre_seleccionado]

# --- CUERPO PRINCIPAL ---
st.title("🗓️ Generador de Horarios Dinámico y Prioritario")
st.subheader(f"Esquema Activo: {semestre_seleccionado} (Solo Materias Base)")

if st.button("🎲 Calcular Horario Óptimo", type="primary"):
    if not lista_materias_trabajo:
        st.warning(f"La base de datos para el **{semestre_seleccionado}** no contiene información.")
    else:
        calendario, prioridad_cumplida, om, om_prof, om_viernes, err = generar_horario_estricto(
            lista_materias_trabajo, profesores_inputs, lm_inicio, lm_fin, aj_inicio, aj_fin, omitir_viernes
        )
        
        if calendario is not None:
            # 🚨 MENSAJE EMERGENTE SOLICITADO PARA MATERIAS DEL VIERNES
            if om_viernes:
                for mat in om_viernes:
                    st.warning(f"⚠️ La materia **{mat}** no se seleccionó porque no está disponible (tiene clase el viernes) y el horario la omitirá.")

            if om:
                st.warning(f"⚠️ **Atención:** Para cumplir tus restricciones de tiempo, se omitieron: {', '.join(om)}.")
            if om_prof:
                st.error(f"👤 **Materia Omitida:** La asignatura **{', '.join(om_prof)}** se omitió debido a cruces con las horas bloqueadas.")

            if len(profesores_inputs) > 0 and len(calendario) > 0:
                if prioridad_cumplida:
                    st.info("💎 **Filtro Aplicado Correctamente:** Se fijaron exitosamente tus profesores prioritarios.")
                else:
                    st.warning("⚠️ **Filtro No Aplicado Completamente:** Ciertos profesores prioritarios no se incluyeron por cruce con horas bloqueadas.")
            elif len(calendario) > 0:
                st.success("🎯 ¡Horario estructurado correctamente!")

            if calendario:
                bloques_horas = ["0700-0829", "0700-0859", "0900-1029", "0900-1059", "1100-1229", "1100-1259", "1300-1429", "1300-1459", "1500-1629", "1500-1659", "1700-1829", "1700-1859", "1900-2059"]
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
                st.info("💡 No hay clases por mostrar en la cuadrícula ya que las materias activas fueron omitidas por las restricciones de días.")
        else:
            st.error(err)