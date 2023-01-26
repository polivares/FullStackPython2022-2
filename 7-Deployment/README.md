# Enlaces útiles

- Conexión ssh con putty y archivo ppk: https://www.bluehost.com/help/article/using-ssh-on-windows-putty
- Creación de contraseña de administrador (root) para mysql server (resolución de problema para `mysql_secure_installation`): https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04
- En caso de error 500, esto podría deberse a algún problema en el acceso del servidor web a nuestro proyecto. Algunas opciones para solucionarlo son:
    - Verificar que no haya ningún error en nuestro código (ej. error en la clave del usuario de mysql)
    - Cambiar los permisos de los archivos en nuestro proyecto. 
    
    ```console
        sudo chmod -R 777 2-FlaskMysql/
    ```
    - Agregar el usuario ubuntu al grupo ```www-data``` para que pueda acceder a los archivos de nuestro proyecto.
    ```console
        sudo usermod -aG www-data ubuntu
    ```