package VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Controladores;

import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Modelos.Rol;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Modelos.Usuario;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Repositorios.RepositorioRol;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Repositorios.RepositorioUsuario;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/usuarios")
public class ControladorUsuario {
    @Autowired
    private RepositorioUsuario miRepositorioUsuario;

    @Autowired
    private RepositorioRol miRepositorioRol;

    @GetMapping("")
    public List<Usuario> index(){
        return miRepositorioUsuario.findAll();
    }

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping
    public Usuario create(@RequestBody Usuario infoUsuario){
        infoUsuario.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
        return miRepositorioUsuario.save(infoUsuario);
    }

    /**
     * Se añade una función para manejar el encriptado de las
     * contraseñas
     * */

    public String convertirSHA256(String password){
        MessageDigest md = null;
        try{
            md = MessageDigest.getInstance("SHA-256");
        }catch (NoSuchAlgorithmException e){
            e.printStackTrace();
            return null;
        }
        byte[] hash = md.digest(password.getBytes());
        StringBuffer sb = new StringBuffer();
        for(byte b: hash){
            sb.append(String.format("%20x", b));
        }
        return sb.toString();
    }
    @GetMapping("{id}")
    public Usuario show(@PathVariable String id){
        Usuario usuarioActual = miRepositorioUsuario
                .findById(id)
                .orElse(null);
        return usuarioActual;
    }

    @PutMapping("{id}")
    public Usuario update(@PathVariable String id, @RequestBody Usuario infoUsuario){
        Usuario usuarioActual = miRepositorioUsuario
                .findById(id)
                .orElse(null);
        if(usuarioActual!=null){
            usuarioActual.setSeudonimo(infoUsuario.getSeudonimo());
            usuarioActual.setCorreo(infoUsuario.getCorreo());
            usuarioActual.setContrasena(convertirSHA256(infoUsuario.getContrasena()));
            return miRepositorioUsuario.save(usuarioActual);
        }else{
            return null;
        }
    }

    /**
     * Función Delete
     * @param id
     */
    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        Usuario usuarioActual = miRepositorioUsuario
                .findById(id)
                .orElse(null);
        if(usuarioActual!=null){
            miRepositorioUsuario.delete(usuarioActual);
        }
    }

    /**
     *Asigna un rol a un usuario
     * @param id_usuario
     * @param id_rol
     * @return Usuario
     */
    @PutMapping("{id_usuario}/rol/{id_rol}")
    public Usuario asignarRolUsuario(@PathVariable String id_usuario,
                                     @PathVariable String id_rol){
        Usuario usuarioActual = miRepositorioUsuario
                .findById(id_usuario)
                .orElse(null);
        Rol rolActual = miRepositorioRol
                .findById(id_rol)
                .orElse(null);
        if(usuarioActual!=null && rolActual!=null){
            usuarioActual.setRol(rolActual);
            return miRepositorioUsuario.save(usuarioActual);
        }else{
            return null;
        }
    }

    @PostMapping("/validar")
    public Usuario validate(@RequestBody Usuario infoUsuario,
                            final HttpServletResponse response)
            throws IOException{
        Usuario usuarioActual = miRepositorioUsuario.getUserByMail(infoUsuario.getCorreo());
        if(usuarioActual!=null && usuarioActual.getContrasena()
                .equals(convertirSHA256(infoUsuario.getContrasena()))){
            usuarioActual.setContrasena((""));
            return usuarioActual;
        }else{
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED);
            return null;
        }
    }
}
