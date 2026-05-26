import streamlit as st
import random
import pandas as pd

# =========================================================================
# 📚 BASE DE DATOS REAL EXTRAÍDA DE TU DOCUMENTO (MATERIAS BASE)
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

    # --- 10mo SEMESTRE ---
    {"nrc": "58255", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "001", "dias": "LM", "hora": "0700-0859", "profesor": "GONZALEZ - CRUZ VICTOR GERARDO", "semestre": "10mo Semestre"},
    {"nrc": "58643", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "002", "dias": "LM", "hora": "1500-1659", "profesor": "CARRO-MEZA DULCE CAROLINA", "semestre": "10mo Semestre"},
    {"nrc": "58714", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "003", "dias": "AJ", "hora": "1700-1859", "profesor": "GONZALEZ-CRUZ VICTOR GERARDO", "semestre": "10mo Semestre"},
    {"nrc": "59139", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "004", "dias": "AJ", "hora": "1300-1459", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "10mo Semestre"},
    {"nrc": "59156", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "005", "dias": "LM", "hora": "0700-0859", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN", "semestre": "10mo Semestre"},
    {"nrc": "57809", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "006", "dias": "LM", "hora": "1300-1459", "profesor": "MERCADO CARNALLA MARIO RENATO", "semestre": "10mo Semestre"},
    {"nrc": "57864", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "007", "dias": "LM", "hora": "0900-1059", "profesor": "MOTO-MARTINEZ TERESA LEDOINA", "semestre": "10mo Semestre"},
    {"nrc": "57889", "clave": "ISPS 212", "materia": "Desarrollo Organizacional", "secc": "008", "dias": "AJ", "hora": "1700-1859", "profesor": "ALVAREZ-CARRILLO PAULINA", "semestre": "10mo Semestre"}
]

# =========================================================================
# 🧬 CATÁLOGO DE OPTATIVAS (MATERIAS CON FORMATOS DE 1 HORA Y MEDIA O 3 HORAS)
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
        {"nrc": "58689", "clave": "PSIS 625", "materia": "Estres y Salud en las Organi..", "secc": "002", "dias": "AJ", "hora": "1100-1229", "profesor": "CLEMENTE MARIA ANTONIA DEL CARMEN"},
        {"nrc": "59425", "clave": "ISPS 207", "materia": "Estrategias de Inte en Psi Org", "secc": "004", "dias": "LM", "hora": "0900-1029", "profesor": "ARELLANO BAUTISTA CLAUDIA ANGELICA"}
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
# ⚙️ MOTOR ALGORÍTMICO Y LÓGICA DE CONTROL DE INTERVALOS MIXTOS
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
    ["5to Semestre", "6to Semestre", "7mo Semestre", "8vo Semestre", "9no Semestre", "10mo Semestre"],
    index=0
)

# --- CONFIGURACIÓN DEL SLIDER DE HORARIOS MIXTOS (1.5h y 2h INTERCALADOS) ---
st.sidebar.markdown("---")
st.sidebar.subheader("⏱️ Horario de Referencia")
st.sidebar.markdown(
    "<small style='color: gray; display:block; margin-bottom: 10px;'>"
    "Establece los rangos permitidos incluyendo los bloques independientes de 1.5 horas."
    "</small>", 
    unsafe_allow_html=True
)

horas_visibles = {
    700: "07:00 AM", 830: "08:30 AM", 900: "09:00 AM", 1030: "10:30 AM",
    1100: "11:00 AM", 1230: "12:30 PM", 1300: "01:00 PM", 1430: "02:30 PM",
    1500: "03:00 PM", 1630: "04:30 PM", 1700: "05:00 PM", 1830: "06:30 PM",
    1900: "07:00 PM", 2100: "09:00 PM"
}
valores_horas = list(horas_visibles.keys())

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

# --- SECCIÓN PROFESORES PRIORITARIOS ---
st.sidebar.markdown("---")
st.sidebar.subheader("👤 Profesores Prioritarios")
profesores_inputs = []
for i in range(1, 9):
    pref_name = st.sidebar.text_input(f"Docente Prioritario {i}", key=f"prof_{i}", placeholder="Ej. LUNA-PEREZ")
    if pref_name.strip(): profesores_inputs.append(pref_name.strip())

