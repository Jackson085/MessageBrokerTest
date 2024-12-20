### App richtig forken


## 1) GitHub
#### 1. Neues Repo anlagen und Template als template auswählen
#### 2. Variablen und secrets übernegmen
#### 3 Dev-Branch checken -> `dev` deployed auf `dev-server`
#### 4 Dev-Branch checken -> `prod` deployed auf `prod-server`
#### 5 Runner auf `192.168.178.179` aufsetzen 

## 1) Backend How To
Idee: Commons sind meist konstante werte aus dem Template. Logik steckt in Domain

## 2) neue Ressource im gui ordner

#### 1. neue application erstellen im `gui` ordner
```bash
cd gui
ng generate application NAME --routing=false --style=scss
```
Es sollte NAME unter `projects/Name` erstellt worden sein

#### 2. `app.modules.ts` kopieren wie unter `root`

## 3) Template in Proxmox Forken 
Wichtig: Es gibt nur ein `Dev` Server auf den alle Apps laufen und pro Logik ein `Prod` server. Erstellung des neuen Prod Server:

#### 1) ProxMox Template klonen 
1) `104 (ServerTemplate)` Full Clone und Name mit *Server vergeben
2) statische Ip geben und dokumentieren
3) username: `ouroboros` pw: `root`

#### 2) nginx einrichten 
1) Admin Seite öffnen Ip:81 -> Email: `admin@example.com` Pw: `changeme`
2) Unter Details: domain und ip setzen, Port auf 80 
3) Custome location setzen `/app -> ip/` und container port setzen 



# Was wurde auf dem Template eingestellt 
## user braucht kein pw für root rechte

```bash
sudo visudo
```

Füge die folgende Zeile am Ende der Datei hinzu:

```text
username ALL=(ALL) NOPASSWD: ALL
```

Überprüfe die sudoers-Datei auf Syntaxfehler:

```bash
visudo -c
```

## Nginx proxymanager als docker einrichten
Ordner erstellen unter ~/
```bash
mkdir nginx; cd nginx
```

_hsts_map.conf erstellen (leer) (ist offizieller Workaround)
[GitHub](https://github.com/NginxProxyManager/nginx-proxy-manager/issues/3474#issuecomment-1902790528)

```bash
sudo nano _hsts_map.conf
```

```bash
sudo nano docker-compose.yml
```

Inhalt der docker-compose Datei [_hsts_map.conf](https://github.com/NginxProxyManager/nginx-proxy-manager/issues/3474#issuecomment-1902790528)
wurde nur eingebunden da sonst bug
```yaml
version: '3.8'
services:
  app:
    image: 'jc21/nginx-proxy-manager:latest'
    restart: unless-stopped
    ports:
      - '80:80'
      - '81:81'
      - '443:443'
    volumes:
      - ./data:/data
      - ./letsencrypt:/etc/letsencrypt
      - ./_hsts_map.conf:/app/templates/_hsts_map.conf
```

```bash
sudo docker compose up -d
```

Default Admin User für Adminoberfläche (Port 81):

```text
Email:    admin@example.com
Password: changeme
```


