package VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Controladores;

import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Modelos.Permiso;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Modelos.PermisosRol;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Modelos.Rol;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Repositorios.RepositorioPermiso;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Repositorios.RepositorioPermisosRol;
import VSRegistraduriaT1.BackEndSeguridad.MainSecurity.Repositorios.RepositorioRol;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin
@RestController
@RequestMapping("/permisos-roles")
public class ControladorPermisosRoles {
    @Autowired
    private RepositorioPermisosRol miRepositorioPermisosRol;

    @Autowired
    private RepositorioPermiso miRepositorioPermiso;

    @Autowired
    private RepositorioRol miRepositorioRol;

    /**
     * Devuelve el listado de los Permisos y Roles
     * @return
     */

    @GetMapping("")
    public List<PermisosRol> index(){
        return miRepositorioPermisosRol.findAll();
    }

    /**
     * Asigna los permisos a cada rol
     * @param id_rol
     * @param id_permiso
     * @return
     */

    @ResponseStatus(HttpStatus.CREATED)
    @PostMapping("rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRol create(@PathVariable String id_rol,
                              @PathVariable String id_permiso){
        PermisosRol nuevoPermisoRol = new PermisosRol();
        Rol elRol = miRepositorioRol.findById(id_rol)
                .orElse(null);
        Permiso elPermiso = miRepositorioPermiso.findById(id_permiso)
                .orElse(null);
        if(elRol!=null && elPermiso!=null){
            nuevoPermisoRol.setRol(elRol);
            nuevoPermisoRol.setPermiso(elPermiso);
            return miRepositorioPermisosRol.save(nuevoPermisoRol);
        }else{
            return null;
        }
    }

    /**
     * Muestra los permisos de un  rol especifico
     * @param id_PermisosRol
     * @return
     */

    @GetMapping("{id_permisosRol}")
    public PermisosRol show(@PathVariable String id_PermisosRol){
        PermisosRol permisosRolActual = miRepositorioPermisosRol
                .findById(id_PermisosRol)
                .orElse(null);
        return permisosRolActual;
    }

    /**
     * Modificaciones Rol y Permiso y asignar un nuevo rol o permiso
     * @param id_permisosRol
     * @param id_rol
     * @param id_permiso
     * @return PermisosRol
     */
    @PutMapping("{id_permisosRol}/rol/{id_rol}/permiso/{id_permiso}")
    public PermisosRol update(@PathVariable String id_permisosRol,
                              @PathVariable String id_rol,
                              @PathVariable String id_permiso){
        PermisosRol permisosRolActual = miRepositorioPermisosRol
                .findById(id_permisosRol)
                .orElse(null);
        Rol elRol = miRepositorioRol.findById(id_rol)
                .orElse(null);
        Permiso elPermiso =miRepositorioPermiso.findById(id_permiso)
                .orElse(null);
        if(permisosRolActual!=null && elPermiso!=null && elRol!=null){
            permisosRolActual.setPermiso(elPermiso);
            permisosRolActual.setRol(elRol);
            return miRepositorioPermisosRol.save(permisosRolActual);
        }else{
            return null;
        }
    }

    /**
     * Elimina un permiso Rol
     * @param id
     */

    @ResponseStatus(HttpStatus.NO_CONTENT)
    @DeleteMapping("{id}")
    public void delete(@PathVariable String id){
        PermisosRol permisosRolActual = miRepositorioPermisosRol
                .findById(id)
                .orElse(null);
        if(permisosRolActual!=null){
            miRepositorioPermisosRol.delete(permisosRolActual);
        }
    }

    /**
     * @context Validar si un rol tiene determinado permiso
     * @param id_rol
     * @return PermisosRol
     */
    @GetMapping("validar-permiso/rol/{id_rol}")
    public PermisosRol getPermisos(@PathVariable String id_rol,
                                  @RequestBody Permiso infoPermiso){
        Permiso elPermiso= miRepositorioPermiso
                .getPermiso(infoPermiso.getUrl(),
                        infoPermiso.getMetodo());
        Rol elRol = miRepositorioRol.findById(id_rol).get();
        if(elPermiso!=null && elRol!=null){
            return miRepositorioPermisosRol.getPermisoRol(elRol.get_id(),
                    elPermiso.get_id());
        }else{
            return null;
        }
    }

}