# --- EXPANDER DE SELECCIÓN DE OPTATIVAS ---
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
                # 📅 SECCIÓN DE CONSTRUCCIÓN E INYECCIÓN DE DATOS INTELIGENTE
                bloques_completos = [
                    "07:00 - 08:29", "07:00 - 08:59", "09:00 - 10:29", "09:00 - 10:59",
                    "11:00 - 12:29", "11:00 - 12:59", "13:00 - 14:29", "13:00 - 14:59",
                    "13:00 - 15:59", "15:00 - 16:29", "15:00 - 16:59", "17:00 - 18:29",
                    "17:00 - 18:59", "19:00 - 20:59"
                ]
                
                df_horario = pd.DataFrame("&nbsp;", index=bloques_completos, columns=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
                
                for m in calendario:
                    # Formateo estético del contenido de la celda en HTML avanzado
                    info_celda = f"📚 <b>{m['materia']}</b><br><span style='color:#555;'>Secc. {m['secc']}</span><br>👤 {m['profesor']}<br><span style='color:#1E3A8A; font-weight:bold;'>[NRC: {m['nrc']}]</span>"
                    ini_mat, fin_mat = parse_hora(m['hora'])
                    
                    for bloque in bloques_completos:
                        b_str_ini, b_str_fin = bloque.split(" - ")
                        b_ini = int(b_str_ini.replace(":", ""))
                        b_fin = int(b_str_fin.replace(":", ""))
                        
                        # Mapeo matemático: Si la materia toca total o parcialmente el bloque, se replica con gracia
                        if ini_mat < b_fin and b_ini < fin_mat:
                            if 'L' in m['dias']: df_horario.at[bloque, "Lunes"] = info_celda
                            if 'M' in m['dias']: df_horario.at[bloque, "Miércoles"] = info_celda
                            if 'A' in m['dias']: df_horario.at[bloque, "Martes"] = info_celda
                            if 'J' in m['dias']: df_horario.at[bloque, "Jueves"] = info_celda
                            if 'V' in m['dias']: df_horario.at[bloque, "Viernes"] = info_celda

                # Ocultamos dinámicamente celdas y días que se queden 100% en blanco
                filas_activas = [f for f in df_horario.index if not (df_horario.loc[f] == "&nbsp;").all()]
                columnas_activas = [col for col in df_horario.columns if not (df_horario[col] == "&nbsp;").all()]
                df_horario_filtrado = df_horario.loc[filas_activas, columnas_activas]

                # 🎨 INYECCIÓN DE ESTILOS CSS PERSONALIZADOS (REEMPLAZA A ST.TABLE TRADICIONAL)
                st.write("### 📅 Vista de Calendario Semanal")
                st.markdown(
                    """
                    <style>
                        .styled-table table {
                            font-family: 'Segoe UI', Arial, sans-serif !important;
                            border-collapse: collapse !important;
                            width: 100% !important;
                            margin: 10px 0 !important;
                            font-size: 13px !important;
                            box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
                            border-radius: 8px !important;
                            overflow: hidden !important;
                        }
                        .styled-table th {
                            background-color: #1E3A8A !important;
                            color: white !important;
                            text-align: center !important;
                            font-weight: 600 !important;
                            padding: 12px !important;
                            border: 1px solid #1E3A8A !important;
                        }
                        .styled-table td {
                            padding: 12px !important;
                            text-align: left !important;
                            vertical-align: top !important;
                            height: 105px !important;
                            background-color: #F8F9FA !important;
                            border: 1px solid #E5E7EB !important;
                            line-height: 1.5 !important;
                        }
                        .styled-table tr:hover td {
                            background-color: #F1F5F9 !important;
                        }
                    </style>
                    """, 
                    unsafe_allow_html=True
                )
                
                # Renderizado seguro convirtiendo el DataFrame a HTML plano interpretable
                st.markdown('<div class="styled-table">', unsafe_allow_html=True)
                st.write(df_horario_filtrado.to_html(escape=False, justify='center'), unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.write("### 📝 Detalle del Horario Activo")
                df_lista = pd.DataFrame(calendario)[['nrc', 'clave', 'materia', 'secc', 'dias', 'hora', 'profesor']]
                df_lista.columns = ['NRC', 'Clave', 'Materia', 'Sección', 'Días', 'Horario', 'Docente']
                st.dataframe(df_lista, use_container_width=True, hide_index=True)
            else:
                st.info("💡 No hay clases por mostrar en la cuadrícula debido a las restricciones activas.")
        else:
            st.error(err)