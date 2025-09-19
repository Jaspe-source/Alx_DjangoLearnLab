# Deployment Configuration for HTTPS

To ensure the application enforces HTTPS:

1. **SSL/TLS Certificates**  
   - Obtain SSL certificates (e.g., from Let’s Encrypt).
   - Place them in your server’s secure directory (e.g., `/etc/ssl/`).

2. **Nginx Configuration Example**  
   ```nginx
   server {
       listen 80;
       server_name example.com;
       return 301 https://$host$request_uri;
   }

   server {
       listen 443 ssl;
       server_name example.com;

       ssl_certificate /etc/ssl/certs/fullchain.pem;
       ssl_certificate_key /etc/ssl/private/privkey.pem;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto https;
       }
   }

<VirtualHost *:80>
    ServerName example.com
    Redirect permanent / https://example.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName example.com
    SSLEngine on
    SSLCertificateFile /etc/ssl/certs/fullchain.pem
    SSLCertificateKeyFile /etc/ssl/private/privkey.pem

    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
</VirtualHost>
