# Integración de Make a Wazuh para gestionar alertas

### Descripción - Español
Integración Wazuh personalizada de Make que te permite recibir alertas y así poder monitorizarlas. Hay dos archivos, el script bash permite que el archivo python (.py) sea leído correctamente.

---
### Pasos para Ejecutar

#### 1. Crear un webhook en Make.

Insertamos el módulo de WEBHOOK, y acto seguido le damos un nombre. Una vez hecho, se generará un link, que usaremos más adelante para establecer la conexión.

#### 2. Configurar la integración en Wazuh.

Iniciamos sesión en Wazuh y vamos a:

Server Management > Settings

Nos dirigimos a la opción "Edit Configuration" que se encuentra en la esquina superior derecha.
Debajo de la etiqueta <global></global> insertamos el siguiente trozo de código:
```
  <integration>
    <name>custom-make</name>
    <hook_url>https://hook.eu1.make.com/4vmo1kve9voqqs8vfic1s024vp72uwkc</hook_url>
    <alert_format>json</alert_format>
  </integration>
```
Entonces reiniciamos Wazuh Manager.

#### 3. Instalar los scripts y darles permisos.

Ahora para obtener los scripts podemos hacer dos cosas.
Descargar la carpeta de Make y ponerla dentro de:
```
/var/ossec/integrations
```

o bien

Asegurarnos de tener permisos de superusuario temporalmente:
```
sudo su
```
Abrir la carpeta de integraciones:
```
cd /var/ossec/integrations
```
Descargar los archivos:
```
wget https://raw.githubusercontent.com/vnd76/IntegracionWazuh-Make/refs/heads/main/integrations/make/custom-make
wget https://raw.githubusercontent.com/vnd76/IntegracionWazuh-Make/refs/heads/main/integrations/make/custom-make.py
```

Para verificar que todo se ha descargado correctamente:
```
ls -l
```

Una vez tenemos los scripts en la carpeta correcta, les daremos permisos de ejecución.
```
sudo chmod 750 /var/ossec/integrations/custom-*
sudo chown root:wazuh /var/ossec/integrations/custom-*
```
---

### Description - English
Wazuh custom integration for Make that allows you to receive alerts and monitor them. There's two files, the bash script allows the python file (.py) to be read correctly.
